# DR-027: Composition Levels, Module Package, and Run Track Engineering

**Status:** Accepted
**Date:** 2026-02-15
**Related FAQ:** Q92, Q93, Q94, Q95

## Context

After the Build Track detailing (DR-026), several conceptual gaps were identified through analysis and discussion:

1. **Module Version and Product Version are not just verification checkpoints.** They are composite systems with emergent operational properties, deployable at their composition level, and serve as communication bridges across organizational scopes. Calling System Version "the unit of deployment" understated the deployability of Module and Product compositions.

2. **Environment-specific work is not just configuration.** The Run Track introduces code — operational subsystems (probes, reconcilers, automation) — per environment. These are legitimate Systems (Dim 5) with code, repos, and System Versions. The Run Track is an engineering track, not just an operational track.

3. **The deployed composition is richer than the built composition.** Module Version (Build Track artifact) is verified but not operationally complete. What's deployed includes operational systems and environment-specific configuration. There was no entity to represent this enriched, deployable composition.

4. **The Run Track lacked work decomposition entities.** While the Build Track had Epics, Stories, and Technical Tasks for engineering work, the Run Track had no equivalent for its operational engineering work. Operational system development was informal and invisible.

5. **Technical Task scoping to "System" was ambiguous.** Module Version and Product Version are "systems" in the systems-thinking sense (composite systems with emergent properties), but Technical Tasks are scoped to Dim 5 Systems (atomic level). The word "system" was used at all three composition levels without disambiguation.

6. **Module Version lacked binding configuration.** The composition-level decisions (which adapters, protocol versions, capability flags) that constrain a composition to its legal form were not modeled.

7. **System (Dim 5) lacked a Purpose field.** There was no way to distinguish product Systems (serving end-user Personas) from operational Systems (serving Operational Personas) in the definition model.

## Decisions

### C1: Composition Levels (Atomic, Integrated, Complete)

**Decision:** Formalize three composition levels: **Atomic** (System, Dim 5), **Integrated** (Module, Dim 8 realized through Module Version/Package), **Complete** (Product, realized through Product Version/Package). All three levels are deployable and operationally real.

**Rationale:** "System" in the systems-thinking sense applies at all three levels, but each level has distinct entity names, deployment mechanisms, and operational characteristics. Formalizing composition levels prevents ambiguity when discussing Technical Task scoping (atomic), Module Package deployment (integrated), or Product Package deployment (complete).

### C2: Reframe "Unit of Deployment"

**Decision:** Change "System Version is the unit of deployment" to "System Version is the **atomic** deployment unit." Acknowledge Module Package as the **integrated** deployment unit and Product Package as the **complete** deployment unit.

**Rationale:** System Version is the independently deployable atomic unit, but Module Packages and Product Packages are also deployed — at their respective composition levels. The original framing understated the deployability of composed artifacts.

### C3: Module Package (Run Track Artifact)

**Decision:** Introduce Module Package as a Run Track artifact: Module Version + operational System Versions + operational configuration. The integrated deployment unit.

**Rationale:** What is deployed to an environment is richer than what the Build Track produces. The Run Track enriches Module Version with operational systems (probes, reconcilers, automation) and environment-specific configuration. Module Package captures this enrichment as a distinct entity with clean ownership: Build Track produces Module Version, Run Track produces Module Package.

### C4: Product Package (Run Track Artifact)

**Decision:** Introduce Product Package as a Run Track artifact: Product Version + Module Packages + cross-module operational wiring. The complete deployment unit.

**Rationale:** Mirrors Module Package at the product level. Cross-module operational concerns (product-wide monitoring, cross-module scaling coordination) need a composition entity.

### C5: Run Epic and Run Story (Run Track Work Entities)

**Decision:** Introduce Run Epic (Module-scoped) and Run Story as Run Track work entities for operational engineering work. Run Epics produce operational System Versions. Run Deliberations produce ODRs.

**Rationale:** The Run Track builds operational Systems — probes, reconcilers, automation. This engineering work needs the same decomposition as product engineering: Epic → Story → Technical Task. Without Run Epics and Run Stories, operational engineering is informal and invisible, conflated with incident response and maintenance.

### C6: Binding Configuration on Module Version

**Decision:** Add a Binding Configuration field to Module Version capturing the wiring, orchestration, and composition constraints that make the composition operational and legal. Environment-independent.

**Rationale:** Module Version's composition is not unconstrained assembly. Build-time choices — adapter selection, protocol version binding, capability activation — determine what this composition delivers and constrain it to valid combinations. Binding configuration captures these legal composition constraints.

### C7: System Purpose Field (Persona Reference)

**Decision:** Add a Purpose / Serving Persona(s) field to System (Dim 5) that references Persona(s) from Dim 4 and Operational Personas from Dim 7.

**Rationale:** Distinguishes product Systems (serving end-user Personas) from operational Systems (serving Operational Personas) through Persona references rather than a static enum. This connects System purpose to the existing Persona model and makes the distinction extensible.

### C8: Build Track Two-Layer Framing

**Decision:** Document (not structurally change) the Build Track's two-layer nature: specification/commitment layer (Epics, Stories — Module-scoped) and execution layer (Technical Tasks — System/Component-scoped).

**Rationale:** This framing helps explain why Epics/Stories feel like specification entities while Technical Tasks feel like execution entities. The distinction is conceptual, not structural — both layers are within the Build Track.

## Consequences

**Positive:**
- All three composition levels (atomic, integrated, complete) are formally named, deployable, and disambiguated
- Run Track engineering work is visible and plannable through Run Epics and Run Stories
- Operational systems are modeled as legitimate Systems (Dim 5) with purpose-based distinction via Personas
- Module Package and Product Package provide clean ownership boundary: Build Track produces verified artifacts, Run Track produces deployable compositions
- Binding configuration captures legal composition constraints on Module Version
- Build Track's two-layer nature is documented for organizational clarity

**Negative:**
- Four new entities to manage (Module Package, Product Package, Run Epic, Run Story)
- Run Track complexity increases — it is now explicitly both an operational track and an engineering track
- Module Package/Product Package assembly requires cross-track coordination (Build → Run handoff)
- Operational System ownership model needs organizational definition (which team owns payments-healthcheck?)
- SRE skill profiles expand — operational engineering requires development skills

**Updates to existing decisions:**
- DR-004 and DR-026 are refined (not superseded) — the three-tier versioning model remains, but deployment language is updated to reflect three deployment levels
- The Run Track section of `draft-work-model.md` is significantly expanded

---
