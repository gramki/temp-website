# Components (v0.1)

Canonical component guidance for the Foundry Web App.

## Implementation baseline

- Use Radix UI primitives with Foundry-owned wrappers and shadcn-style composition.
- Feature code MUST import UI from `prototype/src/foundry-ui/components` (or future
  module equivalent), not directly from third-party libraries.

## Core components

## Shell and navigation

- App shell (global nav + content container)
- Breadcrumb
- Console side navigation
- Page header (title, subtitle, actions)

## Data and status

- Entity list row / card
- Detail panel
- Status badge (stage, gate, health)
- Timeline / activity row
- Empty, loading, error containers

## Actions and forms

- Primary, secondary, and destructive buttons
- Inputs, selects, search bars
- Filter chips
- Dialog and confirmation modal

## Behavior constraints

- Primary actions appear once per surface and remain visually dominant.
- Badge color and text must use standardized status semantics.
- List rows must support keyboard focus and visible selected state.
- Destructive actions always require explicit confirmation.

## Status badge mapping

Use this mapping for all badge-style status indicators. Do not redefine per console.

| Badge semantic | Background token | Text token | Border token | Notes |
|----------------|------------------|------------|--------------|-------|
| Info | `color.status.info` | `color.text.inverse` | `color.status.info` | General informational state |
| Success | `color.status.success` | `color.text.inverse` | `color.status.success` | Completed or passing state |
| Warning | `color.status.warning` | `color.text.inverse` | `color.status.warning` | Attention needed, not blocking |
| Error | `color.status.error` | `color.text.inverse` | `color.status.error` | Failed or invalid state |
| Blocked | `color.status.blocked` | `color.text.inverse` | `color.status.blocked` | Workflow blocked pending dependency |
| Governance Pass | `color.governance.pass` | `color.text.inverse` | `color.governance.pass` | Governance check approved |
| Governance Review | `color.governance.review` | `color.text.inverse` | `color.governance.review` | Human review required |
| Governance Fail | `color.governance.fail` | `color.text.inverse` | `color.governance.fail` | Governance check rejected |
| Governance Soft Block | `color.governance.softBlock` | `color.text.inverse` | `color.governance.softBlock` | Can proceed with explicit acknowledgment |
| Governance Hard Block | `color.governance.hardBlock` | `color.text.inverse` | `color.governance.hardBlock` | Must not proceed until resolved |

## Badge component constraints

- Badge text should be short (one to three words) and use canonical labels.
- Use the same semantic badge across list rows, detail panels, and timelines.
- If color is used, pair with text label and icon so meaning does not depend on color alone.

## Component review checklist

- Does this reuse an existing component pattern?
- Does this component introduce new visual primitives?
- Does it support loading/empty/error where applicable?
- Does it meet keyboard and focus requirements?

If introducing a new component type, update `patterns.md` and `change-log.md`.
