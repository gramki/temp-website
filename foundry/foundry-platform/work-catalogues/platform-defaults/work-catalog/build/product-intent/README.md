# Product Intent

**Orchestration Item for the Build track.**

## Overview

A Product Intent (PI) represents a product idea or feature request that will progress through specification, development, QA, and release. The PI is the coordination token that synchronizes work across multiple Workspaces.

## Lifecycle

```
start → draft-ready → ready-for-specification → in-specification → 
in-ux-design → specified → in-qa → ready-for-release → released → end
```

### Stage Descriptions

> Stages are Product Intent coordination points that **route Work Orders to functional [stations](../../../../../../ace/workspaces/README.md)** — they are not the stations themselves. One stage can create Work Orders in several stations at once (e.g., `specified`), and a station can be engaged across multiple stages.

| Stage | Description | Work Orders Created |
|-------|-------------|---------------------|
| `start` | Initial state | — |
| `draft-ready` | PI submitted, awaiting PO approval | User task for approval |
| `ready-for-specification` | Approved, awaiting Release Intent milestone | — |
| `in-specification` | Specification work in progress | Product Specification WO |
| `in-ux-design` | Spec approved, UX design in progress | UX Design WO |
| `specified` | Spec + UX complete, ready for development | Development + QA prep WOs |
| `in-qa` | Development complete, QA testing | QA test WO |
| `ready-for-release` | QA passed, preparing release | Release acceptance + prep WOs |
| `released` | Released to customers | — |
| `end` | Terminal state | — |

## OI Workflow

→ [workflow.yaml](workflow.yaml) — Complete workflow definition

Key features:
- Manual approval gates (draft approval, acceptance)
- Release Intent milestone triggers
- Parallel Work Order groups (dev + QA prep)
- Governance invocations at key transitions
- Timeout handling and escalation

## Workspaces and Scenarios

> **Indicative specs.** The scenario `*.yaml` files below are worked examples. Their inputs, outputs, skills, and tasks are placeholders and do not capture the true detail or structure — they will be replaced with real definitions during specification. The `workflow.yaml` orchestration is the reliable part.

| Workspace | Scenarios | Purpose |
|-----------|-----------|---------|
| [product-specification/](product-specification/) | `create-product-specification` | Define detailed requirements |
| [ux-design/](ux-design/) | `design-user-experience` | Design the experience for the spec |
| [development/](development/) | `implement-product-specification` | Build the feature |
| [qa/](qa/) | `prepare-test-suite-for-product-specification`, `test-developed-feature` | Test the implementation |
| [release/](release/) | `accept-completed-product-intent`, `prepare-customer-release` | Release to customers |
| [governance/](governance/) | `product-specification-review`, `ux-design-review`, `test-plan-review`, `test-coverage-review`, `customer-release-package-review` | Governance gates at each transition |

## Example Flow

1. **PI "Add dark mode" created** → enters `start`, immediately transitions to `draft-ready`
2. **Product Owner approves** → transitions to `ready-for-specification`
3. **Release Intent milestone reached** → creates WO in Product Specification, transitions to `in-specification`
4. **Specification WO completes** → `product-specification-review` governance check, transitions to `in-ux-design`
5. **UX Design WO completes** → `ux-design-review` governance check, transitions to `specified`
6. **Creates parallel WOs** → Development implements, QA prepares test suite
7. **Both WOs complete** → `test-plan-review` governance check, transitions to `in-qa`
8. **QA WO completes successfully** → `test-coverage-review` governance check, transitions to `ready-for-release`
9. **Release WOs complete** → `customer-release-package-review` (hard block), transitions to `released`, then `end`

## Customization

Organizations can override this workflow at:
- **Foundry level** — Organization-wide modifications
- **Workshop level** — Team-specific adaptations

Common customizations:
- Add/remove governance gates
- Modify timeout durations
- Add additional scenarios on the existing stations (e.g., a Security Review governance scenario)
- Change notification channels

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../README.md](../README.md) — Build track overview
- [../../user-guide/authoring-oi-workflows.md](../../user-guide/authoring-oi-workflows.md) — How to customize workflows
