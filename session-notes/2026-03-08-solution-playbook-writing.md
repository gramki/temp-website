# Session Notes: Enterprise Solutions Playbook — Writing

**Date:** 2026-03-08 (Phase 2 of multi-phase conversation)  
**Focus:** Implementing the full mini-book — all 12 chapters, prologue, epilogue, README, and bridging document  
**Chat reference:** [Solution story & Zeta analysis](82616faf-d44a-4bc2-8ca3-43f7c401226b)

## Summary

Implemented the entire Enterprise Solutions Playbook as planned. Wrote the prologue directly to set tone and voice, then used parallel subagents to write chapters in batches. All files created under `org-8.0/what-we-sell/solution-story/`.

## Execution Approach

1. **Prologue written directly** — to establish the voice, tone, and four-archetype contrast pattern that all subsequent chapters would follow
2. **Deep chapters in parallel batches of 3**:
   - Batch 1: Ch 2 (Opportunity Discovery), Ch 6 (Buying Dynamics), Ch 9 (Economics)
   - Batch 2: Ch 8 (Delivery Models), Ch 7 (Deal Shaping), Ch 11 (Platformization)
3. **Concise chapters in parallel batches of 2**:
   - Ch 1 (Problem Archetypes), Ch 3 (Opportunity Sizing)
   - Ch 4 (Value Pools), Ch 5 (Solutions Archetypes)
   - Ch 10 (Scaling), Ch 12 (Strategic Positioning)
4. **Epilogue written directly** — closing message about archetypes as lenses, not labels
5. **README and bridging document** — table of contents, reading guide, companies referenced table, and initial Zeta bridging thoughts

## Files Created (16 files)

| File | Type | Content |
|---|---|---|
| `README.md` | Overview | Table of contents, reading guide, companies referenced |
| `00-prologue.md` | Prologue | The Playbook Confusion — four archetypes, cost of misapplication |
| `01-problem-archetypes.md` | Concise | Types of enterprise problems that support solutions businesses |
| `02-opportunity-discovery.md` | Deep | Pattern recognition, diagnostic discovery, transformation triggers; Palantir, Veeva, ServiceNow case studies |
| `03-opportunity-sizing.md` | Concise | How to size enterprise solutions markets |
| `04-enterprise-value-pools.md` | Concise | Four major enterprise value pools |
| `05-solutions-business-archetypes.md` | Concise | Five archetypes within the solutions category |
| `06-enterprise-buying-dynamics.md` | Deep | Buying committees, three conversations, political dynamics |
| `07-deal-shaping.md` | Deep | Value framing, ROI narratives, POC strategies, pricing |
| `08-delivery-models.md` | Deep | Five delivery models, engagement engineering pattern |
| `09-economics.md` | Deep | Solutions economics vs SaaS metrics |
| `10-scaling.md` | Concise | Reference-customer-driven growth, land-and-expand |
| `11-platformization.md` | Deep | Four phases, premature/reluctant platformization traps |
| `12-strategic-positioning.md` | Concise | Four identity end-states and their implications |
| `13-epilogue.md` | Epilogue | Beyond archetypes — evolution, context, creating your own |
| `bridging-to-zeta-reality.md` | Bridge | Framework-to-Zeta observations (6 chapters mapped) |

## Bridging Document Observations

The bridging doc (`bridging-to-zeta-reality.md`) captured initial observations by reading Zeta's internal strategy documents:

- `problems.md` → textbook compound problem discovery (systems gap + plumbing + modernization trap)
- `business-model.md` → three-persona buyer analysis maps to the book's "three conversations"
- Business model narrative → Exploration investment ($100K–$1M) is a structured POC model
- Engagement Engineering → strong instantiation of the book's structured delivery methodology
- Hub Way framework → solutions thinking expressed as architecture (models work, not features)
- Prologue anti-patterns → several confirmed by user (PMs defining features, GTM running funnels, pricing as tiers)

## Stylistic Conventions Established

- Bold **Key Questions** at chapter opening
- Four-column contrast tables as recurring device
- Named case studies with public references
- "The Mistake" / "The Correction" teaching pattern
- Explicit callouts in concise chapters explaining why they are kept brief
