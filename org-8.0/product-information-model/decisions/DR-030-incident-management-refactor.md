# DR-030: Incident Management Refactor — ITSM-Aligned Artifact/Entity Separation

**Status:** Accepted
**Date:** 2026-02-25

## Context

The original `track3-incident.md` was a skeletal work entity with "To be refined" fields and statuses. Incident was conflated as both the observation (what happened) and the work (what to do about it). ITSM incident management practice distinguishes clearly between the incident record, the response work, and the post-incident learning. The UPIM needed an ITSM-aligned design that separates observation from response, provides structured severity classification, enables incident correlation, and closes feedback loops to both Run Track planning and Definition Model assessment.

## Decisions

### D1: Incident is a work artifact, not a work entity

**Decision:** Reframe Incident from a work entity to a work artifact — a durable observation record of service degradation.

**Rationale:** An Incident records *what happened*. The work of *handling it* is modeled separately. This parallels the Deployment pattern (DR-029): Deployment Task (work entity) produces Deployment (artifact/record). The separation enables independent assessment of what happened vs. how well we responded.

### D2: Severity uses SEV-0 through SEV-4

**Decision:** Replace P1/P2/P3/P4 severity labels with SEV-0/SEV-1/SEV-2/SEV-3/SEV-4.

**Rationale:** P1/P2 is overloaded across organizations (some use P for priority, some for severity). SEV-N is unambiguous — it labels severity specifically. SEV-0 is reserved for total service outage, providing a level above SEV-1 for catastrophic events.

### D3: Incident Response Task is the primary work entity

**Decision:** Introduce Incident Response Task as the work entity for triage-through-resolution.

**Rationale:** Without a work entity, the response work is invisible in the Work Model. Incident Response Task captures escalation, workaround, resolution, and the cross-track outputs (Bug, Signal, emergency Change Request).

### D4: Post-Incident Review is a standalone deliberation entity

**Decision:** Introduce Post-Incident Review as a standalone entity, not a subtype of another entity.

**Rationale:** PIR parallels Deliberation (Track 1) and Win Review (Track 4) — all are structured assessment activities that produce structured outputs. Making it standalone ensures it has its own fields, statuses, and output types appropriate to incident learning.

### D5: SEV-0/1/2 incidents require PIR; Operating Model may override

**Decision:** The Work Model states that SEV-0, SEV-1, and SEV-2 incidents require a Post-Incident Review. The Operating Model may adjust this threshold.

**Rationale:** This positions a sensible default without being rigidly prescriptive. Organizations that want stricter PIR coverage (e.g., all SEV-3 for a specific module) can extend. Organizations that want lighter coverage (e.g., waive PIR for SEV-2 incidents resolved within 15 minutes) can narrow. The Work Model states the default; the Operating Model owns the policy.

### D6: Post-Incident Report is an assessment artifact

**Decision:** Post-Incident Report is the durable knowledge artifact produced by PIR — timeline, RCA, contributing factors, impact, corrective actions, lessons learned.

**Rationale:** Without a structured artifact, PIR learning is verbal and ephemeral. The Post-Incident Report makes learning durable, queryable, and referenceable by downstream work (Bugs, Run Epics, Signals).

### D7: Customer Communication Task is a Run Track entity

**Decision:** Introduce Customer Communication Task as a Run Track work entity for incident communication.

**Rationale:** The Run Track owns incident communication because SRE/DevOps has real-time technical context (blast radius, mitigation progress, ETA). The Win Track consumes summarized or enhanced views in their regular routines (Win Reviews, QBRs, proactive engagement). This avoids duplication while ensuring the right people produce the communication.

### D8: Incident carries correlation and causation fields

**Decision:** Add Parent Incident, Related Incidents, and Caused By fields to the Incident artifact.

**Rationale:** Parent/child correlation prevents counting N incidents when there is 1 root cause with N symptoms. Related Incidents enables recurrence tracking. Caused By closes the deployment-to-incident feedback loop — critical for assessing deployment quality and informing future deployment risk assessment.

### D9: Bug gains a Workaround field

**Decision:** Add a Workaround field to the Bug entity for Known Error documentation.

**Rationale:** When an incident is resolved with a workaround (not a permanent fix), the resulting Bug carries the workaround description. This makes the workaround discoverable for future incidents of the same type without introducing a new entity. The Bug serves as the Known Error registry.

### D10: Incident informs Run Track planning tasks

**Decision:** Incident history is a first-class input to Deployment Planning Task, Capacity Planning Task, and Run Epic scoping — not just PIR and Discovery.

**Rationale:** PIR looks backward (what happened, why). Discovery looks at systemic patterns (is this a product-level problem?). Run Track planning looks forward operationally (given incident history, how do we de-risk upcoming work?). A module with recent SEV-1 incidents may warrant a more cautious deployment strategy or block promotion at a Station.

## Consequences

**Positive:**
- Clear separation of observation, response, learning, and communication — each has its own entity with appropriate fields and statuses
- Incident correlation and causation enable accurate impact assessment and deployment quality tracking
- SEV-based PIR mandate provides a sensible default while remaining Operating Model-flexible
- Known Error/Workaround pattern reuses existing Bug entity without new entities
- Incident-to-planning feedback loops are explicit rather than implicit
- Definition Model assessment connections are formalized: Customer Promise (Dim 3), Operational Target (Dim 7), Operational Readiness (Dim 7), Operational Pain (Dim 7)

**Negative:**
- More entities to maintain (3 new work entities + 1 refactored artifact)
- The Incident artifact's terminal status "Reviewed" requires organizational discipline to track
- SEV-0..4 scale requires agreement on severity definitions — the Work Model provides defaults but organizations must calibrate

---
