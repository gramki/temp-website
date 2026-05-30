# Foundries Page

**Path:** `/foundries`

## Purpose

The Foundries page lists all Foundries in the platform and provides the entry point for creating new Foundries.

## Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Platform Admin                                              [Admin Name ▼] │
├─────────────────────────────────────────────────────────────────────────────┤
│  Dashboard │ Foundries │ Infrastructure │ Settings                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Foundries                                          [+ Create Foundry]      │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🔍 Search foundries...          Status: [All ▼]  Region: [All ▼]   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Name            Status     Admin           Region    Created       │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │  Acme Corp       ● Active   alice@acme.com  us-east-1 2026-03-15   →│   │
│  │  Corp Dev        ● Active   bob@corp.io     us-east-2 2026-04-22   →│   │
│  │  NewCo           ○ Created  charlie@new.co  eu-west-1 2026-05-28   →│   │
│  │  Demo Inc        ◐ Archived demo@demo.io    us-east-1 2026-01-10   →│   │
│  │  Startup XYZ     ● Active   diana@xyz.co    us-east-1 2026-02-18   →│   │
│  │  ...             ...        ...             ...       ...          →│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  Showing 1-20 of 24 Foundries                    [< Prev] [1] [2] [Next >] │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Foundry List

### Columns

| Column | Description |
|--------|-------------|
| **Name** | Foundry display name |
| **Status** | Lifecycle state (Created, Active, Archived) |
| **Admin** | Primary Foundry Admin email |
| **Region** | Data residency region |
| **Created** | Creation date |
| **→** | Navigate to detail |

### Status Indicators

| Status | Icon | Description |
|--------|------|-------------|
| Created | ○ | Awaiting admin onboarding |
| Active | ● | Operational |
| Archived | ◐ | Disabled, data retained |

## Filtering

### Search

Full-text search across:
- Foundry name
- Foundry slug
- Admin email

### Status Filter

- All
- Active
- Created
- Archived

### Region Filter

Dynamic list of regions with Foundries.

## Create Foundry

Clicking "Create Foundry" opens a modal:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Create New Foundry                                                    [×] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Foundry Name *                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Acme Corporation                                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  Slug *                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  acme-corp                                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  This will be used in URLs: acme-corp.foundry.example.com                   │
│                                                                              │
│  Admin Email *                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  alice@acme.com                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  An invitation will be sent to this email.                                  │
│                                                                              │
│  Admin Name *                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Alice Smith                                                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  Region *                                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  us-east-1                                                       ▼│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  PostgreSQL Instance (optional)                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Auto-assign                                                     ▼│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  Leave as auto-assign for automatic instance selection.                     │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Resource Quotas (defaults can be changed later)                            │
│                                                                              │
│  Max Users        Max Workshops     Max Workbenches     Storage (GB)        │
│  ┌──────────┐    ┌──────────┐      ┌──────────┐        ┌──────────┐        │
│  │  500     │    │  10      │      │  100     │        │  500     │        │
│  └──────────┘    └──────────┘      └──────────┘        └──────────┘        │
│                                                                              │
│  Monthly Model Budget (USD)                                                 │
│  ┌──────────────────────┐                                                   │
│  │  10000               │                                                   │
│  └──────────────────────┘                                                   │
│                                                                              │
│                                        [Cancel]  [Create Foundry]           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Validation

| Field | Rules |
|-------|-------|
| Name | Required, 3-100 characters |
| Slug | Required, lowercase alphanumeric and hyphens, unique |
| Admin Email | Required, valid email format |
| Admin Name | Required, 2-100 characters |
| Region | Required, from available regions |
| Quotas | Positive integers within platform maximums |

### On Submit

1. Validate all fields
2. Check slug uniqueness
3. Submit to API
4. Show provisioning progress
5. On success, navigate to Foundry detail page

## Row Actions

Clicking a row navigates to Foundry detail page.

Hover reveals action menu:

| Action | Condition | Behavior |
|--------|-----------|----------|
| View | Always | Navigate to detail |
| Resend Invitation | Status = Created | Resend admin invite email |
| Archive | Status = Active | Archive the Foundry |
| Unarchive | Status = Archived | Reactivate the Foundry |
| Delete | Any | Confirm and delete (destructive) |

## API Dependencies

```yaml
GET /api/v1/admin/foundries
Query: search, status, region, page, limit
Response:
  foundries:
    - id: "fnd-123"
      name: "Acme Corp"
      slug: "acme-corp"
      status: "active"
      admin_email: "alice@acme.com"
      admin_name: "Alice Smith"
      region: "us-east-1"
      created_at: "2026-03-15T00:00:00Z"
  pagination:
    total: 24
    page: 1
    limit: 20

POST /api/v1/admin/foundries
Body:
  name: "Acme Corporation"
  slug: "acme-corp"
  admin_email: "alice@acme.com"
  admin_name: "Alice Smith"
  region: "us-east-1"
  pg_instance: null
  quotas:
    max_users: 500
    max_workshops: 10
    max_workbenches: 100
    max_storage_gb: 500
    monthly_model_budget_usd: 10000
Response:
  foundry_id: "fnd-456"
  status: "provisioning"

POST /api/v1/admin/foundries/{id}/resend-invitation
Response: 200 OK

PATCH /api/v1/admin/foundries/{id}
Body: { status: "archived" }
Response: { foundry: {...} }

DELETE /api/v1/admin/foundries/{id}
Response: 204 No Content
```

## Empty State

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                              No Foundries Yet                               │
│                                                                              │
│           Create your first Foundry to get started with the platform.       │
│                                                                              │
│                          [+ Create Foundry]                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```
