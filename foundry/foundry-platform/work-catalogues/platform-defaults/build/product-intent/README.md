# Product Intent

**Orchestration Item for the Build track.**

## Overview

A Product Intent (PI) represents a product idea or feature request that will progress through specification, development, QA, and release. The PI is the coordination token that synchronizes work across multiple Workspaces.

## Lifecycle

```
start → draft-ready → ready-for-specification → in-specification → 
specified → in-development → in-qa → ready-for-release → released → end
```

### Stage Descriptions

| Stage | Description | Work Orders Created |
|-------|-------------|---------------------|
| `start` | Initial state | — |
| `draft-ready` | PI submitted, awaiting PO approval | User task for approval |
| `ready-for-specification` | Approved, awaiting Release Intent milestone | — |
| `in-specification` | Specification work in progress | Product Specification WO |
| `specified` | Spec complete, ready for development | Development + QA prep WOs |
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

| Workspace | Scenarios | Purpose |
|-----------|-----------|---------|
| [product-specification/](product-specification/) | `create-product-specification` | Define detailed requirements |
| [ux-design/](ux-design/) | `design-user-experience` | Design UI/UX |
| [development/](development/) | `implement-product-specification`, `implement-bugfix` | Build the feature |
| [qa/](qa/) | `prepare-test-suite`, `test-developed-feature` | Test the implementation |
| [release/](release/) | `accept-completed-product-intent`, `prepare-customer-release` | Release to customers |
| [governance/](governance/) | `product-specification-review`, `code-review-gate`, etc. | Governance checks |

## Example Flow

1. **PI "Add dark mode" created** → enters `start`, immediately transitions to `draft-ready`
2. **Product Owner approves** → transitions to `ready-for-specification`
3. **Release Intent milestone reached** → creates WO in Product Specification, transitions to `in-specification`
4. **Specification WO completes** → governance check, transitions to `specified`
5. **Creates parallel WOs** → Development implements, QA prepares test suite
6. **Both WOs complete** → governance check, transitions to `in-qa`
7. **QA WO completes successfully** → governance check, transitions to `ready-for-release`
8. **Release WO completes** → governance check, transitions to `released`, then `end`

## Customization

Organizations can override this workflow at:
- **Foundry level** — Organization-wide modifications
- **Workshop level** — Team-specific adaptations

Common customizations:
- Add/remove governance gates
- Modify timeout durations
- Add additional workspaces (e.g., Security Review)
- Change notification channels

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../README.md](../README.md) — Build track overview
- [../../user-guide/authoring-oi-workflows.md](../../user-guide/authoring-oi-workflows.md) — How to customize workflows
