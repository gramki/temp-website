# DR-032: FIR (First Information Report) — Universal Intake Pattern

**Status:** Accepted
**Date:** 2026-04-06

## Context

The UPIM Work Model has multiple reactive/responsive entities across tracks — Win Case (Track 4), Incident (Track 3), Bug (Track 2), Signal (Dim 1) — that can all originate from product-in-operation feedback. Without a universal intake mechanism, the same customer report may create disconnected work items across tracks with no common parent, no consistent triage process, and incomplete traceability from initial report to resolution.

ITSM frameworks establish the principle of a "single point of contact" for all service interactions. The UPIM needed an equivalent pattern that works across all tracks, not just the Run Track.

The model also needed to address: who creates intake items (only Win team, or any team?), whether reactive Win Cases can exist independently, and how monitoring alerts relate to customer-facing feedback.

## Decisions

### D1: FIR is a Track 4 work entity, not a work artifact

FIR has a lifecycle (Created → Triaged → In Progress → Resolved → Closed), is triaged by the Win team, and actively routes work to other tracks. This is work that requires judgment, coordination, and tracking — not a passive observation record like an Incident artifact.

**Rationale:** The triage decision is substantive work. Determining "this customer report is actually a service degradation + a product gap" requires investigation, correlation with monitoring data, and routing decisions. This is work entity behavior, not artifact behavior.

### D2: Always FIR-first — every Win Case originates from an FIR

Win Cases (Query, Service Request, Complaint, Escalation) cannot be created independently. Every Win Case is a sub-item of an FIR. Even when a Win team member discovers a complaint during a QBR, they log an FIR and route it.

**Rationale:** Universal intake ensures complete coverage. If Win Cases can be created without an FIR, there is a bypass path that breaks the traceability chain. The overhead of creating an FIR for a trivial query is minimal (FIRs support direct resolution at triage), and the traceability benefit is significant. This also ensures FIR volume metrics accurately reflect the total feedback burden.

**Consequence:** The Win Case entity now has a required `Originating FIR` field.

### D3: FIR is created by any team to ensure PFR-Win is the single origination point

Run teams (SREs detecting alerts), Build teams (QA observing regressions), and Win teams (customer support receiving complaints) all create FIRs. The `Provenance` field distinguishes the creator context: `External`, `Run`, `Build`, `Internal`.

**Rationale:** If only the Win team creates FIRs, then monitoring alerts and QA observations bypass the universal intake and PFR-Win is incomplete. By requiring all teams to create FIRs, PFR-Win becomes the comprehensive, single origination point for all product-in-operation feedback.

**Consequence:** The Operating Model must define the Run Team FIR Creation process (potentially automated for monitoring alerts) and the Build Team FIR Creation process.

### D4: Auto-routing for monitoring alerts is permitted

When a monitoring system detects an alert, an FIR can be auto-created and auto-routed (e.g., FIR auto-created with Provenance: Run, Category: Service Degradation → auto-routes to Incident in Track 3). The FIR still exists as the intake record, but triage is automated rather than human.

**Rationale:** Requiring human triage for every monitoring alert would create unsustainable overhead. The Provenance field and Category field enable auto-routing rules while maintaining the FIR record for traceability. The Operating Model defines which categories and provenances permit auto-routing.

### D5: FIR sub-items retain bidirectional references

Every sub-item created from an FIR carries an `Originating FIR` reference back to the parent FIR. The FIR carries a `Sub-Items` list referencing all routed work items. This bidirectional linking enables both "given this FIR, what work was done?" and "given this Bug, where did it come from?"

**Rationale:** Unidirectional references (only FIR → sub-item) would require traversal from FIR to find related work. Bidirectional references enable efficient querying in both directions and support PEIR lineage edges.

### D6: FIR can be resolved directly at triage with zero sub-items

For trivial inquiries (e.g., "What currencies do you support?"), the FIR can transition Created → Triaged → Resolved → Closed without creating any sub-items. The Triage Assessment captures the response.

**Rationale:** Not every customer interaction warrants a work item in another track. Forcing sub-item creation for trivial queries would create noise. The FIR record still exists for volume tracking and pattern analysis, but no downstream work is generated.

## Consequences

**Positive:**
- Complete traceability from initial report through resolution across all tracks
- PFR-Win is the single, comprehensive origination point for all operational feedback
- FIR volume metrics accurately reflect total feedback burden
- Win Reviews can assess triage quality and routing patterns
- Cross-track correlation is enabled (same FIR producing Incident + Win Case + Signal)

**Negative:**
- Every feedback interaction requires an FIR, adding a step to existing workflows
- Auto-routing rules must be carefully designed to avoid incorrect routing
- FIR triage process must be defined in the Operating Model (new ceremony/process)
- Run teams must adopt FIR creation as part of their incident response workflow

## Affected Entities

- **New:** `track4-fir.md`
- **Updated:** `track4-win-case.md` (required Originating FIR), `track3-incident.md`, `track2-bug.md`, `dim1-problem.md`, `dim1-need.md`, `dim1-opportunity.md`, `track3-maintenance-task.md` (optional Originating FIR references)
- **Updated:** `track4-win-monitoring.md`, `track4-win-review.md`, `track4-feedback.md` (FIR-related references)
- **Updated:** `draft-work-model.md`, `draft-work-execution-framework.md`, `entities/README.md`
