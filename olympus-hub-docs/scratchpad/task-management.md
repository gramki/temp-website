
# Task Management

Basic premise, Hub Applications can delegate task to agents in the Workbench they belong to. They do this by emiting tasks and allowing SX to assign them to Agents based on the Scenario and Workbench settings. SX relies on the Task Management systemt to observe the tasks created and assign them to the agents. Task management system is also responsible track the task to closure by escalating them and alerting relevant stakeholders about the SLA breaches.

SX keeps Hub Application informed about any task status changes. Technically, SX informs Application Runtime and it inturn delegates the update to the Hub Application. The exact contract between Application Runtime and its' Application are specific to each runtime and are not part of this document.

Application --- (create task) --> Request -- (Assign Task to Agent) --> Agent
Agent --- (Update Task) --> Request ---- (Report Task update) ---> Application 

From this perspective an Application is an orchestrator of updates from Agents regarding their tasks. 


## Task Queue at a Workbench scope;
* A Task created in a request is assigned to an agent through a Task Queue. 
* A Task Queue has a group of agents as canddiates for task assignment - Using 'role', 'user-group', or by explicitly listing them
* User can be madually added or removed by supervisor

### Specifying candidate agents for a Task Queue
When defining a task queue, the candidate agents can be specified using any of the logical references:
* IAM Role
* IAM User Group
* Role associated with Workbench (Supervisor, Administrator) - These are named users in the Workbench configuration. Hub creates a User Group per each such role for each Workbench.
* Role Associated with the Request (Subject, Originator, All assignees, All Actors) - These are dynamically resolved per request per task action. 

These logical references can be used for specifying candidates for each level in the Escalation Matrix of the Task Queue. By default, a task starts at level zero of the Escalation Matrix of the Task Queue.

## Task Allocation and Workload Balancing
* A Task Queue has an associated Allocation Alorithm; 
* Every task orginating from a Hub Application (or otherwise) is attributed to a Task Queue for completion. 
* There is a default Task Queue configured per Workbench to assign tasks that are not assigned to task queue at the time of creation.
* Scenario specification can provide the default task queue that overrides Workflow's default task queue.
* Allocation may happen only when an agent is available, or assignment may happen immediately on task arrival. Task Management system may periodically review assignments and change them to rebalance the workload. All such allocation behavior is governed by the allocation algorithm. Each Allocation Algorithm may provide some parameters that can be tuned per queue. 
* All allocation algorithms to be available are outside the scope of the current discussion. <You can add a couple of algorithms as placeholders>

### Escalation Matrix
- Every Task Queue has an associated escalation matrix. 
- The default level is zero.
- Tasks are escalated to agents at higher level based on the threshold time for escalation, for a pending task.
-- Escalation Thresholds (per level, threshold duration in minutes and the agents (by IAM role, by group, by explicit names, by role-in-request, by role-in-scenario, by role-in-workbench) )
-- Escalation Level <1..N> assignee 
-- All agents at all levels the task is escalated to is an 'assignee' of the task
-- All assignees at all levels are actors associted with Request 
-- Any agent who may have ever been associated with the request (through any task at any escalation level) is an actor asscoaited with the Request


### Manual Task reassignment
Depending on the configuration settings on the scenario, a task may be manually reassigned at each escalation level to other users in that or higher escalation level.

A Supervisor should be able to change the assignee at any level at any time until the task is completed.

## Special Task Queues
- Subject Task Queue: The agents are resolved by the request-specific-role - subject at EL 0. Next levels are Scenario specific. 
- Request Originator Task Queue: The agents are resolved by the request-specific-role - subject at EL 0. Next levels are Scenario specific. 
- Supervisor Task Queue: The agents are resolved by the workbench-specific-role - supervisor at EL 0. Next levels are Workbench specific.


## How does an Agent work on a Task
1. An agent is notified about the tasks assigned to them (optional, based on workbench,scenario configurations and agent preferences)
2. Agent can retrieve tasks assigned to him through any UX channels (Agent Desk, MS Teams, MCP, etc.,)
3. Agent uses the Task Solver Component to understand the task and request context and takes an action that could mark the task a complete or assign the task to someone else.
4. Agent can add Memos and Thoughts as they may please at any scope - task, request, subject, etc.,
5. If configuration on the task permitting, Agent may opt-out abandon the task without explicitly assigning to any other agent. This goes back to allocation.


[5 tools called]

I have the context. Before I proceed, I have a few clarifying questions:

## Clarification Questions

### 1. Task Creation Source
You mentioned "Hub Applications can delegate task to agents" and tasks can originate from "Hub Application (or otherwise)". What are the other sources besides Hub Applications?
- Can Supervisors create tasks directly? 
> Yes, through any channel available.
- Can agents create tasks (e.g., delegate to another agent)? 
> Yes, if permitted in the scenario.
- Can external systems create tasks via signals? 
> Yes, what an agent can do any other authorized enteprise system can also do. 

Every Task any agent or system may create must be a supported task in the scenario. All such supported tasks will have a task creation template that should be used by the agents to provide necessary information to create and solve the task.

### 2. Task vs Task Queue Relationship
- Is a Task always attributed to exactly one Task Queue at any point in time?
> Yes
- When a task is escalated, does it stay in the same queue (just with higher escalation level), or can it move to a different queue?
> Task queue is same. Allocations are done per escalation level. The 'Task Queue' here is not same as the queue/inbox of an agent. This is a conceptual 'set' of tasks that are outstanding and are logically grouped.

### 3. Task Assignment vs Task Allocation
- **Allocation** = Task Management system assigns task to an agent from the queue
- **Assignment** = The result of allocation (agent is now assigned)
Is this interpretation correct? Or is there a distinction between system-driven allocation and manual assignment?
> Allocation is the process followed by the Allocation algorithm. Assginment is the result.

### 4. Multiple Assignees at Escalation
You said "All agents at all levels the task is escalated to is an 'assignee' of the task". 
- Does this mean multiple agents can be working on the same task simultaneously?
> Yes, technically. However, the first one to complet the task wins. Practically, when a task is escalated, the agent to who it is escalted is working on it or nudging the lower level to work on it.
- Or is there still one "active assignee" and others are "notified escalation recipients"?
> No all levels are 'active' assignees.

### 5. Task Completion Authority
- Can any assignee at any escalation level mark the task as complete?
> Yes
- Or only the agent at the current (highest) escalation level?


### 6. SLA Breach vs Escalation
- Escalation happens based on threshold time for a **pending** task
- What about SLA breach alerting? Is it:
  - Same as escalation (triggers escalation)?
  - Separate from escalation (alerts stakeholders but doesn't change assignees)?
  - Both (escalates AND alerts)?
> SLA is a different concepts from Escalation.
> SLA give contracted time to complete the task. Ideally, the escalations should happen well before the SLA is breached to give time for the newly assigned agent. But thes configurations are left to supervisors.
### 7. Agent Opt-Out / Abandon
You mentioned agents can "opt-out abandon the task without explicitly assigning to any other agent. This goes back to allocation."
- Does the task return to the same queue at the same escalation level?
> Yes
- Is there any tracking of abandon history (e.g., to avoid re-assigning to same agent)?
> Yea, all agent actions are captured as request scoped memos.

### 8. Request-Scoped Roles Resolution
For "Subject, Originator, All assignees, All Actors" - these are resolved per request. 
- Are these resolved at task creation time (snapshot) or dynamically (e.g., "All Actors" grows as more agents touch the request)?
> These are resolved at every instance of the allocation algorithm run.
> These are also resolved when any agent asks for this information

### 9. Task Solver Component
You mentioned "Agent uses the Task Solver Component to understand the task and request context". 
- Is Task Solver a UI component, an AI assistant, or something else?
> UI Component.
- Is it part of Task Management or a separate subsystem?
> Check the UX Architecture. 