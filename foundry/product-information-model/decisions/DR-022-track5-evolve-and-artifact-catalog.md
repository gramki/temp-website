# DR-022: Evolve Track and Artifact Type Catalog

**Status:** Accepted
**Date:** 2026-02-19

## Context

The UPIM Work Model originally had four tracks (Discovery, Build, Run, Win) that describe the work of evolving the product. However, the Work Model and Operating Model themselves also need to evolve — entity definitions, artifact type definitions, DoD criteria, and guidance structures must be assessed, refined, and updated as the product, organization, and market change.

Initial proposals considered: (a) embedding process evolution work within each existing track, (b) creating a "bridge document" between the Work Model and Operating Model, or (c) creating a dedicated fifth track. Discussion established that process evolution work has all the structural characteristics of a track — goals, entity types, artifacts, participants, a lifecycle — and treating it with less structural rigor (as a bridge or per-track addition) would undermine its importance.

Separately, the Work Execution Framework's artifact taxonomy had five top-level categories (Decision, Evidence, Specification, Delivery, Assessment) but no named subtypes per track and no assessment criteria. Stakeholders need to know not just *what category* an artifact belongs to, but *what type* it is and *what makes a good instance*.

## Decisions

### D1: Process evolution is the Evolve Track, not a bridge document or per-track addition

Process evolution work is modeled as **Evolve** with full track structural conventions — entity files, relationships, artifacts, DoD, the complete template. The "bridge" between Work Model and Operating Model is a *relationship characteristic* of Track 5, not an alternative structural form.

A model that cannot account for its own evolution is dead. Track 5 ensures the model stays alive by making process evolution explicit, structured, and assessable.

### D2: Four entity types and one transitional artifact

Track 5 has four work entity types and one transitional artifact:

- **Evolve Planning** — scopes evolution cycles (Plan)
- **Evolve Review** — assesses process effectiveness, artifact quality, guidance adequacy (Assess)
- **Evolve Definition Task** — creates/updates Work Model and Operating Model definitions (Define)
- **Evolve Monitoring** — tracks process adherence and artifact quality continuously (Monitor)
- **Evolve Findings** — transitional artifact produced by Evolve Reviews, consumed by Evolve Definition Tasks or promoted to Discovery Signals

This parallels the entity structure of other tracks: planning, execution, assessment, monitoring, and a transitional artifact.

### D3: Artifact type catalog with per-type assessment criteria

The Work Execution Framework is extended with a **Section 1b: Artifact Type Catalog** that defines named artifact types per track within each of the five categories. Each type has a description and **assessment criteria** — what makes a good instance of that artifact.

Assessment criteria are a Work Model concern (they define "what good looks like"), not an Operating Model concern (which defines "how to achieve good"). This distinction matters because assessment criteria are properties of the artifact type, not of the team producing it.

### D4: Track 5 as the structural bridge between Work Model and Operating Model

Track 5 is the only track whose outputs directly modify both the Work Model (entity/artifact definitions, DoD criteria, assessment criteria) and the Operating Model (guidance content, ceremony definitions, role descriptions). All other tracks produce outputs that modify the Definition Model or external systems. This bridge characteristic is structural, not just descriptive — it means Track 5 is the mechanism by which the three-model architecture stays coherent as it evolves.

## Rationale

**Why not per-track evolution entities?** Each track already has monitoring entities, but these monitor domain outcomes (build quality, system health, customer health), not process effectiveness. Process evolution crosses track boundaries — an Evolve Review might assess cross-track handoffs (PSD quality affecting Build Track, Feedback quality affecting Discovery Track). A dedicated track can assess the whole system, not just one track's process health.

**Why not a bridge document?** If process evolution has goals, entity types, artifacts, participants, and a lifecycle, calling it something other than "track" invents new architectural terminology and gives it less structural rigor. The "bridge" is a relationship characteristic, not a structural form.

**Why "Evolve" not "Process" or "Improve"?** "Evolve" parallels the active-verb naming of other tracks (Discover, Build, Run, Win). "Process" is a noun — it describes what is evolved, not what the track does. "Improve" implies the current state is always deficient; "Evolve" acknowledges that process changes may be adaptations to new circumstances, not just corrections.

**Why assessment criteria in the Work Model?** Assessment criteria define what a good artifact instance looks like — this is an intrinsic property of the artifact type (information model concern), not a team practice (organizational concern). A PDR that lacks alternatives considered is a poor PDR regardless of which team produced it.

## Consequences

**Positive:**
- The UPIM explicitly accounts for its own evolution, preventing model stagnation
- Process improvements are tracked as structured work with artifacts and DoD, not informal agreements
- Artifact quality can be systematically assessed through named types and criteria
- The bridge between Work Model and Operating Model has a clear structural mechanism
- Track 5 provides the mechanism for the iterative detailing plan (Phases 1–5 of the Work Execution Framework)

**Negative:**
- Adds a fifth track, increasing the model's surface area
- Process evolution work may feel like overhead in small or early-stage organizations
- Assessment criteria require ongoing maintenance (but Track 5 provides the mechanism for that maintenance)

**Mitigations:**
- Track 5 scales with organizational maturity — small teams may have lightweight Evolve Reviews and minimal assessment criteria
- Assessment criteria are explicitly skeletal/initial, with iterative refinement planned
- Track 5 is the mechanism for its own evolution — meta-meta-work is just Track 5 operating on itself

---
