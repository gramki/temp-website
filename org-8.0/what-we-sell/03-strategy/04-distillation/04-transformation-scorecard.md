# Chapter 04.04: The Domain Transformation Scorecard

*Prepared for strategic deliberation. June 2026.*

---

## 1. Purpose

The book's central commercial claim is measurable transformation: that a bank can know what fraction of a domain's work is AI-absorbed, prove that each domain costs less than the last, and answer the regulator at domain scale. The [CEO motion](03-ceo-gtm.md) reports these claims to boards; the [CEO narrative](../05-narrative-for-customer/02-ceo-narrative.md) promises a "denominator you can finally see"; the [thesis](../../02-the-thesis/05-thesis.md) argues that without domain-level visibility, executives can count AI projects but cannot measure AI transformation.

This chapter defines the instrument behind those claims. The **Domain Transformation Scorecard** is a standard artifact with three lives:

1. **Diagnostic output** — its first version is produced by the 6–8 week diagnostic, establishing the baseline.
2. **Delivery instrument** — every Engagement updates it; the program is steered by it.
3. **Board report** — a one-page quarterly projection becomes the recurring artifact through which the CEO narrates the program.

**What this document does not do:** specify the telemetry implementation in Evolution Fabric, or the per-domain work taxonomies (those are Hub Way modeling concerns — see [the enablement guide](../../02-the-thesis/07-the-hub-way/03-enablement/README.md)). It defines *what is measured, how it is normalized, and what discipline keeps it honest*.

---

## 2. The Five Panels

The scorecard has five panels. Each answers one executive question; together they make the thesis falsifiable.

| Panel | Executive question | Core measures |
|---|---|---|
| A. Visibility | "Do we actually know the work of this domain?" | Work units modeled; coverage confidence; discovery rate; estate induction coverage |
| B. Absorption | "Who resolves the work today — and which way is the dial moving?" | Resolution mix per work unit; absorption depth; dial movements this period |
| C. Outcomes | "What has changed in the business because the dial moved?" | Applications retired; capacity redeployed; cost per resolution; quality and cycle time |
| D. Compounding | "Is this getting cheaper, or are we accumulating projects?" | Cost and time per domain/Scenario vs. predecessor; reuse ratio; change lead time |
| E. Confidence | "Can we govern and defend what the agents are doing?" | Decision-record coverage; replay readiness; override and escalation rates; agent accountability coverage |

### Panel A — Visibility (the denominator)

The denominator is the domain's **work inventory**: the enumerated Streams (external commitments), Loops (internal disciplines), and their constituent Scenarios, as declared in the domain's Work Model. Measures:

- **Work units modeled** — count of Scenarios under declared Streams and Loops, weighted by resolution volume where volume data exists.
- **Coverage confidence** — the modeled inventory is always an estimate of the true work. Confidence is graded per Stream/Loop (declared-and-verified / declared / suspected-seam), so the denominator carries its own uncertainty rather than hiding it.
- **Discovery rate** — work units added per period through AI-assisted discovery of seam work (the [seventh principle](../../02-the-thesis/05-thesis.md#ai-is-a-partner-in-understanding-the-domain-not-just-operating-within-it)). A healthy domain discovers steadily early and asymptotically later; a flat zero from day one means nobody is looking.
- **Estate induction coverage** — the share of systems the domain's Work Model touches that are enrolled under Tool Contracts as registered Machines. An un-inducted system is a visibility gap: the work that depends on it cannot be governed, measured, or absorbed.

### Panel B — Absorption (the dial)

For each work unit, the **resolution mix** records who resolves it, on a five-position dial:

| Position | Definition |
|---|---|
| H | Human-resolved, unassisted |
| H+ | Human-resolved, AI-assisted (tooling, drafting, triage) |
| A/H | AI-resolved with human approval in the loop |
| A | AI-resolved under governance, human escalation path |
| M | Mechanically automated (deterministic, no judgment) |

The headline metric is **work absorption**: the volume-weighted share of the domain's modeled work at A/H, A, or M. The discipline that matters: **H+ is not absorption.** Tool-assist makes people faster; it does not change who resolves the work. Counting copilots as absorption is how banks convince themselves they are transforming when they are accelerating the status quo — the [Level 1 trap](../../02-the-thesis/04-enterprise-ai-adoption.md#level-1-ai-as-a-tool). Report H+ separately as assist coverage.

**Dial movements this period** — which work units moved position, in which direction (movements back toward H are reported, not buried; a reversible dial is the design, per the [third principle](../../02-the-thesis/05-thesis.md#the-model-must-survive-when-the-who-changes)).

### Panel C — Outcomes

Absorption is the mechanism; these are the results a CFO will audit:

- **Applications retired** (and pending retirement with target dates) — the single most credible transformation metric, because it is binary and verifiable.
- **Capacity redeployed** — FTE-equivalents released from coordination, handoff, and exception work, and where they went.
- **Cost per resolution** — by work unit class, trended; includes the AI run cost (model, infrastructure, governance overhead), not just the labor saved. Net, not gross.
- **Quality and speed** — error/rework rates, cycle time, and (for customer-facing domains) resolution rate and CSAT, against the pre-absorption baseline.

### Panel D — Compounding

The claim that distinguishes the model from a project portfolio, instrumented:

- **Nth-domain delta** — cost and elapsed time of the current domain (or Scenario family) deployment versus its predecessor, like-for-like scoped. The [CEO motion](03-ceo-gtm.md#deal-shape) commits this number to the board at Horizon 2.
- **Reuse ratio** — share of the deployment built from existing model elements, Tool Contracts, and governance structures versus net-new.
- **Change lead time** — elapsed time for a representative change (new product variant, new regulation mapped, new agent admitted) trended across the program. This is the [fifth CEO question](03-ceo-gtm.md#3-the-ceo-question-bank) made measurable.

### Panel E — Confidence

What the CRO, the CCO, and the examiner read:

- **Decision-record coverage** — share of AI-resolved work units whose decisions produce complete Memory Fabric records (decision, evidence, authority, outcome).
- **Replay readiness** — share of recorded decisions that can be replayed/explained on demand; time-to-answer for an examiner query.
- **Override and escalation rates** — by work unit; spikes are an early-warning signal that a dial moved too far, and feed the dial-back decisions in Panel B.
- **Agent accountability coverage** — share of active agents with verified identity, declared authority derivation, and a named accountable human (Trust Fabric + Agent Fabric), including — as counterparty channels open — *external* agents operating under delegation.

---

## 3. Honesty Rules

A scorecard that flatters is worse than no scorecard: it converts the book's strongest claim into a credibility liability. Five rules are non-negotiable:

1. **The denominator is allowed to grow.** Discovery of seam work increases the work inventory and can *reduce* the absorption percentage from one quarter to the next. This is the instrument working, not failing. Always report the pair (absorption %, denominator size), never the percentage alone.
2. **Assist is not absorption.** H+ is reported as its own line and never blended into the headline.
3. **Net cost, not gross savings.** AI run cost, governance overhead, and platform amortization are inside the cost-per-resolution number.
4. **Verified or marked.** Every Panel C outcome is either verified (system-of-record evidence) or explicitly marked `[claimed]`. Board projections carry only verified numbers.
5. **Reversals are reported.** Dial-backs, overrides, and retired-then-reinstated applications appear in the period they occur.

---

## 4. Cadence and Audiences

| Audience | Cadence | Form |
|---|---|---|
| Domain team (Hub owner, squads) | Weekly | Full scorecard, work-unit granularity |
| Executive sponsor coalition | Monthly | Five panels, exceptions and dial decisions highlighted |
| Board | Quarterly | One page: absorption trend with denominator, outcomes verified this quarter, Nth-domain delta, confidence summary |

The baseline scorecard is produced at diagnostic close — Panels A and B fully, Panel C as baseline values, Panels D and E as empty frames with targets. This is deliberate: the bank sees, before committing to Horizon 1, exactly the instrument it will be governed by.

---

## 5. Instrumentation Notes

- **Sources.** Panel A/B derive from the domain Work Model and Hub runtime telemetry (Evolution Fabric); Panel E from Memory Fabric decision records and Trust/Agent Fabric registries; Panel C partly from bank systems of record (HR, application inventory, cost accounting) — which means parts of Panel C are *manually attested in early deployments*. Mark them as such rather than approximating from platform data.
- **Early-deployment reality.** A first domain produces an honest Panel A/B and a thin Panel D (no predecessor). Resist back-filling Panel D with estimates; its first real value arrives with the second domain — which is precisely the Horizon 2 commercial moment.
- **Productization.** The scorecard template, the work-unit weighting method, and the board one-pager format should be standard deliverables of the diagnostic — part of [what must be true](03-ceo-gtm.md#6-what-must-be-true) for the CEO motion to scale.

---

## 6. Open Items

1. **Volume weighting standard.** Weighting work units by resolution volume is right for servicing-class domains, wrong for low-volume/high-stakes domains (e.g., regulatory reporting). A per-domain-class weighting convention is needed from the first two deployments' experience.
2. **Cross-bank comparability.** Once multiple banks run scorecards, anonymized absorption and compounding benchmarks become a strategic asset ("operational intelligence as an asset class"). Whether and how to build that benchmark is a leadership decision with confidentiality implications — logged in the [decision log](05-decisions.md).
3. **Exposure panel.** A sixth panel measuring agentic-era exposure (share of deposits/products held by agent-assisted customers, agent-readiness of the product catalog) is plausible once counterparty channels exist. Deferred until Storyline A deployments produce the data.

---

*Source documents: [the thesis](../../02-the-thesis/05-thesis.md), [enterprise AI adoption](../../02-the-thesis/04-enterprise-ai-adoption.md), [The Hub Way](../../02-the-thesis/07-the-hub-way/README.md), [the CEO motion](03-ceo-gtm.md).*
