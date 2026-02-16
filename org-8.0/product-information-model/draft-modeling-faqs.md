# UPIM Modeling FAQs

Design decisions and rationale captured during model refinement.

---

### Q1: Why is the Bridge tier placed after the Technical tier, not before it?

The Bridge (Dimensions 8–9: Structural Topology and Data & Information) provides the taxonomy and ontology that **connects** Strategy, Business, and Technical entities. Placing it after all three tiers allows the reader to first understand what each tier defines independently, and then see how the Bridge unifies them. The Bridge doesn't sit "between" two tiers — it spans all three.

---

### Q2: Should Definition Model entities (like Idea) appear in the Work Model?

**No.** The Definition Model describes *what the product is* (static structure). The Work Model describes *what people do* (motion/process). Entities like Problem, Need, Opportunity, Idea, and PSD belong in Dimension 1 (Strategy). The Work Model's track entities are work items — Research Tasks, Experiments, etc. — that teams create and manage to *mutate* those definition entities. Including definition entities in the Work Model blurs this boundary.

---

### Q3: What enters the Discovery Track — a Signal or an Idea?

**Both, at different stages.** The Discovery Track has two distinct phases of work, each with its own entity types:

1. **Signal Exploration** (input: Signal → output: Ideas) — **Signal Exploration Tasks** and **Deliberations** (brainstorms) are performed to deeply understand the Signal, identify root causes and adjacent patterns, and synthesize candidate solution hypotheses (Ideas).
2. **Idea Validation** (input: Idea → output: Validated Idea or Kill) — **Research Tasks**, **Experiments**, **Prototypes/Spikes**, and **Deliberations** (evaluative councils) test whether a specific hypothesis holds up. A Deliberation may also directly produce a PDR without prior empirical validation, when an authorized group exercises collective judgment.

The act of arriving at Ideas for a given Signal is real, trackable work. Framing the track as only accepting Ideas would leave the upstream exploration work unrepresented. Similarly, not all validation is empirical — authorized group deliberation is a legitimate decision path (see FAQ Q21).

---

### Q4: Is a PSD a Work Model entity or a Definition Model entity?

**Definition Model (Dimension 1).** A PSD describes *what the product will be* — it is a specification, not a unit of work. The Discovery Track *produces* PSDs through its work entities (Research Tasks, Experiments, Specification Tasks), but the PSD itself lives in the Strategy Dimension as the formal contract between Product and Engineering.

---

### Q5: Should Idea validation implicitly lead to a PSD?

**No.** A validated Idea confirms the bet is worth taking, but translating it into PSDs is substantial, separate work — scoping modules, defining acceptance criteria, coordinating with engineering, decomposing into shippable increments. Furthermore, a single validated Idea may fan out into **multiple PSDs** covering different modules.

The refined chain in Dimension 1 is: **Idea → validated by → PDR → justifies → PSD(s).** The Product Decision Record (PDR) captures the evidence and reasoning, and PSDs reference it as their formal justification. The Discovery Track includes a **Specification Task** entity to represent the PSD-authoring work explicitly.

---

### Q6: Why add a Product Decision Record (PDR) to the Definition Model?

The PDR fills a traceability gap. Without it, Dimension 1 has {Problem | Need | Opportunity} → Idea → PSD, but no artifact formally records *why* a decision was made or *what evidence* supports it. The Idea says "we bet on X." The PSD says "build X this way." Neither captures the reasoning in between.

The PDR is a **Definition Model entity** (not a Work Model entity) because it documents a persistent, referenceable product decision — not a workflow transition. It differs from the earlier-rejected Discovery Decision Record (DDR), which was a process artifact governing go/no-go workflow. The PDR is a knowledge artifact: "here is the reasoning, evidence, and trade-offs behind a product decision."

Key design choices:
- **Captures any significant decision** — Go, Kill, and Pivot alike. A "Kill" PDR is just as valuable for institutional memory as a "Go" PDR.
- **References Work Model artifacts** (Research Tasks, Experiments, Prototypes) — creating cross-model traceability from evidence to decision.
- **Referenced by PSD(s)** — one PDR can justify multiple PSDs across different modules.
- **The revised Dimension 1 chain:** {Problem | Need | Opportunity} → spawns → Idea(s) → validated by → PDR → justifies → PSD(s).

---

### Q7: Why split "Problem" into Problem, Need, and Opportunity?

The single "Problem" entity was too narrow and conditioning. Not everything entering discovery originates from a problem — the word itself constrains what Product Managers and other stakeholders can capture. The three-way classification provides distinct Signal types with different origins, natures, and beneficiary lenses:

- **Problem:** Limitations, gaps, or challenges in the *existing* product (not functional Bugs). Specified at Module/Capability/Feature granularity. Reported by internal or external stakeholders. Upvotable.
- **Need:** A missing Capability or Feature expressed by customers or prospects. Always external in origin. Always about *expanding* the product. Traceable to requesting customers. Upvotable.
- **Opportunity:** An initiative to increase revenue, reduce cost, or expand market segments. Always internal in origin. The beneficiary is always the vendor.

Each type aligns naturally with a different tier of the Definition Model:
- Problem → Technical + Bridge tiers (existing product structure at M/C/F)
- Need → User-Centric tier (customer/user demand)
- Opportunity → Business tier (vendor economics)

All three converge into Ideas, and from there the downstream flow is identical. The classification matters for traceability, prioritization (upvotes, business impact), and routing (who investigates?).

Feedback from the Win Track maps to a **Problem** or a **Need** — never directly to an Opportunity (though Feedback patterns may *inspire* an Opportunity created by an internal stakeholder).

---

### Q8: Why use "Product Specification Document" (PSD) instead of "Product Requirements Document" (PRD)?

The UPIM deliberately uses **Specification** over **Requirements** because each term maps to a distinct phase of the Dimension 1 chain, and conflating them loses precision:

1. **Signals are captured upstream.** The Signal layer (Problem, Need, Opportunity) already captures *what warrants attention* — the observations, gaps, and strategic indicators. By the time the PSD is written, the Signal investigation phase is over.
2. **Decisions are captured midstream.** The Product Decision Record (PDR) captures *what we're committing to and why* — the evidence and trade-offs. This is also not the PSD's job.
3. **Specifications are what remains.** The PSD's job is to precisely *specify what to build and how it should behave* — scope boundaries, acceptance criteria, module decomposition, behavioral contracts. This is specification work, not requirements work.

The terminology creates a clean separation of concerns across the chain:

| Phase | Entity | What it captures |
|---|---|---|
| Signal | Problem / Need / Opportunity | What warrants attention (observation) |
| Decision | PDR | What we're committing to and why (evidence + rationale) |
| Specification | PSD | Precisely what to build and how it should behave (contract) |

Additionally, **naming consistency**: the Work Model already has **Specification Task** as the work entity that produces PSDs. The PSD + Specification Task pairing is self-documenting.

The trade-off is that "PRD" is deeply entrenched industry vocabulary. However, since the UPIM defines its own precise ontology, clarity within the model takes priority over convention.

---

### Q9: Why is a PSD scoped to a single module?

A PSD is a cross-dimensional impact assessment anchored to a structural change (Dimension 8). Because each module has its own **archetype** (Human-Interactive, Programmatic-Interactive, or Reactive/Background), its own engineering team, and its own dimensional impact profile, scoping a PSD to a single module keeps the specification focused and actionable.

When a validated Idea (via PDR) affects multiple modules substantially, each module gets its own PSD. These sibling PSDs reference each other for cross-module coordination. The threshold for "needs its own PSD" is: does the module change require its own acceptance criteria and Epic decomposition? If yes, it warrants a standalone PSD. Minor ripple effects on adjacent modules may be documented as cross-module dependencies within the primary PSD.

PSD templates are provided per module archetype because the **primary specification surface** differs by archetype:
- **Human-Interactive:** UX (Dim 4) is the deep section
- **Programmatic-Interactive:** Extensibility (Dim 6) and Technical (Dim 5) are the deep sections
- **Reactive/Background:** Technical (Dim 5), Operational (Dim 7), and Data (Dim 9) are the deep sections

Every PSD must acknowledge all 9 dimensions, but the depth varies — ensuring thoroughness where it matters most without forcing boilerplate where it doesn't.

---

### Q10: Why rename "Views" to "Dimensions"?

"Dimensions" better conveys that each aspect of the product is an independent axis of description that can be analyzed on its own, while also being part of a multi-dimensional whole. "Views" can imply passive observation; "Dimensions" implies structural facets of the product's identity.

---

### Q11: Why add Objectives and Initiatives to the Strategy Dimension, and why does each track own its own planning work?

Without strategic entities, every Signal (Problem, Need, Opportunity) is an equal candidate for discovery at every point in time. This is impractical — organizations need to prioritize discovery work based on strategic direction.

**Objectives** answer "where are we going?" — they are strategic goals set by leadership for a planning horizon. **Initiatives** are the programs that advance Objectives — they serve as the prioritization vehicle that associates Signals for coordinated discovery and delivery. Signals may exist independently before being associated with an Initiative during a planning cycle.

Rather than creating a separate "Plan Track" (which would centralize planning unnaturally), each track owns its own planning activities:

| Track | Planning Work | Definition Model Output |
|---|---|---|
| Discovery | Objective Setting, Initiative Scoping, Prioritization | Objectives, Initiatives (Dim 1) |
| Build | Release Planning, Milestone Planning, Iteration Planning | Customer Release scope, Milestones |
| Run | Deployment Planning, Capacity Planning | Deployment plans, infrastructure readiness |
| Win | Go-to-Market Planning, Customer Rollout Planning | Launch plans, rollout schedules |

This distributed approach keeps planning close to the teams that execute, while strategic entities in Dimension 1 provide the top-down filter that connects business strategy to tactical work.

---

### Q12: Why use "Customer Release" instead of "Release," and why does it use names instead of version numbers?

The word "release" is deeply overloaded. In the DevOps ecosystem, "release" universally means a versioned build artifact that has passed quality gates — GitHub Releases, GitLab Releases, Helm releases, release pipelines, release branches, release tags. This usage is too entrenched to fight.

SAFe and the Continuous Delivery community explicitly **decouple "release" from "deployment":**
- **Deployment** = installing a software version on an environment (technical act)
- **Release** = making software available to users (business act)

The UPIM follows this convention but uses **"Customer Release"** to make the distinction unambiguous:
- **"Customer Release"** = the business act of making capabilities available to customers (Definition Model, Dim 1)
- **"Module Version with status Released"** = a versioned build artifact that has passed quality gates (Work Model, Build Track output)

The qualifier "Customer" eliminates any collision — no one will confuse "Customer Release: LATAM Expansion" with "payments-service v2.3.3 released to artifact registry."

**Why names instead of version numbers?** Customer Releases use descriptive names (e.g., "LATAM Expansion", "Project Mercury") rather than semver or numbered versions because:
1. **Business identity:** Names convey what the release delivers; "Release 3.2" is meaningless to business stakeholders.
2. **Decoupling:** A single Customer Release may span multiple Product Versions (e.g., v3.2.0 through v3.2.4 as patches are applied during rollout). Pinning to a version number creates a false 1:1 mapping.
3. **Precedent:** Many products use named releases (macOS Sonoma/Sequoia, Android codenames, enterprise program names).

---

### Q13: Why distinguish Module Version, Product Version, and Customer Release as three separate concepts?

These three concepts operate at different levels and serve different purposes:

| Concept | Level | Nature | Versioning | Owner |
|---|---|---|---|---|
| **Module Version** | Per-module | Continuously produced CI/CD output | Semver | Build Track |
| **Product Version** | Product-wide | Verified composition (BOM) of compatible Module Versions | Semver | Build Track |
| **Customer Release** | Business | Named delivery of capabilities to customers | Named (no versions) | Discovery + Win Track |

**Why all three are necessary:**
- Without **Module Version**, there is no granular tracking of what each module's CI/CD pipeline produces.
- Without **Product Version**, there is no way to certify that a specific composition of Module Versions is compatible, tested, and reproducible. This causes real problems: composition integrity failures, inability to reference "the product" for documentation/compliance, and difficulty reproducing production states.
- Without **Customer Release**, there is no business-level planning construct that bundles outcomes of Initiatives into a coherent customer-facing delivery, decoupled from technical versioning.

**Module Version and Product Version are Work Model entities** (Build Track outputs) because they are *results* of engineering progress, not planned upfront. In CI/CD, versions are routinely and continuously incremented — they are byproducts of the build process. **Customer Release is a Definition Model entity** (Dimension 1, Strategy) because it is a business planning construct that is deliberately scoped, named, and scheduled.

---

### Q14: Why does Product Version use a Bill of Materials (BOM) with version ranges?

Product Versions declare compatible version ranges for constituent modules (Declared BOM) rather than pinning specific versions. This follows established dependency management conventions:

- `^2.3.0` — compatible with any 2.x.x (minor/patch changes OK)
- `~1.8.0` — compatible with any 1.8.x (patch changes OK)
- `>=4.1.0 <5.0.0` — explicit range

A Product Version has two facets:
- **Declared BOM:** Compatible ranges (like `package.json`)
- **Resolved BOM:** Specific versions tested and certified together (like `package-lock.json`)

This allows flexibility — a Module Version patch (e.g., `payments-service v2.3.4` fixing a security issue) can be adopted without re-certifying the entire Product Version, as long as it falls within the declared range. The Resolved BOM records exactly what was tested for reproducibility.

---

### Q15: Why is Deployment tracked per-environment rather than as a status of the Module Version?

A single Module Version (e.g., `payments-service v2.3.3`) may need to be deployed to multiple environments: staging, production-us, production-eu, production-ap, disaster recovery. These deployments happen at different times, with different strategies (canary, blue-green, rolling), and may have different outcomes (succeeded in prod-us, pending in prod-eu).

Modeling "Deployed" as a status of the Module Version would imply a binary state — either deployed or not — which doesn't reflect reality. Instead, Deployment is modeled as a **Run Track entity** with per-environment tracking:

| Module Version | Environment | Status | Strategy | Timestamp |
|---|---|---|---|---|
| payments-service v2.3.3 | staging | Succeeded | Direct | 2026-02-10 |
| payments-service v2.3.3 | production-us | Succeeded | Canary | 2026-02-12 |
| payments-service v2.3.3 | production-eu | Planned | Rolling | — |

This correctly models the operational reality and supports the decoupling of deployment from release — a Module Version can be deployed (even to production) without being part of an activated Customer Release (e.g., behind a feature flag).

---

### Q16: Why use "Signal" instead of "intake item" or "backlog item" for {Problem, Need, Opportunity}?

The UPIM uses **Signal** as the collective term for Problem, Need, and Opportunity. This is a deliberate terminology choice driven by the mindset it fosters.

**Why not "intake item"?** In practice, "intake" carries an implicit obligation to process and deliver. When a customer submits something through an "intake" process, organizations tend to treat it as a requirement that *should* be completed. This conditioning suppresses the very discovery, decision-making, and prioritization process that the UPIM explicitly mandates. An "intake" from a customer is reflexively treated as a customer requirement — not as a hint, symptom, or observation that warrants investigation.

**Why not "backlog item"?** In Scrum, "Product Backlog Item" (PBI) refers to User Stories, Bugs, and Spikes — Build Track entities in our model. Using "backlog item" for Problems/Needs/Opportunities conflates two very different levels separated by several layers (Signal → Idea → PDR → PSD → Epic → Story). Additionally, "backlog" implies the item is already in a prioritized queue awaiting work. Many Signals will sit unassociated and unranked indefinitely — they are not "in the backlog."

**Why "Signal"?**

| Property | Signal | Intake Item | Backlog Item |
|---|---|---|---|
| Implies obligation? | **No** — a signal is interpreted, not fulfilled | Yes — "process the intake" | Yes — "work the backlog" |
| Invites investigation? | **Yes** — "what does this signal mean?" | Weakly | Weakly |
| Allows dismissal? | **Naturally** — signals can be weak or noise | Awkwardly | Awkwardly |
| Multiple items → one insight? | **Yes** — "several signals point to the same issue" | Not implied | Not implied |
| Strength varies? | **Yes** — signals are strong or weak, frequent or rare | Not implied | Not implied |
| Source-agnostic? | **Yes** — works for customers, engineers, SREs, executives | Weakly | Yes |
| Aligns with discovery mindset? | **Perfectly** | Weakly | Not at all |

**Source-agnostic is critical.** Signals come from both external sources (customers, prospects) and internal sources (SREs identifying scaling issues, engineers identifying technical debt, operations teams identifying cost inefficiencies). Terms like "market signal" were rejected because they would alienate internal stakeholders whose product knowledge is essential for SaaS products. Bare "Signal" is inclusive of all sources.

**Examples of Signals in practice:**

| Signal Type | Source | Example | What it is NOT |
|---|---|---|---|
| Problem | Customer (external) | "FX rate-lock confirmation takes 6 clicks" | Not a requirement to reduce clicks |
| Problem | SRE (internal) | "Payment DB connection pool exhausted under peak load" | Not a commitment to fix it now |
| Need | Enterprise prospect (external) | "We require batch payout file upload (CSV/SFTP)" | Not a promise to build it |
| Need | Support team (internal) | "Customers keep asking for multi-currency reporting" | Not an automatic feature request |
| Opportunity | Strategy team (internal) | "LATAM currencies could capture $2M ARR" | Not an approved initiative |
| Opportunity | Engineering (internal) | "Consolidating payment adapters could save 40% infra cost" | Not a committed project |

**The definition:** *A Signal is an observation or indicator — from any source, internal or external — that something about the product warrants attention. A Signal is explicitly not a requirement, a commitment, or an obligation. It is an input to be interpreted and investigated through the Discovery Track. Multiple Signals may point to the same underlying issue; a single Signal may be noise.*

---

### Q17: Why are Service Commitment and Compliance Posture separate Customer Promise subtypes, not part of Value Proposition?

Customer Promise has three subtypes — **Value Proposition**, **Service Commitment**, and **Compliance Posture** — that are *peers*, not nested. This is a deliberate design choice:

1. **Different audiences within the buyer:** Value Propositions address the buyer's desired *outcomes* ("reduce cost by 60%"). Service Commitments address the buyer's *operational risk concerns* ("will your system stay up?"). Compliance Posture addresses the buyer's *regulatory/security requirements* ("are you PCI-DSS certified?"). Each speaks to a different facet of the buying decision — often evaluated by different people in the procurement process (finance/LOB, IT/SRE, legal/compliance respectively).

2. **Different mapping targets:** Value Propositions map to the structural model (Value Streams and Capabilities in Dim 8). Service Commitments map to the operational model (Dim 7 infrastructure). Compliance Posture influences both structure (Dim 8 Capabilities are shaped by compliance requirements) and operations (Dim 7 monitoring, audit trails). Conflating them in Value Proposition would obscure these distinct structural relationships.

3. **Different metric types:** Each subtype is evidenced by a different Customer Value Metric subtype — ROI Metrics (financial/time return), Service Level Metrics (uptime, latency), Compliance Metrics (audit pass/fail, certification validity). A single "Value Proposition" entity trying to capture all three would become unwieldy and lose metric specificity.

4. **Different lifecycle cadences:** Value Propositions change when product capabilities change. Service Commitments change when SLAs are renegotiated or infrastructure changes. Compliance Posture changes when regulations change or new certifications are pursued. Coupling them would create unrelated change triggers.

**Together, the three subtypes represent the complete product promise** — outcome delivery, reliability guarantees, and compliance assurance — each measured by its own metric type.

---

### Q18: Why introduce Value Stream as a Dim 8 entity alongside Capabilities?

Dimension 8's vertical decomposition (Product → Module → Capability → Feature) describes *what the product can do* — a taxonomy of abilities. But many customer outcomes require activities that cut *across* multiple modules. No single module "owns" the outcome "Reduce cross-border payment cost by 60%" — it emerges from the orchestrated collaboration of Invoice, FX, Compliance, Payment, and Settlement modules.

**Value Stream** fills this gap as the *horizontal composition* in Dim 8:

| Concept | Perspective | Example |
|---|---|---|
| **Capability** (Dim 8) | What the product *can do* — a static ability | "Automated Rate Locking" |
| **Value Stream** (Dim 8) | How the product *delivers value* — an end-to-end flow | "Cross-Border Payout Processing" |
| **User Journey** (Dim 4) | How the *user experiences* the flow — human perspective | "AP Clerk processes international payout" |

Value Streams and User Journeys often align but are not identical. A Value Stream may include automated backend steps invisible to the user (e.g., OFAC sanctions screening). A User Journey may include cognitive/emotional steps invisible to the system (e.g., "user checks manager approval before submitting").

**Impact on Value Propositions:** With Value Streams, outcome-based Value Propositions can map precisely to end-to-end flows, not just individual capabilities:
- *Outcome-based VP:* "Reduce payment cost by 60%" → maps to **Value Stream** "Cross-Border Payout Processing" → measured by end-to-end flow metrics (cycle time, cost per transaction)
- *Ability-based VP:* "Lock FX rates in real-time" → maps to **Capability** "Automated Rate Locking" → measured by point metrics (lock speed, currency coverage)

Without Value Stream, outcome-based Value Propositions could only point to a list of Capabilities, losing the orchestration narrative — the *flow* that produces the outcome.

---

### Q19: Why introduce Modeling Task as a Discovery Track work entity?

Discovery work in the UPIM produces three types of output:
1. **PSDs** — engineering specifications for module changes (via Specification Task)
2. **Definition Model updates** — evolution of entities in Dims 2–9 (via **Modeling Task**)
3. **PDRs** — decision records justifying either or both of the above

Before Modeling Task, only Specification Task existed to represent "productive discovery output." But much of discovery work — particularly for new markets, segments, or capabilities — involves understanding and documenting the product's context rather than specifying engineering changes. Examples:

| Modeling Task | Dimension | What changes |
|---|---|---|
| "Define LATAM Enterprise customer segment" | Dim 3 | Customer Segment, Buyer Persona, Outcomes |
| "Map Cross-Border Payout Processing value stream" | Dim 8 | Value Stream, Module relationships |
| "Design LATAM pricing tier structure" | Dim 2 | Pricing Tier / Package |
| "Document LGPD compliance posture" | Dim 3 | Compliance Posture |
| "Define LATAM AP Clerk user persona" | Dim 4 | User Persona |

Without Modeling Task, this knowledge work is invisible and untracked. Product Managers do it implicitly, but it doesn't appear in any planning or tracking system. Making it explicit ensures:
- **Plannable:** PMs can include Modeling Tasks in sprint/iteration planning
- **Traceable:** Definition Model updates can be traced to the discovery work that produced them
- **Visible:** Stakeholders can see that "we're investing in understanding our customer, not just building features"

Modeling Task sits alongside Signal Exploration Task, Research Task, Experiment, Prototype/Spike, Deliberation, and Specification Task as co-equal Discovery Track work entities.

---

### Q20: Why split "Research Task" into Signal Exploration Task and Research Task?

The original "Research Task" was conflating two fundamentally different types of work under one name:

| Phase | Nature | Mindset | Output |
|---|---|---|---|
| **Signal → Idea(s)** | Divergent, open-ended exploration | "What does this signal mean? What could we do?" | Ideas (hypotheses) |
| **Idea → Validated/Killed** | Convergent, targeted evidence gathering | "Is this specific Idea viable? What's the evidence?" | Evidence for/against |

These require different skills, different planning, and different outputs. A PM exploring a Signal is doing creative synthesis — connecting dots across customer feedback, market data, and product constraints to form a hypothesis. A PM validating an Idea is doing focused investigation — gathering specific evidence to test a known hypothesis.

**Signal Exploration Task** is the new entity for Phase 1 work. It captures the structured investigation of a Signal — understanding context, root causes, affected segments, adjacent patterns — and the synthesis of candidate Ideas from that understanding. It is input-anchored: you start from a Signal and explore.

**Research Task** is narrowed to mean targeted, convergent investigation — specific data gathering, user interviews, competitive analysis — to answer a known question or test a known hypothesis. Research Tasks primarily serve Idea Validation but can also be spawned during Signal Exploration when specific data is needed.

The naming follows the established UPIM pattern: entities are named for what they process, not what they produce. Signal Exploration processes Signals (like Specification Task processes specifications). Research Task gathers research (targeted evidence).

**Key distinction:** If you don't yet have a hypothesis, you need Signal Exploration. If you have a hypothesis and need evidence, you need Research (or Experiment/Prototype).

---

### Q21: Why introduce Deliberation as a Discovery Track entity?

Not all product decisions are made through empirical validation. In practice, many significant decisions emerge from structured group discussions — product councils, architecture review boards, customer advisory meetings, cross-functional brainstorms. Before Deliberation, this entire class of decision-making work was invisible in the model.

**What makes Deliberation distinct from every other Discovery entity:**

| Entity | Mode | Source of output | Solo or Group? |
|---|---|---|---|
| Signal Exploration Task | Divergent | Individual investigation + synthesis | Individual / small team |
| Research Task | Targeted | Empirical evidence gathering | Individual / small team |
| Experiment | Convergent | Formal test with criteria | Individual / small team |
| Prototype / Spike | Convergent | Building to learn | Individual / small team |
| **Deliberation** | **Either** | **Collective judgment of an authorized group** | **Group (inherently)** |

Deliberation is the only Discovery entity that is inherently *collaborative*. Its output comes from the group's combined expertise, experience, and perspective — not from individual investigation or formal testing.

**Deliberation spans both discovery phases:**

- **Exploration mode (divergent):** A cross-functional brainstorm generating candidate Ideas from Signals. The group's diverse expertise produces hypotheses that no single investigator would arrive at alone. (e.g., "Cross-functional brainstorm: generate Ideas for batch payout automation")
- **Evaluation mode (convergent):** A product council evaluating an Idea and deciding Go/Kill/Pivot. The group's authority makes the decision legitimate without requiring empirical validation. (e.g., "Product council: evaluate LATAM expansion approaches, decide on preferred strategy")

**Deliberation may directly produce a PDR** — this is a first-class decision path. Not every product decision needs an Experiment or Prototype. When the CFO, CTO, and VP Product deliberate on whether to enter the LATAM market, their collective judgment is the evidence. The PDR records the reasoning.

**Not every meeting is a Deliberation.** A Deliberation is tracked when the group activity produces a consequential outcome — Ideas, PDRs, or significant strategic direction. Status syncs, sprint ceremonies, and routine check-ins are NOT Deliberations.

---

### Q22: Why expand Economic Buyer Persona to Buying Persona with role types?

In enterprise B2B, purchases are rarely approved by a single person. A **buying committee** evaluates the product through multiple lenses:

| Role | Evaluates | Deal impact |
|---|---|---|
| **Economic Buyer** | ROI, cost justification, budget | Can approve or reject spend |
| **Technical Buyer** | Integration, security, architecture | Can veto on technical grounds |
| **User Buyer** | Usability, workflow fit, team adoption | Can block on adoption concerns |
| **Coach / Champion** | Internal politics, change management | Navigates the buying process |

Modeling only the Economic Buyer left the Technical Buyer invisible — yet many deals die at technical evaluation ("your API requires 6 weeks to integrate"). The User Buyer is partially covered by User Persona (Dim 4) but occupies a distinct buying role. The Coach/Champion is unique to Dim 3 — they don't use the product or approve the budget, but they shepherd the deal.

Expanding to a single **Buying Persona** entity with a `Role Type` field (rather than creating four separate entities) keeps the model compact while capturing the full committee. Each role type has different Key Concerns and different Pains they care about — enabling role-specific messaging and identifying where deals stall.

---

### Q23: Why introduce Pain as a Dim 3 entity? How does it relate to Business Outcome?

**Pain** and **Business Outcome** together form the complete "Why Buy" motivation:

| Entity | Perspective | Nature | Example |
|---|---|---|---|
| **Business Outcome** | Buyer (strategic) | What they need to *achieve* | "Reduce FX costs by 40%" |
| **Pain** | User (operational) | What they *suffer* today | "4 hours/day manual reconciliation" |

Business Outcome is the rational justification ("this is why we should buy"). Pain is the visceral urgency ("this is what we're suffering right now"). Value Propositions address *both* — delivering outcomes AND relieving pains.

**The critical distinction is "who endures" vs. "who cares":**
- The **User Persona** (Dim 4) *endures* the Pain — they experience it in their daily workflow.
- The **Buying Persona** (Dim 3) *cares about* the Pain — it motivates their purchase decision, even if they never personally experience it.

This separation matters because the same Pain is cared about by different Buying Personas for different reasons. "AP Clerk spends 4 hours/day on manual reconciliation" — the CFO cares about the cost ($), the AP Ops Manager cares about team productivity, the CTO cares about error rates. Each needs a different message.

**JTBD mapping is now complete:**
- Buyer's Job → Business Outcome
- User's Pain → Pain
- Value delivered → Value Proposition (addresses Outcomes + relieves Pains)
- User's Job → User Journey (Dim 4)

Pains are captured at a granularity that makes them actionable for positioning and sales — not at feature-level detail. "4 hours/day manual reconciliation" is the right level; "screen lacks a filter dropdown" is too granular.

---

### Q24: Why does Adoption Barrier have 8 types and a relationship to Customer Promise?

**Expanded types:** The original 4 types (Regulatory, Technical, Organizational, Competitive) missed common enterprise adoption blockers:

- **Financial** — budget ceiling doesn't match pricing floor
- **Contractual** — locked into competitor's multi-year contract
- **Data** — migration of historical data is prohibitively complex
- **Cultural** — risk-averse organization requires extended proof-of-concept

These were being misclassified under "Organizational" or "Technical," losing specificity.

**Barrier → Promise relationship:** An Adoption Barrier may directly challenge or undermine a Customer Promise. For example:
- "Data residency requirement" (Regulatory Barrier) **challenges** "GDPR compliant" (Compliance Posture)
- "No self-service onboarding" (Technical Barrier) **challenges** "Get started in under 24 hours" (Value Proposition)

Making this relationship explicit exposes gaps between what the product promises and what prevents customers from realizing that promise — a critical input for discovery prioritization.

---

### Q25: Why introduce Strategic Theme and Portfolio as Dim 1 entities?

**The gap:** Objectives are time-bound and product-scoped — "Expand to LATAM currencies by H2 2026." But the strategic direction "invest in LATAM" may span years and multiple Objectives. Without an explicit entity for this persistent direction:
- Strategic continuity across planning horizons is implicit
- Resource allocation across strategic directions is invisible
- Cross-product coordination (when a theme spans a portfolio) has no shared language

**Strategic Theme** is a persistent, cross-cutting direction that generates Objectives over multiple horizons. The relationship is hierarchical: Theme → Objective(s) → Initiative(s). Themes provide the *why behind the why*.

**The portfolio dimension:** Themes may be **Portfolio-scoped** (declared at portfolio level, adopted by multiple products) or **Product-scoped** (originated locally). This matters because a product doesn't exist in isolation — the strategic direction "LATAM Market Leadership" applies to the Payment Gateway, the Merchant Portal, and the Settlement Platform simultaneously.

**Portfolio** is a thin, local reference entity — the UPIM does not own or manage the portfolio. It exists solely so that portfolio-scoped Themes have a traceable origin and the product's place within the portfolio is documented.

**Key design choices:**
- **Theme is optional on Objectives.** Reactive Objectives ("Remediate critical security vulnerability") don't belong to any Theme. Themes organize proactive strategic investment, not reactive work.
- **Themes filter resource allocation; Objectives filter prioritization.** "40% of discovery capacity to LATAM" (Theme) is different from "expand to BRL/MXN/COP/CLP by H2" (Objective).
- **Product-scoped Themes can be elevated to Portfolio scope** when the direction is adopted across products. The Scope field changes; the entity persists.
- **Dormant status.** A Theme with no current Objectives is Dormant (not Retired). "Developer Experience" may have no active Objectives this half but remain a strategic direction for next half.

---

### Q26: Why add a common Signal lifecycle across Problem, Need, and Opportunity?

All three Signal types previously had `_To be refined._` for statuses — leaving the model unable to answer basic operational questions: "How many Signals are we exploring?" "How many are parked?"

The common lifecycle applies to all three Signal types:

`New` → `Triaged` → `Exploring` / `Associated` / `Parked` → `Addressed` / `Dismissed`

Key design choices:
- **`Triaged` is distinct from `New`.** A PM must actively review a Signal to confirm it's legitimate. This prevents unreviewed Signals from polluting active queues.
- **`Exploring` and `Associated` can coexist conceptually** — a Signal may be both under exploration AND linked to an Initiative. The model prioritizes the more advanced state: once Associated, the Signal is coordinated within an Initiative.
- **`Addressed` means "PDR produced"** — not "feature shipped" or "customer satisfied." The Signal is addressed when a formal decision is made about it. Whether that decision leads to shipped PSDs is tracked elsewhere.
- **`Parked` → `Triaged` allows re-entry.** Signals parked in one cycle can re-enter consideration in a future cycle without being re-created.
- **`Dismissed` captures noise and duplicates.** A dismissed Signal with rationale is more valuable than a silently deleted one — it prevents re-investigation of the same noise.

---

### Q27: Why three models (Definition, Work, Operating) instead of four?

An earlier design proposed four models: Definition Model, Work Model, Operating Model (ceremonies/coordination), and Organization Model (roles/teams/skills/tools). This required determining the dependency direction between Operating and Organization — and every ordering felt wrong.

**The problem:** Strict layering implies one-way dependency (A depends on B, never the reverse). But coordination and organization have **bidirectional dependency:**

- Coordination → Organization: "We chose Scrum → we need a Scrum Master"
- Organization → Coordination: "We only have 3 PMs → we can't run 6 parallel Signal Reviews"

They co-constrain. They co-evolve. Forcing one "above" the other distorts the relationship.

**The resolution:** Consolidate into a single **Operating Model** with two entangled facets — Coordination and Organization. In everyday business language, "our operating model" naturally encompasses both how we're structured and how we coordinate. The split was only needed when the architecture tried to force strict layering.

**The resulting three-model stack:**

| Layer | Depends on | Question it answers |
|---|---|---|
| **Operating Model** | Work Model | How does the org execute? (coordination + organization) |
| **Work Model** | Definition Model | What work exists? (entities, artifacts, state transitions) |
| **Definition Model** | — (foundation) | What is the product? (9 Dimensions) |

**Internal structure deferred:** The Definition Model has 9 Dimensions and the Work Model has 4 Tracks — both terms earned through iterative modeling. The Operating Model's subdivision pattern will emerge when we detail it. We know it covers Coordination and Organization; we don't yet know if a third facet exists, or what the right structural metaphor is. Premature naming would be like calling Dimension 3 "The ROI Dimension" before discovering it's about the full buying committee, pain, promises, and barriers.

See DR-014 for the full decision record.

---
