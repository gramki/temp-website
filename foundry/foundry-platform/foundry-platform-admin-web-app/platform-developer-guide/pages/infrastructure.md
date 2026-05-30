# Infrastructure Page

**Path:** `/infrastructure`

## Purpose

The Infrastructure page provides visibility into the platform's underlying infrastructure: PostgreSQL instances, object storage, and system health. This helps Platform Admins monitor capacity, troubleshoot issues, and plan for growth.

## Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Platform Admin                                              [Admin Name ▼] │
├─────────────────────────────────────────────────────────────────────────────┤
│  Dashboard │ Foundries │ Infrastructure │ Settings                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Infrastructure                                                             │
│                                                                              │
│  ┌──────────────────┬─────────────────────┬─────────────────────┐          │
│  │ PostgreSQL       │ Object Storage      │ System Health       │          │
│  └──────────────────┴─────────────────────┴─────────────────────┘          │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  POSTGRESQL INSTANCES                                                │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  pg-us-east-1-prod-01                          ● Healthy      │  │   │
│  │  │  us-east-1 • 4 Foundries • 45% capacity                       │  │   │
│  │  │  ──────────────────────────────────────────────────────────── │  │   │
│  │  │  CPU: 23%    Memory: 45%    Connections: 124/500    Storage:  │  │   │
│  │  │  ████░░░░░░  █████░░░░░    ███░░░░░░░░░░░           234 GB   │  │   │
│  │  │                                                      [View →] │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  pg-us-east-2-prod-01                          ⚠ Warning      │  │   │
│  │  │  us-east-2 • 8 Foundries • 72% capacity                       │  │   │
│  │  │  ──────────────────────────────────────────────────────────── │  │   │
│  │  │  CPU: 78%    Memory: 68%    Connections: 340/500    Storage:  │  │   │
│  │  │  ████████░░  ███████░░░    ███████░░░░░░           456 GB    │  │   │
│  │  │                                                      [View →] │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │  pg-eu-west-1-prod-01                          ● Healthy      │  │   │
│  │  │  eu-west-1 • 12 Foundries • 61% capacity                      │  │   │
│  │  │  ──────────────────────────────────────────────────────────── │  │   │
│  │  │  CPU: 34%    Memory: 52%    Connections: 278/500    Storage:  │  │   │
│  │  │  ████░░░░░░  ██████░░░░    ██████░░░░░░░           389 GB    │  │   │
│  │  │                                                      [View →] │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tabs

### PostgreSQL Tab

Lists all PostgreSQL instances with health and capacity metrics.

#### Instance Card

Each instance displays:
- Instance identifier
- Region
- Number of Foundries hosted
- Capacity percentage
- Health status (Healthy, Warning, Critical)
- Resource gauges (CPU, Memory, Connections, Storage)

#### Health Status

| Status | Condition |
|--------|-----------|
| ● Healthy | All metrics within normal range |
| ⚠ Warning | Any metric above 70% threshold |
| 🔴 Critical | Any metric above 90% threshold or instance unreachable |

#### Instance Detail View

Clicking "View →" expands to show:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  pg-us-east-2-prod-01                                            [Close ×] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  METRICS (last 24 hours)                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  CPU Usage                                                          │   │
│  │  100%─┐                                                             │   │
│  │       │     ╭──╮      ╭─────╮                                      │   │
│  │   50%─┤ ╭───╯  ╰──────╯     ╰───────╮                              │   │
│  │       │─╯                            ╰───────────────────────────── │   │
│  │    0%─┴──────────────────────────────────────────────────────────── │   │
│  │        00:00        06:00        12:00        18:00        Now     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  FOUNDRIES ON THIS INSTANCE                                                │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Foundry          Database              Size      Connections      │    │
│  │  ────────────────────────────────────────────────────────────────  │    │
│  │  Acme Corp        foundry_acme_corp     12 GB     24              │    │
│  │  Corp Dev         foundry_corp_dev      45 GB     89              │    │
│  │  Startup XYZ      foundry_startup_xyz   8 GB      18              │    │
│  │  Beta Test        foundry_beta_test     3 GB      7               │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  CONFIGURATION                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Instance Type    db.r6g.xlarge                                    │    │
│  │  vCPUs            4                                                │    │
│  │  Memory           32 GB                                            │    │
│  │  Storage          1 TB (SSD)                                       │    │
│  │  PostgreSQL       15.4                                             │    │
│  │  Availability     Multi-AZ                                         │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Object Storage Tab

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  OBJECT STORAGE                                                             │
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │  TOTAL USED      │  │  TOTAL OBJECTS   │  │  ALLOCATION      │          │
│  │     2.4 TB       │  │     156K         │  │     78%          │          │
│  │  +120 GB /month  │  │  +12K /month     │  │  of 3.2 TB       │          │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘          │
│                                                                              │
│  USAGE BY FOUNDRY                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Foundry           Used       Quota      Usage    Objects          │    │
│  │  ──────────────────────────────────────────────────────────────── │    │
│  │  Acme Corp         234 GB     500 GB     47%      42,156          │    │
│  │  Corp Dev          456 GB     500 GB     91%   ⚠ 78,234          │    │
│  │  Startup XYZ       89 GB      200 GB     45%      15,678          │    │
│  │  Demo Inc          12 GB      100 GB     12%      3,456           │    │
│  │  ...               ...        ...        ...      ...             │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  STORAGE GROWTH (last 6 months)                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  3TB─┐                                              ╭───────────── │   │
│  │      │                                   ╭──────────╯              │   │
│  │  2TB─┤                         ╭─────────╯                         │   │
│  │      │               ╭─────────╯                                   │   │
│  │  1TB─┤     ╭─────────╯                                             │   │
│  │      │─────╯                                                       │   │
│  │   0──┴───────────────────────────────────────────────────────────  │   │
│  │       Dec    Jan    Feb    Mar    Apr    May                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### System Health Tab

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SYSTEM HEALTH                                                              │
│                                                                              │
│  PLATFORM SERVICES                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Service                    Status     Response Time   Uptime      │    │
│  │  ──────────────────────────────────────────────────────────────── │    │
│  │  API Gateway               ● Up        45ms            99.99%     │    │
│  │  Metadata Service          ● Up        12ms            99.98%     │    │
│  │  Workshop Sync Service     ● Up        89ms            99.95%     │    │
│  │  Orchestrator              ● Up        34ms            99.97%     │    │
│  │  Agent Fabric              ● Up        67ms            99.96%     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  EXTERNAL INTEGRATIONS                                                      │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  Integration              Status     Last Check       Notes        │    │
│  │  ──────────────────────────────────────────────────────────────── │    │
│  │  GitHub App              ● Up        2 min ago                     │    │
│  │  Olympus Cipher          ● Up        1 min ago                     │    │
│  │  MS Teams Webhook        ● Up        5 min ago                     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  RECENT INCIDENTS                                                           │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  No incidents in the last 7 days                                   │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Alerts

Infrastructure-related alerts appear at the top of the page:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠ pg-us-east-2-prod-01 CPU sustained above 70% for 30 minutes    [View]   │
│  ⚠ Corp Dev storage at 91% of quota                                [View]   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Data Refresh

- All metrics auto-refresh every 30 seconds
- Historical charts update every 5 minutes
- Manual refresh button available

## API Dependencies

```yaml
GET /api/v1/admin/infrastructure/postgres
Response:
  instances:
    - id: "pg-us-east-1-prod-01"
      region: "us-east-1"
      status: "healthy"
      foundries_count: 4
      capacity_percent: 45
      metrics:
        cpu_percent: 23
        memory_percent: 45
        connections_active: 124
        connections_max: 500
        storage_gb: 234
      config:
        instance_type: "db.r6g.xlarge"
        vcpus: 4
        memory_gb: 32
        storage_gb: 1000
        postgres_version: "15.4"
        multi_az: true
      foundries:
        - foundry_id: "fnd-abc123"
          name: "Acme Corp"
          database: "foundry_acme_corp"
          size_gb: 12
          connections: 24

GET /api/v1/admin/infrastructure/storage
Response:
  summary:
    used_bytes: 2638827906048
    allocated_bytes: 3518437208064
    object_count: 156000
  by_foundry:
    - foundry_id: "fnd-abc123"
      name: "Acme Corp"
      used_gb: 234
      quota_gb: 500
      usage_percent: 47
      object_count: 42156

GET /api/v1/admin/infrastructure/health
Response:
  services:
    - name: "API Gateway"
      status: "up"
      response_time_ms: 45
      uptime_percent: 99.99
  integrations:
    - name: "GitHub App"
      status: "up"
      last_check: "2026-05-29T00:00:00Z"
  incidents: []
```

## Actions

The Infrastructure page is primarily read-only. Actions that affect infrastructure (adding instances, resizing, etc.) are performed through cloud provider consoles or infrastructure-as-code pipelines.

However, Platform Admins can:
- Acknowledge alerts
- Trigger manual health checks
- Export metrics data
