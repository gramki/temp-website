# Prototype Route and Console Coverage

Verification matrix for spec-aligned prototype implementation.

## Home pages

| Page | Route | Status |
|------|-------|--------|
| Foundry Home | `/` | Implemented |
| Workshop Home | `/workshops/{workshopId}` | Implemented |
| Workbench Wall (landing) | `/workbenches/{workbenchId}` | Implemented — side nav + Wall |

## Detail pages

| Page | Route | Status |
|------|-------|--------|
| Orchestration Item | `/workbenches/{id}/orchestration/{type}/{itemId}` | Implemented |
| Team Member Profile | `/workbenches/{id}/team/{memberId}` | Implemented |
| Workspace Session | `/workbenches/{id}/sessions/{sessionId}` | Implemented |

## Console groups (29 consoles)

All consoles use `/workbenches/{workbenchId}/consoles/{consoleId}`.

| Group | Consoles | Status |
|-------|----------|--------|
| Work | work-overview, orchestration, progress, work-rituals, my-work | Implemented |
| Workspaces | workspaces-overview, workspace-product-spec, workspace-ux-design, workspace-development, workspace-qa, workspace-release, workspace-governance | Implemented |
| Build | ci, components, findings, quality-status, release-artifacts | Implemented |
| Workforce | workforce-overview, team, agent | Implemented |
| Governance | governance, rituals, controls, registers, reports, quality-compliance | Implemented |
| Resources | repositories | Implemented |
| Settings | admin, governance-admin | Implemented |

## Build Track depth (scenario workbench)

Default scenario: `buildTrackTwoWorkOrders` on `wb-photon-payment-gateway`.

| Capability | Location | Status |
|------------|----------|--------|
| Product Intent context | Workbench Wall, Orchestration detail, BuildTrackPanel | Implemented |
| Two prioritized WOs (`wo-3014`, `wo-3015`) | release-artifacts, quality-status, orchestration detail | Implemented |
| Task drilldown | BuildTrackPanel, Workspace Session detail | Implemented |
| Governance verdicts | governance, quality-compliance, controls, BuildTrackPanel | Implemented |
| Traceability links | Workbench Wall, Orchestration detail | Implemented |
| Team snapshot | team console, BuildTrackPanel | Implemented |

## Navigation contract

- Top-down: Foundry → Workshop → Workbench → Wall or Console
- Wall is the first item in workbench side nav and the default landing route
- Breadcrumbs on workbench shell and detail pages
- Side nav group order matches `platform-developer-guide/pages/consoles/README.md`

## Rule compliance

- Radix imports only in `src/foundry-ui`
- Feature code uses `foundry-ui` wrappers and design tokens
- Mock data loaded via `src/lib/data.ts` adapters

## Verification commands

```bash
npm run lint
npm run build
npm run dev
```

Suggested walkthrough:

1. Open `/` and navigate to Photon → Payment Gateway workbench
2. Confirm Workbench Wall (landing) with side nav; Wall link active at top
3. Open `release-artifacts` and `quality-status` for Build Track panel
4. Open Orchestration → PI detail for full Build Track depth
5. Open Team console → member profile detail
6. Open Workspaces Overview → session detail
