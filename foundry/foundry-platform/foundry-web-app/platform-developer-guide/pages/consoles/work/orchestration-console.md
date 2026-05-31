# Orchestration Console

The Orchestration console provides a unified view of all orchestration items: Product Intent, Discovery Case, and Release Intent.

## Type

List + Detail

## Audience

Product Managers, Engineering Managers, Governance

## Sections

### Orchestration Items List

Tabbed or filtered view by orchestration type:
- **Product Intent** — Product evolution items
- **Discovery Case** — Discovery track work
- **Release Intent** — Release coordination

Each item shows:
- Title
- Type
- Status
- Owner
- Due date
- Governance badges

### Item Detail Panel

Clicking an item opens detail panel or navigates to detail page showing:
- Full description
- Progress indicators
- Linked Work Orders
- Workspace distribution
- Governance status
- Activity timeline

## Actions

| Action | Description |
|--------|-------------|
| Create orchestration item | Start new PI / Discovery Case / Release Intent |
| Filter by type | Show only one orchestration type |
| Filter by status | Show only specific status |
| View detail | Open orchestration item detail page |
| Edit item | Modify orchestration item |

## Detail Page

**Orchestration Item Details** — `/workbenches/{workbenchId}/orchestration/{type}/{itemId}`

Uses track-based APIs per [../../../../../foundry-work-plan/phase-1/api-surface.md](../../../../../foundry-work-plan/phase-1/api-surface.md):

- Discovery Case: `/tracks/discovery/cases/{dcId}`
- Product Intent: `/tracks/build/product-intents/{piId}`

Full page view with:
- Complete item information
- All linked Work Orders
- Progress by Workspace
- Governance controls and status
- Activity history
- Comments and attachments

## URL

`/workbenches/{workbenchId}/consoles/orchestration`
