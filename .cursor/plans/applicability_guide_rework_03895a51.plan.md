---
name: Applicability Guide Rework
overview: Complete rewrite of the Hub Applicability Guide as an internal PM/Sales tool for identifying ideal customer profiles, understanding where Hub fits, and positioning Hub effectively.
todos:
  - id: rewrite-applicability
    content: Complete rewrite of olympus-hub-applicability-guide.md with new structure
    status: completed
  - id: remove-fabricated-metrics
    content: Remove or flag unsupported ROI claims for future validation
    status: completed
  - id: align-terminology
    content: Ensure all terminology matches glossary definitions
    status: completed
---

# Hub Applicability Guide Rework

## Current Problems

The existing [olympus-hub-docs/01-concepts/olympus-hub-applicability-guide.md](olympus-hub-docs/01-concepts/olympus-hub-applicability-guide.md) has several issues:

1. **Outdated framing** — Uses "operations" language rather than "information-centric work"
2. **Incorrect exclusions** — Claims Hub doesn't fit for creative work, relationship-intensive work, unpredictable environments (contradicts the vision discussion)
3. **Missing core concepts** — No mention of Scenarios, collaboration modalities, Persona-Channel framework, four pillars
4. **Fabricated metrics** — Contains unsupported ROI percentages (20-40% reduction, etc.)
5. **Generic enterprise content** — Implementation phases and maturity models could apply to any software
6. **Dual audience confusion** — Tries to serve both external customers and internal PM/Sales

## Revised Structure (Internal PM/Sales Focus)

### Part 1: Understanding the Fit

**1.1 What Hub Is For**

- Information-centric work definition (link to [Glossary](olympus-hub-docs/01-concepts/glossary.md))
- The core question: "Does work involve receiving, interpreting, deciding, acting on information?"
- The collaboration dimension: Human-Human, Human-AI, AI-AI modalities
- The governance dimension: Audit, compliance, accountability needs

**1.2 When Hub Fits Well**

- Information as the medium (vs. physical transformation)
- Collaborative problem-solving (team coordination, multi-agent scenarios)
- Governed operations (traceable decisions, regulatory requirements)
- Organizational learning (memory and improvement over time)

**1.3 When Hub May Not Fit**

- Pure physical operations (manufacturing floor, warehouse picking)
- Completely novel one-time activities with no reusable pattern
- Simple single-user tools with no collaboration need
- NOTE: Explicitly correct the old guide's errors (creative work CAN fit, relationship work CAN fit)

### Part 2: Assessing Fit

**2.1 The Four-Question Assessment**

1. Is the work information-centric? (inputs, transformation, outputs)
2. Does it involve collaboration? (human-human, human-AI, or multi-agent)
3. Is governance important? (audit, compliance, accountability)
4. Would organizational memory improve outcomes?

**2.2 Work Spectrum Analysis**

- Structured processes → Semi-structured → Exploratory → Creative
- How Hub supports each (full automation → rich context and memory)

**2.3 Collaboration Maturity Path**

- Human-Human → Human-AI → AI-AI progression
- Starting point based on organizational readiness
- Not a mandatory path — organizations choose their level

### Part 3: Customer Profiles

**3.1 Ideal Customer Characteristics**

- Enterprise scale with multi-domain operations
- Information-centric functions (even if the business is physical)
- Compliance or governance requirements
- Interest in AI-Human collaboration (current or planned)

**3.2 Industry Fit Analysis**

| Industry | Why It Fits | Example Scenarios |
|----------|-------------|-------------------|
| Financial Services | Highly regulated, information-centric | Lending, disputes, compliance |
| Healthcare Administration | Coordination-intensive, audit-heavy | Claims, eligibility, care coordination |
| IT Operations | Signal-rich, governance-critical | Incidents, changes, service requests |
| Insurance | Document-intensive, decision-heavy | Underwriting, claims, policy admin |
| Professional Services | Knowledge work, client coordination | Engagements, deliverables, billing |
| Software Development | Pure information-centric, collaborative | See [Hub for Software Development](olympus-hub-docs/scratchpad/0WIP-hub-for-software-development.md) |

**3.3 Function Fit Analysis**

- Operations (any domain) — core fit
- Customer Service — signal-driven, governed
- Compliance and Risk — governance-critical
- HR and Legal — document and policy-intensive
- Finance and Accounting — structured, auditable
- R&D and Innovation — context and memory value (exploratory end)

### Part 4: Positioning and Differentiation

**4.1 What Hub Is Not**

- Not a workflow engine (goal-oriented, not procedure-oriented)
- Not an AI model provider (infrastructure for AI, not AI itself)
- Not a replacement for enterprise systems (collaboration layer)

**4.2 Competitive Positioning**

- vs. BPM platforms (scenario-oriented, not workflow-oriented)
- vs. AI copilots (governed, not ad-hoc)
- vs. Task management tools (operational platform, not project tracking)

**4.3 Key Differentiators**

- Four pillars: context, structure, memory, governance
- Scenario-oriented thinking (goals, not procedures)
- Multi-modal collaboration (Human-Human to AI-AI)
- Persona-Channel framework (meet users where they work)

### Part 5: Adoption Patterns

**5.1 Starting Points**

- By domain: Pick one Workbench, prove value, expand
- By modality: Start Human-Human, add AI progressively
- By work type: Start structured, extend to exploratory

**5.2 Signs of Readiness**

- Some process documentation exists
- Clear roles and responsibilities
- Governance is valued (not just tolerated)
- Interest in AI collaboration

**5.3 Signs of Unreadiness**

- "We don't need processes" culture
- No audit or compliance requirements
- Pure cost-cutting motivation (Hub is transformation, not just efficiency)

## Key Changes from Current Guide

| Aspect | Current Guide | Revised Guide |
|--------|---------------|---------------|
| Framing | "Operations" | Information-centric work |
| Creative work | Excluded | Included (exploratory end of spectrum) |
| Relationship work | Excluded | Included (coordination and memory value) |
| Core concepts | Missing | Scenarios, collaboration modalities, four pillars |
| Maturity model | CMM-like levels | Simple readiness signals |
| ROI claims | Specific percentages | Removed (or flagged as "to be validated") |
| Implementation phases | Generic enterprise rollout | Hub-specific adoption patterns |
| Audience | Mixed external/internal | Internal PM/Sales focus |

## Documents to Reference

- [Vision and Mission](olympus-hub-docs/00-_why/vision.md) — for framing and language
- [Introduction](olympus-hub-docs/01-concepts/introduction.md) — for six dimensions, four pillars
- [Glossary](olympus-hub-docs/01-concepts/glossary.md) — for terminology (information-centric work, operation, scenario)
- [Hub for Software Development](olympus-hub-docs/scratchpad/0WIP-hub-for-software-development.md) — for industry example pattern