---
name: Hub Dev Flow Guide Revision
overview: Revise the hub-development-flow guide to reframe the development model around paradigm differences (persistent vs ephemeral, promotion vs merge) rather than isolation, broaden the audience beyond "regulated industries" to include AI-assisted development and context-switching teams, and provide proper context for trade-offs.
todos:
  - id: revise-why-different
    content: Revise 01-why-different-model.md with new framing (paradigm difference, AI context)
    status: pending
  - id: revise-merits
    content: Update 08-merits.md to broaden audience and add AI-assisted development context
    status: pending
    dependencies:
      - revise-why-different
  - id: revise-limitations
    content: Reframe 09-limitations.md trade-offs with proper context
    status: pending
    dependencies:
      - revise-why-different
  - id: update-best-practices
    content: Minor update to 10-best-practices.md for consistency
    status: pending
    dependencies:
      - revise-limitations
---

# Hub Development Flow Guide Revision

## Objective

Revise the hub-development-flow guide to:

1. Reframe workbenches as **persistent, always-available** (not "always running")
2. Reduce over-emphasis on **regulated industries** — broaden to small teams + AI-assisted development
3. Clarify that **isolation is shared by both models** — the real differences are persistence and integration model
4. Provide proper **context for trade-offs** — who is affected, when does this matter

---

## Files to Modify

### 1. [01-why-different-model.md](olympus-hub-docs/10-guides/hub-development-flow/01-why-different-model.md)

**Changes:**

| Section | Change |
|---------|--------|
| Lines 12-14 (short answer) | Broaden from "small teams in regulated enterprises" to include AI-assisted development and context-switching |
| Lines 17-27 (Context section) | Add AI-assisted development context: shrinking team sizes, frequent context switching |
| Lines 28-68 (Problem with Branches) | Reframe as **paradigm difference** — merge vs promotion, ephemeral vs persistent — not just compliance |
| Lines 71-74 (Workbenches as Isolated Contexts) | Change heading to "Workbenches as Persistent Contexts" — both models provide isolation |
| Line 150 ("complete, running environment") | Clarify: "always-available environment" — scale-to-zero, not always running |
| Lines 156-168 (Is This Right for Everyone?) | Reorder: small teams + AI context first, compliance as one benefit |

---

### 2. [08-merits.md](olympus-hub-docs/10-guides/hub-development-flow/08-merits.md)

**Changes:**

| Section | Change |
|---------|--------|
| Lines 7-9 (intro) | Broaden from "small teams in regulated enterprises" |
| Lines 11-65 (Compliance section) | Keep content but consider moving down — lead with simpler model benefits |
| Lines 222-238 (Small Team Friendly) | Add: AI-assisted development reduces team sizes; smaller teams switch contexts more; Hub's model benefits this |
| Lines 241-251 (When Hub Shines) | Add rows: "AI-assisted development", "Frequent context switching" |
| New section | Add merit: "No Local Workspace Required" — development in cloud workspace, no "works on my machine" issues |

---

### 3. [09-limitations.md](olympus-hub-docs/10-guides/hub-development-flow/09-limitations.md)

**Changes:**

| Section | Change |
|---------|--------|
| Lines 13-46 (No Git Branch Support) | Reframe as **paradigm difference**: both models provide isolation. The difference is integration model (merge vs promotion) and environment model (ephemeral vs persistent). |
| Lines 33-39 (What you give up/gain table) | Revise: "Familiar branching" → "Merge-based integration"; "Complete environment isolation" → "Persistent, always-available environments" |
| Lines 49-75 (Workbench Creation Overhead) | Add context: workbenches are scale-to-zero (low cost), persistent (state preserved). Overhead is upfront creation, not ongoing cost. |
| Line 264 (Bottom line) | Broaden from "regulated environments" to "small teams prioritizing simplicity, especially with compliance needs or frequent context-switching" |
| Lines 238-248 (When Hub Might Not Be the Right Fit) | Add nuance: some items are paradigm differences, not inherent weaknesses |

---

### 4. [10-best-practices.md](olympus-hub-docs/10-guides/hub-development-flow/10-best-practices.md)

**Changes:**

| Section | Change |
|---------|--------|
| Lines 25-36 (When to Create a Feature Workbench) | Add note: workbenches are cost-efficient (scale-to-zero), but creation overhead exists — default to primary DEV unless genuinely needed |

---

## Key Messaging Changes

| Old Framing | New Framing |
|-------------|-------------|
| "Isolated contexts" | "Persistent, always-available contexts" |
| "Complete, running environment" | "Always-available environment (scale-to-zero)" |
| "Small teams in regulated enterprises" | "Small teams prioritizing simplicity — especially with AI-assisted development or compliance needs" |
| "No Git branching = less isolation" | "Different integration model (promotion vs merge) — both provide isolation" |
| Compliance as primary driver | One of several benefits alongside simplicity and context-switching support |

---

## Execution Order

1. **01-why-different-model.md** — Sets the framing for the entire guide
2. **08-merits.md** — Aligns benefits with the new framing
3. **09-limitations.md** — Reframes trade-offs with proper context
4. **10-best-practices.md** — Minor adjustment for consistency