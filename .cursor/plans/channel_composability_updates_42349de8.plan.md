---
name: Channel composability updates
overview: Weave the Channel composability principle and the domain-scoped vs organization-scoped persona distinction into the enablement doc (05-modeling-channels.md), the business narrative (narrative.md), and the framework reference (README.md).
todos:
  - id: update-05-channels
    content: "Update enablement/05-modeling-channels.md: composability in section 1, persona scope + recomposition in section 7, extend anti-pattern and heuristics"
    status: completed
  - id: update-narrative
    content: Update narrative.md Channels section with composability and persona scope in business prose
    status: pending
  - id: update-readme-channel
    content: Update README.md Channel section with brief composability and persona scope additions
    status: completed
isProject: false
---

# Channel Composability Updates

Two new principles need to be woven into the HSLC documentation:

1. **Channels are composable**: A Channel is a collection of composable, interaction-paradigm-specific and technology-specific components — not a monolithic system. Because Channels are composed from components, they can be recomposed.
2. **Persona scope differs between Channel and Channel Product**: Both are persona-optimized. A Hub Channel serves a domain-scoped persona (customer-as-payer, agent-as-dispute-investigator). A Channel Product serves an organization-scoped persona (customer-as-banking-relationship-holder). Same components, different composition logic, different persona scope.

---

## Files to Update

### 1. [enablement/05-modeling-channels.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/05-modeling-channels.md)

**Section 1** — Add composability principle after the existing "comprehensive system" framing. Current section establishes "not a UI, it's a system." New content extends: "not a monolithic system either — it's a collection of composable components." Include:

- Components are interaction-paradigm-specific and technology-specific (task presentation renders as cards on a desk, notifications in Teams, webhooks on REST, tool listings on MCP)
- Same underlying capability, paradigm-native component
- Because Channels are composed from components, they can be recomposed — this is what enables Channel Products

**Section 7 (Channel vs Channel Product)** — Strengthen with two additions:

- **Composability in action**: A Hub composes components for its domain context. A Channel Product recomposes components from multiple Hubs for the persona's organizational context. Not just API aggregation — genuine recomposition for least friction and maximum delight.
- **Persona scope distinction**: Both Hub Channels and Channel Products are persona-optimized. The difference is persona scope:
  - Hub Channel: domain-scoped persona (customer-as-payer, agent-as-dispute-investigator)
  - Channel Product: organization-scoped persona (customer-as-banking-relationship-holder, agent-as-unified-operations-staff)
  - The persona model itself may differ — a Hub defines domain-scoped personas; a Channel Product may define organizational personas that don't map one-to-one to any single Hub's personas
  - Neutrino's job includes bridging this persona scope gap
- Update the comparison table to add a **Persona scope** row and a **Composition** row that reflects composability (currently says "Atomic" for Channel — should reflect "Composed from paradigm-specific components" vs "Recomposed from multiple Hub Channels' components")

**Section 8 (Anti-patterns)** — Extend the Monolith Channel anti-pattern to include: a Channel built as a single indivisible system that cannot be recomposed is also a Monolith Channel.

**Section 9 (Heuristics)** — Add heuristic: "Design Channel components for reuse; a Channel Product may compose them differently than the Hub does."

**Summary** — Update to mention composability and persona scope.

### 2. [narrative.md](org-8.0/what-we-sell/hubs-streams-loops-channels/narrative.md)

**Channels section** (lines 53-65) — Weave in two ideas in narrative prose, maintaining the business-audience tone:

- Channels are built from composable components, not as monolithic systems. This means the same capabilities can be presented differently depending on context.
- The Channel Product paragraph (line 65) should include the persona scope insight: a Hub sees the customer through its domain lens; the Channel Product sees the customer in their full banking relationship. The recomposition optimizes for the persona's holistic experience, not just aggregation.

### 3. [README.md](org-8.0/what-we-sell/hubs-streams-loops-channels/README.md)

**Channel section** (lines 49-63) — Add one sentence on composability after "A Channel is not a UI." Brief and definitional — this is the reference doc, not the enablement guide.

- The Channel vs Channel Product paragraph (line 63) should add the persona scope distinction in one sentence: "A Channel optimizes for a domain-scoped persona; a Channel Product optimizes for an organization-scoped persona."

---

## Style Consistency Notes

- **05-modeling-channels.md**: Uses tables, structured sections with `##` headings, banking examples. New content should follow the same pattern — tables for comparisons, prose for principles, examples grounded in banking.
- **narrative.md**: Readable prose, no tables, no implementation details, banking examples woven into sentences. New content must be narrative, not technical.
- **README.md**: Concise definitions, bullet lists, brief. One or two sentences per concept. New content should be minimal and definitional.

