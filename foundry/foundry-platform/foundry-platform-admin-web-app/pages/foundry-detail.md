# Foundry Detail Page

**Path:** `/foundries/{foundry_id}`

## Purpose

The Foundry Detail page provides a comprehensive view of a single Foundry, including its configuration, resource usage, and management actions. This is where Platform Admins monitor and manage individual Foundries.

## Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Platform Admin                                              [Admin Name ▼] │
├─────────────────────────────────────────────────────────────────────────────┤
│  Dashboard │ Foundries │ Infrastructure │ Settings                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ← Back to Foundries                                                        │
│                                                                              │
│  Acme Corporation                                   ● Active                │
│  acme-corp.foundry.example.com                                              │
│                                                                              │
│  ┌─────────┬────────────┬───────────┬─────────────┐                        │
│  │ Overview│ Resources  │ Quotas    │ Activity    │                        │
│  └─────────┴────────────┴───────────┴─────────────┘                        │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  OVERVIEW                                                            │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                      │   │
│  │  Foundry ID         fnd-abc123                                      │   │
│  │  Created            March 15, 2026 (75 days ago)                    │   │
│  │  Region             us-east-1                                       │   │
│  │  PostgreSQL         pg-us-east-1-prod-01                            │   │
│  │                                                                      │   │
│  │  ──────────────────────────────────────────────────────────────────│   │
│  │                                                                      │   │
│  │  ADMIN                                                              │   │
│  │  Name               Alice Smith                                     │   │
│  │  Email              alice@acme.com                                  │   │
│  │  Last Login         2 hours ago                                     │   │
│  │                                                                      │   │
│  │  ──────────────────────────────────────────────────────────────────│   │
│  │                                                                      │   │
│  │  USAGE SUMMARY                                                      │   │
│  │  Users              127 of 500                                      │   │
│  │  Workshops          3 of 10                                         │   │
│  │  Workbenches        12 of 100                                       │   │
│  │  Storage            234 GB of 500 GB                                │   │
│  │  Model Usage (MTD)  $2,340 of $10,000                               │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  Actions                                                                    │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐         │
│  │  Open Foundry    │  │  Archive         │  │  Delete          │         │
│  │  Web App ↗       │  │  Foundry         │  │  Foundry         │         │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tabs

### Overview Tab

Displays:
- Foundry metadata (ID, created date, region, infrastructure)
- Admin information (name, email, last login)
- Usage summary (users, workshops, workbenches, storage, model usage)

### Resources Tab

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  RESOURCES                                                                   │
│                                                                              │
│  DATABASE                                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Instance        pg-us-east-1-prod-01                               │   │
│  │  Database        foundry_acme_corp                                  │   │
│  │  Size            12.4 GB                                            │   │
│  │  Connections     24 active, 100 max                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  STORAGE                                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Prefix          s3://foundry-data/fnd-abc123/                      │   │
│  │  Used            234 GB                                             │   │
│  │  Objects         42,156                                             │   │
│  │  ──────────────────────────────────────────────────────────────────│   │
│  │  Breakdown:                                                         │   │
│  │  ├─ artifacts/     180 GB (28,000 objects)                         │   │
│  │  ├─ uploads/       52 GB (12,000 objects)                          │   │
│  │  └─ backups/       2 GB (2,156 objects)                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  WORKSHOP REPOSITORY                                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Repository      platform-org/acme-corp-workshop-definition         │   │
│  │  Last Commit     2 hours ago                                        │   │
│  │  Commits         156                                                │   │
│  │                                  [View on GitHub ↗]                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Quotas Tab

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  QUOTAS                                                   [Edit Quotas]     │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Quota              Current    Limit     Usage                      │    │
│  ├────────────────────────────────────────────────────────────────────┤    │
│  │  Users              127        500       ████████░░░░░░░  25%      │    │
│  │  Workshops          3          10        ████████░░░░░░░  30%      │    │
│  │  Workbenches        12         100       ██░░░░░░░░░░░░░  12%      │    │
│  │  Storage (GB)       234        500       ███████████░░░░  47%      │    │
│  │  Model (USD/mo)     2,340      10,000    ████░░░░░░░░░░░  23%      │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  Quota History                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  • May 1, 2026: Model budget increased from $5,000 to $10,000      │    │
│  │  • April 15, 2026: Storage increased from 200 GB to 500 GB         │    │
│  │  • March 15, 2026: Initial quotas set                              │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Activity Tab

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ACTIVITY                                                                    │
│                                                                              │
│  Filter: [All ▼]  Date: [Last 7 days ▼]                                    │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Today                                                              │    │
│  │  ├─ 10:34 AM  alice@acme.com created Workshop "Mobile App"         │    │
│  │  └─ 09:12 AM  System: Storage usage alert triggered (85%)          │    │
│  │                                                                     │    │
│  │  Yesterday                                                          │    │
│  │  ├─ 4:22 PM   bob@acme.com joined Foundry                          │    │
│  │  ├─ 2:15 PM   alice@acme.com updated Foundry settings              │    │
│  │  └─ 11:30 AM  System: Daily backup completed                        │    │
│  │                                                                     │    │
│  │  May 27, 2026                                                       │    │
│  │  ├─ 3:45 PM   Workshop Sync: 12 configs updated                    │    │
│  │  └─ 9:00 AM   System: Monthly billing cycle started                │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  [Load More]                                                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Actions

### Open Foundry Web App

Opens the Foundry's web app in a new tab. Useful for troubleshooting.

### Archive Foundry

Confirmation dialog:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Archive Foundry?                                                      [×] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Archiving "Acme Corporation" will:                                        │
│                                                                              │
│  • Disable all user access                                                  │
│  • Stop all running Workspace Sessions                                      │
│  • Retain all data for future recovery                                      │
│  • Continue to count against platform limits                                │
│                                                                              │
│  The Foundry can be unarchived later to restore access.                    │
│                                                                              │
│                                        [Cancel]  [Archive Foundry]          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Delete Foundry

Confirmation dialog with safeguards:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Delete Foundry?                                                       [×] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ⚠️ This action is IRREVERSIBLE                                            │
│                                                                              │
│  Deleting "Acme Corporation" will permanently:                             │
│                                                                              │
│  • Delete all users, teams, and roles                                      │
│  • Delete all Workshops, Workbenches, and Workspaces                       │
│  • Delete the PostgreSQL database                                           │
│  • Delete all object storage data                                           │
│  • Delete the Workshop Definition Repository                                │
│                                                                              │
│  Type "acme-corp" to confirm:                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│                                        [Cancel]  [Delete Foundry]           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Edit Quotas

Modal for adjusting quotas:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Edit Quotas                                                           [×] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Max Users                                                                  │
│  ┌──────────────────────┐  Current usage: 127                              │
│  │  500                 │                                                   │
│  └──────────────────────┘                                                   │
│                                                                              │
│  Max Workshops                                                              │
│  ┌──────────────────────┐  Current usage: 3                                │
│  │  10                  │                                                   │
│  └──────────────────────┘                                                   │
│                                                                              │
│  Max Workbenches                                                            │
│  ┌──────────────────────┐  Current usage: 12                               │
│  │  100                 │                                                   │
│  └──────────────────────┘                                                   │
│                                                                              │
│  Storage (GB)                                                               │
│  ┌──────────────────────┐  Current usage: 234 GB                           │
│  │  500                 │                                                   │
│  └──────────────────────┘                                                   │
│                                                                              │
│  Monthly Model Budget (USD)                                                 │
│  ┌──────────────────────┐  Current MTD: $2,340                             │
│  │  10000               │                                                   │
│  └──────────────────────┘                                                   │
│                                                                              │
│                                        [Cancel]  [Save Changes]            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Validation:**
- New quota must be >= current usage
- Warning if significantly reducing quotas

## Status-Specific UI

### Created Status (Pending Onboarding)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  NewCo                                              ○ Created               │
│  newco.foundry.example.com                                                  │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ⏳ AWAITING ADMIN ONBOARDING                                        │   │
│  │                                                                      │   │
│  │  Invitation sent to: charlie@new.co                                 │   │
│  │  Sent: May 28, 2026 (1 day ago)                                     │   │
│  │  Expires: June 4, 2026                                              │   │
│  │                                                                      │   │
│  │  [Resend Invitation]                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Archived Status

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Demo Inc                                           ◐ Archived              │
│  demo.foundry.example.com                                                   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  ℹ️ FOUNDRY ARCHIVED                                                 │   │
│  │                                                                      │   │
│  │  Archived on: May 20, 2026                                          │   │
│  │  Archived by: admin@example.com                                     │   │
│  │  Data retained until: May 20, 2027                                  │   │
│  │                                                                      │   │
│  │  [Unarchive Foundry]                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## API Dependencies

```yaml
GET /api/v1/admin/foundries/{foundry_id}
Response:
  id: "fnd-abc123"
  name: "Acme Corporation"
  slug: "acme-corp"
  status: "active"
  region: "us-east-1"
  admin:
    email: "alice@acme.com"
    name: "Alice Smith"
    last_login: "2026-05-29T08:00:00Z"
  resources:
    database:
      instance: "pg-us-east-1-prod-01"
      name: "foundry_acme_corp"
      size_gb: 12.4
      connections_active: 24
      connections_max: 100
    storage:
      prefix: "s3://foundry-data/fnd-abc123/"
      used_gb: 234
      object_count: 42156
    workshop_repo: "platform-org/acme-corp-workshop-definition"
  usage:
    users: 127
    workshops: 3
    workbenches: 12
    model_usage_mtd_usd: 2340
  quotas:
    max_users: 500
    max_workshops: 10
    max_workbenches: 100
    max_storage_gb: 500
    monthly_model_budget_usd: 10000
  created_at: "2026-03-15T00:00:00Z"

GET /api/v1/admin/foundries/{foundry_id}/activity
Query: type, start_date, end_date, page, limit
Response: { events: [...], pagination: {...} }

PATCH /api/v1/admin/foundries/{foundry_id}/quotas
Body: { max_users: 600, max_storage_gb: 1000 }
Response: { quotas: {...} }
```
