# Ontology: Execution Layer

**Layer Question:** *"How is it done?"*

The Execution Layer is where **work actually happens**. Here, normative rules and goals are operationalized into **operations**:
- **Procedures** (deterministic steps for a role),
- **Workflows** (deterministic binding of procedures across multiple roles), and
- **Cases** (non-deterministic, evolving collaborations across roles).

These operations prescribe **activities**, which in turn consist of atomic **actions** performed by **agents**—humans or AI—when agent involvement is required, often collaborating as a **Human–AI Team**. Some operations may be fully automated with no agent involvement. Training also lives here, ensuring agents have the skills needed to bridge their capabilities to specific role requirements.

It is the execution muscle: the actual practice of duties under real conditions.

---

**Navigation:** [← Normative Layer](./ontology-2-normative-layer.md) | [Ontology Reference](./ontology-reference.md) | [Automation Layer →](./ontology-4-automation-layer.md)

---

## Table of Contents

- [Operation (abstract)](#operation-abstract)
- [Procedure](#procedure)
- [Workflow](#workflow)
- [Case](#case)
- [Activity](#activity)
- [Task](#task)
- [Escalation](#escalation)
- [Task Queue](#task-queue)
- [Action](#action)
- [Agent](#agent)
- [Human](#human)
- [AI Agent](#ai-agent)
- [Human–AI Team](#humanai-team)
- [Training](#training)

---

## Operation (abstract)
**Definition:** Runtime instance of work invoked by a [Scenario](./ontology-1-perception-layer.md#scenario), instantiated from an [Automation](./ontology-4-automation-layer.md#automation).  
**Kinds:** [Procedure](#procedure), [Workflow](#workflow), [Case](#case).  
**Role:** Prescribes [Activities](#activity) for [Agents](#agent). **Governed by** [SOPs](./ontology-2-normative-layer.md#sop-standard-operating-procedure).  
**Relationships:** Instantiated by [Automation](./ontology-4-automation-layer.md#automation); occurs within [Scenario](./ontology-1-perception-layer.md#scenario); governed by [SOP](./ontology-2-normative-layer.md#sop-standard-operating-procedure).  
**Example:** "Password Reset Operation," "Aircraft Separation Workflow," "Fraud Investigation Case."

**See also:** [Automation](./ontology-4-automation-layer.md#automation), [Activities](#activity), [SOP](./ontology-2-normative-layer.md#sop-standard-operating-procedure)

---

## Procedure
**Definition:** A type of [Operation](#operation-abstract) that represents a sequence of decisions and activities for a **single [Role](./ontology-2-normative-layer.md#role)** to meet its [Goals](./ontology-2-normative-layer.md#goal) in a [Scenario](./ontology-1-perception-layer.md#scenario).  
**Role:** Unit playbook for one role; deterministic sequence of steps.  
**Relationships:** Is an [Operation](#operation-abstract); prescribes [Activities](#activity); executed by a single [Role](./ontology-2-normative-layer.md#role).  
**Note:** Procedures are not limited to deterministic, rule-based sequences. They can include human judgment, creative decision-making, and adaptive activities that rely on human agency and expertise. The term "procedure" refers to the structured approach to work, not the elimination of human discretion.  
**Example:** Analyst procedure: check logs → verify user → reset password.

**See also:** [Operation](#operation-abstract), [Workflow](#workflow), [Case](#case)

---

## Workflow
**Definition:** Deterministic binding of multiple [Procedures](#procedure) across different [Roles](./ontology-2-normative-layer.md#role).  
**Role:** Cross-role orchestration with a defined sequence.  
**Relationships:** Binds [Procedures](#procedure); is an [Operation](#operation-abstract).  
**Example:** New employee onboarding: HR → IT → Manager.

**See also:** [Case](#case), [Automation](./ontology-4-automation-layer.md#automation)

---

## Case
**Definition:** Non-deterministic, evolving collaboration across [Roles](./ontology-2-normative-layer.md#role) to resolve a [Scenario](./ontology-1-perception-layer.md#scenario).  
**Role:** Supports flexible paths; can incorporate new [Signals](./ontology-1-perception-layer.md#signal) over time.  
**Relationships:** Aggregates [Procedures](#procedure); may update with [Signals](./ontology-1-perception-layer.md#signal); collaboration between [Agents](#agent).  
**Note:** Cases handle non-deterministic work within **known scenarios**. For completely unknown scenarios that emerge outside the defined ontology, new scenarios and their corresponding operations must be created through human agency and creative problem-solving.  
**Example:** Security incident response that evolves as new alerts arrive.

**See also:** [Workflow](#workflow), [Signal](./ontology-1-perception-layer.md#signal)

---

## Activity
**Definition:** An operationally observable step performed during an [Operation](#operation-abstract). Represents the **intent** to be achieved.  
**Role:** Track progress within an Operation; each Activity represents a meaningful milestone or step.  
**Relationships:**  
- Prescribed by [Operations](#operation-abstract)  
- Consist of [Actions](#action) (atomic execution steps)  
- **Some** Activities are delegated to [Agents](#agent) as [Tasks](#task)  
- May be fully automated (no Task) or require agent involvement (becomes a Task)  

**Example:**  
- "Receive Alert" (automated, no Task)  
- "Analyze Transaction" (delegated to Security Analyst as a Task)  
- "Notify Customer" (automated, no Task)  

**See also:** [Task](#task), [Actions](#action), [Operation](#operation-abstract)

---

## Task
**Definition:** A **subset of [Activities](#activity)** that require delegation to an [Agent](#agent) (Human or AI).  
**Role:** The assignable, trackable unit of work with ownership, status, and lifecycle. Not all Activities become Tasks—only those requiring agent involvement.  
**Relationships:**  
- A Task **is an** [Activity](#activity) that requires agent involvement  
- Assigned to [Agents](#agent) (Human or AI)  
- Executed within an [Operation](#operation-abstract)  
- May be queued in a Task Queue for assignment  
- Has status (pending, in-progress, completed, cancelled)  
- Consists of [Actions](#action) to achieve the Activity's intent  

**Task Assignment Methods:**
| Method | Description |
|--------|-------------|
| **Direct Assignment** | Assigned to a specific Agent |
| **Queue Assignment** | Placed in a Task Queue for any qualified Agent to pick up |
| **Group Assignment** | Assigned to a group where any member can complete |
| **Delegation** | Transferred from one Agent to another |

**Example:** "Analyze Transaction" assigned to Security Analyst; "Generate Summary Report" delegated to AI Agent.

**See also:** [Activity](#activity), [Agent](#agent), [Actions](#action), [Escalation](#escalation)

---

## Escalation
**Definition:** The process of advancing an unresolved [Task](#task) to the next level in its Escalation Matrix when the current level's threshold is exceeded.  
**Role:** Ensures Tasks are resolved within acceptable timeframes by progressively involving higher-priority or more capable assignees.  
**Relationships:** Governs [Task](#task) lifecycle; references [Roles](./ontology-2-normative-layer.md#role), Groups, or individual [Agents](#agent) at each level.

### Escalation Matrix (EM)

An Escalation Matrix defines the levels through which a [Task](#task) progresses if unresolved:

| Component | Description |
|-----------|-------------|
| **Level** | A stage in the escalation path (0, 1, 2, ...) |
| **Assignee** | Task Queue for a Role, Group, or specific user at that level |
| **Threshold** | Time or condition after which escalation to next level occurs |

**Key Principles:**
- Every [Task](#task) definition has an **implicit Escalation Matrix** with at least one level (Level 0)
- A Task is initially assigned at **Level 0** of its associated EM
- If the Task remains unresolved when the threshold is exceeded, it is assigned to the next level
- Each level represents a task queue for a [Role](./ontology-2-normative-layer.md#role), Group, or named user

**Escalation Flow:**

```
Task Created
     │
     ▼
Level 0 (Initial Assignment)
  └── Assignee: Role/Group/User queue
  └── Threshold: e.g., 4 hours
     │
     │ (threshold exceeded, unresolved)
     ▼
Level 1 (First Escalation)
  └── Assignee: Senior Role/Manager queue
  └── Threshold: e.g., 2 hours
     │
     │ (threshold exceeded, unresolved)
     ▼
Level 2 (Second Escalation)
  └── Assignee: Supervisor/Specialist queue
  └── Threshold: e.g., 1 hour
     │
     ▼
  ... (continues as defined)
```

**Escalation Matrix Example:**

| Level | Assignee | Threshold |
|-------|----------|-----------|
| 0 | Dispute Analyst Queue (Role) | 4 hours |
| 1 | Senior Analyst Queue (Role) | 2 hours |
| 2 | Dispute Manager (User) | 1 hour |
| 3 | Operations Head (User) | 30 minutes |

**Implicit vs. Explicit EM:**
- **Implicit EM**: Every Task has a default single-level EM (Level 0 only, no escalation)
- **Explicit EM**: Task definition specifies multiple levels with thresholds

**Example:** A "Review Disputed Transaction" Task starts with Dispute Analyst queue (Level 0). If unresolved after 4 hours, escalates to Senior Analyst queue (Level 1). If still unresolved after 2 more hours, escalates to Dispute Manager (Level 2).

**See also:** [Task](#task), [Task Queue](#task-queue), [Role](./ontology-2-normative-layer.md#role), [Agent](#agent)

---

## Task Queue
**Definition:** A holding area for [Tasks](#task) awaiting assignment to or pickup by [Agents](#agent).  
**Role:** Enables work distribution based on [Role](./ontology-2-normative-layer.md#role), Group, or individual assignment; supports load balancing and capacity management.  
**Relationships:**  
- Holds [Tasks](#task) pending assignment  
- Associated with [Roles](./ontology-2-normative-layer.md#role), Groups, or specific [Agents](#agent)  
- Referenced in [Escalation](#escalation) Matrix levels  
- Defined within a [Workbench](./ontology-1-perception-layer.md#workbench)  

**Queue Attributes:**

| Attribute | Description |
|-----------|-------------|
| **Name** | Identifier for the queue (e.g., "Dispute Analyst Queue") |
| **Associated Role/Group** | Which Role or Group this queue serves |
| **Capacity** | Optional limit on queue depth |
| **Assignment Strategy** | How tasks are distributed to agents |
| **Priority Rules** | How tasks are ordered within the queue |

**Assignment Strategies:**

| Strategy | Description |
|----------|-------------|
| **FIFO** | First-in, first-out; oldest task assigned first |
| **Priority** | Higher priority tasks assigned first |
| **Round-Robin** | Tasks distributed evenly across available agents |
| **Skills-Based** | Tasks matched to agent skills/capabilities |
| **Load-Balanced** | Tasks assigned to least-loaded agent |

**Task Queue Lifecycle:**

```
Task Created
     │
     ▼
Task Queue (pending)
     │
     ├── Agent picks up (pull model)
     │   or
     └── System assigns (push model)
           │
           ▼
     Agent works on Task
           │
           ▼
     Task Completed/Escalated
```

**Visibility:**
- Agents see tasks in queues they are eligible for (based on Role/Group membership)
- Supervisors see aggregate queue metrics (depth, wait time, throughput)
- Access controlled per [Workbench](./ontology-1-perception-layer.md#workbench)

**Example:** "Dispute Analyst Queue" holds dispute review tasks. Agents with "Dispute Analyst" role can pick tasks from this queue. If a task remains in queue beyond threshold, it escalates to "Senior Analyst Queue".

**See also:** [Task](#task), [Escalation](#escalation), [Role](./ontology-2-normative-layer.md#role), [Agent](#agent), [Workbench](./ontology-1-perception-layer.md#workbench)

---

## Action
**Definition:** Atomic executable step taken to achieve an [Activity's](#activity) intent.  
**Role:** The actual execution—the "doing" that advances an Activity toward completion.  
**Relationships:** Compose [Activities](#activity); may invoke [Tools](./ontology-4-automation-layer.md#tool-abstract); may involve inline [Decisions](./ontology-2-normative-layer.md#decision).  

> **Clarification:** Actions may invoke [Tools](./ontology-4-automation-layer.md#tool-abstract) (Commands, Decision Applications, Prediction Applications, etc.) to effect change or to aid decisions. The Action is the execution; the Tool is the capability being used.  

**Action Types:**
| Type | Description | Example |
|------|-------------|---------|
| **Command Invocation** | Invoke an actuator/API on a [Machine](./ontology-1-perception-layer.md#machine) | Call `/lockAccount`, restart service |
| **Inline Decision** | Make a decision without a Decision Application | Choose next step based on data |
| **Data Operation** | Read, transform, or write data | Fetch customer history, update record |
| **Communication** | Send notification or message | Email customer, post to Slack |
| **Observation** | Log, record, or emit a signal | Write audit log, emit metric |

**Example:** "Check OTP," "Call API /lockAccount," "Update ticket status," "Decide to escalate."

**See also:** [Activity](#activity), [Tool](./ontology-4-automation-layer.md#tool-abstract), [Command / Actuator](./ontology-4-automation-layer.md#command--actuator), [Decision](./ontology-2-normative-layer.md#decision)

---

## Agent
**Definition:** Performer of work—human or AI.  
**Role:** Plays [Roles](./ontology-2-normative-layer.md#role), makes [Decisions](./ontology-2-normative-layer.md#decision), uses [Tools](./ontology-4-automation-layer.md#tool-abstract), performs [Activities](#activity), receives [Tasks](#task).  
**Relationships:** Specialized into [Human](#human) and [AI Agent](#ai-agent); enabled by/has [Capabilities](./ontology-2-normative-layer.md#capability); limited by [Capacity](./ontology-2-normative-layer.md#capacity); assigned [Tasks](#task).  
**Note:** Agent is an abstract concept that encompasses both Human and AI agents. Agents are not merely process executors—they exercise judgment, creativity, and agency. Human agents bring unique capabilities for creative problem-solving, ethical reasoning, and handling novel situations, while AI agents provide computational power, pattern recognition, and automation capabilities. The collaboration between human and AI agents leverages the strengths of both.

**See also:** [Human–AI Team](#humanai-team), [Tool](./ontology-4-automation-layer.md#tool-abstract), [Task](#task), [Capability](./ontology-2-normative-layer.md#capability), [Capacity](./ontology-2-normative-layer.md#capacity)

---

## Human
**Definition:** A human participant in operations who exercises judgment, creativity, and accountability. Humans are [Agents](#agent) with unique cognitive and social capabilities.  
**Role:** Performs [Activities](#activity), makes [Decisions](./ontology-2-normative-layer.md#decision), collaborates with [AI Agents](#ai-agent), and provides oversight for automated processes.

**Unique Value of Human Agents:**

| Capability | Description | Banking Example |
|------------|-------------|-----------------|
| **Contextual Reasoning** | Understanding nuance and exceptions | Recognizing a legitimate transaction that looks fraudulent |
| **Ethical Judgment** | Making value-based decisions | Deciding whether to waive a fee for a long-standing customer |
| **Empathy** | Understanding customer emotions | De-escalating an angry customer during a dispute |
| **Creative Problem-Solving** | Handling novel situations | Finding a solution for an unusual regulatory scenario |
| **Accountability** | Taking responsibility for outcomes | Signing off on a high-value credit decision |

**When Humans Are Essential:**
- High-stakes decisions with significant consequences
- Novel situations not covered by existing [SOPs](./ontology-2-normative-layer.md#sop-standard-operating-procedure)
- Customer interactions requiring empathy
- Regulatory attestations and sign-offs
- Ethical dilemmas and judgment calls

**Banking Examples:**
- **Dispute Resolution:** Understanding the customer's story beyond transaction data
- **Credit Exceptions:** Approving a loan outside standard criteria based on context
- **Fraud Investigation:** Interviewing customers and merchants
- **Compliance Escalations:** Determining SAR filing requirements

**See also:** [Agent](#agent), [Human–AI Team](#humanai-team), [AI Agent](#ai-agent)

---

## AI Agent
**Definition:** A software agent capable of autonomous perception, decision-making, and action within defined boundaries. AI Agents are [Agents](#agent) that operate programmatically, often using machine learning or rule-based systems.  
**Role:** Performs high-volume, repetitive, or data-intensive [Tasks](#task); assists [Humans](#human) with analysis and recommendations; executes [Commands](./ontology-4-automation-layer.md#command--actuator) on [Machines](./ontology-1-perception-layer.md#machine).

**AI Agent Capabilities:**

| Capability | Description | Banking Example |
|------------|-------------|-----------------|
| **Pattern Recognition** | Detecting anomalies in large datasets | Identifying fraud patterns across millions of transactions |
| **Document Processing** | Extracting information from documents | Reading and classifying KYC documents |
| **Natural Language** | Understanding and generating text | Summarizing customer communication history |
| **Predictive Analytics** | Forecasting outcomes | Predicting probability of loan default |
| **Process Automation** | Executing repetitive workflows | Auto-populating forms, sending notifications |

**AI Agent Operating Modes:**

| Mode | Description | Banking Example |
|------|-------------|-----------------|
| **Autonomous** | Acts independently within policy bounds | Auto-approving low-risk transactions |
| **Assistive** | Recommends actions for human approval | Suggesting dispute resolution outcome |
| **Supervised** | Human must approve before action | Recommending account closure |
| **Monitoring** | Observes and alerts, no action | Watching for unusual patterns |

**Governance and Oversight:**
- AI Agents operate under policies defined by [SOPs](./ontology-2-normative-layer.md#sop-standard-operating-procedure)
- High-stakes decisions require human oversight
- Actions are logged for audit and compliance
- Confidence thresholds determine when to escalate to humans

**Banking Examples:**
- **Transaction Scorer:** Assigns risk score to each transaction in real-time
- **Document Classifier:** Categorizes incoming customer documents (ID, proof of address, etc.)
- **Chatbot Agent:** Handles routine customer inquiries and escalates complex issues
- **Reconciliation Agent:** Matches transactions between systems and flags exceptions

**See also:** [Agent](#agent), [Tool](./ontology-4-automation-layer.md#tool-abstract), [Human](#human), [Human–AI Team](#humanai-team)

---

## Human–AI Team
**Definition:** Group of [Agents](#agent) (human + AI) collaborating in an [Operation](#operation-abstract).  
**Role:** Execute multi-role work.  
**Relationships:** Composed of [Agents](#agent); interacts with the [Automation Runtime](./ontology-4-automation-layer.md#automation-system).

**See also:** [Workflow](#workflow), [Case](#case)

---

## Training
**Definition:** **Pre-deployment** learning to equip [Agents](#agent) with role-specific skills—bridging general [Capability](./ontology-2-normative-layer.md#capability) to a specific [Role](./ontology-2-normative-layer.md#role) and its [Responsibilities](./ontology-2-normative-layer.md#responsibility).  
**Role:** Ensures agents are qualified to perform their duties; required before agents can be assigned [Tasks](#task).  
**Relationships:** Develops [Capabilities](./ontology-2-normative-layer.md#capability); may reference [SOPs](./ontology-2-normative-layer.md#sop-standard-operating-procedure); required for [Role](./ontology-2-normative-layer.md#role) assignment.

**Training for Human vs. AI Agents:**

| Aspect | Human Agent Training | AI Agent Training |
|--------|---------------------|-------------------|
| **Method** | Courses, mentorship, certification | Model training, fine-tuning, prompt engineering |
| **Content** | SOPs, regulations, tools, soft skills | Training data, examples, rules, guardrails |
| **Validation** | Exams, assessments, observation | Testing, validation datasets, A/B testing |
| **Ongoing** | Refresher training, updates | Model updates, continuous learning |

**Banking Training Examples (Human):**
- **Dispute Analyst Training:** Card network rules (Visa, Mastercard), investigation techniques, customer communication
- **AML Analyst Training:** BSA/AML regulations, CAMS certification, SAR writing
- **Credit Underwriter Training:** Credit policy, financial analysis, regulatory requirements

**Banking Training Examples (AI):**
- **Fraud Model Training:** Historical fraud patterns, feature engineering, threshold calibration
- **Document Classifier Training:** Labeled document examples, OCR optimization, accuracy validation
- **Chatbot Training:** Intent recognition, response templates, escalation rules

**Training Lifecycle:**
```
Identify Role Requirements
         │
         ▼
Design Training Curriculum
         │
         ▼
Deliver Training (Human) / Train Model (AI)
         │
         ▼
Assess Competency
         │
         ▼
Certify for Role ──► Agent can receive Tasks
         │
         ▼
Ongoing Development / Model Updates
```

**See also:** [Capability](./ontology-2-normative-layer.md#capability), [SOP](./ontology-2-normative-layer.md#sop-standard-operating-procedure), [Role](./ontology-2-normative-layer.md#role), [Agent](#agent)

---

**Navigation:** [← Normative Layer](./ontology-2-normative-layer.md) | [Ontology Reference](./ontology-reference.md) | [Automation Layer →](./ontology-4-automation-layer.md)

