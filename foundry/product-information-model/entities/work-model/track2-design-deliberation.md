# Design Deliberation

**Model:** Work Model
**Track:** Build
**Owner:** Tech Lead, Developers, Architects

## Definition

A collaborative technical discussion that arises during Build Track work when a significant architectural or design question requires deliberate resolution. Design Deliberation is the Build Track's counterpart to the Discovery Track's Deliberation — but with a narrower scope focused on **implementation-time** architectural questions.

Design Deliberation produces one or more ADRs (Technical). The ADR captures the decision; the Design Deliberation captures the process (who participated, what was considered, why the chosen option was selected).

> **Discovery Deliberation vs. Design Deliberation:** Discovery Track Deliberation is *strategic* — it addresses questions that shape the product's direction and produces PDRs (Strategy) and sometimes ADRs. Design Deliberation is *tactical* — it addresses questions that arise during engineering (e.g., "Should we use gRPC or REST for this service-to-service call?" or "Should we shard the payments database now or later?"). Both produce ADRs, but the provenance differs. See DR-026.

## Purpose

Makes architectural decision-making during build work explicit and traceable. Without Design Deliberation:
- Architectural decisions made during development are invisible — they hide in Slack threads, PR comments, or verbal agreements
- ADRs produced during build work have no structured origin — "where did this ADR come from?" has no answer
- Design trade-offs are lost — only the outcome survives, not the reasoning

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "gRPC vs REST for fx-service ↔ payments-service") |
| Trigger | Text | What prompted this deliberation (Epic, Story, Technical Task, code review finding) |
| Epic | Reference (Build) | Which Epic this deliberation is related to (if applicable) |
| Story | Reference (Build) | Which Story this deliberation arose from (if applicable) |
| System(s) | List of References (Technical) | Which Systems are affected by this decision |
| Participants | List of Strings | Who participated in the deliberation |
| Options Considered | Text | What alternatives were evaluated |
| Decision | Text | Summary of the chosen option and rationale |
| ADR(s) Produced | List of References (Technical) | ADR(s) produced by this deliberation |

## Statuses

| Status | Description |
|---|---|
| Raised | Question identified; deliberation needed |
| In Discussion | Team is evaluating options |
| Decided | Decision reached; ADR being drafted |
| Documented | ADR(s) produced and filed |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Triggered by | Epic (Build) | Deliberation may be triggered by an Epic |
| Triggered by | Story (Build) | Deliberation may be triggered by a Story |
| Triggered by | Technical Task (Build) | Deliberation may be triggered during Task implementation |
| Affects | System(s) (Technical) | Deliberation affects one or more Systems |
| Produces | ADR(s) (Technical) | Design Deliberation produces Architecture Decision Records |

## Examples

| Deliberation | Trigger | Systems | Decision | ADR |
|---|---|---|---|---|
| "gRPC vs REST for fx↔payments" | FX Rate Locking Epic | fx-service, payments-service | gRPC — lower latency, streaming support for rate updates | ADR-031 |
| "Database sharding strategy for payments" | Payment volume growth concern during Story refinement | payments-service | Shard by merchant ID — aligns with tenant isolation pattern | ADR-032 |
| "Event schema versioning approach" | Integration Story: payments→compliance event flow | payments-service, compliance-service | Use schema registry with backward compatibility — avoids consumer breakage | ADR-033 |
| "Cache invalidation for FX rates" | Technical Task: Redis TTL configuration | fx-service | TTL-based with pub/sub invalidation on rate source update | ADR-034 |

---
