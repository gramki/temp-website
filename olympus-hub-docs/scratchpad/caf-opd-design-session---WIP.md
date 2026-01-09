# CAF OPD & Enterprise Learning Services — Design Session

> **Status:** 🟡 Working Document — Q&A in progress
> **Goal:** Comprehensive design for CAF implementation of AOSM OPD requirements + Enterprise Learning Services
> **Gap Reference:** HUB-CAF-010, HUB-CAF-005

---

## Part 1: AOSM OPD Foundation

### 1.1 OPD Recap (From AOSM)

| Element | Definition | Two Senses |
|---------|------------|------------|
| **Observability** | Ability to understand a teammate's state | Capability (agent→env) / Property (others→agent) |
| **Predictability** | Ability to understand what teammate will do | Capability / Property |
| **Directability** | Ability to require/request teammate to act | Capability / Property |

For CAF, we focus on **OPD as Property** — making AI agents observable, predictable, and directable BY humans and other agents in the HAT.

### 1.2 Role-Based OPD Scopes (From AOSM)

| HAT Role | Observability Scope | Directability Scope |
|----------|---------------------|---------------------|
| **Delegator** | All activities of agents they delegated to | Full direction within delegation scope |
| **Team Member** | Relevant activities to coordinate | Based on coordination needs |
| **Supervisor/Overwatch** | All activity, deviations, failures | Review, intervention, correction |
| **Accountable Human** | All activity with explanations | Kill-switch, revocation, override |

---

## Part 2: Cognitive Operations Personas

> **Q2.1:** Please introduce the personas you have in mind for cognitive operations in an enterprise setting.

**Persona Template:**

| Attribute | Description |
|-----------|-------------|
| **Name/Title** | |
| **Role in HAT** | Delegator / Team Member / Supervisor / Accountable |
| **Primary Responsibilities** | |
| **OPD Needs** | What do they need to observe? Predict? Direct? |
| **Cognitive Operations Involvement** | How do they interact with agents, memory, learning? |

### Personas (To be filled)

#### Persona 1: [Name]
<!-- User to provide -->

#### Persona 2: [Name]
<!-- User to provide -->

#### Persona 3: [Name]
<!-- User to provide -->

#### Persona 4: [Name]
<!-- User to provide -->

---

## Part 3: Observability — Q&A

### 3.1 State Exposure

> **Q3.1.1:** What agent state should be visible to each persona?
> 
> Examples: Current task, decision being made, evidence being considered, confidence level, tool invocations, memory retrievals

| Persona | Visible State Elements |
|---------|----------------------|
| | |

> **Q3.1.2:** Should observability be real-time, near-real-time, or retrospective?

| Observability Mode | Use Case | Implementation |
|-------------------|----------|----------------|
| Real-time | ? | ? |
| Near-real-time | ? | ? |
| Retrospective | ? | ? |

> **Q3.1.3:** How does CAF's Episodic Memory relate to observability?
> - Decision Records as "what was decided"
> - Context Records as "what was known"
> - Evidence Bundles as "what was considered"

---

### 3.2 Monitoring Mechanisms

> **Q3.2.1:** What monitoring mechanisms should CAF provide or integrate with?

| Mechanism | Description | Persona(s) Served |
|-----------|-------------|-------------------|
| Live dashboard | ? | ? |
| Alert/notification | ? | ? |
| Audit trail query | ? | ? |
| Activity stream | ? | ? |

> **Q3.2.2:** How should CAF integrate with Olympus Watch for operational observability vs. cognitive observability?

| Aspect | Olympus Watch | CAF/Enterprise Memory |
|--------|---------------|----------------------|
| Purpose | | |
| Content | | |
| Consumers | | |

---

## Part 4: Predictability — Q&A

### 4.1 Behavior Models

> **Q4.1.1:** What defines an agent's expected behavior?

| Behavior Source | Description | Where Defined |
|-----------------|-------------|---------------|
| Guardrails | ? | Seer Training Spec |
| SOPs | ? | Hub Scenario Spec |
| Decision Criteria | ? | ? |
| Constraints | ? | ? |

> **Q4.1.2:** How should CAF catalog/reference an agent's behavior model for predictability?

---

### 4.2 Guardrail Evidence

> **Q4.2.1:** Should guardrail activations be recorded in Enterprise Memory?

| Record Type | Content | Purpose |
|-------------|---------|---------|
| Guardrail Activation | ? | ? |
| Guardrail Suppression | ? | ? |
| Boundary Approach | ? | ? |

> **Q4.2.2:** How does predictability relate to "controlled autonomy"?

---

### 4.3 Counterfactuals

> **Q4.3.1:** When should counterfactual explanations be generated?

| Trigger | Example | Generator |
|---------|---------|-----------|
| On demand | ? | ? |
| Automatic (high-impact) | ? | ? |
| Post-outcome variance | ? | ? |

---

## Part 5: Directability — Q&A

### 5.1 Override Mechanisms

> **Q5.1.1:** What types of human directives should be recorded?

| Directive Type | Description | Record Type |
|----------------|-------------|-------------|
| Override | Countermand agent decision | Override Record ✓ |
| Guidance | Adjust approach without stopping | ? |
| Constraint Addition | Add new boundary | ? |
| Kill-switch | Emergency stop | ? |
| Revocation | Remove authority | ? |

> **Q5.1.2:** How should directive chains be modeled? (Human → Agent → Sub-agent)

---

### 5.2 Command Interface

> **Q5.2.1:** What interfaces do personas use to direct agents?

| Persona | Interface | CAF Record |
|---------|-----------|------------|
| | | |

> **Q5.2.2:** How is directive acknowledgment/compliance captured?

---

## Part 6: Enterprise Learning Services Integration

> **Reference:** HUB-CAF-005 — currently defined as "conceptual design complete; manual process initially"

### 6.1 Learning Triggers

> **Q6.1.1:** What events should trigger learning consideration?

| Trigger | Source | Learning Type |
|---------|--------|---------------|
| Decision outcome variance | ? | ? |
| Pattern emergence | Semantic Memory | ? |
| Human override | Episodic Memory | ? |
| Repeated escalation | ? | ? |

### 6.2 Learning Artifacts

> **Q6.2.1:** What gets learned and where does it go?

| Learning Type | Input | Output | Destination |
|---------------|-------|--------|-------------|
| Skill refinement | ? | ? | Procedural Memory |
| Constraint discovery | ? | ? | Semantic Memory |
| Preference capture | ? | ? | Preference Memory |
| Knowledge promotion | ? | ? | Knowledge Bank (ETSL) |

### 6.3 Human-in-the-Loop Learning

> **Q6.3.1:** Which personas are involved in learning validation?

| Learning Stage | Persona | Responsibility |
|----------------|---------|----------------|
| Identify candidate | ? | ? |
| Validate/curate | ? | ? |
| Approve promotion | ? | ? |
| Monitor application | ? | ? |

> **Q6.3.2:** How does learning relate to OPD?
> - Learning makes agents more predictable (refined behavior)
> - Learning should be observable (what was learned, why)
> - Humans should be able to direct learning (approve, reject, modify)

---

## Part 7: Comprehensive Design Questions

### 7.1 CAF Scope

> **Q7.1.1:** Should CAF be the unified control plane for OPD + Learning, or should these be separate subsystems?

| Option | Pros | Cons |
|--------|------|------|
| Unified CAF | | |
| Separate subsystems | | |

### 7.2 Record Schema Extensions

> **Q7.2.1:** What new record types are needed for full OPD?

| Record Type | Memory Class | Purpose |
|-------------|--------------|---------|
| Guardrail Event | Episodic | ? |
| Directive | Episodic | ? |
| Learning Candidate | ? | ? |
| Behavior Model Reference | ? | ? |

### 7.3 API Surface

> **Q7.3.1:** What APIs should CAF expose for OPD and Learning?

| API | Consumer | Purpose |
|-----|----------|---------|
| Observability Query | ? | ? |
| Predictability Model | ? | ? |
| Directive Recording | ? | ? |
| Learning Submission | ? | ? |

---

## Part 8: Design Decisions Log

| Decision | Options Considered | Choice | Rationale |
|----------|-------------------|--------|-----------|
| | | | |

---

## Next Steps

1. [ ] Complete personas (Part 2)
2. [ ] Answer Observability questions (Part 3)
3. [ ] Answer Predictability questions (Part 4)
4. [ ] Answer Directability questions (Part 5)
5. [ ] Answer Learning Services questions (Part 6)
6. [ ] Synthesize comprehensive design (Part 7)
7. [ ] Document decisions
8. [ ] Create implementation spec

---

## References

- [AOSM OPD Requirements](../../aosm-meta-model/agent-oriented-system.md#26-interaction-elements-opd-requirements)
- [AOSM Book Summary - OPD](../../aosm-meta-model/book-ref/book-summary.md#opd-elements-agent-interaction)
- [CAF README](../04-subsystems/cognitive-audit-fabric/README.md)
- [CAF Explanation Service](../04-subsystems/cognitive-audit-fabric/explanation-service.md)
- [GAPS.TODO - HUB-CAF-010, HUB-CAF-005](./GAPS.TODO)



======
Concepts:
* CAF should have integrated Enterprise-Learning Services
* CAF records should include guardrail activity in Episodic Memory - Critical; However, CAF-contributing guardrails should be explicitly tagged so in the Training and Employment Specifications.
* Agent Visibility: 
* Agent Directability: Doer Agents; Scenario recourse, re-execution with different context

Learning Objectives:
1. Promote Episodic Memory to Semantic, Procedural, and Preferencial memory
2. Strengthen Agent Behavior and Guardrails 


Let us first pick Directability of Agents as a goal.

# Derictability

## Mechanism of Intervention
Should every Scenario have an Escalation Matrix?
- Application exception are handled by Scenario Escalation Matrix

When is Task Queue Escalation Matrix used and when is Agent's Escaltion Matrix used?
- Task related exceptions are handled by Task Queue Escalation Matrix

## Intervention mental model
Agents can be Thinkers, Doers, Orchestrators, or Governors.
Thinker deals with:
- Decision Request, Decision Result 
Orchestrator deals with:
- Task Assignment Decisions. 
Doer deals with:
- Action Request, Action Result 
Governor deals with:
- Observations; Observations are not rejected, they are just recorded. 

There may be many reasons any of Requests or Results can be rejected by Agents, Guardrails, Scenario Policies, Automation Applications, etc.. Such rejections are reported to Signal Exchange.

On any Rejections, an Observation is Created and assigned to next escalation level in the task Queue. Escalation task queue is given the task. 
Accountbale Human is notified. Additional watchers are also notified.

On Rejection - 
    - Decision Result 
        -- Identify Escalation (from Application to Scenario EM; from Task Agent to TaskQueue EM)
            -- Change Context and re-run thinking
            -- Change the Decision continue Scenario
    - Decision Request 
        -- Identify Escalation (from Application to Scenario EM; from Task Agent to TaskQueue EM)
            -- Change Context and re-run thinking
            -- Fail the Scenario
    - Task Assignment
        -- Identify Escalation (from Application to Scenario EM; from Task Agent to TaskQueue EM)
            -- Assign Task to Alternative Agent in the Task Queue
            -- Give Task Failure Result
            -- Abandon Task
    - Task Completion
        - Not Applicable; 
        - A task will be action or decision task, and completion is a usually a Action Result or Decision Result.
        - If a task is a governance task, the results cannot be rejected.
    - Action Request
        -- Identify Escalation (from Application to Scenario EM; from Task Agent to TaskQueue EM)
            -- Reject the action
    - Action Result
        -- Identify Escalation (from Application to Scenario EM; from Task Agent to TaskQueue EM)
            -- Create a corrective action task (likely a different scenario)
            -- Assign Task to Alternative Agent in the Task Queue
            -- Give Task Failure Result
            -- Abandon Task

## CAF Integration
- Any changes to the decision generate override records.
- Any changes to Context generate ContextIntervention records.

This makes everything under a scenario directable. 
Share your comments on the sufficiency of this approach.


This is a well-structured directability model. Let me analyze its sufficiency and offer structured feedback.

---

## Analysis of the Directability Model

### What Works Well

| Aspect | Strength |
|--------|----------|
| **Agent Archetypes** | Clean separation (Thinker/Doer/Orchestrator/Governor) maps well to PIDA responsibilities |
| **Escalation Hierarchy** | Three-level model (Agent → TaskQueue → Scenario) provides clear escalation paths |
| **Rejection as Trigger** | Using rejection as the universal intervention trigger is elegant and auditable |
| **Governor Special Case** | Correctly identifies that observations are never rejected—they're facts, not proposals |
| **CAF Records** | Override + ContextIntervention records provide audit trail for all interventions |

---

### Questions & Clarifications Needed

#### 1. Escalation Matrix Ownership

> **Q:** You distinguish Scenario EM vs TaskQueue EM — who defines each?

| Escalation Matrix | Defined In | Owned By |
|-------------------|------------|----------|
| Scenario EM | Scenario Normative Spec? | Process Architect? |
| TaskQueue EM | Task Queue Config? | Supervisor? |
| Agent EM | Training Spec? Employment Spec? | Developer? |

**Recommendation:** Make this explicit in the Scenario Development journey (Process Architect → Developer → Supervisor).

> All escalation matrices are defined by the Supervsior. You seem to be loosing context :)
> You should reload Hub Task management, Personas and Journeys context.
---

#### 2. Intervention vs Override Semantics

You distinguish:
- **Override Record** — changes to decision
- **ContextIntervention Record** — changes to context

> **Q:** What about these intervention types?

| Intervention | Current Coverage | Record Type? |
|--------------|------------------|--------------|
| Change decision outcome | ✓ Override | Override |
| Change context, re-run | ✓ ContextIntervention | ContextIntervention |
| Reassign to different agent | ? | TaskReassignment? |
| Abandon task | ? | TaskAbandonment? |
| Kill-switch (emergency stop) | ? | EmergencyHalt? |
| Authority revocation | ? | AuthorityRevocation? |

**Suggestion:** Consider if Override and ContextIntervention are sufficient, or if we need a richer intervention taxonomy.

> Task assignment records already defined. Reference them. You should reload hub task management context.
> Kill Switch is not a business domain intervention. 
> AuthorityRevocation is not an inline decision. Requires deliberation and due consideration, likely from analysis of multiple observation - an Enterprise Learning scenario rather than a operational directability scenario, imo.

---

#### 3. Governor Role Clarification

> **Q:** Governors deal with Observations that are "just recorded." But do Governors have any directability over other agents?

| Governor Action | Directability? |
|-----------------|----------------|
| Record observation | No (passive) |
| Flag anomaly | Triggers escalation? |
| Recommend intervention | Suggests but doesn't direct? |
| Enforce policy | Yes (automatic rejection) |

**Observation:** Governors seem to sit outside the rejection-escalation loop. Is that intentional? Or should Governor observations trigger escalation reviews?

> Governor escalation, by design, shouldn't trigger escalation in the context of that specific request. These are audit observations that could trigger Enterprise Learning workflows.
---

#### 4. Orchestrator as Special Case

Orchestrators deal with Task Assignment Decisions. But:

> **Q:** Is an Orchestrator a Thinker (deciding who gets the task) or a distinct archetype?

| View | Implication |
|------|-------------|
| Orchestrator = Specialized Thinker | Task assignment is just a decision type |
| Orchestrator = Distinct | Needs its own escalation patterns |

**Recommendation:** Consider if Orchestrator is a role (how agent is deployed) vs. archetype (what agent does).

> All the types of Agents - Thinker, Does, Orchestrator, and Governor are archetype. An 'agent' might where all the hats. The Hub framework does not get into the semantics of activities of individual agents or applications. 

---

#### 5. Signal Exchange Integration

You state: *"Rejections are reported to Signal Exchange."*

This aligns with existing design [[memory:12921058]]: Signal Exchange routes messages to Hub Applications, not to tasks/agents directly.

> **Q:** Does Signal Exchange:
> - Only route the rejection notification?
> - Or also route the escalation assignment?

| Signal Exchange Role | Current Understanding |
|---------------------|----------------------|
| Route `REQUEST_UPDATE` with rejection | ✓ Yes |
| Create escalation task | ? (Is this Hub Application responsibility?) |
| Notify Accountable Human | ? (Direct or via Hub Application?) |

**Recommendation:** Clarify that Signal Exchange routes; Hub Application (or Task Management) creates escalation tasks.

> All Task Assignments are always reported to SX by the task management subsystem. Although it may perform the actions independent of SX.
---

### Gaps to Address

#### Gap 1: Proactive Directability

Your model is **reactive** (rejection → escalation). What about **proactive** directability?

| Proactive Directive | Example | Handling |
|--------------------|---------|----------|
| "Pause and await my review" | Human wants to review before action | ? |
| "Prioritize this task" | Reprioritization without rejection | ? |
| "Use this approach instead" | Guidance without rejection | ? |
| "Stop all work on this case" | Kill-switch | ? |

**Suggestion:** Add a `Directive` record type for proactive human→agent commands that aren't triggered by rejection.

> This can be achieved by putting a Policy or Guardrail to generate a rejction. 
When to use 'Directive' records vs. policies or guardrails could be confusing. This doesn't seem essential to be. Argue if you believe I am missing something.

---

#### Gap 2: Directive Acknowledgment

When an escalation is handled:

> **Q:** How do we record that the directive was acknowledged and executed?

| Event | Record |
|-------|--------|
| Directive issued | Override / ContextIntervention |
| Directive acknowledged | ? |
| Directive executed | ? |
| Directive outcome | ? |

**Suggestion:** Consider a `DirectiveResolution` record or add `resolution_status` to intervention records.
> As all records are immutable and append-only to request context, we should go with DirectiveResolution records with subtypes as ack and outcome.
---

#### Gap 3: Cross-Scenario Directability

You mention: *"Create a corrective action task (likely a different scenario)"*

> **Q:** How is cross-scenario directability recorded?

| Aspect | Question |
|--------|----------|
| Provenance | How does the new scenario know it was triggered by intervention? |
| Authority | Does the Accountable Human's authority flow to the new scenario? |
| CAF Linking | How are the records linked across scenarios? |

**Suggestion:** Ensure `ContextIntervention` or `Override` records include `spawned_scenario_id` for traceability.

> The Scenario invocation should have suffient trace information. If the initiated scenario in the same Workbench, the request would have been child to the parent and both parent and child will have references. If the invoked Scenario is another Workbench, then this would have been a Tool use call with all relevant traces. 

---

### Refined Model Proposal

Based on your input, here's a refined structure:

```
┌─────────────────────────────────────────────────────────────────┐
│                     DIRECTABILITY MODEL                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Agent Archetypes (by function):                                 │
│    ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│    │ Thinker  │  │  Doer    │  │Orchestr- │  │ Governor │       │
│    │          │  │          │  │  ator    │  │          │       │
│    │ Decision │  │ Action   │  │ Task     │  │ Observe  │       │
│    │ Req/Res  │  │ Req/Res  │  │ Assign   │  │ (record) │       │
│    └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘       │
│         │             │             │             │              │
│         └──────┬──────┴──────┬──────┘             │              │
│                │             │                    │              │
│         ┌──────▼─────────────▼──────┐      ┌──────▼──────┐      │
│         │      Rejection Event      │      │ Observation │      │
│         │   (Guardrail, Policy,     │      │  (No reject │      │
│         │    Agent, Application)    │      │   possible) │      │
│         └──────────────┬────────────┘      └─────────────┘      │
│                        │                                         │
│                        ▼                                         │
│         ┌──────────────────────────────┐                        │
│         │      Signal Exchange         │                        │
│         │   (Route REQUEST_UPDATE)     │                        │
│         └──────────────┬───────────────┘                        │
│                        │                                         │
│                        ▼                                         │
│         ┌──────────────────────────────┐                        │
│         │    Escalation Resolution     │                        │
│         ├──────────────────────────────┤                        │
│         │ 1. Identify Escalation Matrix│                        │
│         │    - Agent EM → TaskQueue EM │                        │
│         │    - TaskQueue EM → Scenario │                        │
│         │                              │                        │
│         │ 2. Create Escalation Task    │                        │
│         │    - Assign to escalation Q  │                        │
│         │    - Notify Accountable      │                        │
│         │    - Notify Watchers         │                        │
│         │                              │                        │
│         │ 3. Resolution Options:       │                        │
│         │    - Change Context, re-run  │                        │
│         │    - Change Decision         │                        │
│         │    - Reassign Agent          │                        │
│         │    - Fail Task/Scenario      │                        │
│         │    - Spawn Corrective Action │                        │
│         └──────────────┬───────────────┘                        │
│                        │                                         │
│                        ▼                                         │
│         ┌──────────────────────────────┐                        │
│         │        CAF Records           │                        │
│         ├──────────────────────────────┤                        │
│         │ • Override Record            │                        │
│         │ • ContextIntervention Record │                        │
│         │ • (+ DirectiveResolution?)   │                        │
│         └──────────────────────────────┘                        │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

### Verdict on Sufficiency

| Criterion | Assessment |
|-----------|------------|
| **Covers reactive directability** | ✅ Sufficient |
| **Covers proactive directability** | ⚠️ Needs Directive record for non-rejection commands |
| **Escalation hierarchy** | ✅ Clear (Agent → TaskQueue → Scenario) |
| **CAF integration** | ✅ Override + ContextIntervention cover core cases |
| **Governor handling** | ⚠️ Clarify if Governor observations trigger escalation review |
| **Cross-scenario traceability** | ⚠️ Need explicit linking for spawned scenarios |
| **Directive lifecycle** | ⚠️ Need acknowledgment/resolution tracking |

---

### Recommended Additions

1. **Directive Record** — For proactive human commands not triggered by rejection
2. **DirectiveResolution** — Or add `resolution_status` to Override/ContextIntervention
3. **Escalation Matrix CRD** — Formalize the three EM levels in specs
4. **`spawned_scenario_id`** — Link corrective actions to triggering intervention

---

Shall I incorporate this refined model into the design session document and proceed to Observability or Predictability next?