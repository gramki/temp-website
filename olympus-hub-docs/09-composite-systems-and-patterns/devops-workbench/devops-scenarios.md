# DevOps Scenarios

> **Status:** 🟡 Draft
> **Category:** Composite Patterns / DevOps Workbench

---

## Overview

DevOps Scenarios are Hub Scenarios that automate development activities for Automation Product Owner, Process Architect, and Developer personas. These scenarios run in the DevOps Workbench (D), triggered by signals from Business Workbenches (A).

Each scenario follows the standard Hub pattern:
- **Trigger** — DevOps Event from business workbench
- **Application** — Cognitive application (AI-assisted) or workflow
- **Tasks** — Assigned to persona queue (AI agent + human)
- **Outcome** — Action taken in business workbench or artifact produced

---

## Scenario Categories

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVOPS SCENARIO CATEGORIES                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  APO SCENARIOS                PA SCENARIOS              DEVELOPER SCENARIOS │
│  ─────────────                ────────────              ─────────────────── │
│                                                                              │
│  • Idea Triage               • Intent Review           • App Scaffolding    │
│  • Intent Drafting           • Scenario Drafting       • Test Diagnosis     │
│  • Feedback Triage           • SOP Generation          • Build Resolution   │
│  • Outcome Review            • Normative Validation    • Promotion Review   │
│                                                                              │
│  TRIGGER: idea.*             TRIGGER: intent.*         TRIGGER: test.*      │
│           feedback.*                  charter.*                 build.*     │
│                                                                  artifact.* │
│                                                                              │
│  QUEUE: apo-queue            QUEUE: pa-queue           QUEUE: dev-queue    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## CRD Output Summary

DevOps scenarios produce CRDs that are **committed to the Business Workbench's Git repository**. The Git repo is registered as a Machine (`{workbench}-git`) in the DevOps Workbench. All writes go through the **Pull Request workflow** for human review.

### Machines Used

| Machine | Purpose |
|---------|---------|
| `{workbench}-gateway` | Query resources in Business Workbench (knowledge, memory, data, CAF) |
| `{workbench}-git` | Commit CRDs to Business Workbench Git repository |

### CRD Outputs by Scenario

| Scenario | CRDs Committed to Git | PR Reviewer |
|----------|----------------------|-------------|
| **Idea Triage** | — (updates idea status via API) | — |
| **Intent Drafting** | — (updates intent status via API) | — |
| **Intent Review** | Charter (via API, not CRD) | PA |
| **Scenario Drafting** | `ScenarioNormativeSpec` | PA |
| **SOP Generation** | `SOPDocumentSpec` | PA |
| **Normative Validation** | — (validation report) | — |
| **App Scaffolding** | `HubApplicationSpec`, `ScenarioAutomationSpec`, `TriggerSpec`, Seer Agent Specs if agentic | Developer |
| **Tool Integration** | `ToolDefinition`, `ToolInstance` | Developer / Admin |
| **Data Store Provisioning** | `GanymedeStore`, `CallistoStore`, `EuropaStore` | Admin |
| **Test Diagnosis** | — (diagnosis report) | — |
| **Build Resolution** | — (fix recommendations, may create patch CRDs) | Developer |
| **Promotion Review** | `ScenarioDeploymentSpec` (for target environment) | Developer |

### Git Workflow

```
1. Agent generates CRD content
2. Agent calls git_create_branch (devops/{scenario}-{id})
3. Agent calls git_commit_crd (write CRD file)
4. Agent calls git_push
5. Agent calls git_create_pr (assigns reviewers based on CRD type)
6. Human reviews PR in Git UI (GitHub, GitLab, etc.)
7. Human approves and merges
8. Hub operators reconcile CRD → applied to Hub state
9. Merge event signals back to DevOps Workbench
```

---

## Automation Product Owner Scenarios

### Idea Triage

**Purpose:** Categorize, estimate, and recommend action for submitted ideas.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `idea.submitted` |
| **Queue** | `apo-queue` |
| **Autonomy** | Medium — AI suggests, APO approves |

**Workflow:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IDEA TRIAGE SCENARIO                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. RECEIVE                                                                 │
│     • Idea submitted event from business workbench                         │
│     • Extract: title, description, submitter, related context              │
│                                                                              │
│  2. ENRICH (AI Agent)                                                       │
│     • Query business workbench knowledge (via gateway)                     │
│     • Retrieve similar past ideas                                          │
│     • Retrieve related scenarios and SOPs                                  │
│     • Retrieve relevant enterprise memory                                  │
│                                                                              │
│  3. ANALYZE (AI Agent)                                                      │
│     • Categorize: process_automation | data_quality | integration | other  │
│     • Estimate value: high | medium | low                                  │
│     • Estimate effort: high | medium | low                                 │
│     • Identify dependencies and risks                                      │
│     • Check for duplicates                                                 │
│                                                                              │
│  4. RECOMMEND (AI Agent)                                                    │
│     • Promote to Intent (high value)                                       │
│     • Park for later (low priority)                                        │
│     • Reject with reason (not feasible, duplicate)                         │
│     • Request clarification                                                │
│                                                                              │
│  5. DECIDE (Human APO or AI if high confidence)                            │
│     • Review AI recommendation                                             │
│     • Approve, modify, or override                                         │
│     • If promote: Trigger intent-drafting                                  │
│                                                                              │
│  6. RECORD                                                                  │
│     • Update idea status in business workbench                             │
│     • Create triage record in CAF                                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Scenario Specification:**

```yaml
apiVersion: hub.olympus.io/v1
kind: Scenario
metadata:
  name: idea-triage
  namespace: dispute-devops
spec:
  description: "Triage submitted ideas and recommend action"
  
  trigger:
    event_type: devops_event
    condition: "event.type == 'idea.submitted'"
  
  application:
    type: cognitive
    runtime: seer
    config:
      agent_id: apo-assistant
      prompt_template: idea-triage-prompt
      tools:
        - name: query_knowledge
          machine: "{{source_workbench}}-gateway"
        - name: query_memory
          machine: "{{source_workbench}}-gateway"
        - name: get_similar_ideas
          machine: "{{source_workbench}}-gateway"
  
  tasks:
    - name: triage-decision
      type: decision
      queue: apo-queue
      description: "Review idea and decide on action"
      input:
        idea: "{{trigger.idea}}"
        analysis: "{{analysis}}"
        recommendation: "{{recommendation}}"
      output:
        decision: enum[promote, park, reject, clarify]
        notes: string
  
  outcomes:
    - condition: "decision == 'promote'"
      action: emit_signal
      signal:
        type: idea.promoted
        payload:
          idea_id: "{{idea.id}}"
          intent_id: "{{generated_intent_id}}"
    
    - condition: "decision == 'park'"
      action: update_idea_status
      status: parked
    
    - condition: "decision == 'reject'"
      action: update_idea_status
      status: rejected
```

---

### Intent Drafting

**Purpose:** Create initial intent document from promoted idea.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `idea.promoted` |
| **Queue** | `apo-queue` |
| **Autonomy** | Medium — AI drafts, APO refines |

**Workflow:**

```
1. RECEIVE promoted idea event
2. RETRIEVE idea details and triage notes
3. GENERATE intent draft:
   • Business case summary
   • Problem statement
   • Proposed solution approach
   • Success criteria (measurable)
   • Stakeholders
   • Risks and dependencies
4. PRESENT draft to APO
5. APO REFINES and completes
6. MARK intent as completed
7. EMIT intent.completed signal
```

---

### Feedback Triage

**Purpose:** Categorize and prioritize feedback from production.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `feedback.promoted`, `problem.promoted` |
| **Queue** | `apo-queue` |
| **Autonomy** | Medium |

**Workflow:**

```
1. RECEIVE feedback/problem from production workbench
2. CLASSIFY type:
   • Bug — implementation defect
   • Issue — operational constraint
   • Critical Limitation — design flaw
   • Observation — behavioral pattern
   • Suggestion — improvement idea
   • Learning — process insight
3. PRIORITIZE based on:
   • Severity
   • Frequency
   • Business impact
   • Related open items
4. RECOMMEND action:
   • Accept for backlog
   • Create new idea (if suggestion)
   • Assign to scenario for immediate fix
   • Reject with reason
5. APO DECIDES
6. UPDATE feedback status (reflected in source workbench)
```

---

### Outcome Review

**Purpose:** Summarize automation performance and flag concerns.

| Aspect | Detail |
|--------|--------|
| **Trigger** | Scheduled (weekly) or `milestone.reached` |
| **Queue** | `apo-queue` |
| **Autonomy** | Low — generates report, APO reviews |

**Workflow:**

```
1. AGGREGATE metrics from business workbench:
   • Request volumes by scenario
   • Success/failure rates
   • Agent performance
   • Cost metrics
2. COMPARE against success criteria (from charter)
3. IDENTIFY anomalies and trends
4. GENERATE summary report
5. FLAG items requiring attention
6. APO REVIEWS and takes action
```

---

## PA Scenarios

### Intent Review

**Purpose:** Analyze intent and suggest design approach.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `intent.completed` |
| **Queue** | `pa-queue` |
| **Autonomy** | Medium |

**Workflow:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INTENT REVIEW SCENARIO                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. RECEIVE                                                                 │
│     • Intent completed event                                               │
│     • Extract business case, success criteria, approach                    │
│                                                                              │
│  2. ANALYZE (AI Agent)                                                      │
│     • Query existing scenarios in business workbench                       │
│     • Identify overlap with existing automation                            │
│     • Query knowledge for similar patterns                                 │
│     • Retrieve relevant SOPs                                               │
│                                                                              │
│  3. DESIGN ASSESSMENT (AI Agent)                                            │
│     • Recommend automation approach:                                       │
│       - Conventional (workflow, rules)                                     │
│       - Agentic (AI-driven)                                                │
│       - Hybrid                                                             │
│     • Identify required capabilities                                       │
│     • Estimate complexity                                                  │
│     • Suggest task decomposition                                           │
│                                                                              │
│  4. PRESENT to PA                                                           │
│     • Summary of analysis                                                  │
│     • Recommended approach with rationale                                  │
│     • Questions/clarifications needed                                      │
│                                                                              │
│  5. PA DECIDES                                                              │
│     • Accept intent → Creates Charter                                      │
│     • Request clarification → Back to APO                                  │
│     • Reject → Not feasible                                                │
│                                                                              │
│  6. EMIT charter.created signal                                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### Scenario Drafting

**Purpose:** Generate scenario skeleton from charter.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `charter.created` |
| **Queue** | `pa-queue` |
| **Autonomy** | High for initial draft, Medium for refinement |
| **Output** | `ScenarioNormativeSpec` CRD pushed to Business Workbench |

**Workflow:**

```
1. RECEIVE charter created event
2. RETRIEVE charter details:
   • Scope
   • Task decomposition
   • Roles involved
   • Success criteria
3. QUERY existing patterns (via {workbench}-gateway):
   • Similar scenarios in workbench (list_scenarios, get_scenario)
   • Template scenarios from platform
   • Best practices from knowledge bank (query_knowledge)
4. GENERATE ScenarioNormativeSpec CRD content (YAML)
   • Trigger definition
   • Task sequence
   • Role assignments
   • Escalation rules
   • Request policies
5. COMMIT to Business Workbench Git (via {workbench}-git):
   • git_create_branch("devops/scenario-{name}")
   • git_commit_crd("crds/scenarios/{name}.yaml", crd_content)
   • git_push()
   • git_create_pr(reviewers: ["@pa-team"], labels: ["pa-review", "scenario"])
6. PA REVIEWS Pull Request in Git UI
7. PA APPROVES and merges → Operators apply CRD
8. EMIT scenario.created signal (triggers app-scaffolding)
```

**AI Agent Tools:**

```yaml
tools:
  - name: list_scenarios
    machine: "{{source_workbench}}-gateway"
  - name: get_scenario
    machine: "{{source_workbench}}-gateway"
  - name: query_knowledge
    machine: "{{source_workbench}}-gateway"
  - name: get_sop
    machine: "{{source_workbench}}-gateway"
  - name: generate_scenario_yaml
    type: internal
  - name: validate_scenario
    type: internal
```

---

### SOP Generation

**Purpose:** Draft SOP from scenario definition.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `scenario.created` or manual |
| **Queue** | `pa-queue` |
| **Autonomy** | High for draft, PA reviews |
| **Output** | `SOPDocumentSpec` CRD pushed to Business Workbench |

**Workflow:**

```
1. RECEIVE scenario details (via {workbench}-gateway get_scenario)
2. GENERATE SOPDocumentSpec CRD content (YAML):
   • Purpose and scope
   • Roles and responsibilities
   • Step-by-step procedure
   • Decision criteria
   • Escalation paths
   • Evidence requirements
3. COMMIT to Business Workbench Git (via {workbench}-git):
   • git_create_branch("devops/sop-{scenario-name}")
   • git_commit_crd("crds/sops/{name}.yaml", sop_content)
   • git_push()
   • git_create_pr(reviewers: ["@pa-team"], labels: ["pa-review", "sop"])
4. PA REVIEWS Pull Request in Git UI
5. PA APPROVES and merges → Operators apply CRD
6. SOP available in Knowledge Bank
```

---

### Normative Validation

**Purpose:** Validate scenario against governance policies.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `scenario.ready_for_validation` |
| **Queue** | `pa-queue` |
| **Autonomy** | High for checks, PA approves |

**Workflow:**

```
1. RETRIEVE scenario specification
2. CHECK against policies:
   • Required roles present
   • Escalation matrix defined
   • SOP linkage
   • Knowledge access configured
   • Compliance requirements met
3. REPORT validation results
4. PA APPROVES or requests fixes
```

---

## Developer Scenarios

### App Scaffolding

**Purpose:** Generate Hub Application skeleton from scenario.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `scenario.created` |
| **Queue** | `dev-queue` |
| **Autonomy** | High — generates code, Developer reviews |
| **Output** | `HubApplicationSpec`, `ScenarioAutomationSpec`, `TriggerSpec` CRDs + code artifacts |

**Workflow:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    APP SCAFFOLDING SCENARIO                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. RECEIVE scenario created event                                          │
│                                                                              │
│  2. ANALYZE scenario (via {workbench}-gateway):                             │
│     • Get scenario definition (get_scenario)                               │
│     • Task types (decision, action, governance)                            │
│     • Automation approach (rule-based, workflow, agentic)                  │
│     • Tool requirements                                                    │
│     • Data requirements                                                    │
│                                                                              │
│  3. SELECT runtime:                                                         │
│     • Atlantis — rule-based (Drools/DMN)                                   │
│     • Rhea — workflow (BPMN)                                               │
│     • Seer — agentic (AI)                                                  │
│     • Perseus — batch                                                      │
│     • ChronoShift — durable workflow                                       │
│                                                                              │
│  4. COMMIT CRDs to Business Workbench Git (via {workbench}-git):            │
│     • git_create_branch("devops/app-{scenario-name}")                      │
│     • git_commit_crd("crds/applications/{app}.yaml", HubApplicationSpec)   │
│     • git_commit_crd("crds/scenarios/{name}-automation.yaml", ...)         │
│     • git_commit_crd("crds/triggers/{name}.yaml", TriggerSpec)             │
│     • If agentic: git_commit_crd("crds/seer/{agent}.yaml", TrainingSpec)   │
│     • git_push()                                                           │
│     • git_create_pr(reviewers: ["@dev-team"], labels: ["dev-review"])      │
│                                                                              │
│  5. COMMIT code artifacts to same branch:                                   │
│     • Project structure                                                    │
│     • Entry point and handlers                                             │
│     • Tool bindings                                                        │
│     • Test stubs                                                           │
│                                                                              │
│  6. Developer REVIEWS Pull Request in Git UI                                │
│     • Reviews CRDs and code together                                       │
│     • Implements business logic in branch                                  │
│     • Approves and merges                                                  │
│                                                                              │
│  7. Operators apply CRDs → Hub state updated                                │
│                                                                              │
│  8. EMIT application.created signal (triggers CI)                           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### Test Diagnosis

**Purpose:** Analyze test failures and suggest fixes.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `test.failed` |
| **Queue** | `dev-queue` |
| **Autonomy** | High — AI diagnoses, Developer validates |

**Workflow:**

```
1. RECEIVE test failure event
2. RETRIEVE:
   • Test logs
   • Failed test code
   • Application code
   • Recent changes (git diff)
3. ANALYZE failure:
   • Classify: regression | new feature | flaky | environment
   • Identify root cause
   • Suggest fix
4. GENERATE fix proposal:
   • Code patch (if simple)
   • Investigation steps (if complex)
   • Similar past failures and resolutions
5. Developer REVIEWS and applies fix
6. RE-RUN tests
```

**Example AI Analysis:**

```json
{
  "diagnosis": {
    "failure_type": "regression",
    "root_cause": "Missing null check in processRefund() after recent change",
    "confidence": 0.87,
    "evidence": {
      "failing_test": "testRefundEligibility_NullCase",
      "exception": "NullPointerException at RefundService.java:45",
      "recent_commit": "abc123 - Refactored refund logic",
      "similar_failures": 2
    }
  },
  "recommendation": {
    "action": "apply_patch",
    "patch": "--- a/src/RefundService.java\n+++ b/src/RefundService.java\n@@ -43,6 +43,9 @@\n     public RefundResult processRefund(RefundRequest request) {\n+        if (request == null) {\n+            return RefundResult.invalid(\"Request cannot be null\");\n+        }\n         // existing logic",
    "tests_to_rerun": ["testRefundEligibility_NullCase", "testRefundEligibility_ValidCase"]
  }
}
```

---

### Build Resolution

**Purpose:** Analyze build failures and suggest resolution.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `build.failed` |
| **Queue** | `dev-queue` |
| **Autonomy** | High |

**Workflow:**

```
1. RECEIVE build failure event
2. RETRIEVE build logs
3. PARSE error:
   • Compilation error
   • Dependency issue
   • Configuration error
   • Resource constraint
4. SUGGEST resolution:
   • Code fix
   • Dependency update
   • Config change
   • Retry (if transient)
5. Developer APPLIES fix
```

---

### Promotion Review

**Purpose:** Validate artifact readiness for promotion.

| Aspect | Detail |
|--------|--------|
| **Trigger** | `promotion.requested` |
| **Queue** | `dev-queue` |
| **Autonomy** | Medium — AI checks, Developer approves |

**Workflow:**

```
1. RECEIVE promotion request
2. VALIDATE:
   • All tests passing
   • Coverage thresholds met
   • No critical vulnerabilities
   • Documentation complete
   • Change log updated
3. GENERATE readiness report
4. Developer APPROVES or requests fixes
5. EMIT promotion.approved or promotion.rejected
```

---

## Task Queue Configuration

### Automation Product Owner Queue

```yaml
task_queues:
  - name: apo-queue
    description: "APO tasks for ideation and feedback"
    enrolled_agents:
      - type: human
        role: automation_product_owner
        assignment: round_robin
      
      - type: ai
        agent_id: apo-assistant
        autonomy:
          level: medium
          auto_complete_conditions:
            - "confidence >= 0.85 AND decision NOT IN ['reject', 'clarify']"
          escalate_conditions:
            - "confidence < 0.7"
            - "decision == 'reject'"
            - "requires_business_judgment == true"
    
    escalation:
      ai_to_human:
        enabled: true
        timeout: 30m
      human_escalation:
        enabled: true
        levels:
          - role: senior_apo
            timeout: 4h
```

### PA Queue

```yaml
task_queues:
  - name: pa-queue
    description: "Process Architect tasks for design"
    enrolled_agents:
      - type: human
        role: process_architect
      
      - type: ai
        agent_id: pa-assistant
        autonomy:
          level: medium
          auto_complete_conditions:
            - "task_type == 'sop_generation' AND quality_score >= 0.8"
          escalate_conditions:
            - "involves_new_pattern == true"
            - "cross_domain == true"
    
    escalation:
      ai_to_human:
        enabled: true
        timeout: 1h
```

### Dev Queue

```yaml
task_queues:
  - name: dev-queue
    description: "Developer tasks for implementation"
    enrolled_agents:
      - type: human
        role: developer
      
      - type: ai
        agent_id: dev-assistant
        autonomy:
          level: high
          auto_complete_conditions:
            - "task_type == 'test_diagnosis' AND fix_confidence >= 0.9"
            - "task_type == 'build_resolution' AND resolution_type == 'retry'"
          escalate_conditions:
            - "requires_architecture_change == true"
            - "security_related == true"
    
    escalation:
      ai_to_human:
        enabled: true
        timeout: 2h
```

---

## Related Documentation

- [DevOps Workbench Overview](./README.md)
- [Signal Routing via Atropos](./signal-routing-via-atropos.md)
- [AI Assistant Agents](./ai-assistant-agents.md)
- [Automation Ideation](../../04-subsystems/automation-ideation/README.md)
- [CI Subsystem](../../04-subsystems/ci-subsystem/README.md)

