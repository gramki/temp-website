# Persona Twin Creation Guide

> **Last Updated:** 2026-01-14
> **Audience:** Collaborators (any persona)

---

## Overview

This guide explains how to create a **Persona Twin**—a personal AI agent that handles tasks, notifications, and scheduled activities on your behalf. Persona Twins are available to any collaborator in a workbench, regardless of their persona (Developer, Supervisor, Process Architect, etc.).

---

## What is a Persona Twin?

A Persona Twin is your personal AI assistant that:
- **Responds to tasks** assigned to you
- **Handles notifications** meant for you
- **Runs on schedules** you configure
- **Operates with your authority** (never exceeds your permissions)
- **Is private** by default (only you and admins can see it)

---

## Prerequisites

Before creating a Persona Twin, ensure you have:

| Requirement | Description |
|-------------|-------------|
| **Workbench Membership** | You must be a member of the workbench where you want the twin |
| **Active Collaborator Status** | Your account must be active in the subscription |
| **Persona Twin Blueprint Access** | At least one Persona Twin Blueprint must be available |

---

## Step-by-Step Creation

### Step 1: Access Workbench Studio

1. Navigate to your workbench in Hub
2. Open **Workbench Studio**
3. Select **Scenarios** from the navigation

### Step 2: Navigate to Persona Twins Section

1. In the Scenarios view, select the **Persona Twins** section
2. You'll see two sub-sections:
   - **My Twins** — Your existing Persona Twins
   - **All Twins** — All visible Persona Twins (admin view)
3. Click **Create Persona Twin**

### Step 3: Select a Blueprint

Choose a Persona Twin Blueprint that matches your needs:

| Blueprint | Best For |
|-----------|----------|
| **Collaborator Assistant** | General task management and information gathering |
| **Task Triage Assistant** | Supervisors handling many incoming tasks |
| **Compliance Monitor** | Compliance officers monitoring alerts |
| **Knowledge Assistant** | Capturing and organizing knowledge |
| **On-Call Assistant** | Developers/operators handling off-hours monitoring |

The blueprint provides:
- **Signal suggestions** — Common triggers you might want
- **Filter suggestions** — OPA policies for filtering signals
- **Schedule suggestions** — Common schedule patterns

### Step 4: Configure Signals

Select which signals your twin should respond to:

#### Task Assignment Signal

Enable this to have your twin respond when tasks are assigned to you:

```
✅ Task Assignments
   When tasks are assigned to me:
   
   Priority Filter:
   ○ All tasks
   ● High and critical only
   ○ Custom filter...
   
   Category Filter:
   ☑ Dispute review
   ☑ Customer inquiry
   ☐ Routine processing
```

#### Platform Notification Signal

Enable this to route workbench notifications to your twin:

```
☐ Platform Notifications
   When I receive workbench notifications:
   
   Categories:
   ☑ Security alerts
   ☑ High priority
   ☐ All notifications
```

#### Time Schedule Signal

Enable this to have your twin run on a schedule:

```
✅ Time Schedules
   Run on schedule:
   
   ● Daily Summary at 5:00 PM (Mon-Fri)
   ○ Weekly Review on Friday at 3:00 PM
   ○ Morning Briefing at 8:00 AM (Mon-Fri)
   ○ Custom schedule...
```

### Step 5: Customize Training

Adjust the twin's behavior to match your preferences:

#### System Prompt

Customize how your twin should behave:

```
You are my personal task assistant. When reviewing tasks:
- Summarize the key issues briefly
- Identify required information that's missing
- Suggest next steps based on our SOPs
- Escalate anything related to VIP customers immediately
```

#### Knowledge Sources

Add knowledge bases your twin should reference:

```
☑ Team SOPs (dispute-sops-kb)
☑ My Preferences (john-preferences-kb)
☐ Regulatory Guidelines (compliance-kb)
```

#### Skills

Select or customize skills:

```
☑ Task Triage
☑ Context Gathering
☑ Recommendation Drafting
☐ Report Generation
```

### Step 6: Configure Authority Delegation

Define what authority your twin receives:

#### Roles and Groups

```
Delegation:
● Inherit all my roles
○ Select specific roles:
  ☐ Analyst
  ☐ Reviewer

● Inherit all my groups
○ Select specific groups:
  ☐ disputes-team
```

#### OPA Policies (Advanced)

Optionally add fine-grained restrictions:

```
Additional Restrictions:
☐ No financial actions
☐ Read-only mode
☐ Custom policy...
```

### Step 7: Set Visibility

Choose who can see your Persona Twin:

```
Visibility:
● Private (only me and admins)
○ Public (all workbench members)
```

### Step 8: Train and Test

Before deploying, test your twin:

1. Click **Train Twin** to create the Training Spec
2. Review the training summary
3. Click **Test with Sample** to run test scenarios
4. Review test results and adjust configuration if needed

### Step 9: Deploy

When satisfied with testing:

1. Click **Deploy Twin**
2. Review the Employment Spec summary
3. Confirm the deployment
4. Your Persona Twin is now active!

---

## Example: Creating a Task Triage Assistant

Here's a complete example for a supervisor creating a task triage assistant:

### Configuration

```yaml
# Blueprint
blueprint: task-triage-assistant

# Signals
signals:
  taskAssignment:
    enabled: true
    filter: high-priority-only  # Only high/critical tasks
  platformNotification:
    enabled: false
  timeSchedule:
    enabled: true
    schedule: daily-summary

# Training
prompts:
  system: |
    You are my task triage assistant. For each task:
    1. Assess urgency based on customer tier and amount
    2. Gather relevant context from case history
    3. Prepare a brief recommendation
    4. Flag anything that needs immediate attention

knowledge:
  - dispute-sops-kb
  - customer-tiers-kb

# Authority
delegation:
  roles: "*"  # Inherit all roles
  groups: "*" # Inherit all groups

# Visibility
visibility: private
```

### Result

The twin will:
- Receive high-priority tasks assigned to the supervisor
- Automatically triage and prepare recommendations
- Generate a daily summary at 5 PM
- Operate privately (only supervisor and admins can see)

---

## Tips and Best Practices

### Start Small

- Begin with one signal type (e.g., just task assignments)
- Add more signals after you're comfortable with the basic behavior
- Gradually refine filters based on experience

### Use OPA Filters Wisely

- Start with suggested filters (e.g., high-priority-only)
- Test filters with sample signals before deploying
- Avoid overly complex filters that are hard to debug

### Review and Iterate

- Check your twin's activity regularly
- Review recommendations it generates
- Adjust prompts and filters based on actual behavior

### Security Considerations

- Your twin inherits your authority — it can do what you can do
- Use OPA policies to restrict sensitive actions if needed
- Private visibility keeps your workflows confidential

---

## Troubleshooting

### Twin Not Receiving Tasks

| Symptom | Possible Cause | Solution |
|---------|----------------|----------|
| No requests created | OPA filter blocking | Review filter policy, test with sample |
| Wrong tasks | Delegator mismatch | Verify trigger delegator matches your user ID |
| Delayed | Trigger not active | Check trigger status in scenario settings |

### Twin Exceeding Authority

| Symptom | Possible Cause | Solution |
|---------|----------------|----------|
| Action denied | Authority ceiling hit | This is expected; twin cannot exceed your authority |
| Unexpected scope | Roles too broad | Narrow role delegation |

---

## Related Documentation

- [Persona Twin Management Guide](./persona-twin-management-guide.md) — Managing existing twins
- [Persona Twins Concept](../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md) — Technical concept
- [Persona Twin Blueprint](../../olympus-seer-docs/seer-design/implementation-concepts/persona-twin-blueprint.md) — Blueprint details
- [Scenario Definitions](../04-subsystems/workbench-management/scenario-definitions.md) — Scenario configuration

---

*This guide helps collaborators create Persona Twins for personal task delegation. For advanced management, see the Persona Twin Management Guide.*
