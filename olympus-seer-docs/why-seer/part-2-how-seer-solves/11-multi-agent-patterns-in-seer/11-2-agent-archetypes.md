# 11.2 Agent Archetypes

Seer categorizes agents into four functional archetypes based on what they do in the collaboration. These are perspectives, not exclusive categories—a single agent may wear multiple hats depending on context.

## The Four Archetypes

| Archetype | Primary Function | Question Answered |
|-----------|------------------|-------------------|
| **Thinker** | Reasoning and decisions | *What should be done?* |
| **Doer** | Executing actions | *How do I do it?* |
| **Orchestrator** | Assigning and coordinating work | *Who should do what?* |
| **Governor** | Observing and auditing | *Is this appropriate?* |

## Thinker

The Thinker archetype focuses on reasoning, analysis, and decision-making.

### Characteristics

| Aspect | Description |
|--------|-------------|
| **Core function** | Analyze information, form judgments, make decisions |
| **Inputs** | Context, evidence, policies, precedents |
| **Outputs** | Decisions, recommendations, assessments |
| **Rejectable artifacts** | Decision Request, Decision Result |

### Examples

- **Document Analyst:** Reviews documents, determines authenticity
- **Risk Assessor:** Evaluates risk factors, provides risk score
- **Eligibility Checker:** Applies policy rules to determine eligibility

### Governance

Thinkers are subject to:
- Authority ceilings on decision values
- Approval requirements for high-stakes decisions
- Audit logging of all decisions with rationale

## Doer

The Doer archetype focuses on executing actions and producing tangible results.

### Characteristics

| Aspect | Description |
|--------|-------------|
| **Core function** | Execute actions, invoke tools, produce results |
| **Inputs** | Instructions, parameters, context |
| **Outputs** | Action results, side effects |
| **Rejectable artifacts** | Action Request, Action Result |

### Examples

- **Notification Sender:** Sends emails, SMS, or push notifications
- **Data Updater:** Updates records in operational systems
- **Report Generator:** Creates formatted reports

### Governance

Doers are subject to:
- Tool access policies (which tools can be invoked)
- Rate limits (how often actions can be taken)
- Approval gates for sensitive actions

## Orchestrator

The Orchestrator archetype focuses on coordinating work across multiple agents.

### Characteristics

| Aspect | Description |
|--------|-------------|
| **Core function** | Assign tasks, coordinate agents, manage workflow |
| **Inputs** | Goals, agent capabilities, current state |
| **Outputs** | Task assignments, workflow updates |
| **Rejectable artifacts** | Task Assignment |

### Examples

- **Case Orchestrator:** Manages a case through its lifecycle
- **Workflow Coordinator:** Coordinates multi-step processes
- **Dispatch Agent:** Routes work to appropriate specialists

### Governance

Orchestrators are subject to:
- Delegation limits (who they can assign work to)
- Scope boundaries (which scenarios they manage)
- Audit of all assignments and coordination decisions

## Governor

The Governor archetype focuses on observation, auditing, and compliance.

### Characteristics

| Aspect | Description |
|--------|-------------|
| **Core function** | Monitor, audit, flag issues |
| **Inputs** | Observations, records, policies |
| **Outputs** | Observations, alerts, flags (non-rejectable) |
| **Rejectable artifacts** | None—observations are facts |

### Examples

- **Compliance Monitor:** Watches for policy violations
- **Quality Auditor:** Samples decisions for quality review
- **Drift Detector:** Monitors for behavioral drift

### Governance

Governors are subject to:
- Read-only access (cannot modify data)
- Observation scope limits
- Audit of observation and flagging activities

## Archetype Combinations

A single agent may embody multiple archetypes:

| Agent | Primary | Secondary |
|-------|---------|-----------|
| **Dispute Analyst** | Thinker | Doer (sends notifications) |
| **Case Manager** | Orchestrator | Thinker (decides priorities) |
| **Supervisor Bot** | Governor | Orchestrator (escalates) |

### Conflict Resolution

When archetypes conflict, governance rules apply:

| Situation | Resolution |
|-----------|------------|
| Orchestrator assigns to self | Prevented by policy (conflicts of interest) |
| Governor modifies data | Prevented by access controls |
| Thinker bypasses Orchestrator | Task management routes all work |

## Archetype-Specific Desk Access

Each archetype has different desk access needs:

| Archetype | Primary Desk | Purpose |
|-----------|--------------|---------|
| **Thinker** | Agent Desk | Access to context, tools, decisions |
| **Doer** | Agent Desk | Access to tools, execution |
| **Orchestrator** | Supervisor Desk | Queue management, assignments |
| **Governor** | Compliance Desk | Audit access, observation |

---

**References:**
*   `olympus-seer-docs/WHY-SEER-OUTLINE-DRAFT.md` — Section 5.9, Agent Archetypes
*   `olympus-hub-docs/04-subsystems/task-management/README.md`
