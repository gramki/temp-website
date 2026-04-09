# DR-006: "Signal" as Collective Term for Problem, Need, Opportunity

**Status:** Accepted
**Date:** 2026-02-15
**Related FAQ:** Q16

---

## Context

The UPIM Dimension 1 (Strategy) classifies inputs into three types: Problem, Need, and Opportunity. A collective term was needed to refer to all three. Two established candidates were considered:

1. **"Intake item"** — the term used in early model iterations.
2. **"Backlog item"** — the term common in Agile/Scrum.

Both were found to carry problematic connotations that would undermine the discovery-first mindset the UPIM is designed to enforce.

### The Problem with "Intake Item"

In practice, "intake" carries an implicit obligation to process and deliver. When a customer submits something through an "intake" process, organizations reflexively treat it as a **requirement** that *should* be completed. This conditioning suppresses the discovery, decision-making, and prioritization process that the UPIM explicitly mandates through its Idea → PDR → PSD chain.

Observed organizational behaviors with "intake item" terminology:
- Customer intake is treated as a customer requirement, not a hint or symptom
- The complete discovery and validation process is bypassed or compressed
- Product teams feel guilty about unprocessed intake items, creating urgency that undermines prioritization
- Internal stakeholders frame their inputs as requests that "should" be fulfilled

### The Problem with "Backlog Item"

- In Scrum, "Product Backlog Item" (PBI) refers to User Stories, Bugs, and Spikes — Build Track entities in our model. Using "backlog item" for Problems/Needs/Opportunities conflates two very different levels separated by several layers (Signal → Idea → PDR → PSD → Epic → Story).
- "Backlog" implies the item is already in a prioritized queue awaiting work. Many of these entities will sit unassociated and unranked indefinitely — they are not "in the backlog."
- "Backlog" carries negative connotations — the ever-growing, never-shrinking list that teams feel guilty about.

## Decision

Use **"Signal"** as the collective term for Problem, Need, and Opportunity.

**Definition:** *A Signal is an observation or indicator — from any source, internal or external — that something about the product warrants attention. A Signal is explicitly not a requirement, a commitment, or an obligation. It is an input to be interpreted and investigated through the Discovery Track. Multiple Signals may point to the same underlying issue; a single Signal may be noise.*

## Rationale

### 1. Fosters an investigation mindset, not a fulfillment mindset

The word "Signal" naturally invites the question "what does this signal mean?" rather than "when will this be done?" This is precisely the relationship the UPIM intends between {Problem, Need, Opportunity} and the Discovery Track.

| Property | Signal | Intake Item | Backlog Item |
|---|---|---|---|
| Implies obligation? | **No** | Yes | Yes |
| Invites investigation? | **Yes** | Weakly | Weakly |
| Allows dismissal as noise? | **Naturally** | Awkwardly | Awkwardly |
| Multiple items → one insight? | **Yes** | Not implied | Not implied |
| Strength varies? | **Yes** | Not implied | Not implied |

### 2. Source-agnostic — includes all contributors

Signals come from both external and internal sources:

**External sources:**
- Customers reporting friction with existing product (Problem)
- Prospects requesting missing capabilities (Need)
- Market analysis revealing competitive gaps (Opportunity)

**Internal sources:**
- SREs identifying scaling bottlenecks (Problem)
- Support teams surfacing recurring customer requests (Need)
- Engineering identifying technical debt or cost optimization (Opportunity)
- Operations teams identifying process inefficiencies (Opportunity)
- Strategy teams identifying market expansion potential (Opportunity)

Terms like "market signal" were explicitly rejected because they would alienate internal stakeholders (SREs, engineers, operations teams) whose product knowledge is essential — especially for SaaS products where internal teams interact with the product daily. Bare "Signal" is inclusive of all sources without prefix bias.

### 3. No terminology collision within the UPIM

Within Dimension 1 (Strategy), "Signal" is unambiguous — it means {Problem | Need | Opportunity}. Infrastructure monitoring signals, analytics signals, and system events are not entities in Dimension 1, so there is no collision within the model context.

### 4. Natural language properties

- **Aggregates naturally:** "We received 23 new signals this quarter"
- **Classifies naturally:** "15 problem signals, 5 need signals, 3 opportunity signals"
- **Pairs with verbs of investigation, not fulfillment:** "investigate a signal," "interpret a signal," "act on a signal" — vs. "complete an intake item," "deliver a backlog item"
- **Strength is inherent:** signals can be strong, weak, recurring, isolated, corroborated, or contradictory

### 5. Examples across Signal types and sources

| Signal Type | Source | Example | What it is NOT |
|---|---|---|---|
| Problem | Customer (external) | "FX rate-lock confirmation takes 6 clicks" | Not a requirement to reduce clicks |
| Problem | SRE (internal) | "Payment DB connection pool exhausted under peak load" | Not a commitment to fix it now |
| Need | Enterprise prospect (external) | "We require batch payout file upload (CSV/SFTP)" | Not a promise to build it |
| Need | Support team (internal) | "Customers keep asking for multi-currency reporting" | Not an automatic feature request |
| Opportunity | Strategy team (internal) | "LATAM currencies could capture $2M ARR" | Not an approved initiative |
| Opportunity | Engineering (internal) | "Consolidating payment adapters could save 40% infra cost" | Not a committed project |

## Alternatives Considered

| Term | Why Rejected |
|---|---|
| **Intake item** | Implies obligation to process and deliver; suppresses discovery mindset |
| **Backlog item** | Conflates with Scrum PBIs; implies prioritized queue; carries guilt connotation |
| **Market signal** | Excludes internal sources (SREs, engineers, operations); alienates crucial contributors |
| **Product signal** | Potential collision with product analytics terminology ("product signals show users drop off at step 3") |
| **Strategy signal** | Feels too formal for individual customer complaints or engineer observations |
| **Discovery signal** | Confuses the signal itself (which exists before discovery) with the discovery process |
| **Demand signal** | Too narrow — Problems are friction reports, not demand; Opportunities from engineering (cost optimization) are not "demand" |

## Consequences

- **Positive:** Terminology actively reinforces the discovery-first mindset. Teams are conditioned to *investigate* Signals, not *fulfill* them.
- **Positive:** All stakeholders (external customers, internal SREs, engineers, support, strategy) are equally valid Signal sources with zero terminology bias.
- **Positive:** Natural language properties (aggregation, strength, investigation verbs) align with how product teams should think about inputs.
- **Positive:** No collision within the UPIM; context (Dimension 1) provides disambiguation from other uses of "signal."
- **Negative:** "Signal" is unconventional in product management vocabulary. Teams accustomed to "requirements," "backlog items," or "feature requests" will need onboarding.
- **Negative:** External stakeholders (customers submitting feedback) won't use the term "Signal" — they'll say "I have a request" or "here's a problem." The terminology is internal to the product organization.
- **Mitigation:** The three concrete types (Problem, Need, Opportunity) are self-explanatory. "Signal" is the internal classification umbrella, not customer-facing language.
