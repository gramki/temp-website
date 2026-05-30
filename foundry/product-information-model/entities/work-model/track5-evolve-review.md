# Evolve Review

**Model:** Work Model
**Track:** Evolve
**Owner:** Process Leads, Product Ops, Engineering Managers

## Definition

Evolve Review is a structured assessment of current process effectiveness, artifact quality, and guidance adequacy across one or more tracks. It is the Evolve Track's equivalent of Win Review (Win) and Deliberation (Discovery) — a collaborative, judgment-based assessment that produces structured findings.

## Purpose

Tracks 1–4 produce work and artifacts but do not systematically assess whether their own processes, entity definitions, and guidance remain effective. Evolve Review closes this loop — it is the mechanism by which the Work Model and Operating Model receive structured feedback about their own fitness. Without it, process problems are discovered only through failures, not through deliberate assessment.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Q3 Win Track Artifact Quality Review") |
| Review Type | Enum | `Process Effectiveness`, `Artifact Quality`, `Guidance Adequacy`, `Cross-Track Handoff` |
| Scope | Structured | Which track(s), entity types, artifact types, or handoffs are being reviewed |
| Assessment Period | Date range | The time window being assessed |
| Participants | List | Roles and individuals participating in the review |
| Evidence Sources | List | Monitoring data, artifact samples, stakeholder interviews, retrospective notes |
| Evolve Planning Reference | Reference | The Evolve Planning cycle that scoped this review (if planned; may also be ad hoc) |

## Review Types

| Type | What It Assesses | Key Questions |
|---|---|---|
| **Process Effectiveness** | Whether a track's work entities and state transitions serve their purpose | Are entities used as intended? Are state transitions meaningful? Do teams skip or shortcut entities? |
| **Artifact Quality** | Whether produced artifacts meet their assessment criteria | Do PSDs consistently include cross-dimensional review? Are Win Case resolutions complete? Do DoD checklists get followed? |
| **Guidance Adequacy** | Whether Operating Model guidance is current, complete, and used | Are playbooks up to date? Do new team members find guidance useful? Are there gaps where guidance doesn't exist? |
| **Cross-Track Handoff** | Whether transitional artifacts flow correctly across track boundaries | Does Feedback reach Discovery as Signals? Do PSDs arrive at Build with sufficient detail? Do Evolve Findings result in definition changes? |

## Statuses

| Status | Description |
|---|---|
| Planned | Review is scoped and scheduled |
| In Progress | Review is actively being conducted — evidence gathering, assessment, discussion |
| Findings Produced | Review is complete; Evolve Findings have been authored |
| Closed | Findings have been consumed (by Evolve Definition Task or archived) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped by | Evolve Planning (Evolve) | Planning cycle defines which reviews to conduct |
| Produces | Evolve Findings (Evolve) | Structured observations, gaps, and recommendations |
| Informed by | Evolve Monitoring (Evolve) | Monitoring data provides quantitative evidence |
| Assesses | Work entities (Tracks 1–5) | Reviews assess entity definitions, usage patterns, and effectiveness |
| Assesses | Artifact types (all tracks) | Reviews assess artifact quality against assessment criteria |

## Example

**Name:** "Q3 Win Track Artifact Quality Review"
**Review Type:** Artifact Quality
**Scope:** Win Track — Win Activity artifacts (all 7 subtypes), Win Case resolution records
**Assessment Period:** April 1 – June 30, 2026
**Participants:** Product Ops Lead, Win Track Process Owner, CS Manager, Support Lead
**Evidence Sources:** 50-item artifact sample (stratified by subtype), Win Monitoring quality scores, CS team retrospective notes
**Key Findings:** (1) Implementation/Onboarding go-live checklists missing integration verification in 35% of cases, (2) Win Case resolution records lack root-cause analysis for Complaints, (3) Revenue Operations Engagement has no defined artifact template

---
