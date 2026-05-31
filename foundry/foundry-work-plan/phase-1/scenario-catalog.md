# Phase 1 Scenario Catalog

Minimal scenario set for Phase 1, mapped to platform default Work Catalog definitions. Scenario YAML internals are **indicative** — see [../../foundry-platform/work-catalogues/platform-defaults/README.md](../../foundry-platform/work-catalogues/platform-defaults/README.md).

## Discovery Case scenarios

Source: [discovery/discovery-case/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/)

| Station | Scenario | OI stage | Scope |
|---------|----------|----------|-------|
| Product Specification | `frame-discovery-case` | `discovery-initiated` | ingress |
| Product Specification | `synthesize-evidence` | `insights-synthesized` | ingress |
| Product Specification | `record-product-decision` | `recommendations-ready` | ingress |
| UX Design | `conduct-user-research` | `research-in-progress` (group) | ingress |
| UX Design | `run-usability-experiment` | — | Available; not wired in default workflow |
| UX Design | `build-design-prototype` | — | Available; not wired in default workflow |
| Development | `assess-technical-feasibility` | `research-in-progress` (group) | ingress |
| Development | `run-discovery-spike` | — | Available; on-demand for spikes |
| QA | `assess-testability` | `research-in-progress` (group) | ingress |
| QA | `validate-experiment-evidence` | `insights-synthesized` (group) | ingress |
| Release | `assess-rollout-feasibility` | `research-in-progress` (group) | ingress |
| Governance | `pdr-alignment-review` | `recommendations-ready` (invoke) | ingress |
| Governance | `discovery-closure-review` | `decision-made` (invoke) | ingress |

## Product Intent scenarios

Source: [build/product-intent/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/)

| Station | Scenario | OI stage | Scope |
|---------|----------|----------|-------|
| Product Specification | `create-product-specification` | `in-specification` | ingress |
| UX Design | `design-user-experience` | `in-ux-design` | ingress |
| Development | `implement-product-specification` | `specified` (group), QA fix loop | ingress |
| QA | `prepare-test-suite-for-product-specification` | `specified` (group) | ingress |
| QA | `test-developed-feature` | `in-qa`, retest loop | ingress |
| Release | `accept-completed-product-intent` | `ready-for-release` | ingress |
| Release | `prepare-customer-release` | `ready-for-release` (chained) | ingress |
| Governance | `product-specification-review` | after spec WO | ingress |
| Governance | `ux-design-review` | after UX WO | ingress |
| Governance | `test-plan-review` | after dev+QA prep group | ingress |
| Governance | `test-coverage-review` | after QA test WO | ingress |
| Governance | `customer-release-package-review` | after release WO | ingress (hard block) |

## Phase 1 required vs available

**Required on golden path** — all scenarios marked with an OI stage above.

**Available but not on golden path** — `run-usability-experiment`, `build-design-prototype`, `run-discovery-spike`. Phase 1 engineering may implement these as callable ingress scenarios without wiring them into the default workflow.

**Not in Phase 1** — scenarios for Run, Win, Evolve, Governance Ritual tracks; workspace-internal helper scenarios (defined per module as needed).

## Human vs agent tasks

Phase 1 assumes each scenario decomposes into agent and human tasks per its indicative YAML. Minimum human tasks on golden path:

| Scenario | Human task |
|----------|------------|
| `frame-discovery-case` | Charter review |
| `record-product-decision` | (PDR may be agent-drafted; PM decides at gate) |
| Decision gate | PM: proceed-to-build / park / drop |
| `create-product-specification` | Specification review |
| `design-user-experience` | Design review |
| `implement-product-specification` | Peer review |
| `test-developed-feature` | QA sign-off |
| `accept-completed-product-intent` | Acceptance decision |
| All governance scenarios | Authorize release (hard block on final gate) |

Agent execution depth (real LLM vs stub) is an engineering choice — see [phase-1-scope.md](phase-1-scope.md).

## Customization

Workshops and Workbenches may override scenarios at their catalog level. Phase 1 demo uses **platform defaults only**.

## Read next

- [golden-path.md](golden-path.md) — when each scenario fires
- [governance-mvp.md](governance-mvp.md) — governance scenario behavior
- [../../foundry-platform/work-catalogues/user-guide/authoring-scenarios.md](../../foundry-platform/work-catalogues/user-guide/authoring-scenarios.md) — how to author scenarios
