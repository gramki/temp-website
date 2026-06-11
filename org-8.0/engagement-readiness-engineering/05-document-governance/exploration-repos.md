# Exploration Repository Structure

[← Back to Document Governance](README.md) · [ERE Guide](../README.md)

Each Exploration gets **one Git repo**: `EXP-{CODE}-exploration`

This single repository contains all pre-commitment work — discovery, RFI/RFP responses, solution design, commercial analysis, qualification, and proposal development.

---

## Repository Structure

```
├── README.md                        # Overview, qualification status, key dates
├── customer-context/
│   └── README.md                    # Index of customer docs (SharePoint URLs)
│
├── rfi-rfp/                         # RFI/RFP response work
│   ├── README.md                    # RFI/RFP summary, deadlines, status
│   ├── original/
│   │   └── README.md                # Links to original RFI/RFP in SharePoint
│   ├── questions/
│   │   ├── questions-parsed.md      # Extracted questions from RFI/RFP
│   │   └── question-assignments.md  # Who owns which questions
│   ├── responses/
│   │   ├── section-{n}.md           # Draft responses by section
│   │   └── ...
│   ├── compliance-matrix.md         # Requirement-to-response mapping
│   ├── assumptions.md               # Assumptions and clarifications
│   └── review-notes.md              # Internal review feedback
│
├── discovery/
│   ├── stakeholder-map.md
│   ├── pain-points.md
│   ├── requirements-sketch.md
│   └── meeting-notes/
│       └── {date}-{topic}.md
│
├── solution/
│   ├── preliminary-architecture.md
│   ├── archetype-fit.md
│   ├── gap-assessment.md
│   └── poc/
│       ├── poc-plan.md
│       ├── poc-scope.md
│       └── poc-results.md
│
├── commercial/
│   ├── estimation.md
│   ├── pricing-model.md
│   ├── risk-assessment.md
│   └── assumptions.md               # Commercial assumptions
│
├── qualification/
│   ├── qualification-checklist.md
│   ├── go-no-go-decision.md
│   └── lessons-learned.md           # Capture learnings even if no-go
│
└── proposal/
    ├── proposal-outline.md          # Structure and ownership
    ├── proposal-draft.md            # Working draft (final → SharePoint)
    ├── executive-summary.md
    ├── technical-approach.md
    ├── team-structure.md
    ├── timeline.md
    └── review-feedback.md           # Internal review notes
```

---

## Folder Descriptions

### customer-context/

Index of customer-provided documents. Actual files reside in SharePoint; this folder contains only links and context.

### rfi-rfp/

Complete RFI/RFP response workflow:

| Subfolder/File | Purpose |
|----------------|---------|
| `original/` | Links to the original RFI/RFP documents in SharePoint |
| `questions/` | Parsed questions and assignment tracking |
| `responses/` | Draft responses organized by section |
| `compliance-matrix.md` | Maps requirements to responses for compliance verification |
| `assumptions.md` | Assumptions made during response preparation |
| `review-notes.md` | Feedback from internal reviews |

### discovery/

Customer discovery artifacts:

| File | Purpose |
|------|---------|
| `stakeholder-map.md` | Key stakeholders, their roles, and relationships |
| `pain-points.md` | Documented customer challenges and needs |
| `requirements-sketch.md` | Initial requirements understanding (before formal BRD) |
| `meeting-notes/` | Discovery meeting notes organized by date and topic |

### solution/

Preliminary solution design:

| File | Purpose |
|------|---------|
| `preliminary-architecture.md` | High-level architecture approach |
| `archetype-fit.md` | How well existing archetypes fit the opportunity |
| `gap-assessment.md` | Gaps between customer needs and available capabilities |
| `poc/` | Proof-of-concept planning and results if applicable |

### commercial/

Commercial analysis and estimation:

| File | Purpose |
|------|---------|
| `estimation.md` | Effort and duration estimates |
| `pricing-model.md` | Pricing approach and structure |
| `risk-assessment.md` | Commercial and delivery risks |
| `assumptions.md` | Commercial assumptions underlying estimates |

### qualification/

Go/no-go decision documentation:

| File | Purpose |
|------|---------|
| `qualification-checklist.md` | Criteria for qualifying the opportunity |
| `go-no-go-decision.md` | Documented decision and rationale |
| `lessons-learned.md` | Learnings captured even if the decision is no-go |

### proposal/

Proposal development:

| File | Purpose |
|------|---------|
| `proposal-outline.md` | Proposal structure and section ownership |
| `proposal-draft.md` | Working draft (final version exported to SharePoint) |
| `executive-summary.md` | Executive summary content |
| `technical-approach.md` | Technical approach and methodology |
| `team-structure.md` | Proposed team structure |
| `timeline.md` | Delivery timeline |
| `review-feedback.md` | Internal review notes and feedback |

---

## Transition to Engagement

When an Exploration converts to an Engagement:

1. **Exploration repo becomes read-only** — preserved as historical record
2. **Key artifacts transition** to Engagement repos:
   - Discovery findings → `ENG-{CODE}-requirements/customer-inputs/`
   - Architecture decisions → `ENG-{CODE}-requirements/decisions/`
   - Estimates → `ENG-{CODE}-project/charter/`
3. **SharePoint folders** are created under the `ENG-{CODE}` structure
4. **Links are established** between Engagement repos and the archived Exploration repo

See [Governance Rules](governance-rules.md) for auto-provisioning details.
