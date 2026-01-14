# 24.3 Agent Task Operations

Agents (human and AI) work on tasks through operations that enable them to accept tasks, update progress, and complete tasks with outcomes. Agent task operations are available through multiple channels (Web Portal, MS Teams, MCP) and support various workflows (task acceptance, progress updates, completion, hold/resume, reassignment, abandonment).

Agent task operations are a critical capability that enables agents to work effectively on tasks, providing them with the tools they need to understand task context, make decisions, and complete work. Agent operations integrate with Task Solver Interface for context-rich task views, Signal Exchange for observability, and Notification Services for task notifications.

## Purpose of this Subsection

This subsection describes how agents work on tasks. It explains task acceptance, task updates, task completion, and how agent operations integrate with Task Solver Interface and multiple access channels.

## Core Concepts & Definitions

### Task Discovery

**Task Discovery** is the process by which agents retrieve their assigned tasks through multiple channels:
*   **Agent Desk (Tasks Console)**: Primary interface for viewing and managing tasks
*   **MS Teams**: Tasks appear as actionable cards in Teams
*   **MCP (Agent Gateway)**: AI agents retrieve tasks programmatically
*   **Mobile App**: Mobile access to tasks

Task Discovery enables agents to access tasks through their preferred channels.

### Task Solver Interface

The **Task Solver Interface** is a UX component that provides agents with context and actions for completing tasks. Task Solver:
*   **Is Custom per Task Type**: Each task type has its own solver template
*   **Is Developer-Defined**: Workbench developers create solver templates in Workbench Studio
*   **Is Context-Rich**: Presents all relevant information for decision-making
*   **Is Action-Oriented**: Clear paths to completion

Task Solver Interface enables agents to work effectively on tasks with rich context.

### Agent Operations

**Agent operations** are actions that agents can perform on tasks:

| Operation | Description |
|-----------|-------------|
| **Start Work** | Agent indicates they are starting work on a task |
| **Complete Task** | Agent marks task as complete with an outcome |
| **Place on Hold** | Agent pauses work waiting for external input |
| **Resume Work** | Agent resumes work after hold |
| **Add Memo** | Agent adds notes at various scopes |
| **Add Thought** | Agent adds private working notes |
| **Reassign Task** | Agent reassigns task to another agent (if permitted) |
| **Abandon Task** | Agent opts out of task without explicit reassignment |

Agent operations enable agents to work effectively on tasks.

### Supervisor Operations

**Supervisor operations** are elevated privileges for task management:

| Operation | Description |
|-----------|-------------|
| **View All Tasks** | Supervisors can view all tasks in their workbench |
| **Reassign Any Task** | Supervisors can reassign tasks regardless of Scenario settings |
| **Cancel Task** | Supervisors can cancel tasks |
| **Add/Remove Queue Agents** | Supervisors can manually add or remove agents from queue candidates |
| **Force Escalation** | Supervisors can manually escalate a task |
| **SLA Override** | Supervisors can extend SLA deadlines |

Supervisor operations enable supervisors to manage tasks effectively.

## Conceptual Models / Frameworks

### The Agent Task Workflow Model

Agents work on tasks through a workflow:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          AGENT TASK WORKFLOW                                 │
│                                                                              │
│  1. NOTIFICATION (optional)                                                  │
│     └── Agent notified of new task assignment                                │
│         (based on workbench, scenario, and agent preferences)                │
│                                                                              │
│  2. DISCOVERY                                                                │
│     └── Agent retrieves assigned tasks through UX channels                   │
│         • Agent Desk (Tasks Console)                                         │
│         • MS Teams                                                           │
│         • MCP (Agent Gateway)                                                │
│         • Mobile app                                                         │
│                                                                              │
│  3. INVESTIGATION                                                            │
│     └── Agent uses Task Solver to understand task and request context        │
│         • Read-only view for investigation                                   │
│         • Access to request history, memos, related tasks                    │
│         • Knowledge base and SOP lookup                                      │
│                                                                              │
│  4. ACTION                                                                   │
│     └── Agent takes action to progress the task                              │
│         • Complete task with outcome                                         │
│         • Add memos/thoughts                                                 │
│         • Reassign to another agent (if permitted)                           │
│         • Place on hold (waiting for external input)                        │
│         • Abandon task (if permitted)                                       │
│                                                                              │
│  5. COMPLETION                                                               │
│     └── Task marked complete or moved to next state                          │
│         • Result payload captured                                            │
│         • Hub Application notified                                           │
│         • Request progresses                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

This model ensures that agents can work effectively on tasks with rich context and clear actions.

### The Task Solver Interface Model

Task Solver provides context and actions:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TASK SOLVER                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  TASK HEADER                                                             ││
│  │  Task: Verify KYC Documents | Request: REQ-1234 | SLA: 45min remaining  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────────┐ │
│  │  REQUEST CONTEXT             │  │  TASK DETAILS                        │ │
│  │                              │  │                                      │ │
│  │  Customer: John Smith        │  │  Documents to Verify:                │ │
│  │  Subject ID: cust-67890      │  │  • Passport                          │ │
│  │  Scenario: Dispute           │  │  • Utility Bill                      │ │
│  │  Resolution                  │  │                                      │ │
│  │                              │  │  Instructions:                       │ │
│  │  Request Status: Active      │  │  Verify identity documents           │ │
│  │  Created: 2 hours ago        │  │  match customer record               │ │
│  └──────────────────────────────┘  └──────────────────────────────────────┘ │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  ATTACHED DOCUMENTS                                                      ││
│  │  📄 passport.pdf    📄 utility_bill.pdf                                  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  ACTIONS                                                                 ││
│  │                                                                          ││
│  │  [✓ Approve]  [✗ Reject]  [⏸ Hold]  [↗ Reassign]  [Abandon]             ││
│  │                                                                          ││
│  │  Notes: _______________________________________________                  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

This model ensures that agents have rich context and clear actions for completing tasks.

## Systemic and Enterprise Considerations

### Multi-Channel Access

Agent operations are available through multiple channels:
*   **Web Portal (Agent Desk)**: Primary interface for task management
*   **MS Teams**: Tasks appear as actionable cards; agents can complete tasks in Teams
*   **MCP (Agent Gateway)**: AI agents retrieve and complete tasks programmatically
*   **Mobile App**: Mobile access to tasks for on-the-go work

Multi-channel access enables agents to work from anywhere, increasing productivity and responsiveness.

### Task Solver Customization

Task Solver is customized per task type:
*   **Solver Templates**: Each task type has its own solver template
*   **Developer-Defined**: Workbench developers create solver templates in Workbench Studio
*   **Context-Rich**: Solver templates include request context, task details, attached documents, and actions
*   **Action-Oriented**: Solver templates provide clear paths to completion

Task Solver customization ensures that agents have task-specific context and actions.

### Memo and Thought Scopes

Agents can add memos and thoughts at various scopes:

| Scope | Description |
|-------|-------------|
| **task** | Attached to specific task |
| **request** | Attached to the request |
| **subject** | Attached to the subject (e.g., customer) |

Memo and thought scopes enable agents to capture context at appropriate levels.

### Operation Permissions

Operation permissions are controlled by:
*   **Scenario Configuration**: Scenario settings control which operations are permitted
*   **Agent Role**: Agent role determines which operations are available
*   **Supervisor Privileges**: Supervisors have elevated privileges for task management

Operation permissions ensure that agents can only perform operations they are authorized to perform.

### Directability Operations

When an agent's output is **rejected** (by guardrails, policies, or applications), an escalation task is created for human intervention. Directability operations handle escalation task resolution:
*   **Acknowledge Escalation**: Human acknowledges they are reviewing the rejection
*   **Override Decision**: Human overrides the rejected decision with a new value
*   **Change Context and Re-run**: Human modifies context and requests agent to re-run
*   **Reassign to Alternative Agent**: Human reassigns the original task to a different agent
*   **Fail Scenario**: Human decides to fail the scenario due to unresolvable rejection
*   **Create Corrective Action**: Human creates a corrective action in a different scenario

Directability operations enable human intervention when agent outputs are rejected.

## Common Misconceptions & Failure Modes

### Misconception: AI Agents Cannot Abandon Tasks

Some organizations assume that AI agents cannot abandon tasks. However, AI agents can abandon tasks using the same mechanisms as human agents, and there is no conceptual difference between Human Agents and AI Agents in Task Management.

**Failure mode**: Organizations design systems where AI agents cannot abandon tasks, forcing them to complete tasks they cannot handle, reducing productivity and quality.

### Misconception: Task Solver Is Optional

Some organizations assume that Task Solver is optional. However, Task Solver provides essential context and actions for completing tasks, and agents need rich context to work effectively.

**Failure mode**: Organizations skip Task Solver customization, resulting in agents working with insufficient context, reducing productivity and quality.

### Misconception: All Operations Are Available to All Agents

Some organizations assume that all operations are available to all agents. However, operation permissions are controlled by Scenario configuration and agent role, and supervisors have elevated privileges.

**Failure mode**: Organizations grant all operations to all agents, causing confusion and potential misuse.

## Practical Implications

### Task Solver Design

Organizations should design Task Solver templates that:
*   **Provide Rich Context**: Include request context, task details, attached documents, and related information
*   **Enable Clear Actions**: Provide clear paths to completion with appropriate actions
*   **Support Investigation**: Enable agents to investigate task context before taking action
*   **Match Task Complexity**: Solver templates match the complexity of the task type

Task Solver design directly impacts agent productivity and work quality.

### Operation Configuration

Organizations should configure operations that:
*   **Match Agent Capabilities**: Operations match agent capabilities and authorization
*   **Support Workflows**: Operations support organizational workflows
*   **Enable Flexibility**: Operations enable agents to handle edge cases and exceptions
*   **Maintain Governance**: Operations maintain governance and audit requirements

Operation configuration directly impacts agent productivity and organizational compliance.

## Cross-References

*   **Section 24.1 (Task Lifecycle)**: Describes task states that agent operations affect
*   **Section 24.2 (Task Allocation)**: Describes how tasks are allocated to agents
*   **Section 23.1 (MS Teams Integration)**: Describes MS Teams as a channel for agent operations
*   **Section 12.4 (Deep Observability)**: Describes how Signal Exchange provides agent operation observability

---

**References:**

*   `olympus-hub-docs/04-subsystems/task-management/agent-task-operations.md` — Agent task operations design
*   `olympus-hub-docs/04-subsystems/task-management/task-lifecycle.md` — Task lifecycle design
