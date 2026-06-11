# Engagement Repository Structure

[← Back to Document Governance](README.md) · [ERE Guide](../README.md)

Each Engagement gets **two Git repos** — one for requirements and change management, one for planning and execution.

---

## Repository Overview

| Repository | Purpose |
|------------|---------|
| `ENG-{CODE}-requirements` | Requirements, change requests, gap analysis, decisions, traceability |
| `ENG-{CODE}-project` | Charter, operating model, roadmap, staffing, PI planning, updates, retrospectives |

---

## ENG-{CODE}-requirements

Requirements and change requests — the "what" of the Engagement.

```
├── README.md                    # Overview, links to SharePoint
├── customer-inputs/
│   └── README.md                # Index of customer docs (in SharePoint, linked by URL)
├── requirements/
│   ├── functional/
│   │   └── {feature-area}.md
│   ├── non-functional/
│   │   ├── performance.md
│   │   ├── security.md
│   │   └── ...
│   └── constraints.md
├── change-requests/
│   ├── README.md                # CR process, status summary
│   ├── CR-001-{title}.md
│   └── ...
├── gap-analysis/
│   ├── platform-gaps.md
│   ├── archetype-gaps.md
│   └── inner-source-candidates.md
├── decisions/
│   └── ADR-001-{title}.md       # Architecture Decision Records
└── traceability/
    └── requirements-matrix.md
```

### Folder Descriptions

| Folder | Content |
|--------|---------|
| `customer-inputs/` | Index of customer-provided documents (actual files live in SharePoint) |
| `requirements/` | Analyzed requirements organized by type — functional, non-functional, constraints |
| `change-requests/` | Change request documents with status tracking and impact analysis |
| `gap-analysis/` | Analysis of gaps between requirements and platform/archetype capabilities |
| `decisions/` | Architecture Decision Records (ADRs) documenting key technical decisions |
| `traceability/` | Requirements traceability matrix linking requirements to implementation |

---

## ENG-{CODE}-project

Planning, PIs, and updates — the "how" and "when" of the Engagement. Uses SAFe terminology.

```
├── README.md                    # Engagement overview, quick links
├── charter/
│   └── engagement-charter.md
├── operating-model/
│   ├── roles-raci.md
│   ├── governance.md
│   └── escalation.md
├── roadmap/
│   ├── program-roadmap.md
│   └── release-plan.md
├── staffing/
│   ├── team-composition.md
│   ├── rotation-schedule.md
│   └── skill-matrix.md
├── pi/
│   ├── PI-1/
│   │   ├── README.md            # PI summary, dates, theme
│   │   ├── pi-objectives.md     # Committed objectives (accepted scope)
│   │   ├── pi-backlog.md        # Features/stories planned
│   │   ├── program-board.md     # Dependencies, milestones
│   │   ├── pi-risks.md          # ROAM: Resolved, Owned, Accepted, Mitigated
│   │   ├── confidence-vote.md   # Team confidence scores
│   │   ├── staffing.md          # PI-specific staffing
│   │   ├── decisions/
│   │   │   └── {decision}.md
│   │   ├── iterations/
│   │   │   ├── iteration-1.md
│   │   │   └── ...
│   │   └── pi-retrospective.md
│   └── PI-2/
│       └── ...
├── updates/
│   ├── README.md
│   ├── weekly/
│   │   └── {date}-update.md
│   └── steering-committee/
│       └── {date}-update.md
├── meetings/
│   ├── pi-planning/
│   ├── sync-meetings/
│   └── steering-committee/
├── risks/
│   └── risk-register.md
├── retrospectives/
│   └── engagement-retro.md
└── handover/
    ├── knowledge-transfer.md
    └── runbooks/
```

### Folder Descriptions

| Folder | Content |
|--------|---------|
| `charter/` | Engagement charter defining scope, objectives, and success criteria |
| `operating-model/` | Roles, RACI, governance structure, escalation paths |
| `roadmap/` | Program roadmap and release plan |
| `staffing/` | Team composition, rotation schedules, skill matrix |
| `pi/` | Program Increment folders with planning, execution, and retrospective artifacts |
| `updates/` | Weekly updates and steering committee reports |
| `meetings/` | Meeting notes organized by type |
| `risks/` | Risk register for Engagement-level risks |
| `retrospectives/` | Engagement-level retrospectives (vs. PI-level in `pi/`) |
| `handover/` | Knowledge transfer documentation and runbooks for steady state |

---

## PI Folder Structure

Each PI (Program Increment) folder contains a complete set of SAFe artifacts:

| File | SAFe Concept | Content |
|------|--------------|---------|
| `pi-objectives.md` | PI Objectives | Committed business and technical objectives; SMART format |
| `pi-backlog.md` | Program Backlog (PI slice) | Features, enablers, stories planned for this PI |
| `program-board.md` | Program Board | Delivery timeline, dependencies, milestones |
| `pi-risks.md` | ROAM Board | Risks: Resolved, Owned, Accepted, Mitigated |
| `confidence-vote.md` | Confidence Vote | Squad-by-squad confidence scores (1-5) |
| `iterations/` | Iteration Plans | Per-sprint stories, capacity, goals |
| `pi-retrospective.md` | Inspect & Adapt | What worked, what didn't, improvements |

See [PI Artifacts Reference](../reference/pi-artifacts.md) for detailed definitions.

---

## Cross-Reference Pattern

Git documents reference SharePoint content via URLs:

```markdown
## Customer Inputs

- Original RFP: [Link](https://sharepoint.com/sites/CustomerName/ENG-CODE/Customer-Provided/...)
- Requirements spreadsheet: [Link](https://sharepoint.com/sites/CustomerName/ENG-CODE/...)
```

This maintains the governance boundary while enabling navigation between systems.
