---
name: Act 2-3 Restructure
overview: "Restructure Acts 2-7 of the presentation: merge archetype slides, rewrite mandate and governance slides, move three-domain slides into Act 2, merge old Acts 3+4 into 'The System Design', renumber all downstream slides, reduce from 7 acts to 6."
todos:
  - id: merge-slides-9-10
    content: Merge Slides 9+10 into new Slide 9 (Spend Archetypes) — fix title, headline, remove CPP reference, fold in archetype details
    status: completed
  - id: rewrite-slide-11-mandates
    content: Rewrite Slide 11 as new Slide 10 (Spend Mandates) — proper conceptual introduction, remove locked count
    status: completed
  - id: rewrite-slide-12-governance
    content: "Rewrite Slide 12 as new Slide 11 (Governance: Constraints and Decisions) — structured/unstructured decisions, deliberation control"
    status: completed
  - id: rewrite-slide-13-domains
    content: Rewrite Slide 13 as new Slide 12 (The Three Domains) — why they exist, problem context framing
    status: completed
  - id: merge-slides-13-14-value
    content: Merge old Slides 13+14 into new Slide 13 (Value Added and Value Realized)
    status: completed
  - id: rename-acts-renumber
    content: Merge old Acts 3+4 into 'Act 3 — The System Design', renumber Acts 5-7 to 4-6, renumber all downstream slides (-1), update all references
    status: completed
  - id: update-discussion-file
    content: Apply all structural changes to presentation-contents-discussion.md, update Source Mapping table
    status: completed
  - id: commit-changes
    content: Commit all changes to both files
    status: completed
isProject: false
---

# Act 2-3 Restructure and Slide Content Revisions

## Current State (Slides 9-34, Acts 2-7)

```
Act 2 — The Framework (Slides 9-12)
  9:  Spend Archetypes — Four Workflow Patterns
  10: Archetype Detail — Side-by-Side
  11: Spend Mandates — The Authorization Envelope
  12: Two Natures of Governance

Act 3 — The Three Domains (Slides 13-16)
  13: The Three Domains — Roles and Value Added
  14: All Stakeholders — Value Realized
  15: Systems and Bounded Contexts
  16: Context Boundaries and Integration Points

Act 4 — Entities Within Bounded Contexts (Slides 17-22)
Act 5 — How the Story Becomes Data (Slides 23-27)
Act 6 — Program Lifecycle and Extensibility (Slides 28-32)
Act 7 — The Opportunity (Slides 33-34)
```

## Target State (Slides 9-33, Acts 2-6)

```
Act 2 — The Framework (Slides 9-13)
  9:  Spend Archetypes (MERGED from 9+10, title/headline fixed)
  10: Spend Mandates (REWRITTEN — proper intro, no locked count)
  11: Governance: Constraints and Decisions (REWRITTEN)
  12: The Three Domains (NEW framing — why, roles, problem context)
  13: Value Added and Value Realized (MERGED from 13+14)

Act 3 — The System Design (MERGED from old Acts 3+4, Slides 14-21)
  14: Systems and Bounded Contexts (was 15)
  15: Context Boundaries and Integration Points (was 16)
  16: Bank Domain Entities (was 17)
  17: ESP Domain Entities (was 18)
  18: Corporate Domain Entities (was 19)
  19: Entity Relationships Across Domains (was 20)
  20: Hierarchies — Corporate's and ESP's View (was 21)
  21: Hierarchies — Bank's View (was 22)

Act 4 — How the Story Becomes Data (was Act 5, Slides 22-26)
  22: Corporate Payment Program's Reflection (was 23)
  23: Policy Cascade (was 24)
  24: Authorization Flow (was 25)
  25: Transaction Posting (was 26)
  26: Comprehensive Manifestation (was 27)

Act 5 — Program Lifecycle and Extensibility (was Act 6, Slides 27-31)
  27: Program Lifecycle Overview (was 28)
  28: Setup Phase (was 29)
  29: Operational Phase (was 30)
  30: Financial Phase (was 31)
  31: Embedding and Extension (was 32)

Act 6 — The Opportunity (was Act 7, Slides 32-33)
  32: Meridian End-to-End (was 33)
  33: Next Steps (was 34)
```

Net change: 35 slides (0-34) becomes 34 slides (0-33). One slide removed (old Slide 10 merged into 9). 7 acts become 6 (old Acts 3+4 merge).

## Changes in Detail

### 1. Merge Slides 9+10 into new Slide 9: "Spend Archetypes"

- **Title:** "Spend Archetypes" (remove "Four Workflow Patterns")
- **Headline:** Remove "four" — use "Corporate payments organize into Spend Archetypes — each with a distinct control model, card lifecycle, enrollment pattern, and reconciliation approach."
- **Keep:** The comparison table from old Slide 9
- **Fold in:** Key details from old Slide 10 as bullets (card usage specifics per archetype)
- **Keep:** "Embedded is a delivery mechanism, not an archetype" bullet
- **Remove:** "Each archetype maps 1:1 to a Corporate Payment Product" (CPP not yet introduced, mapping is wrong)
- **Replace with:** "Archetypes are not product names — they are the organizing principle for how corporates govern spend. Each defines a distinct pattern of control, lifecycle, enrollment, and reconciliation."

### 2. Rewrite Slide 10 (was 11): "Spend Mandates"

- **Title:** "Spend Mandates — The Authorization Envelope"
- **Headline:** Rewrite to introduce the *concept* before listing components. Draw from `01-problem-space/05-spend-mandates.md` — the "chain of questions" framing (Why was this allowed? Who authorized it? Whose budget? Which rules? How is it booked? Who is accountable?)
- **Remove:** "eight components" from headline
- **Keep:** The component table (Purpose, Authority, Budget Source, Policy Scope, Limits, Attribution, Validity, Exceptions) with Meridian examples
- **Keep:** "No single system entity called Spend Mandate" bullet

### 3. Rewrite Slide 11 (was 12): "Governance: Constraints and Decisions"

- **Title:** "Governance: Constraints and Decisions"
- **Headline:** "Governance is not enforcement alone. It requires constraints that the platform enforces automatically, and decisions — structured and unstructured."
- **Constraints section:** Keep as-is (budget, spend policy, limits, bank evaluates on every transaction)
- **Decisions section:** Restructure using same examples but organized as:
  - Structured decisions: representable as rules, enforceable (Purpose, Attribution, Validity)
  - Unstructured decisions: require human deliberation — the platform provides deliberation control (Authority escalation, Exceptions)
- **Closing bullet:** The design challenge: enforce constraints automatically, enforce structured decision rules, and provide deliberation control for unstructured decisions

### 4. Rewrite Slide 12 (was 13): "The Three Domains"

- **Title:** "The Three Domains"
- **Reframe:** Focus on *why* three domains exist — rooted in the problem context. Bank organizes around risk (Slide 6 callback), Corporate organizes around governance, neither can collapse into the other. The ESP exists to translate between them.
- **Keep:** Bank/ESP/Corporate role descriptions
- **Keep:** "Each domain owns what it understands best" and separation-of-concerns bullets

### 5. Merge old Slides 13+14 into new Slide 13: "Value Added and Value Realized"

- **Title:** "Value Added and Value Realized"
- **Combine:** What each domain contributes (value added) and what each captures (value realized) into a single slide
- **Keep:** The stakeholder value table from old Slide 14 (Bank, ESP, Corporate, Members)
- **Keep:** "Value is not zero-sum" bullet

### 6. Merge old Acts 3+4 into "Act 3 — The System Design"

- Old Act 3 ("The Three Domains") header and old Act 4 ("Entities Within Bounded Contexts") header both become one act: "Act 3 — The System Design"
- Remove the Act 4 header entirely — its slides (entities, hierarchies) flow directly after systems/boundaries slides under Act 3

### 7. Renumber acts downstream

- Old Act 5 ("How the Story Becomes Data") becomes Act 4
- Old Act 6 ("Program Lifecycle and Extensibility") becomes Act 5
- Old Act 7 ("The Opportunity") becomes Act 6
- Total: 7 acts become 6

### 8. Renumber all downstream slides (-1)

- Old Slides 15-34 become Slides 14-33
- All `Slide N` references throughout both files must update
- Speaker Notes at the end of the outline must update

### 9. Apply same changes to `presentation-contents-discussion.md`

- Same structural changes (merge, rewrite, renumber)
- Update Source Mapping table
- Update all cross-references

### 10. Commit

- Commit all changes with appropriate message

## Files Modified

- `[presentation-outline.md](us-bank-commercial-card/corporate-payment-book-background-work/presentation-outline.md)`
- `[presentation-contents-discussion.md](us-bank-commercial-card/corporate-payment-book-background-work/presentation-contents-discussion.md)`

## Execution Approach

Use Python scripts for the renumbering (collision-safe, high-to-low for increases, low-to-high for decreases). Use StrReplace for content rewrites. Process the outline file first, verify, then the discussion file.