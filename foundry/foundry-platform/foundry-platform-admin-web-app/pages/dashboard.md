# Dashboard Page

**Path:** `/`

## Purpose

The Dashboard provides Platform Admins with an at-a-glance view of platform health, recent activity, and any issues requiring attention.

## Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Platform Admin                                              [Admin Name ▼] │
├─────────────────────────────────────────────────────────────────────────────┤
│  Dashboard │ Foundries │ Infrastructure │ Settings                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │  FOUNDRIES       │  │  ACTIVE USERS    │  │  MODEL USAGE     │          │
│  │     24           │  │     1,847        │  │     $47,230      │          │
│  │  +2 this month   │  │  +156 this week  │  │  78% of budget   │          │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘          │
│                                                                              │
│  ┌─────────────────────────────────────┐  ┌────────────────────────────┐   │
│  │  ALERTS (3)                         │  │  RECENT ACTIVITY           │   │
│  │                                     │  │                            │   │
│  │  ⚠ Foundry "corp-dev" approaching   │  │  • Foundry "newco" created │   │
│  │    storage quota (92%)              │  │    2 hours ago             │   │
│  │                                     │  │                            │   │
│  │  ⚠ DB instance us-east-2 high CPU   │  │  • Foundry "demo" archived │   │
│  │    (sustained >80%)                 │  │    yesterday               │   │
│  │                                     │  │                            │   │
│  │  ℹ 2 Foundries pending onboarding   │  │  • Platform settings       │   │
│  │                                     │  │    updated by admin@...    │   │
│  └─────────────────────────────────────┘  └────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  INFRASTRUCTURE HEALTH                                               │   │
│  │                                                                      │   │
│  │  PostgreSQL Instances                          Object Storage        │   │
│  │  ├─ us-east-1 ●  4 Foundries, 45% capacity    ├─ 2.4 TB used        │   │
│  │  ├─ us-east-2 ●  8 Foundries, 72% capacity    ├─ 78% of allocation  │   │
│  │  └─ eu-west-1 ●  12 Foundries, 61% capacity   └─ 156K objects       │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Metrics

### Summary Cards

| Metric | Description | Source |
|--------|-------------|--------|
| **Foundries** | Total active Foundries | Foundry count |
| **Active Users** | Users active in last 7 days | Aggregated from all Foundries |
| **Model Usage** | MTD model spend across all Foundries | Agent Fabric usage data |

### Alerts Panel

Alerts are prioritized by severity:

| Severity | Icon | Examples |
|----------|------|----------|
| Critical | 🔴 | Infrastructure down, data loss risk |
| Warning | ⚠️ | Approaching quotas, high utilization |
| Info | ℹ️ | Pending actions, completed onboarding |

**Alert Sources:**
- Infrastructure monitoring (DB, storage health)
- Quota monitoring (usage thresholds)
- Foundry lifecycle (pending onboarding, stale invitations)

### Recent Activity

Shows recent platform-level events:

- Foundry created / archived / deleted
- Platform settings changed
- Infrastructure changes
- Admin actions

### Infrastructure Health

Summary of infrastructure status:
- PostgreSQL instance health and capacity
- Object storage usage
- Any degraded services

## Interactions

| Action | Behavior |
|--------|----------|
| Click alert | Navigate to relevant detail page |
| Click Foundry metric | Navigate to Foundries page |
| Click activity item | Navigate to relevant detail or expand |
| Click infrastructure item | Navigate to Infrastructure page |

## Data Refresh

- Summary metrics: Auto-refresh every 60 seconds
- Alerts: Auto-refresh every 30 seconds
- Activity: Auto-refresh every 60 seconds
- Infrastructure: Auto-refresh every 60 seconds

Manual refresh button available.

## API Dependencies

```yaml
GET /api/v1/admin/metrics/summary
Response:
  foundries_total: 24
  foundries_change_30d: +2
  active_users_7d: 1847
  active_users_change_7d: +156
  model_usage_mtd_usd: 47230
  model_budget_mtd_usd: 60000

GET /api/v1/admin/alerts
Response:
  alerts:
    - id: "alert-1"
      severity: "warning"
      title: "Foundry approaching storage quota"
      foundry_id: "fnd-123"
      foundry_name: "corp-dev"
      details: "92% of 500GB quota used"
      created_at: "2026-05-29T00:00:00Z"

GET /api/v1/admin/activity
Response:
  events:
    - id: "evt-1"
      type: "foundry.created"
      actor: "admin@example.com"
      details: { foundry_name: "newco" }
      timestamp: "2026-05-29T00:00:00Z"

GET /api/v1/admin/infrastructure/summary
Response:
  postgres_instances:
    - name: "us-east-1"
      status: "healthy"
      foundries: 4
      capacity_percent: 45
  storage:
    used_bytes: 2576980377600
    allocated_bytes: 3298534883328
    object_count: 156000
```

## Empty States

| State | Message |
|-------|---------|
| No alerts | "No alerts at this time" |
| No activity | "No recent activity" |
| New platform | "Welcome! Create your first Foundry to get started." |
