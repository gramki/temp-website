---
name: Hub Docs Revision + SOT Guide
overview: "Two work streams: (1) Revise hub-development-flow guide to reframe around paradigm differences and broaden audience, and (2) Convert Scenario-Oriented Thinking scratchpad document into a formal decision framework guide suite."
todos:
  - id: revise-why-different
    content: Revise 01-why-different-model.md with new framing (paradigm difference, AI context)
    status: completed
  - id: revise-merits
    content: Update 08-merits.md to broaden audience and add AI-assisted development context
    status: completed
    dependencies:
      - revise-why-different
  - id: revise-limitations
    content: Reframe 09-limitations.md trade-offs with proper context
    status: completed
    dependencies:
      - revise-why-different
  - id: update-best-practices
    content: Minor update to 10-best-practices.md for consistency
    status: completed
    dependencies:
      - revise-limitations
  - id: sot-create-folder
    content: Create scenario-oriented-thinking folder in 11-decision-frameworks
    status: completed
  - id: sot-entry-point
    content: Create entry point doc with overview, reading guide, decision flowchart
    status: completed
    dependencies:
      - sot-create-folder
  - id: sot-core
    content: Create core concepts doc from sections 2-5 (DDD/AOSM, concepts, specs)
    status: completed
    dependencies:
      - sot-create-folder
  - id: sot-argument
    content: Create argument doc from section 8 (normative-first paradigm)
    status: completed
    dependencies:
      - sot-create-folder
  - id: sot-examples
    content: Create examples doc consolidating all examples
    status: completed
    dependencies:
      - sot-create-folder
  - id: sot-alternatives
    content: Create alternatives comparison doc from section 9
    status: completed
    dependencies:
      - sot-create-folder
  - id: sot-adoption
    content: Create adoption/migration doc from sections 10-11
    status: completed
    dependencies:
      - sot-create-folder
  - id: sot-anti-patterns
    content: Create anti-patterns doc (when NOT to use)
    status: completed
    dependencies:
      - sot-create-folder
  - id: sot-update-readme
    content: Update 11-decision-frameworks/README.md with new suite
    status: completed
    dependencies:
      - sot-entry-point
      - sot-core
      - sot-argument
      - sot-examples
      - sot-alternatives
      - sot-adoption
      - sot-anti-patterns
  - id: sot-cleanup
    content: Delete scratchpad file and validate all links
    status: completed
    dependencies:
      - sot-update-readme
---

# Hub Documentation Revision Plan

## Work Stream 1: Hub Development Flow Guide Revision

### Objective
Revise the hub-development-flow guide to:
1. Reframe workbenches as **persistent, always-available** (scale-to-zero, not "always running")
2. Reduce over-emphasis on **regulated industries** — broaden to small teams + AI-assisted development
3. Clarify that **isolation is shared by both models** — the real differences are persistence and integration model
4. Provide proper **context for trade-offs** — who is affected, when does this matter

### Files to Modify

**1. [01-why-different-model.md](olympus-hub-docs/10-guides/hub-development-flow/01-why-different-model.md)**
- Lines 12-14: Broaden from "regulated enterprises" to include AI-assisted development
- Lines 17-27: Add AI context (shrinking team sizes, context switching)
- Lines 28-68: Reframe as paradigm difference (merge vs promotion, ephemeral vs persistent)
- Lines 71-74: Change heading to "Workbenches as Persistent Contexts"
- Line 150: Clarify "always-available" not "always running"
- Lines 156-168: Reorder benefits (small teams + AI first, compliance as one benefit)

**2. [08-merits.md](olympus-hub-docs/10-guides/hub-development-flow/08-merits.md)**
- Broaden intro; add AI-assisted development context to Small Team Friendly section
- Add merit: "No Local Workspace Required"

**3. [09-limitations.md](olympus-hub-docs/10-guides/hub-development-flow/09-limitations.md)**
- Reframe "No Git Branch Support" as paradigm difference
- Add scale-to-zero/low cost context for workbench overhead
- Add nuance to "When Hub Might Not Be the Right Fit"

**4. [10-best-practices.md](olympus-hub-docs/10-guides/hub-development-flow/10-best-practices.md)**
- Add scale-to-zero note for workbench creation guidance

---

## Work Stream 2: Scenario-Oriented Thinking Decision Framework

### Objective
Convert [scratchpad document](olympus-hub-docs/scratchpad/0WIP-scenario-oriented-thinking-for-business-process-automation.md) (~1100 lines) into a formal decision framework guide suite in `11-decision-frameworks/scenario-oriented-thinking/`.

### Phase 2A: Structure

| Task | Description |
|------|-------------|
| Create folder | `olympus-hub-docs/11-decision-frameworks/scenario-oriented-thinking/` |
| Plan document split | 7 files following Hub Agent vs Seer Agent pattern |

### Phase 2B: Document Split

| New File | Source Content | Purpose |
|----------|----------------|---------|
| `scenario-oriented-thinking.md` | New entry point | Overview, reading guide, quick reference, decision flowchart |
| `scenario-oriented-thinking-core.md` | Sections 2-5 | Foundations (DDD/AOSM), core concepts, three specifications |
| `scenario-oriented-thinking-argument.md` | Section 8 | Central thesis: normative-first paradigm shift |
| `scenario-oriented-thinking-examples.md` | Extract from various | Consolidated examples (disputes, payments, onboarding) |
| `scenario-oriented-thinking-alternatives.md` | Section 9 | Comparison with BPM, Low-Code, Temporal, Custom Code |
| `scenario-oriented-thinking-adoption.md` | Sections 10-11 | Migration guidance, best practices |
| `scenario-oriented-thinking-anti-patterns.md` | New + Section 7 | When NOT to use, common mistakes |

### Phase 2C: Content Enhancements

| Task | Description |
|------|-------------|
| Add "The Confusion" framing | Explicitly state the problem being addressed |
| Create decision flowchart | Visual aid: "Should I use Scenario-Oriented Thinking?" |
| Extract/consolidate examples | Pull all examples into dedicated file |
| Create anti-patterns | Document when NOT to use |
| Add audience reading paths | Paths for APO, PA, Developer |
| Review Hub-specific references | Keep conceptual; link out for Hub implementation |

### Phase 2D: Integration

| Task | Description |
|------|-------------|
| Update README | Add suite to `11-decision-frameworks/README.md` index |
| Cross-reference | Link from hub-development-flow, scenario spec docs |
| Delete scratchpad | Remove original file after formalization |
| Quality review | Consistency check, link validation, status markers |

---

## Execution Order

1. **Work Stream 1** (Hub Dev Flow) — 4 files, sets foundational framing
2. **Work Stream 2** (SOT Guide) — Create structure, split content, integrate