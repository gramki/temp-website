---
name: Thesis Folder Restructure
overview: Restructure the persuasion ladder documents into a `the-thesis/` folder, create the bridge document connecting the systems gap to the thesis, and update all cross-references across the documentation suite.
todos:
  - id: create-folder-move
    content: Create the-thesis/ folder and git mv the 5 thesis documents into it (diagnosis.md renamed to thesis.md)
    status: completed
  - id: write-bridge
    content: Write beyond-systems.md -- capabilities are necessary but not sufficient; systems-first absorption is unsustainably expensive, capabilities without coherence don't deliver customer-centricity, and AI (forward handshake) proves why the model is essential
    status: completed
  - id: write-readme
    content: Write the-thesis/README.md as a reading guide that sequences the persuasion ladder
    status: completed
  - id: update-crossrefs
    content: "Update all cross-references: thesis.md hub-way link, narrative.md thesis links (including diagnosis->thesis rename), hub-way README further reading, problems.md gap.md link, benefits.md diagnosis->thesis rename, enterprise-ai-adoption.md backward handshake from beyond-systems"
    status: completed
  - id: verify
    content: Verify git status, all paths resolve, no broken references in the repo
    status: completed
isProject: false
---

# Thesis Folder Restructure and Bridge Document

## Current State

The persuasion ladder documents (`problems.md`, `enterprise-ai-adoption.md`, `gap.md`, `diagnosis.md`, `benefits.md`) are scattered in `what-we-sell/` alongside unrelated files. The Hub Way framework docs live in `the-hub-way/`. A critical bridge document is missing between `gap.md` and the thesis. Additionally, `diagnosis.md` should be renamed to `thesis.md` to reflect that it contains the core thesis (seven principles), not just a diagnosis.

## Target Structure

```
what-we-sell/
  the-thesis/
    README.md                     <- reading guide (NEW)
    problems.md                   <- moved
    gap.md                        <- moved
    beyond-systems.md             <- bridge document (NEW)
    enterprise-ai-adoption.md     <- moved
    thesis.md                     <- moved + renamed from diagnosis.md
    benefits.md                   <- moved
  the-hub-way/
    README.md                     <- updated (Further Reading)
    narrative.md                  <- updated (cross-refs)
    critique.md
    enablement/
  solution-story/
  ...existing files...
```

**Reading order:** problems -> gap -> beyond-systems -> enterprise-ai-adoption -> thesis -> benefits -> the-hub-way/

## Phase 1: Create folder and move files

- Create `org-8.0/what-we-sell/the-thesis/`
- Move 5 files via `git mv`:
  - `problems.md` -> `the-thesis/problems.md`
  - `gap.md` -> `the-thesis/gap.md`
  - `enterprise-ai-adoption.md` -> `the-thesis/enterprise-ai-adoption.md`
  - `diagnosis.md` -> `the-thesis/thesis.md` (rename)
  - `benefits.md` -> `the-thesis/benefits.md`

## Phase 2: Write the bridge document — `beyond-systems.md`

A new document bridging from `gap.md` (the systems gap evidence) and `problems.md` (the Modernization Trap) to `thesis.md` (the core thesis and principles).

**Content outline:**

1. **The gap is real and the capabilities are essential** -- banks genuinely need intelligence, engagement, memory, product composition, innovation infrastructure. No dismissal of the ambition.
2. **The absorption problem** -- reference `problems.md` Modernization Trap (lines 138-163) rather than repeating it. The traditional approach absorbs capabilities one system at a time, one domain at a time, each requiring bespoke integration. With M domains x N capability systems x K channels, the integration surface is combinatorial. The timeline is a decade+. By the time you're halfway, the first systems need replacement.
3. **Capabilities without coherence** -- the critical insight: even if a bank deploys all missing systems, it has a collection of capabilities, not a coherent operational model. The fraud engine works. The identity system works. The engagement platform works. But nobody modeled "process this credit card application" as a single governed piece of work. The customer's experience is whatever the plumbing produces. Capability gaps are closed; the coherence gap remains.
4. **Customer-centricity becomes a matrix problem** -- servicing a customer is cross-domain (the customer has cards, accounts, payments, lending) and cross-channel (mobile, web, branch, contact center). Under the systems approach, each domain has its own engagement, action, and integration stack. Cross-domain servicing and cross-channel continuity each become their own integration programs. The customer still falls through the seams between domains, and channel continuity is plumbing, not structure.
5. **What's actually needed** -- more systems are necessary but not sufficient. The bank needs both the capabilities AND a model of the work that gives those capabilities context, coherence, and composability. Without the model, more systems means more plumbing, more fragmentation, and a longer path to the outcome. With the model, capability absorption becomes tractable -- systems register into the model rather than being bespoke-plumbed to each other.
6. **Closing bridge to enterprise-ai-adoption** -- AI is the most consequential capability arriving at banks. It is also the one that most urgently proves the beyond-systems argument: AI cannot deliver enterprise value without the structural model that the systems-first approach never produces. This forward reference sets up the handshake with `enterprise-ai-adoption.md`.

**Tone:** Respect the ambition ("the capabilities are essential"), challenge the method ("the absorption model is the problem"), land on "necessary but not sufficient" -- not "stop buying systems." No Hub Way terminology -- this is a thesis-level document.

## Phase 3: Write `the-thesis/README.md`

A concise reading guide that:

- Introduces the thesis scope ("Why banks cannot evolve, and what an alternative looks like")
- Sequences the documents with one-line descriptions:
  - `problems.md` -- The felt problems and structural causes
  - `gap.md` -- The detailed systems gap analysis
  - `beyond-systems.md` -- Why closing the gap system-by-system is necessary but not sufficient
  - `enterprise-ai-adoption.md` -- Why AI -- the most consequential capability arriving -- proves the beyond-systems argument
  - `thesis.md` -- Four core concerns, seven governing principles, and the bridge to The Hub Way
  - `benefits.md` -- What changes if the thesis is adopted
- Points forward: "The Hub Way translates this thesis into a concrete framework" with link to `../the-hub-way/`

## Phase 4: Update cross-references

After files move from `what-we-sell/` to `what-we-sell/the-thesis/`, relative paths change. All six updates below are required:

**In `thesis.md` (renamed from `diagnosis.md`, now in `the-thesis/`):**

- Line 129: `[The Hub Way](the-hub-way/README.md)` -> `[The Hub Way](../the-hub-way/README.md)`

**In `the-hub-way/narrative.md`:**

- Line 9: `../problems.md` -> `../the-thesis/problems.md`
- Line 9: `../enterprise-ai-adoption.md` -> `../the-thesis/enterprise-ai-adoption.md`
- Line 9: `../diagnosis.md` -> `../the-thesis/thesis.md`
- Line 117: `../benefits.md` -> `../the-thesis/benefits.md`

**In `the-hub-way/README.md`:**

- Add to "Further Reading" section (line 203+): link to the thesis folder README

**In `enterprise-ai-adoption.md` (now in `the-thesis/`):**

- Add a backward-referencing opening that connects to beyond-systems: AI is not just another missing capability -- it is the first technology wave that requires the structural model the systems-first approach never produces. This completes the handshake started by beyond-systems.md's closing paragraph.

**In `problems.md` (now in `the-thesis/`):**

- In "The Systems Gap" section (around line 115-119): add a parenthetical link to `gap.md` for the detailed enumeration
- Line 199: `enterprise-ai-adoption.md` path stays the same (sibling file -- no change needed)

**In `benefits.md` (now in `the-thesis/`):**

- Update reference from `diagnosis.md` to `thesis.md` (sibling, just filename change)

**In `thesis.md` (now in `the-thesis/`):**

- Internal cross-refs to `problems.md` and `enterprise-ai-adoption.md` remain sibling references -- no path changes needed

## Phase 5: Verify

- Confirm all five moved files (including the diagnosis->thesis rename) are tracked by git
- Verify all cross-reference paths resolve correctly
- Grep for any remaining references to `diagnosis.md` across the repo and update them
- Check no other files in the repo reference the old paths (solution-story/bridging-to-zeta-reality.md mentions `gap.md` by name in a table but not as a link)

