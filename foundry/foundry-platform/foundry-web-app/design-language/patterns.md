# Interaction Patterns (v0.1)

Patterns define reusable interaction structures across consoles and detail pages.

## Canonical console types

Aligned to `platform-developer-guide/pages/consoles/CONSOLE-GUIDE.md`:

- Landing
- Queue
- List + Detail
- Analytics
- Workflow
- Admin
- Resource

## Required pattern anatomy

Each screen should explicitly define:

1. Primary user question
2. Primary entity
3. Primary action
4. Secondary actions
5. State model (loading, empty, error, blocked)

## Pattern guidance

## List + Detail

- Left: filterable list
- Right: selected entity context
- URL should support deep-linking where possible

## Queue

- Prioritized actionable items
- Clear ownership and due/age metadata
- Bulk operations optional; individual actions required

## Workflow

- Stage indicators
- Transition action + rationale capture
- Governance status visibility in flow

## Analytics

- Summary first, drill-down second
- Date range + segment filters
- Export and shareability optional for prototype

## Boundary rule

When deciding whether something is a new console or an extension, follow
`CONSOLE-GUIDE.md` and document rationale in screen specs.
