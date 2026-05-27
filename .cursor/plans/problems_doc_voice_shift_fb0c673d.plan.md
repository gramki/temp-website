---
name: Problems doc voice shift
overview: Reframe problems.md from an analyst's banking industry whitepaper to a Zeta strategic conviction document — articulating the market problem Zeta exists to solve, for Zeta's own board and stakeholders.
todos:
  - id: framing-and-title
    content: New title and opening paragraph — Zeta's voice, market framing
    status: pending
  - id: voice-shift
    content: Ground key claims in observable experience — light framing sentences at section openings
    status: pending
  - id: broaden-urgency
    content: Expand Why This Matters Now — competitive pressure, customer expectations, talent risk, failed transformation spend
    status: pending
  - id: existing-spend
    content: Add existing spend dimension — banks already burning budgets on ineffective coping
    status: pending
  - id: failed-approaches
    content: Elevate failed approaches (ESB, iPaaS, cloud, transformation programs) to more prominent position
    status: pending
  - id: trim-channels
    content: Trim channel section — keep felt consequences, reduce technical detail
    status: pending
  - id: reframe-footnotes
    content: Reframe Hub Way footnotes from product-spec to strategic positioning
    status: pending
  - id: strengthen-closing
    content: Strengthen Compound Picture closing — universality, structural persistence, worsening trajectory
    status: pending
isProject: false
---

# Reframe problems.md for Zeta's Board Audience

The document's analytical structure and problem depth are strong and should be preserved. The changes are primarily about **voice, framing, and emphasis** — making the document say "here is what we understand about the market we serve" rather than "here is an analysis of banking problems."

Target file: [problems.md](org-8.0/what-we-sell/problems.md)

## 1. Add market framing — opening and title

**Title**: Replace "The Problem: Work in Banking Domains Has No Model" with something that leads with consequence and positions Zeta's perspective. Candidate: "Why Banks Cannot Evolve — The Structural Problem We Solve" or similar.

**Opening paragraph** (new, before "The Core Problem"): 2-3 sentences framing this as Zeta's articulation of the market problem — "Across our engagements, we see a structural problem that every bank faces in some configuration..." This sets the voice as authoritative practitioner, not outside analyst.

## 2. Voice shift — ground claims in observable reality

Throughout the document, shift from assertion ("banks have no coherent model") to grounded observation ("across banking domains we work in, we consistently find..."). This is not about adding fake case studies — it is about shifting from third-person analysis to first-person conviction. Key locations:

- Line 5-9 (Core Problem opening)
- Line 39-41 (Organizational Reality opening)
- Line 96 (uneven adoption paragraph)
- Line 104-106 (Plumbing Problem opening)

Light touch — a framing sentence or two per section, not a rewrite. The content stays; the voice wraps it.

## 3. Broaden "Why This Matters Now"

Current section (lines 25-31) has three urgency drivers: AI, gradual transformation, governance. Add:

- **Competitive pressure**: Neobanks and fintechs are building from scratch without legacy plumbing — they can iterate at speeds incumbents cannot match
- **Customer expectations**: Customers compare their bank to their phone, their e-commerce app — coherence and speed are table stakes
- **Talent risk**: The engineers who understand the plumbing are a shrinking pool — retiring, leaving for tech companies, not being replaced. The IP becomes orphaned.
- **Failed transformation spend**: Banks have spent billions on digital transformation programs that addressed symptoms (new channels, cloud migration) without touching the structural problem. The budgets exist; the outcomes disappoint.

## 4. Add "existing spend" dimension

Add a brief subsection or paragraph — either in "Why This Matters Now" or as its own short section — establishing that banks are *already spending heavily* on coping with these problems. Systems integrator contracts, middleware licenses, transformation programs, headcount for plumbing maintenance. This is not theoretical demand — it is real, recurring, large-scale spend that is largely ineffective because it doesn't address the root structural problem. For Zeta's board, this signals: the budget exists and is being burned on approaches that don't work.

## 5. Elevate "failed approaches" into its own subsection

Currently buried at line 168 in the Modernization Trap section. For Zeta's board, this is a critical competitive positioning point: ESBs, iPaaS, cloud migrations, API gateways, and multi-year digital transformation programs have all been tried and have not solved the root problem. This means the market opportunity is still open. Move this to a more prominent position — either as the closing of the Modernization Trap section with its own subheading, or as a bridge between Modernization Trap and Compound Picture.

## 6. Trim channel fragmentation section

Lines 55-65 are the longest sustained block. For Zeta's board:

- **Keep**: The felt consequences — fragmented views within a domain, inconsistent information across channels, customers starting over at the branch
- **Trim**: The identity-bearing system / trust boundary / session management technical explanation (line 63). Reduce to one sentence: "Channels carry their own identity and session boundaries, so crossing channels means starting over."
- **Trim**: The channel team incentive paragraph (line 65) — condense to one sentence within the prior paragraph

## 7. Reframe Hub Way footnotes as strategic positioning

Current footnotes explain *what* Hub Way concepts are (Streams, Loops, Scenarios, Machines, Tools). For Zeta's board, they should explain *why this is a differentiated structural answer*. Rewrite each footnote to lead with the strategic claim, then briefly name the mechanism:

- **Line 33** (Why This Matters Now): Lead with "The Hub Way makes the work itself — not the process, not the system — the stable abstraction" then briefly mention Streams/Loops/Scenarios
- **Line 73** (Organizational Reality): Lead with "The Hub Way matches how banks actually operate — domain by domain, at each domain's own pace" then briefly mention Hubs, Channels, Channel Products
- **Line 100** (Systems Gap): Lead with "The Hub Way eliminates the core-vs-surround hierarchy" then briefly mention Machines/Tools
- **Line 120** (Plumbing Problem): Lead with "The Hub Way provides the shared domain vocabulary that replaces scattered translation logic" then briefly mention Tool contracts
- **Line 172** (Modernization Trap): Lead with "The Hub Way eliminates the combinatorial explosion at the architectural level" then briefly mention the star topology

Migration, Innovation, and Compensation footnotes (lines 130, 140, 150) are already crisp and well-framed — keep as-is.

## 8. Strengthen Compound Picture closing

Lines 185-187 currently end with a structural observation. Add 2-3 sentences that implicitly frame the market opportunity: this compound problem is universal (every bank), structural (not solvable by incremental fixes), worsening (AI wave, competitive pressure, regulatory demands), and currently unaddressed by existing vendor approaches. The implication — that solving this represents a large, durable, defensible opportunity — should be obvious without being stated.

## What stays unchanged

- The analytical structure (Core Problem → Unanswerable Questions → Urgency → Organizational Reality → Systems Gap → Plumbing → Costs → Modernization Trap → Compound Picture)
- The problem depth and compounding logic
- The systems gap table
- The three plumbing cost subsections (migration, innovation, compensation)
- The N(N-1)/2 combinatorial argument
- The plumbing-as-IP paradox

