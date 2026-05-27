---
name: Problems doc restructure opening
overview: Restructure problems.md to open with concrete, felt problems that bank executives recognize immediately, then layer in the structural causes (procurement patterns, integration burden, organizational reality), then the compounding dynamics and what forces action.
todos:
  - id: felt-problems
    content: "Write Section 1: The Problems Banks Live With — concrete, felt problems bank executives recognize"
    status: completed
  - id: procurement
    content: "Write Section 2: How Banks Buy Technology — capability-first, best-of-breed, cost-efficiency trap"
    status: completed
  - id: integration-burden
    content: "Rework Section 3: What Integration Actually Costs — data, timing, errors, state, security, ops support"
    status: completed
  - id: restructure-remainder
    content: Restructure remaining sections (Org Reality, Systems Gap, Modernization Trap with cost-efficiency cycle, What Has Been Tried, What Forces Action, Compound Picture) and update Hub Way footnotes
    status: completed
isProject: false
---

# Restructure problems.md — Lead with Felt Problems

Target file: [problems.md](org-8.0/what-we-sell/problems.md)

The current opening starts with our diagnosis ("banks have no coherent model for this work") and asks questions that presuppose our framework. The new opening starts with problems bank executives already live with — then builds toward the structural explanation.

## New document flow

### Title and framing (keep, with scope qualifier)

Keep the Zeta-voice opening paragraph and title "Why Banks Cannot Evolve." Add a scope qualifier in the opening: this document describes problems of mid-size and large banks operating at scale across multiple domains with multi-vendor technology estates. Community banks and smaller credit unions may face simpler versions. State once, then use "banks" unqualified throughout.

### Section 1: The Problems Banks Live With (NEW — replaces Core Problem + What Banks Cannot Answer)

Lead with the concrete, felt problems every bank executive recognizes. No framework vocabulary. No diagnosis yet. Just the reality:

- Technology spend keeps growing but operational efficiency doesn't improve
- Every change takes too long — business moves at market speed, technology at plumbing speed
- Regulatory compliance is disproportionately expensive — every mandate triggers a program because information is scattered
- Vendor changes are existential programs — multi-year, nine-figure efforts to replace a system the bank depends on
- Customer experience is fragmented and nobody can fix it — each fix is a new layer on top of disconnected backends
- When something goes wrong, nobody can trace what happened — symptom to root cause crosses multiple systems and teams
- The best engineers are consumed by maintenance — keeping existing integrations running, not building new capability
- M&A integration takes 3-5 years — two sets of everything, rationalization takes longer than projected

These should be stated plainly, 2-3 sentences each. The reader should recognize their own bank.

### Section 2: How Banks Buy Technology (NEW — replaces some Plumbing Problem content)

The procurement pattern that structurally feeds the problem:

- **Capability-first, integration-later**: Banks buy capabilities as discrete decisions (RFP, evaluation, contract). Integration is a downstream cost, underestimated, handled by a different team, procured by man-hour cost.
- **Best of breed = least specific to banking**: For horizontal concerns (engagement, identity, intelligence, etc.), "best of breed" means the most widely used vendor across industries — Salesforce, Pega, Adobe, Okta. Excellent products. Not modeled for banking. Every one requires a custom translation layer.
- **Cost efficiency = least change = more plumbing**: The buying process measures man-hour cost, not structural quality. No real metric for "was this built well." The rational choice for every project: do the minimum, patch rather than restructure, add glue rather than rethink. Locally rational, globally destructive.

### Section 3: What Integration Actually Costs (REWORKED — replaces semantic translation burden and parts of Plumbing Problem)

What makes integration so expensive and permanent — the real burden, not the theoretical one:

- **Data is never ready**: The new system needs data in a shape source systems don't provide. Assembling the right data, right shape, right time, right freshness — bulk of the integration work.
- **Timing and sequencing**: Systems run on different clocks — batch overnight, real-time, on-demand, hourly ingestion. Orchestrating across different speeds and consistency guarantees.
- **Error handling and compensation**: Happy path is 20% of the effort. The other 80%: what if a system is down, a batch fails halfway, two systems disagree on state? Every failure mode requires compensating logic.
- **State management across systems**: A business operation touches five systems over three days. Each has its own state. Nobody owns the overall state. Cross-system state tracking is the most fragile part.
- **Security and identity multiplied**: Every system has its own auth, access, token management, certificates. Silent failures (an expired certificate) can bring down a business process.
- **Operational support is permanent**: Monitoring, alerting, log correlation, runbooks, on-call — for every integration. Fifty integrations = fifty operational surfaces.

All of it bespoke. Nothing reusable. Every pair of systems has different characteristics.

The plumbing-as-IP paradox stays here: this bespoke integration layer is the bank's most valuable and most vulnerable technology.

### Section 4: The Organizational Reality (KEEP — lightly edited)

Keep the domain fragmentation, uneven gap profiles, customer seams, channel fragmentation (trimmed), uniqueness content. This section multiplies the integration problem across the bank's structure.

### Section 5: The Systems Gap (KEEP)

Keep the lopsided architecture table and core-vs-surround framing. This explains *what* is missing.

### Section 6: The Modernization Trap (KEEP — with cost-efficiency cycle integrated)

Keep the combinatorial growth and decelerating modernization curve. Integrate the cost-efficiency vicious cycle:

- High cost of change -> pressure to minimize each change
- Minimizing each change -> more plumbing
- More plumbing -> higher cost of next change
- Repeat

### Section 7: What Has Been Tried (KEEP)

ESBs, API gateways, cloud migrations, transformation programs. None addressed the root cause.

### Section 8: What Forces Banks to Act (KEEP)

Real triggers: regulatory, M&A, leadership, cost pressure, vendor EOL, major incidents. Episodic, not seasonal. Brief AI paragraph pointing to companion doc.

### Section 9: The Compound Picture (KEEP — updated)

All threads tied together. Universal, structural, worsening, unaddressed.

### Hub Way footnotes

Brief footnote on each major section. Strategic positioning, not product-spec. Keep existing footnotes on migration/innovation/compensation costs (already crisp). Rewrite others to lead with executive-language outcomes.

## What is removed

- **"The Core Problem" section** (lines 5-11): The "no coherent model" framing is our diagnosis, not their problem. It should emerge from the structural explanation, not lead the document.
- **"What Banks Cannot Answer Today" section** (lines 13-23): These questions presuppose the framework. They may appear later as implications, not as the opening.
- **The semantic translation burden as the primary framing**: Remains as one of several integration challenges, not the dominant narrative. Data, timing, error handling, state management, and security are equally or more important.

