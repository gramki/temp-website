# Signal Monitoring

**Model:** Work Model
**Track:** Track 1: The Discovery Track (Learning)
**Category:** Monitoring
**Owner:** Product Manager, Discovery Lead

## Definition

Continuous tracking of the signal pipeline health, trend analysis across Signals, and discovery velocity metrics. Signal Monitoring sits between periodic assessment (Deliberation, Prioritization Task) and reactive work (Signal Exploration, Research Task) — it surfaces when the signal backlog grows, when themes shift, or when discovery capacity is mismatched to demand.

Signal Monitoring is the Discovery Track's instantiation of the cross-track monitoring pattern: ongoing vigilance that triggers downstream work and feeds periodic reviews.

## Purpose

Makes the continuous oversight of the discovery pipeline explicit. Without Signal Monitoring:
- Signal backlog growth is invisible until Prioritization is overwhelmed
- Theme shifts and emerging patterns across Signals go undetected
- Discovery velocity (Signals explored, Ideas validated per period) is not systematically tracked
- Capacity mismatches (too many Signals, too few exploration slots) surface only in crisis

**Triggers downstream work:** Prioritization Task re-evaluation, new Signal creation, Deliberation scheduling.

## Fields

| Field | Type | Description |
|---|---|---|
| Scope | Text | What is being monitored (e.g., "LATAM Initiative signal pipeline", "All unprioritized Signals") |
| Metrics Tracked | List (text or reference) | Signal backlog count, signals-by-theme, discovery velocity, time-in-state per Signal |
| Thresholds / Alerts | List (text) | When does monitoring trigger action (e.g., "Backlog > 50 unprioritized Signals", "Signal aged > 90 days without exploration") |
| Cadence | Enum | `Continuous` / `Daily` / `Weekly` |
| Owner | String | Role/person responsible for watching |
| Initiative(s) | List of References (Dim 1) | Which Initiative(s) this monitoring supports (if scoped) |
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
| Alert / Trigger | Evidence | When threshold is breached — prompts Prioritization re-evaluation or Signal creation | Prioritization Task, Deliberation |
| Pipeline Report / Dashboard | Assessment | Periodic snapshot of backlog, velocity, theme distribution | Deliberation preparation, Initiative review |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Informs | Prioritization Task (Track 1) | Monitoring surfaces need for re-prioritization |
| May trigger | Signal (Dim 1) | Monitoring may surface need for new Signal creation |
| Feeds | Deliberation (Track 1) | Pipeline reports feed Deliberation preparation |
| Scoped to | Initiative (Dim 1) | Monitoring may be scoped to specific Initiative pipelines |

## Example

"Monitor LATAM Initiative signal pipeline — daily scan of unprioritized Signals; alert when backlog exceeds 20 or any Signal has been in New state > 60 days. Owner: PM Lead. Feeds weekly Discovery sync."
