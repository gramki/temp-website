# User Journey: Persona Twin Creation

> **Last Updated:** 2026-01-14
> **Persona:** Any Collaborator

---

## Journey Overview

This journey describes how a collaborator creates a Persona Twin to delegate personal tasks and responsibilities to an AI agent.

| Attribute | Value |
|-----------|-------|
| **Trigger** | Collaborator wants to automate personal task handling |
| **Goal** | Deploy a personal AI assistant (Persona Twin) |
| **Outcome** | Active Persona Twin responding to tasks/notifications/schedules |
| **Duration** | 15-30 minutes (first time), 5-10 minutes (experienced) |

---

## Actors

| Actor | Role |
|-------|------|
| **Collaborator** | Creates and configures the Persona Twin |
| **Workbench Admin** | Approves promotion to other workbenches (if applicable) |
| **System** | Validates, trains, and deploys the twin |

---

## Journey Map

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          PERSONA TWIN CREATION JOURNEY                              │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   DISCOVER         CONFIGURE          TRAIN            DEPLOY           OPERATE    │
│   ─────────        ─────────          ─────            ──────           ───────    │
│                                                                                     │
│   ┌──────────┐    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐ │
│   │ Browse   │    │ Select   │     │ Test     │     │ Configure│     │ Monitor  │ │
│   │ Blueprints│───▶│ Signals  │────▶│ Behavior │────▶│ Authority│────▶│ Activity │ │
│   │          │    │ & Filters│     │          │     │          │     │          │ │
│   └──────────┘    └──────────┘     └──────────┘     └──────────┘     └──────────┘ │
│        │               │                │                │                │        │
│        ▼               ▼                ▼                ▼                ▼        │
│   ┌──────────┐    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐ │
│   │ Workbench│    │ Customize│     │ Review   │     │ Deploy   │     │ Iterate  │ │
│   │ Studio   │    │ Prompts  │     │ Results  │     │ Twin     │     │ & Refine │ │
│   │          │    │          │     │          │     │          │     │          │ │
│   └──────────┘    └──────────┘     └──────────┘     └──────────┘     └──────────┘ │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Steps

### Phase 1: Discover

**Touchpoint**: Workbench Studio

| Step | Action | System Response |
|------|--------|-----------------|
| 1.1 | Collaborator opens Workbench Studio | Displays workbench overview |
| 1.2 | Navigates to Scenarios → Persona Twins | Shows My Twins section with Create button |
| 1.3 | Clicks "Create Persona Twin" | Displays available blueprints |
| 1.4 | Browses blueprint options | Shows blueprint details, descriptions |
| 1.5 | Selects a blueprint | Loads blueprint configuration wizard |

**Decision Point**: Which blueprint matches my needs?

| Blueprint | Use Case | Suggested For |
|-----------|----------|---------------|
| Collaborator Assistant | General tasks | Most collaborators |
| Task Triage Assistant | High-volume task management | Supervisors |
| Compliance Monitor | Regulatory monitoring | Compliance officers |

### Phase 2: Configure

**Touchpoint**: Blueprint Configuration Wizard

| Step | Action | System Response |
|------|--------|-----------------|
| 2.1 | Reviews signal suggestions | Shows task, notification, schedule options |
| 2.2 | Enables desired signals | Configures trigger types |
| 2.3 | Applies filter suggestions | Sets OPA filters for each signal |
| 2.4 | Customizes prompts | Updates system prompt and skill prompts |
| 2.5 | Binds knowledge sources | Connects relevant knowledge bases |
| 2.6 | Reviews configuration summary | Shows complete configuration |

**Decision Point**: What signals should my twin respond to?

```
Example choices:
✅ Task Assignments (filtered to high priority)
☐ Platform Notifications (not needed)
✅ Daily Summary (5 PM weekdays)
```

### Phase 3: Train

**Touchpoint**: Training Interface

| Step | Action | System Response |
|------|--------|-----------------|
| 3.1 | Clicks "Train Twin" | Creates Training Spec, starts training |
| 3.2 | Monitors training progress | Shows training status and logs |
| 3.3 | Training completes | Shows success notification |
| 3.4 | Runs "Test with Sample" | Executes test scenarios |
| 3.5 | Reviews test results | Displays twin responses and actions |
| 3.6 | Optionally iterates | Returns to configure if needed |

**Decision Point**: Does the test behavior match expectations?

| Result | Action |
|--------|--------|
| Behavior correct | Proceed to deploy |
| Needs adjustment | Return to configure, retrain |

### Phase 4: Deploy

**Touchpoint**: Employment Configuration

| Step | Action | System Response |
|------|--------|-----------------|
| 4.1 | Clicks "Deploy Twin" | Opens employment configuration |
| 4.2 | Configures authority delegation | Sets roles, groups, OPA policies |
| 4.3 | Sets visibility | Chooses public or private |
| 4.4 | Reviews deployment summary | Shows complete Employment Spec |
| 4.5 | Confirms deployment | Creates Employment, activates triggers |
| 4.6 | Receives confirmation | Shows active twin status |

**Decision Point**: What authority should my twin have?

```
Example choices:
● Inherit all my roles (most common)
○ Specific roles only (more restrictive)

● Private visibility (recommended)
○ Public visibility
```

### Phase 5: Operate

**Touchpoint**: Twin Dashboard

| Step | Action | System Response |
|------|--------|-----------------|
| 5.1 | Views twin activity | Shows requests, actions, status |
| 5.2 | Reviews recommendations | Displays twin outputs |
| 5.3 | Monitors performance | Shows metrics and trends |
| 5.4 | Identifies improvements | Notes areas for refinement |
| 5.5 | Updates configuration | Adjusts triggers, filters, prompts |

---

## Touchpoints

| Touchpoint | Phase | Description |
|------------|-------|-------------|
| **Workbench Studio** | Discover, Configure | Main interface for Persona Twin creation |
| **Blueprint Configuration Wizard** | Configure | Step-by-step configuration |
| **Training Interface** | Train | Training and testing |
| **Employment Configuration** | Deploy | Authority and visibility settings |
| **Twin Dashboard** | Operate | Monitoring and management |

---

## Decision Points

### 1. Blueprint Selection

> "Which blueprint matches my needs?"

| Decision | Recommendation |
|----------|----------------|
| General productivity | Collaborator Assistant |
| Task-heavy role | Task Triage Assistant |
| Compliance focus | Compliance Monitor |
| Custom needs | Start with Collaborator Assistant, customize |

### 2. Signal Configuration

> "What signals should my twin respond to?"

| Consideration | Guidance |
|---------------|----------|
| Too many signals | Start small, add more later |
| Missing signals | Can add after deployment |
| Complex filters | Start with suggested filters |

### 3. Authority Delegation

> "What authority should my twin have?"

| Consideration | Guidance |
|---------------|----------|
| Full delegation | Use "inherit all" for maximum capability |
| Restricted scope | Select specific roles for controlled delegation |
| Sensitive actions | Add OPA policies to restrict |

### 4. Visibility Setting

> "Who should see my Persona Twin?"

| Consideration | Guidance |
|---------------|----------|
| Personal workflow | Private (default) |
| Team visibility needed | Public |
| Sensitive work | Private |

---

## Success Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| **Creation Time** | < 30 minutes | Time from start to deployed twin |
| **First Task Handled** | < 1 hour | Time until first request processed |
| **User Satisfaction** | > 4.0/5.0 | Self-reported satisfaction |
| **Adoption Rate** | > 50% | % of collaborators with active twins |

---

## Error Handling

| Error | Resolution |
|-------|------------|
| Blueprint not available | Contact admin to ensure subscription includes blueprints |
| Training fails | Review Training Spec for errors, contact support if persistent |
| Deployment fails | Check authority configuration, ensure within your permissions |
| Trigger not firing | Verify trigger conditions, check OPA filter policy |

---

## Related Journeys

- [Scenario Development](./scenario-development.md) — Business scenario creation
- [Request Lifecycle](./request-lifecycle.md) — How requests flow through Hub
- [Automation Lifecycle](./automation-lifecycle.md) — Agent deployment lifecycle

---

## Related Documentation

- [Persona Twin Creation Guide](../../10-guides/persona-twin-creation-guide.md) — Detailed how-to
- [Persona Twin Management Guide](../../10-guides/persona-twin-management-guide.md) — Managing twins
- [Persona Twins Concept](../../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md) — Technical concept

---

*This journey describes the end-to-end experience of creating a Persona Twin, from discovery to operation.*
