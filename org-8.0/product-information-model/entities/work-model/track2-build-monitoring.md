# Build Monitoring

**Model:** Work Model
**Track:** Track 2: The Build Track (Construction)
**Category:** Monitoring
**Owner:** Tech Lead, QA Lead

## Definition

Continuous tracking of build health (CI/CD pipeline), quality metrics (test coverage, defect rates, technical debt), and velocity trends. Build Monitoring sits between periodic assessment (Release Planning, Milestone reviews) and reactive work (Bug, Technical Task) — it surfaces when quality degrades, when builds destabilize, or when technical debt accumulates.

Build Monitoring is the Build Track's instantiation of the cross-track monitoring pattern: ongoing vigilance that triggers downstream work and feeds periodic reviews.

## Purpose

Makes the continuous oversight of build and quality health explicit. Without Build Monitoring:
- CI/CD failures and flaky builds are noticed only when someone hits them
- Test coverage drift and defect rate trends are invisible
- Technical debt accumulates without systematic visibility
- Velocity trends are not tracked for release forecasting

**Triggers downstream work:** Bug creation, Technical Debt Item creation, Release Planning adjustment, Iteration Planning rebalancing.

## Fields

| Field | Type | Description |
|---|---|---|
| Scope | Text | What is being monitored (e.g., "fx-service CI pipeline", "All Systems — integration test pass rate") |
| Metrics Tracked | List (text) | Build pass/fail rate, test coverage, defect rate, cycle time, technical debt indicators |
| Thresholds / Alerts | List (text) | When does monitoring trigger action (e.g., "Build failure 3 consecutive runs", "Coverage drop below 80%") |
| Cadence | Enum | `Continuous` / `Daily` / `Weekly` |
| Owner | String | Role/person responsible for watching |
| System(s) / Customer Release | Reference | Which System(s) (Dim 5) or Customer Release this monitoring supports (if scoped) |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Active | Monitoring is in effect; thresholds and cadence are defined |
| Paused | Monitoring is temporarily suspended |
| Retired | Monitoring scope is no longer relevant |

## Outputs / Artifacts

| Artifact | Category | Description | Downstream Consumer |
|---|---|---|---|
| Alert / Trigger | Evidence | When threshold is breached — prompts Bug creation, Technical Debt Item creation, or planning adjustment | Bug, Technical Debt Item, Release Planning Task |
| Quality Report / Dashboard | Assessment | Periodic snapshot of build health, coverage, velocity | Release Planning, Milestone review |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May trigger | Bug (Track 2) | Monitoring surfaces defects requiring resolution |
| May trigger | Technical Debt Item (Track 2) | Monitoring may surface technical debt requiring documentation |
| May trigger | Maintenance Task (Track 3) | Monitoring may surface infra or hygiene work |
| Informs | Release Planning Task (Track 2) | Velocity and quality trends inform release scope |
| Informs | Milestone Planning Task (Track 2) | Quality gates inform milestone criteria |

## Example

"Monitor payments-service and fx-service CI — continuous; alert on build failure or integration test pass rate below 95%. Weekly quality report: coverage trend, defect rate. Owner: Tech Lead. Feeds sprint review and release planning."
