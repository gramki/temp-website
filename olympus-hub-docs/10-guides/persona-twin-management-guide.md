# Persona Twin Management Guide

> **Last Updated:** 2026-01-14
> **Audience:** Collaborators (any persona)

---

## Overview

This guide explains how to manage existing Persona Twins, including updating configuration, modifying triggers, retraining, promoting to other workbenches, and deactivating twins.

---

## Accessing Your Persona Twins

### Workbench Studio

1. Navigate to your workbench in Hub
2. Open **Workbench Studio**
3. Select **Scenarios** → **Persona Twins** → **My Twins**

### Agent Lifecycle UI

1. Navigate to **Agent Lifecycle** in Hub
2. Select **Employed Agents**
3. Filter by **Persona Twin = Yes**
4. Filter by **Delegator = (your user ID)**

---

## Managing Multiple Twins

You can have multiple Persona Twins in a workbench, each for different purposes:

| Twin | Purpose | Triggers |
|------|---------|----------|
| Task Triage Assistant | Review incoming tasks | Task assignments |
| Notification Handler | Handle alerts | Platform notifications |
| Daily Summary Bot | End-of-day summaries | 5 PM schedule |
| Compliance Monitor | Regulatory alerts | High-risk notifications |

### Best Practices for Multiple Twins

- **Single purpose per twin**: Keep each twin focused
- **Avoid overlapping triggers**: Don't have multiple twins respond to the same signal
- **Use descriptive names**: Make it clear what each twin does

---

## Updating Twin Configuration

### Modifying Triggers

To change which signals your twin responds to:

1. Open your twin in Workbench Studio
2. Select **Triggers** tab
3. Enable/disable trigger types
4. Modify conditions and filters
5. Click **Save Changes**

#### Adding a New Trigger

```yaml
# Example: Adding a time schedule trigger
trigger:
  type: time_schedule
  schedule:
    cron: "0 9 * * 1"  # Monday 9 AM
    timezone: "America/New_York"
  transform:
    request_type: "WeeklyPlanning"
```

#### Modifying an OPA Filter

```yaml
# Original filter: high priority only
opaFilter: |
  package persona.twin.task_filter
  default allow = false
  allow { input.payload.task.priority == "high" }

# Modified: include critical and from specific scenarios
opaFilter: |
  package persona.twin.task_filter
  default allow = false
  allow { input.payload.task.priority == "high" }
  allow { input.payload.task.priority == "critical" }
  allow { input.payload.task.scenario_id == "sc-vip-customers" }
```

### Modifying Authority Delegation

To change what authority your twin has:

1. Open your twin in Agent Lifecycle UI
2. Select **Authority** tab
3. Modify roles, groups, or OPA policies
4. Click **Update Employment**

**Note**: You cannot give your twin more authority than you have. If you lose a role, your twin automatically loses it too.

### Modifying Prompts and Behavior

To change how your twin behaves:

1. Open your twin in Workbench Studio
2. Select **Training** tab
3. Modify system prompts, skill prompts, or knowledge bindings
4. Click **Save as Draft**
5. Click **Retrain**

---

## Retraining Your Twin

When you make changes to the Training Spec, you need to retrain:

### When to Retrain

- After modifying prompts or behavior configuration
- After adding/removing knowledge sources
- After adding/removing skills

### Retraining Process

1. Save your Training Spec changes
2. Click **Retrain Twin**
3. Wait for training to complete (progress indicator shown)
4. Optionally test with samples
5. When satisfied, click **Redeploy**

### Retraining vs. Reconfiguring

| Change Type | Retraining Required? |
|-------------|---------------------|
| Trigger changes | ❌ No |
| OPA filter changes | ❌ No |
| Authority changes | ❌ No |
| Prompt changes | ✅ Yes |
| Knowledge source changes | ✅ Yes |
| Skill changes | ✅ Yes |

---

## Promoting to Other Workbenches

If you're a member of multiple workbenches, you can promote your twin to operate in them:

### Prerequisites

- Admin authorization required for each target workbench
- You must be a member of the target workbench
- Same Training Spec can be used across workbenches

### Promotion Process

1. Open your twin in Workbench Studio
2. Select **Promotion** tab
3. Select target workbench(es)
4. Click **Request Promotion**
5. Wait for admin approval (per workbench)
6. Once approved, configure triggers for the new workbench
7. Deploy in the target workbench

### Multi-Workbench Behavior

When a twin exists in multiple workbenches:
- Each workbench has its own Employed Agent (different identity)
- Same Training Spec (same behavior)
- Authority delegation is configured per workbench
- Triggers are configured per workbench

```
Training Spec: john-task-assistant
├── Workbench: disputes
│   └── Employed Agent: es-john-task-assistant-disputes
│       ├── Triggers: task assignment, daily summary
│       └── Authority: disputes roles
└── Workbench: compliance
    └── Employed Agent: es-john-task-assistant-compliance
        ├── Triggers: platform notifications only
        └── Authority: compliance roles
```

---

## Monitoring Twin Activity

### Viewing Activity

1. Open your twin in Workbench Studio
2. Select **Activity** tab
3. View recent requests created by the twin
4. Filter by date, status, or trigger type

### Activity Metrics

| Metric | Description |
|--------|-------------|
| **Requests Created** | Total requests created by the twin |
| **Tasks Processed** | Tasks the twin has triaged |
| **Notifications Handled** | Notifications routed to the twin |
| **Scheduled Runs** | Successful scheduled executions |
| **Filter Rejections** | Signals rejected by OPA filters |

### Debugging Issues

If your twin isn't behaving as expected:

1. Check **Activity Log** for errors
2. Review **Filter Rejections** to see what's being blocked
3. Use **Test with Sample** to debug trigger conditions
4. Check **Authority Denials** for permission issues

---

## Suspending and Resuming

### Temporary Suspension

To temporarily disable your twin:

1. Open your twin in Workbench Studio
2. Click **Suspend**
3. Confirm suspension

When suspended:
- Triggers are disabled
- No new requests are created
- Existing requests continue processing
- Authority is retained (not revoked)

### Resuming

To re-enable a suspended twin:

1. Open your suspended twin
2. Click **Resume**
3. Confirm resumption
4. Triggers become active again

---

## Revoking (Permanent Deletion)

### When to Revoke

- Twin no longer needed
- Leaving the workbench
- Security concerns

### Revocation Process

1. Open your twin in Workbench Studio
2. Click **Revoke**
3. Confirm revocation (this is permanent!)

When revoked:
- Triggers are permanently disabled
- Authority is removed
- Employment Spec is marked as revoked
- Training Spec remains for audit (but cannot be redeployed)

**Note**: Revocation is permanent. You'll need to create a new twin if you want this functionality again.

---

## Admin Operations

### Admin View of All Twins

Workbench admins can view all Persona Twins in the workbench:

1. Navigate to Workbench Studio → Scenarios → Persona Twins
2. Select **All Twins** section
3. View all twins regardless of visibility setting

### Admin Actions

| Action | Description |
|--------|-------------|
| **View** | See any twin's configuration (even private ones) |
| **Suspend** | Temporarily disable any twin |
| **Revoke** | Permanently revoke any twin |
| **Audit** | View activity and change history |

**Note**: Admins cannot modify a collaborator's twin—only suspend or revoke for governance purposes.

---

## Troubleshooting

### Twin Not Responding

| Symptom | Check | Solution |
|---------|-------|----------|
| No requests | Is twin suspended? | Resume the twin |
| No requests | Are triggers disabled? | Enable triggers |
| No requests | OPA filter rejecting? | Review filter logic |

### Unexpected Behavior

| Symptom | Check | Solution |
|---------|-------|----------|
| Wrong actions | Review prompts | Update and retrain |
| Missing context | Review knowledge bindings | Add missing KBs |
| Authority denied | Review delegation | Expand authority (within your limits) |

### Performance Issues

| Symptom | Check | Solution |
|---------|-------|----------|
| Slow response | High volume? | Add filters to reduce volume |
| Timeout | Complex operations? | Simplify prompts |

---

## Related Documentation

- [Persona Twin Creation Guide](./persona-twin-creation-guide.md) — Creating new twins
- [Persona Twins Concept](../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md) — Technical concept
- [Trigger Definitions](../04-subsystems/workbench-management/trigger-definitions.md) — Trigger configuration
- [Employment Spec Manager](../../olympus-seer-docs/seer-design/subsystems/agent-lifecycle-manager/employment-spec-manager.md) — Employment details

---

*This guide helps collaborators manage existing Persona Twins. For creating new twins, see the Persona Twin Creation Guide.*
