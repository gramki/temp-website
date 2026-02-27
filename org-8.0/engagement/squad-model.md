# Squad Model and Staffing

[← Back to Guide](README.md)

---

## Squad Types

```
                     Engagement
                          │
        ┌─────────┬───────┼───────────┬──────────┐
        │         │       │           │          │
  Customer    Studio   Verification  Product Line
  Product    Components              │
        │         │       │       ┌───┴────┐
   ┌────┴────┐   ...    AVA     PL Sq X  PL Sq Y
   │         │         Squad
 CP Sq A   CP Sq B
```

### Customer Product (CP) Squads

- Assembled to deliver the Customer Product for an Engagement
- Configure and extend Product Lines
- The Exploration Lead is the preferred candidate for CP Squad EL

### Studio Squads

- Build integration adapters, orchestration flows, custom experiences (UIs, workflows, applications)
- Dedicated Studio Components for data migration when required (migration squads)

### Verification Squad

- Builds and maintains the verification module — IaC environment definitions, assembly-level test suites, test data preparation, CI orchestration
- Directed by the AVA (the AVA is not an EL; authority comes from the architect role and certification responsibility)
- Reports through AVA to EO (independent from EPM's functional squads) — this independence preserves the AVA's release-block authority
- Composed of engineers, assigned through the same staffing process (via PPM) as any other squad. There is no dedicated "QA function" or "SDET function" — these are engineers doing verification engineering.
- Activated when Engagement scope and complexity warrant a dedicated squad; for smaller Engagements the AVA handles verification directly

See [Verification and Certification](verification-and-certification.md) for the full verification model.

### Product Line (PL) Squads

- Stable, long-lived squads owning Product Line capability
- Contribute engineers to Engagement squads via the rotation model
- Own inner source review and merge for their Product Line

---

## Squad Composition

Each functional squad (CP, Studio) has:

| Role | Description |
|------|-------------|
| **Engineering Lead (EL)** | Squad-level delivery and tech leadership |
| **Squad PM** | Backlog prioritization and execution priorities |
| **Engineers** | Development, configuration, integration, testing (includes Product Line Engineers, Integration Engineers, and domain specialists). Testing — test design, execution, automation — is engineering work done by engineers within the squad, not a separate role. |
| **Scrum Master** | Process facilitation; may serve 1-3 squads; reports to EPM (not EL). See [Scrum Master](roles.md#scrum-master). |
| **Product Line Analysts** | Domain/business analysis, requirements clarification (drawn from Product Line Squads or shared pool) |

The Verification Squad has a different composition: AVA + engineers (1-3). No EL, no Squad PM, no Scrum Master — the AVA directs the squad through architectural authority.

---

## Staffing

See [team-composition.md](../product-line-engineering/processes/team-composition.md) for the detailed process.

Staffing has two stages:

**Engagement-level role assignment** (at Initiate):

- **ERC** assigns **Client Partner** (per-client, may already be in place), **EO**, **EPM**, **EA**, **AVA**, and ensures **CPA** support for the Client Partner
- **EO** assigns **ELs**, **EPO**, **SRE Lead**

**Squad-level staffing** (at Discover, once ELs are in place):

- ELs submit staffing requests to the ERC Portfolio Program Manager (PPM); PPM consolidates demand across Engagements and presents a unified view to PL Squad leads; PL Squad leads check capacity and commit individuals; Engineering Leadership resolves priority conflicts; named individuals are assigned with return dates; team is convened and RACI and escalation are agreed

For the complete formation model — including designation-to-complexity matching, phase-by-phase team evolution, and scaling patterns — see [Engagement Formation](engagement-formation.md).

---

## Rotation as Learning Lever

See [rotation-model.md](../product-line-engineering/processes/rotation-model.md).

- Individual rotation every 6–12 months (or per Engagement need)
- Staggered rotation to maintain continuity
- Rotation builds breadth and cross-pollination

---

## Migration Squads

When an Engagement requires data migration, a dedicated Studio squad may be activated specifically for migration work. This squad follows the same composition and governance model but is scoped to migration deliverables.

---

[← Previous: Engagement Formation](engagement-formation.md) | [→ Next: Architecture and Archetypes](architecture-and-archetypes.md)
