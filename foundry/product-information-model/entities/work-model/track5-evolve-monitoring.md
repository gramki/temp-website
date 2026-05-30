# Evolve Monitoring

**Model:** Work Model
**Track:** Evolve
**Owner:** Process Leads, Product Ops, Engineering Managers

## Definition

Evolve Monitoring is continuous tracking of process adherence, artifact quality trends, DoD compliance rates, and guidance usage across all tracks. It surfaces when processes are not followed, when artifact quality degrades, when DoD criteria are routinely skipped, or when guidance is outdated or unused.

## Purpose

Each track has its own monitoring entity (Signal Monitoring, Build Monitoring, System Monitoring, Win Monitoring) focused on the track's domain outcomes. Evolve Monitoring is different — it monitors the *process health* of all tracks: are the work entities, artifacts, DoD criteria, and guidance structures serving their purpose? It provides the quantitative evidence that triggers and informs Evolve Reviews.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Cross-Track DoD Compliance Monitor") |
| Metrics Tracked | List | Specific process health metrics being monitored |
| Scope | Structured | Which track(s), entity types, or artifact types are being monitored |
| Thresholds | List | Alert conditions (e.g., "DoD skip rate > 20%", "artifact quality score < 3.0/5") |
| Data Sources | List | Where monitoring data comes from (project tools, artifact repositories, retrospective summaries) |
| Alert Recipients | List | Who receives alerts when thresholds are breached |

## Metrics Categories

| Category | What It Measures | Example Metrics |
|---|---|---|
| **Process Adherence** | Whether teams follow defined work entity flows | Entity skip rate, state transition compliance, mandatory field completion |
| **Artifact Quality** | Whether produced artifacts meet assessment criteria | Assessment criteria pass rate, reviewer rejection rate, template adherence score |
| **DoD Compliance** | Whether DoD criteria are satisfied before state transitions | DoD checklist completion rate, exit criteria violation rate |
| **Guidance Usage** | Whether Operating Model guidance is current and used | Playbook access frequency, guidance staleness (last update age), new-hire onboarding feedback |
| **Cross-Track Flow** | Whether transitional artifacts flow correctly | Feedback → Signal promotion rate, PSD → Build handoff cycle time, Evolve Findings → Definition Task conversion rate |

## Statuses

| Status | Description |
|---|---|
| Active | Monitoring is configured and running |
| Alert | One or more thresholds have been breached — requires attention |
| Paused | Monitoring temporarily suspended (e.g., during organizational change) |
| Retired | Monitoring scope no longer relevant |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Triggers | Evolve Review (Evolve) | Threshold breaches trigger ad hoc or accelerated reviews |
| Informs | Evolve Planning (Evolve) | Monitoring trends inform evolution cycle scoping |
| Monitors | Work entities (Tracks 1–5) | Tracks process adherence and DoD compliance |
| Monitors | Artifact types (all tracks) | Tracks artifact quality against assessment criteria |

## Example

**Name:** "Cross-Track DoD Compliance Monitor"
**Metrics Tracked:** DoD checklist completion rate per entity type, exit criteria violation rate, mandatory artifact production rate
**Scope:** All tracks — all work entities with defined DoD
**Thresholds:** Alert when any entity type's DoD completion rate drops below 80% for a rolling 30-day window
**Data Sources:** Project management tool (Jira/Linear), artifact repository (Confluence), quarterly retrospective summaries
**Alert Recipients:** Product Ops Lead, affected Track Process Owner

---
