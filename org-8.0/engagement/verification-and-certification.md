# Verification and Certification

[← Back to Guide](README.md)

---

## Verification as an Artifact Group

The Engagement Assembly is a logical container — there is no single release version, no single deployable artifact. But verifying the assembly produces concrete, executable engineering artifacts: test environment definitions, test suites, test data preparation tooling, CI orchestration configurations. These are code. They are version-controlled, reviewed, and maintained with the same engineering rigor as any other component of the assembly.

The Engagement Assembly has **three artifact groups**:

1. **Customer Product artifacts** — Product Line configurations, extensions, integrations, business logic
2. **Studio Component artifacts** — integration adapters, orchestration flows, UIs, workflows, operational artifacts
3. **Verification artifacts** — IaC environment definitions, assembly-level test suites, test data preparation, CI orchestration, certification records

The verification module is a first-class artifact group. It is a deliverable — handed over to the run team or customer at Transfer.

---

## The System-Under-Test Boundary

This is the central design concept. The Engagement Assembly represents many systems. Verifying it means defining a clear **system-under-test boundary**: what is inside the boundary (the assembly being verified) and what is at the edges (everything external to the assembly).

EA and AVA jointly define this boundary:

- **Inside the boundary:** The full assembly topology — Product Line instances, extensions, Studio Components, integrations, orchestration. These are deployed as real components because that is what is being verified. The assembly under test is a large and complex system boundary.
- **At the boundary edges:** External systems, third-party services, customer systems, production data sources are mocked, simulated, or stubbed. This is correct test design, not a compromise. The edges that need mocking or simulation are determined by where the assembly boundary sits.
- **The boundary is an architectural decision.** It depends on what the assembly includes, which external systems it integrates with, and what the customer's environment looks like. EA defines the architecture; AVA determines the test boundary and designs the edge treatment.

Standard testing practices apply throughout. Tests run from a known initial state, apply known inputs, and observe changed state. Environment state can be reset between runs. Test orchestration may use CI tooling for triggering, state management, and result collection.

---

## The EA-AVA Verification Model

EA and AVA are **peer architects**: EA architects the functional system; AVA architects the verification system. Both require full-breadth understanding of the assembly. Both work across all squads. Both make architecture-level design decisions.

How they jointly design and execute verification:

- **EA** defines what "correct assembly" means — architecture, integration seams, configuration expectations, cross-platform interfaces
- **AVA** designs how to verify it — verification strategy, test environment topology, test data model, scenario design, CI orchestration
- **Joint output:** Assembly acceptance criteria — the contract between architecture intent and verification evidence
- **Through the lifecycle:** Strategy design at Discover, continuous execution during Build, handover at Transfer

The assembly acceptance criteria are the bridge between architecture and verification. EA articulates the criteria (what must be true for the assembly to be correct); AVA designs the verification that provides evidence.

---

## Verification Strategy (Discover)

At Discover, EA and AVA produce the verification strategy. This is design work:

- **Assembly acceptance criteria definition** — what "correct assembly" means for this Engagement, expressed as testable criteria
- **System-under-test boundary definition** — what's inside the boundary, what's at the edges, how edges are simulated
- **Integration boundary identification** — which seams need assembly-level verification vs. what's covered at squad level
- **Configuration correctness definition** — what "correctly configured" means for this archetype
- **Test data design** — what data sets exercise cross-system flows, integration boundaries, and configuration-dependent behavior. This is design work: understanding which data exercises the integration seams, which data reveals configuration issues, which data represents realistic customer usage patterns.
- **PL version absorption strategy** — how the assembly handles Product Line version changes during Build:
  - **Pin and upgrade:** Pin PL versions at Build start; plan explicit upgrade events with re-verification. Stable but may accumulate version drift.
  - **Rolling absorption:** Accept PL changes as they come; continuous verification catches issues. Faster but noisier.
  - **Windowed absorption:** Accept PL changes within defined windows (e.g., first week of each sprint); verify the new assembly state at increment boundary.
- **Verification Squad composition** — whether a dedicated squad is warranted (see [The Verification Squad](#the-verification-squad))

---

## The Verification Module (Build)

The verification module is what the AVA (with the Verification Squad) builds and maintains during Build. All of it is codified and version-controlled:

### Environment Definitions (IaC)

Infrastructure-as-code that defines the assembly topology for the test environment. The topology is maintained and evolved as the assembly evolves. Environment instances can be ephemeral (spun up from IaC definitions, torn down after use) or long-lived, depending on cost and practicality — the definitions are the persistent artifact, not the instances.

### Test Suites

Executable scenarios targeting:

- **Integration seams** — component boundaries within the assembly (Product Line to extension, extension to Studio Component, Studio Component to integration adapter)
- **End-to-end customer journeys** — flows that cross component boundaries and exercise the assembly as a customer would experience it
- **Configuration correctness** — does the archetype configuration produce the expected behavior across the assembled components?
- **Failure and degradation scenarios** — what happens when a component fails, a connection drops, a service degrades (designed with SRE Lead input)
- **Security verification scenarios** — cross-component authentication, authorization across integration seams, data-in-transit integrity, and compliance with customer-specific security requirements (EA defines security requirements; AVA designs verification)

### Test Data Preparation

Scripts and tooling that produce representative data sets. Data sets are loadable into a known initial state before test execution. Test data design considers:

- What data exercises the integration seams
- What data reveals configuration correctness issues
- What data represents realistic customer usage patterns
- Cross-system referential integrity (data that spans multiple components must be consistent)

### CI Orchestration

Pipelines that trigger test runs, manage environment state (reset, deploy, configure), collect results, and report. The orchestration uses CI tooling; the tests themselves execute against the deployed assembly topology.

---

## Two Verification Activities

Not tiers, not gates — two distinct kinds of work:

### Continuous Verification

Automated, triggered by component changes. When a squad delivers a new component version, CI pipelines deploy the updated component into the test environment, reset state to a known baseline, run the relevant test suites, and report results. This catches regressions. No manual judgment required — pass/fail is automated.

### Increment Certification

The AVA's periodic assessment at each increment boundary. This is judgment work:

- **Review continuous verification results** — patterns, trends, flaky vs. real failures
- **Assess test suite adequacy** — has the suite kept pace with the assembly, or have new seams connected without corresponding tests?
- **Track progressive acceptance criteria** — which criteria are now testable that weren't before? Which are passing? Which are blocked?
- **Design and run exploratory scenarios** for newly connected seams
- **Produce the certification record:** assembly manifest (component versions), criteria status, known issues, risk assessment

### Progressive Acceptance Criteria

At Discover, EA and AVA define the full acceptance criteria set. These criteria become testable at different points as the assembly evolves — not at pre-planned milestones:

| Criteria category | Becomes testable when... |
|---|---|
| Individual component correctness | Squad delivers the component |
| Integration seam correctness | Both sides of the seam are connected |
| Configuration correctness | Archetype configuration is applied |
| End-to-end customer journeys | Enough seams are connected to form a flow |
| Operational readiness | SRE Lead has monitoring/alerting in place |
| Full assembly certification | All of the above are testable and passing |

The AVA certifies against whatever subset of criteria is currently testable at each increment. The certification record shows which criteria were evaluated, which passed, and which are not yet testable. Certification scope grows naturally as the assembly evolves.

### Decision Points Are Emergent

Go-live readiness is just the increment where all go-live criteria happen to be met. Transfer readiness is the increment where test suite handover is complete. The AVA doesn't do anything structurally different at these points — they've been certifying at every increment. The governance around these decisions (who communicates, who signs off, who escalates) belongs in [Governance and Escalation](governance.md).

---

## The Verification Squad

When Engagement scope and complexity warrant it, the AVA directs a dedicated **Verification Squad** that builds and maintains the verification module.

### Independence

The Verification Squad reports to the AVA, who reports to the EO — independent from EPM's functional squads. This independence is essential: the AVA's release-block authority is compromised if the verification squad reports through the same chain as the squads it verifies.

The AVA is not an EL. The Verification Squad has no EL. The AVA directs engineers through architectural authority and certification responsibility, not through the EL role. ELs remain scoped to functional squads under EPM.

### Composition

AVA + engineers (1–3 depending on assembly complexity). The engineers are assigned from Product Line Squads or the engineering pool through the same staffing process (via PPM) as any other squad. There is no dedicated "SDET function" or "QA function" — these are engineers doing verification engineering work (test automation, IaC, test data design, CI orchestration). The same engineer could be in a CP squad next quarter. The work is engineering; the domain is verification.

### Scaling

For smaller Engagements (one CP squad, simple architecture), the AVA may handle verification without a dedicated squad — this is a scaling decision, not a fixed structure. For large Engagements (multiple PLs, many squads, complex integration), the squad may be larger.

### Rotation

Same model as other squads — engineers rotate back to Product Line Squads or to other Engagements, carrying verification knowledge with them.

### Key Attribute

The hardest-to-find quality is cross-domain breadth. Squad-level engineers can be specialists in one Product Line. Verification Squad engineers must understand enough of every component in the assembly to test their interactions.

### Relationship to Squad-Level Testing

- Engineers within functional squads handle component-level testing *within* the squad boundary — this is part of their engineering work, not a separate function
- The Verification Squad handles assembly-level testing *across* squad boundaries
- Coordination: squad engineers may flag integration concerns up to the Verification Squad; the AVA may push verification requirements down to squads for edge cases better tested at the component level
- No reporting relationship between squad engineers doing testing and the Verification Squad — squad engineers report through their EL; the Verification Squad reports through the AVA to EO

---

## Test Suite Handover (Transfer)

The full verification module is a deliverable. At Transfer:

- Environment definitions (IaC), test suites, test data preparation tooling, CI orchestration configuration are handed over
- Documentation of what the suite covers, known gaps, and maintenance expectations
- Recipient: run team (Fully Managed / Co-Managed) or customer (Customer-Operated)
- The recipient must be able to run, maintain, and extend the test suite for ongoing verification

---

## References

- [Roles and Responsibilities](roles.md) — EA and AVA role descriptions, mandatory architect consultation
- [Engagement Lifecycle](../product-line-engineering/processes/engagement-lifecycle.md) — Phase-by-phase activities
- [Architecture and Archetypes](architecture-and-archetypes.md) — Archetype framework that influences verification strategy
- [Governance and Escalation](governance.md) — Decision-point governance (go-live, transfer)

---

[← Previous: Architecture and Archetypes](architecture-and-archetypes.md) | [→ Next: Engagement Readiness Council (ERC)](engagement-readiness-council.md)
