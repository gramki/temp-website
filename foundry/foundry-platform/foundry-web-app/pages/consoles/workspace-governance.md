# Governance Workspace Console

The Governance Workspace console shows work execution within the Governance workspace, focused on transition validation.

## Type

Queue + List + Detail

## Audience

Governance Officers, Compliance Analysts, QA Governance Leads

## Sections

### Work Queue

Transition validation Work Orders waiting to be picked up:
- Ordered by priority
- Shows estimated effort
- Transition type (workspace-to-workspace, release gate)
- Control objectives to validate
- Governance badges

### In Progress

Work Orders currently being worked:
- Assignee
- Active session indicator
- Time in progress
- Blockers
- Validation checklist progress
- Evidence collection status

### Active Sessions

Sessions currently running in this workspace:
- Session owner
- Attached Work Orders
- Session duration
- Validations in progress
- Quick actions

### Completed

Recently completed Work Orders:
- Completion date
- Validation outcome (pass/fail/conditional)
- Evidence artifacts
- Linked governance findings

## Actions

| Action | Description |
|--------|-------------|
| Pick up Work Order | Assign validation Work Order to self |
| Start session | Launch Workspace Session |
| View Work Order | Open Work Order detail |
| View session | Open Workspace Session Details |
| Approve transition | Mark transition as validated |
| Reject transition | Block transition with findings |
| Request evidence | Request additional evidence |
| Mark complete | Complete validation Work Order |

## URL

`/workbenches/{workbenchId}/consoles/workspace-governance`
