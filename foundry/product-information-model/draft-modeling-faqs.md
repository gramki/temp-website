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
- **"System Version with status Released"** = a versioned build artifact that has passed quality gates (Work Model, Build Track output)

The qualifier "Customer" eliminates any collision — no one will confuse "Customer Release: LATAM Expansion" with "payments-service v2.3.3 (System Version) released to artifact registry."

**Why names instead of version numbers?** Customer Releases use descriptive names (e.g., "LATAM Expansion", "Project Mercury") rather than semver or numbered versions because:
1. **Business identity:** Names convey what the release delivers; "Release 3.2" is meaningless to business stakeholders.
2. **Decoupling:** A single Customer Release may span multiple Product Versions (e.g., v3.2.0 through v3.2.4 as patches are applied during rollout). Pinning to a version number creates a false 1:1 mapping.
3. **Precedent:** Many products use named releases (macOS Sonoma/Sequoia, Android codenames, enterprise program names).

---

### Q13: Why distinguish System Version, Module Version, Product Version, and Customer Release as four separate concepts?

These four concepts operate at different levels and serve different purposes. See also DR-026 for the three-tier versioning model.

| Concept | Level | Nature | Versioning | Owner |
|---|---|---|---|---|
| **System Version** | Per-system | Continuously produced CI/CD output — atomic deployment unit | Semver | Build Track |
| **Module Version** | Per-module | Integration-verified composition of System Versions — integrated deployment unit + integration verification | Semver | Build Track |
| **Product Version** | Product-wide | Certified composition of compatible Module Versions (BOM) — complete deployment unit + certification | Semver | Build Track |
| **Customer Release** | Business | Named delivery of capabilities to customers | Named (no versions) | Discovery + Win Track |

**Why all four are necessary:**
- Without **System Version**, there is no granular tracking of what each System's CI/CD pipeline produces, and no deployment unit for the Run Track.
- Without **Module Version**, there is no integration verification layer — you jump from individual System testing to full-product testing (an O(n²) problem). Module Version proves that the Systems implementing a Module (Dim 8) work together.
- Without **Product Version**, there is no way to certify that a specific composition of Module Versions is compatible, tested, and reproducible. This causes real problems: composition integrity failures, inability to reference "the product" for documentation/compliance, and difficulty reproducing production states.
- Without **Customer Release**, there is no business-level planning construct that bundles outcomes of Initiatives into a coherent customer-facing delivery, decoupled from technical versioning.

**System Version, Module Version, and Product Version are Work Model artifacts** (Build Track outputs) because they are *results* of engineering progress, not planned upfront. In CI/CD, versions are routinely and continuously incremented — they are byproducts of the build process. **Customer Release is a Definition Model entity** (Dimension 1, Strategy) because it is a business planning construct that is deliberately scoped, named, and scheduled.

**Each artifact tier is a composite system and a communication bridge.** Module Version and Product Version are not just verification checkpoints — they are systems in their own right, with emergent operational properties at each composition level (end-to-end latency, integrated failure modes, cross-module workflows). They are also communication bridges at progressively broader organizational scope: System Version is the shared vocabulary between Build and Run teams; Module Version bridges Build, Run, and Product teams (PMs, SREs, and engineers all reference "Payments Module v4.1"); Product Version is the ubiquitous language across all teams and customers (Win teams, compliance, customers all reference "Product v3.2"). See `stories/versioning-alternatives-analysis.md` for how alternative approaches address these challenges.

---

### Q14: Why does Product Version use a Bill of Materials (BOM) with version ranges?

Product Versions declare compatible version ranges for constituent Module Versions (Declared BOM) rather than pinning specific versions. This follows established dependency management conventions:

- `^2.3.0` — compatible with any 2.x.x (minor/patch changes OK)
- `~1.8.0` — compatible with any 1.8.x (patch changes OK)
- `>=4.1.0 <5.0.0` — explicit range

A Product Version has two facets:
- **Declared BOM:** Compatible Module Version ranges (like `package.json`)
- **Resolved BOM:** Specific Module Versions tested and certified together (like `package-lock.json`), each containing its constituent System Versions

This allows flexibility — a Module Version update (e.g., `Payments Module v2.3.1` with a new System Version `payments-service v2.3.4` fixing a security issue) can be adopted without full Product-level re-certification, as long as it falls within the declared range. The Resolved BOM records exactly what was tested for reproducibility.

---

### Q15: Why is Deployment tracked per-environment rather than as a status of the System Version?

A single System Version (e.g., `payments-service v2.3.3`) may need to be deployed to multiple environments: staging, production-us, production-eu, production-ap, disaster recovery. These deployments happen at different times, with different strategies (canary, blue-green, rolling), and may have different outcomes (succeeded in prod-us, pending in prod-eu).

Modeling "Deployed" as a status of the System Version would imply a binary state — either deployed or not — which doesn't reflect reality. Instead, Deployment is modeled as a **Run Track entity** with per-environment tracking:

| System Version | Environment | Status | Strategy | Timestamp |
|---|---|---|---|---|
| payments-service v2.3.3 | staging | Succeeded | Direct | 2026-02-10 |
| payments-service v2.3.3 | production-us | Succeeded | Canary | 2026-02-12 |
| payments-service v2.3.3 | production-eu | Planned | Rolling | — |

This correctly models the operational reality and supports the decoupling of deployment from release — a System Version can be deployed (even to production) without being part of an activated Customer Release (e.g., behind a feature flag). See DR-026.

> **DR-029 update:** Deployment is now an artifact (records that a descriptor was applied); the work is performed by Deployment Task. See DR-029.

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

**Internal structure deferred:** The Definition Model has 9 Dimensions and the Work Model has 5 Tracks — both terms earned through iterative modeling. The Operating Model's subdivision pattern will emerge when we detail it. We know it covers Coordination and Organization; we don't yet know if a third facet exists, or what the right structural metaphor is. Premature naming would be like calling Dimension 3 "The ROI Dimension" before discovering it's about the full buying committee, pain, promises, and barriers.

See DR-014 for the full decision record.

---

### Q28: Why restructure Dimension 2 as the Vendor Value Dimension (Why It Wins) with an AAARRR lens?

The original Dimension 2 ("Business Value — Vendor Economics") had 4 shell entities (Business Model, Pricing Tier, Value Metric, Business KPI) with no fields, no statuses, and no cross-dimensional relationships. It modeled the product as a simple financial vehicle — "how we price" — ignoring the full complexity of how the vendor succeeds commercially.

**The challenge:** For complex enterprise B2B products, the vendor's path from signed contract to revenue realization involves an elaborate, multi-stakeholder journey — Pre-Sales, Implementation, Go-Live, Revenue Realization, Optimization, Renewal. This journey is not self-evident; it requires the same discovery and investigation mindset as the customer's buying journey (Dim 3).

**The AAARRR lens (Awareness, Acquisition, Activation, Retention, Revenue, Referral)** provides the lifecycle framework. Each stage has:
- Different **Win Stakeholders** responsible (analog of Buying Personas)
- Different **Win Outcomes** defining success (analog of Business Outcomes)
- Different **Delivery Frictions** that the vendor suffers (analog of Pains)
- Different **Win Barriers** that structurally block success (analog of Adoption Barriers)
- Different **Business KPIs** measuring performance (analog of Customer Value Metrics)

The restructured Dim 2 now mirrors Dim 3's analytical depth, with **Customer Segment (Dim 3) as the shared anchor** between the two dimensions — the same segment that has Buying Personas and Pains also has Win Stakeholders and Delivery Frictions.

See DR-015 for the full decision record.

---

### Q29: Why introduce Win Stakeholder as a Dim 2 entity? Isn't that an Operating Model concern?

Win Stakeholders are **functional archetypes**, not organizational roles. The distinction:
- **Operating Model (future):** "We have 3 Pre-Sales Engineers in LATAM, reporting to VP Sales" — organizational reality
- **Dim 2 (Definition Model):** "The product's commercial success requires a Pre-Sales Engineer role that demonstrates technical fit during Acquisition" — functional requirement

A startup may have one person covering Pre-Sales, Implementation, and CS. The Win Stakeholder model still distinguishes the three functions because they have different concerns, different frictions, and different success criteria. When the startup hires, the Win Stakeholder model tells them *what roles the product's commercial model requires*.

Win Stakeholders also serve as the "who endures" anchor for Delivery Frictions (paralleling how User Persona is the "who endures" anchor for Pain in Dim 3) and the "who's responsible" anchor for Win Outcomes. Without them, vendor-side frictions and outcomes are abstract — "the vendor suffers" has no human face.

---

### Q30: Why do all Dim 2 changes require PDRs?

Dim 2 entities define the product's commercial model — how the vendor generates revenue, what success looks like, and what pricing the market sees. Changes to these entities have direct commercial consequences:

- Changing a **Pricing Tier** affects active customers and sales motions
- Changing a **Business KPI target** affects resource allocation and team incentives
- Adding a **Win Barrier** may trigger strategic reprioritization
- Documenting a **Delivery Friction** creates pressure to invest in fixes

These are not casual updates. Every Dim 2 change follows one of two governed paths:

1. **Deliberation → PDR → Modeling Task:** For strategic design (pricing strategy, AAARRR target-setting, Win Outcome definition). Win Stakeholders participate in Deliberations; the PM/PMM authors entities through Modeling Tasks.

2. **Signal → Discovery → PDR → Modeling Task:** For field observations (Delivery Frictions, Win Barriers). Win Stakeholders observe and file Signals; Discovery investigates; PDR records the decision; Modeling Task updates Dim 2.

The PDR requirement ensures traceability — "why did we change the LATAM pricing tier?" has a referenceable answer — and prevents ad-hoc modifications to the commercial model.

---

### Q31: Why does Win Outcome carry "Achievement Levers" and what is the Lever Portfolio?

Not all Win Outcomes are advanced by product capabilities alone. An Awareness Win Outcome ("80% brand recall in LATAM fintech CFOs") is barely moved by product features — the lever is GTM (marketing campaigns, analyst relations). An Acquisition Win Outcome ("close LATAM deals in 90 days") depends heavily on Sales Enablement (competitive battlecards, POC tooling). Without explicitly identifying the levers at modeling time, organizations default to building features when the actual lever may be a sales enablement program.

The **Lever Portfolio** is a finite, referenceable set of categorical levers defined on the Business Model entity (Dim 2). Five standard categories: **Product** (Build Track), **GTM** (Win Track), **Sales Enablement** (Win Track), **Customer Success** (Win Track), **Operational** (Operating Model). The portfolio varies by product — a developer API might not have a Sales Enablement lever. Initiatives reference the Lever Portfolio when declaring their lever mix.

Each Win Outcome declares its **Achievement Levers** (primary/secondary) from the portfolio. This forces the question: "Is this primarily a product problem, a GTM problem, or both?" The answer shapes what kinds of Initiatives and Win Track work are needed.

See DR-015 (Dim 2 restructure, where Lever Portfolio is defined) and DR-016 (Win Track lever alignment).

---

### Q32: Why did Initiative evolve from "Discovery program" to "cross-track coordination construct"?

Originally, Initiative was defined as a mechanism for grouping Signals for discovery, implying a flow: Initiative → Discovery → PSD → Build. The Dim 2 restructure (DR-015) and the lever discussion (DR-016) revealed that an Initiative like "LATAM Enterprise Market Entry" drives work across *all four tracks* — product development (Build), GTM execution (Win), sales enablement (Win), CS programs (Win), infrastructure (Run), and potentially organizational changes (Operating Model).

Three additions make the cross-track nature explicit:

1. **Lever Mix** — weighted allocation (e.g., Product 40%, GTM 25%, SE 20%, CS 15%). Tells downstream planners how much investment each track needs.
2. **Embedded Targets** — time-bound, quantitative measures per Win Outcome, like OKR Key Results. Assessed by Win Reviews.
3. **Cross-track work alignment** — Win Track entities (Planning, Enablement, Engagement) reference the Initiative they advance.

Objectives remain lever-agnostic. The lever mix is an Initiative-level concern, keeping strategy → execution separation clean.

See DR-017 for the full decision record.

---

### Q33: Why were targets embedded in Initiatives rather than kept as a standalone "Adoption Goal" entity?

Three problems with standalone Adoption Goal:

1. **"Adoption" is stage-specific.** Only Activation is about "adoption." Awareness targets ("80% brand recall"), Revenue targets ("$2M MRR"), and Acquisition targets ("15 deals closed") are not adoption. The name misrepresented the entity's scope.

2. **"Goal" conflicts with Objectives.** Objectives are goals. Adding another "goal" entity created hierarchy confusion — is an Adoption Goal above or below an Objective?

3. **Targets are attributes, not independent entities.** In the OKR model, Key Results are not standalone — they're embedded in the Objective they measure. Similarly, targets belong in the Initiative that drives toward them. They're set during planning, tracked during execution, and assessed during Win Reviews — always in the context of their Initiative.

Eliminating the standalone entity simplifies the model and follows the OKR pattern: Initiative (with embedded targets) parallels Objective (with Key Results).

---

### Q34: Why does the Win Track have six categories instead of the original three?

The original Win Track had three buckets: Planning (GTM, Rollout), Execution (Implementation), and Measurement (Adoption Goal, Feedback). This missed several critical classes of work:

| Category | What was missing |
|---|---|
| **Enablement** (Equip) | Building reusable assets — battlecards, demo environments, playbooks. This one-to-many work is fundamentally different from engagement (one-to-one). |
| **Engagement** (Execute, expanded) | Pre-sales (POC, demo, RFP), Retention (health intervention, renewal), Expansion (upsell), Segment-level (webinars, workshops). Only Implementation/Onboarding existed. |
| **Win Case** (Respond) | Reactive, customer-initiated work — queries, complaints, escalations. This is where Service Commitments are tested and Cost-to-Serve is measured. |
| **Win Review** (Assess) | Structured assessment producing Feedback. Without it, observations "appeared" with no traceable review event. Parallels Deliberation in Discovery Track. |

The Enablement vs. Engagement distinction is particularly important: Sales Enablement (building a battlecard) is fundamentally different from Pre-sales (using that battlecard in a POC for Prospect X). One is one-to-many preparation; the other is one-to-one execution. Conflating them makes enablement investment invisible.

See DR-016 for the full decision record.

---

### Q35: Why is Win Case separate from Run Track Incident?

They serve different audiences and track different concerns:

| | Win Case | Run Track Incident |
|---|---|---|
| **Initiated by** | Customer or prospect | Monitoring system or internal team |
| **Perspective** | Customer-facing ("my payouts are delayed") | System-facing ("API latency spiked to 5s") |
| **Handled by** | Win Stakeholders (Support, CS) | SRE, DevOps |
| **Tests** | Service Commitments (Dim 3) | Operational SLAs (Dim 7) |
| **Measures** | Cost-to-Serve, CSAT (Dim 2 KPIs) | MTTR, Availability (Dim 7 metrics) |

A Win Case may *trigger* a Run Track Incident (customer reports a problem that turns out to be infrastructure), but the two are tracked independently. The Win Case tracks the customer interaction and satisfaction; the Incident tracks the technical resolution.

"Complaint" was chosen over "Problem" as a Win Case type because (a) "Problem" is already a Signal type in Dim 1, and (b) "Complaint" accurately describes customer-expressed dissatisfaction, whereas ITSM "Problem" means root cause analysis of recurring incidents — a technical, internal activity.

---

### Q36: Why is Feedback an artifact rather than a work item?

A work item is something someone *does* — it has a status lifecycle representing progress (Planned → In Progress → Done). Feedback is something someone *produces* during a Win Review. You do a QBR and *produce* Feedback records, just as you do a Deliberation and *produce* a PDR.

Feedback is a **transitional artifact**: born in the Win Track, consumed by the Discovery Track when promoted to a Signal. The lifecycle is: observation occurs during Win Review → recorded as Feedback → reviewed → either promoted to Signal (warrants Discovery investigation) or archived (noise, already known, no action needed).

This parallels the PDR pattern: Deliberation (work) → PDR (artifact). Win Review (work) → Feedback (artifact). The work entity is traceable; the artifact captures the output.

Win Review also produces a second output: **Initiative target progress updates** — quantitative assessment against embedded targets. Together, the qualitative (Feedback) and quantitative (target progress) outputs give a complete picture.

---

### Q37: Why introduce a Work Execution Framework? Isn't this Operating Model territory?

Three execution dimensions were missing from the Work Model: (1) what artifacts each work type produces, (2) when the work is done (Definition of Done), and (3) how to navigate the work (playbooks/guidance). The first two are information model concerns — artifacts and completion criteria are properties of the work itself, not team-specific practices. A Win Review *always* produces Feedback and target progress updates, regardless of which team runs it.

The third dimension — guidance — is genuinely Operating Model territory. Playbooks vary by team, product, and organizational maturity. The Work Model captures the *structure* of guidance (what a playbook should cover: triggers, activities, decision points, pitfalls) but not the *content* (the actual procedures). Entity files reference Operating Model playbooks; they don't contain them.

The framework also introduces an **artifact taxonomy** (Decision, Evidence, Specification, Delivery, Assessment) and the distinction between **transitional** artifacts (born in one track, consumed by another — like PSD, Feedback) and **terminal** artifacts (consumed within their own track). This makes cross-track handoff contracts explicit.

See DR-018 for the full decision record.

---

### Q38: Why add monitoring as a work entity in every track?

Every track has continuous monitoring work that triggers reactive work (Incidents, Bugs, Win Activities, Prioritization re-evaluation) and feeds periodic assessment (Win Review, Deliberation, Release Planning). That work was implicit — teams monitored dashboards and alerts, but the Work Model didn't represent it. Adding Signal Monitoring (Track 1), Build Monitoring (Track 2), System Monitoring (Track 3), and Win Monitoring (Track 4) makes the pattern explicit: same structure (scope, metrics, thresholds, cadence, owner; outputs: alert/trigger, report/dashboard), track-specific scope. Run Track's System Monitoring is the most established in practice (SRE/DevOps); it is now modeled. Win Monitoring includes revenue monitoring — tracking revenue metrics and surfacing signals when targets are missed. See DR-019.

---

### Q39: Why Partner Enablement and Partner Engagement instead of a separate "partner track"?

Partners are intermediaries (Awareness, Acquisition); they need enablement and engagement distinct from internal sales and from customers. Modeling them as subtypes of Win Enablement and Win Activity keeps one Win Track: partner work is still "value realization" work, just directed at partners instead of end customers. Partner Enablement (partner demo environments, co-marketing kits, certification) uses the GTM lever and is distinct from Sales Enablement (internal teams). Partner Engagement (onboarding, co-selling, pipeline management) is account-level (one partner); it references external PRM. Engagement Planning explicitly includes partner prioritization and sequencing. See DR-019.

---

### Q40: What is Revenue Operations Engagement and how does it differ from Expansion Engagement?

**Revenue Operations Engagement** is account-level, customer-facing work to ensure *committed* revenue is realized: invoicing/billing communication, collections follow-up, renewal processing, revenue recognition coordination with Finance. It advances Revenue Win Outcomes (e.g., on-time collection, renewal rate). **Expansion Engagement** is upsell/cross-sell — growing account value. Both are Revenue-stage work; one secures and collects, the other grows. Billing disputes are handled as Win Case (Complaint). Revenue *monitoring* (tracking NRR, pipeline, churn signals) is covered by Win Monitoring, not by Revenue Operations Engagement. See DR-019.

---

### Q41: Why don't Dim 2 and Dim 3 entities link to each other?

Dim 2 (Vendor Value) and Dim 3 (Customer Value) use the same analytical pattern — stakeholder, outcome, suffering, impediment, metric — but model opposite perspectives. Win Outcome (vendor target) and Business Outcome (buyer target) are not equivalents; a vendor's Win Outcome might be "acquire 50 LATAM accounts" while the buyer's Business Outcome is "reduce FX costs." Delivery Friction (vendor suffering) and Pain (customer suffering) affect different people through different mechanisms. Win Barrier and Adoption Barrier are distinct impediments; where an Adoption Barrier causes a Win Barrier, the link flows through the Signal pipeline (Dim 1), not a direct entity relationship. Both dimensions connect through **Customer Segment** — the shared anchor. Adding pairwise cross-dimensional links would overstate conceptual parallels as operational relationships.

---

### Q42: Why do Dim 2/3 entities link to Dim 8 (structural dimension)?

Several Dim 2 and Dim 3 entities benefit from traceability to the product's structural topology (Dim 8). Win Outcome's Achievement Levers say *what kind* of effort advances it; the Dim 8 link says *which product structure* supports it. Delivery Friction's Dim 8 link enables structural root-cause analysis ("this friction is rooted in the FX Module's integration capability"). Win Barrier and Adoption Barrier Dim 8 links identify product gaps. These links are **optional** — pure GTM Win Outcomes, operational Delivery Frictions, and Financial/Contractual barriers have no product root. But when the link exists, making it explicit enables impact analysis across the strategy-to-structure boundary.

---

### Q43: Why is competitive intelligence a structured field on Customer Segment rather than a standalone entity?

Competitive positioning is always segment-scoped — you may be a leader in one segment and a new entrant in another. A "Competitor" entity would need scoping to segments anyway, creating a segment-competitor matrix that adds complexity without adding structural insight. The Competitive Context sub-structure on Customer Segment captures the structural positioning: key competitors, position (Leader/Challenger/Niche/New Entrant), primary threats (referencing Competitive-type Win Barriers), key differentiators, and incumbent/status quo. Detailed competitive intelligence (battlecards, positioning guides, win/loss playbooks) is Operating Model / Sales Enablement content — not Definition Model entities. Value Proposition already carries per-promise competitive detail (Primary Alternative, Key Differentiator).

---

### Q44: Why does Business Outcome carry Buyer's Internal KPI separately from Customer Value Metric?

Customer Value Metric measures whether the *vendor's promise* is being fulfilled: "Did we deliver 99.9% uptime?" "Did we reduce transaction cost by 60%?" The vendor defines these metrics and tracks them. Buyer's Internal KPI is how the *purchasing organization* measures whether the investment paid off — what the CFO reports to the board. "Cross-border payment cost as a percentage of revenue" is the buyer's KPI; "60% cost reduction" is the vendor's promise metric. They may correlate but they're different measurements, owned by different parties, used for different purposes. Buyer's Internal KPI, paired with Current Baseline, establishes the "before → after" narrative critical for sales positioning, renewal justification, and case study creation.

---

### Q45: Why is Job (JTBD) a standalone entity rather than a field on User Persona?

Jobs are reusable across Personas — an AP Clerk and a Treasury Analyst may share the job "Verify FX rate applied." A field on Persona would duplicate this shared job. More importantly, Job is the structural bridge between three dimensions: user intent (Dim 4 — Persona has Job), product structure (Dim 8 — Job is enabled by Value Stream / Capability), and buyer justification (Dim 3 — Job contributes to Business Outcome). Without a standalone entity, these cross-dimensional relationships have no anchor. Job also gives User Journey its purpose — a Journey *accomplishes* a Job; without the Job entity, "why does this Journey exist?" has no formal answer. See DR-020.

---

### Q46: Why deprecate Touchpoint from the Definition Model?

Touchpoints (specific UI elements — buttons, dropdowns, forms) are implementation-level artifacts that change with every sprint. The Definition Model captures structural product truth — entities that persist across releases. Touchpoints are below this waterline. They belong in Build Track work artifacts: PSDs specify UI behavior for a module, Prototypes validate journey flows, and design specifications detail UI component inventories. The Definition Model captures down to **User Journey** (a named, purposeful flow); everything below is work artifact territory. This keeps the model maintainable — no team would sustain an entity catalog of individual buttons and dropdowns. See DR-020.

---

### Q47: How does UX Channel relate to Human-Interactive Module (Dim 8)?

One-to-one. A UX Channel is the experiential definition (Dim 4) — "through what medium does the user access the product?" A Human-Interactive Module is the structural realization (Dim 8) — "what bounded technical context delivers that channel?" Each Channel is implemented by one HI Module; each HI Module implements one Channel. The module archetype taxonomy already defines Human-Interactive as an interaction boundary; UX Channel refines it with two sub-axes: Interaction Modality (Web, Mobile, Chat, Voice, Email, CLI) and Engagement Mode (Self-serve, Assisted, Managed). The Channel carries experiential characteristics and Journey references; the HI Module carries Capabilities, Features, and technical implementation. See DR-020.

---

### Q48: Why two axes for UX Channel (Interaction Modality × Engagement Mode)?

Because they are orthogonal. A Web channel can be Self-serve (customer dashboard), Assisted (co-browsing with support agent), or Managed (agent acts on behalf of customer). A Chat channel can be Self-serve (chatbot) or Assisted (live agent). The Modality axis captures *technology constraints* (screen size, synchronicity, input method). The Engagement Mode axis captures *service model* (who acts — user alone, user + agent, agent on behalf of user). Each combination produces distinct UX constraints, Win Track implications, and HI Module requirements. A product defines which cells in this matrix it occupies; most products serve a subset. See DR-020.

---

### Q49: How is multi-channel journey continuity modeled?

Two lightweight mechanisms, both as reference fields on User Journey: (1) **Journey Equivalence** — references to journeys in other channels that accomplish the same Job. "Initiate and approve payout" (Web) is equivalent to "Approve payout" (Mobile) — same Job, different channel, user picks one. (2) **Journey Continuity** — references to journeys in other channels that this journey can hand off to or receive from. "Request payout approval" (Email) is continuable to "Approve payout" (Mobile) — user starts on email, finishes on mobile. Both are simple reference fields — no unified cross-channel flow model, no new entities. The Definition Model doesn't model the cross-channel handoff mechanism (that's implementation); it records that the possibility exists. See DR-020.

---

### Q50: How does Job map to Value Stream vs. Capability (Dim 8)?

Both relationships exist at different granularity levels. Job → Value Stream is the primary structural mapping: "Process a cross-border payout" maps to the "Cross-Border Payout Processing" Value Stream. A Value Stream may serve multiple Jobs across different Personas (AP Clerk processes, Treasury Analyst verifies, Compliance Officer audits — same stream, different jobs). Job → Capability is a direct mapping for simpler jobs that don't require a full end-to-end flow: "Check my FX rate lock status" → "Automated Rate Locking" Capability. Since Value Stream already traverses Capabilities, Job → Capability is derivable from Job → Value Stream → Capability. But direct Job → Capability links are useful for capability-scoped jobs that don't involve cross-module flows. Both are many-to-many. See DR-020.

---

### Q51: Why is "Embedded" an Interaction Modality rather than a Dim 6 (extensibility) concern?

A component being technically embeddable (iframe, SDK, web component) is a Dim 6 / Build Track concern. But a product *deciding* that certain journeys should be embeddable in customer or third-party applications is a channel-level strategic decision. It requires its own HI Module, its own journey design (fragment, not full flow), and its own UX constraints (vendor controls the component, not the host page; must be self-contained). "Payment Widget" is a UX Channel — typed as Embedded + Self-serve — just as "Customer Dashboard" is typed as Web + Self-serve. Both are product access mechanisms; Embedded ones happen to be hosted in someone else's application. The Dim 6 extensibility dimension captures the *programmatic interface* that delivers the embeddable component (API, SDK); the Dim 4 Channel captures the *experiential surface* the user interacts with. See DR-020.

---

### Q52: Why does User Journey reference both Value Stream and Capability (Dim 8)?

Value Stream traversal tells you "which end-to-end flow does this journey follow?" — it's the broad structural mapping. Capability engagement tells you "which specific product abilities are required at each step?" — it's the finer-grained mapping. Both are valuable for different analyses. If a Capability changes (e.g., "OFAC Screening" adds new required fields), Value Stream traversal alone doesn't tell you which Journeys are affected. Capability engagement directly answers: "Initiate and approve a payout" and "Generate compliance audit report" both engage OFAC Screening — both need journey review. Value Stream traversal identifies the flow; Capability engagement identifies the structural dependencies within the flow.

---

### Q53: Why are Developer Persona and Programmatic User Persona in Dim 6 rather than Dim 4?

Dim 4 and Dim 6 represent fundamentally different interaction paradigms. Dim 4 is visual/experiential — its vocabulary (Journey, Channel, Touchpoint, experience attributes) describes how humans navigate a product's UI. Dim 6 is programmatic/contractual — developers read docs, write code, test in sandboxes, iterate over days. Programmatic User Personas are non-human systems (customer's ERP, partner middleware) with throughput requirements and SLA expectations — they cannot meaningfully carry Dim 4 fields like "Frustrations" or "Preferred Channel." The same human may appear in both dimensions: an Integration Engineer is a Dim 4 Persona when using the Developer Portal and a Dim 6 Developer Persona when writing API integration code. This correctly reflects two interaction surfaces with different design concerns. See DR-021.

---

### Q54: Why is extensibility a deliberate product strategy, not an incidental API property?

Every distributed module has internal APIs. If every module with an API appeared in Dim 6, the dimension would flood with implementation detail. Dim 6 exists only when there is a deliberate, demand-driven strategy to make capabilities externally consumable for well-understood use cases. "Our module has REST APIs" is Dim 5/Dim 8. "We will design, build, and maintain a Payments API surface for customers integrating payment processing into their ERP systems" is Dim 6. The distinction is demand-driven (ecosystem need, PDR-level decision) vs. supply-driven (architecture happenstance). See DR-021.

---

### Q55: Why are Dim 6 modules structurally Dim 8 modules rather than a parallel hierarchy?

A Dim 6 API Module is a Dim 8 module — it sits in the Product → Module → Capability → Feature hierarchy, has a bounded context, archetype, Dim 5 internals, and Build Track versioning. Creating a separate Dim 6 hierarchy would duplicate relationship management and obscure the compositional link between Dim 6 surfaces and underlying Dim 8 capabilities. What makes a module a "Dim 6 module" is its purpose (external extensibility), its composition pattern (curating capabilities from other modules), and its specialized concerns (Developer Personas, API contracts, versioning commitments). This parallels Dim 4: Human-Interactive modules are Dim 8 modules carrying Dim 4 concerns. See DR-021.

---

### Q56: Why three core module types (API, Extension, SDK) plus Integration Module, rather than a single "API Product" entity?

Each type represents a genuinely different product decision. API Module is a protocol-agnostic programmatic surface (REST, batch/SFTP, Kafka, webhooks, gRPC, GraphQL are all delivery mechanisms within one module). Extension Module provides a plugin/hook framework for third parties to extend product behavior (sandboxing, permission model, marketplace). SDK/Library Module wraps API surfaces in language-specific idioms (dependency management, code generation, testing support).

Integration Module was initially defined as "APIs bundled for a scenario," which overlapped heavily with API Module. The sharpened distinction: Integration Module is a **pre-built bridge/connector** between the product and a specific external system or system category (e.g., "SAP Connector," "Salesforce Adapter," "ERP Integration"). It includes data mappings, protocol translations, and workflow adapters — not just "our APIs" but "the glue between us and your system." If a product doesn't ship connectors to specific external systems, it has API Modules but no Integration Modules. Collapsing all types into one entity would lose distinctions that drive architecture, documentation, governance, and versioning strategy. See DR-021.

---

### Q57: How does Client-Distributed deployment topology differ from Vendor-Hosted?

Vendor-Hosted modules (monolith or distributed microservices) are deployed and operated in the vendor's infrastructure. Client-Distributed modules are built by the vendor but deployed in the consumer's environment — mobile apps (app stores → user devices), PWAs (CDN → user browsers), SDKs (package registries → customer codebases), CLI tools (package managers → developer machines), embedded widgets (CDN → customer web apps). Both are structurally valid Dim 8 modules with full entity structure (Capabilities, Features, Dim 5 internals, Build Track versioning). Their Dim 7 (Operational) footprint differs: CI/CD + distribution channel + version adoption tracking rather than clusters and containers. See DR-021.

---

### Q58: Why a unified API Operation entity rather than separate Endpoint and Event entities?

Both endpoints and events are named, versioned, contractual commitments belonging to an API Module, consumed by the same Developer and Programmatic User Personas, subject to the same API Compatibility Contract. The boundary blurs in practice: a "Create Payment" submitted via Kafka is a command message; a "payment.settled" status retrieved via polling is a query. The transport mechanism makes the endpoint/event distinction a protocol concern, not a structural one. A single entity with a pattern classification (Command, Query, Event, Callback, Batch) preserves the analytical distinction — "what events do we publish?" is a pattern filter — while keeping one entity, one relationship set, one place in the Module → Operation hierarchy. This parallels Win Case (subtypes: Query, Service Request, Complaint, Escalation) and Signal (subtypes: Problem, Need, Opportunity). See DR-021.

---

### Q59: Why SLOs on API Operations rather than Payload Schema in the Definition Model?

Payload Schema (specific field definitions for request/response payloads) follows the same granularity pattern as Touchpoints in Dim 4 — it changes frequently with each version and belongs in PSD/Build artifacts. SLOs, by contrast, are strategic commitments: "Create Payment has p99 < 500ms and 99.95% availability" is a product promise that drives architecture, capacity planning, pricing tiers, and customer contracts. SLOs are the Dim 6 analog of experience attributes in Dim 4 — the qualitative (or quantitative) promise about what consumers can expect. They connect richly to Customer Promise (Dim 3) via SLAs, API Compatibility Contract (performance stability across versions), and Win Monitoring (SLO compliance tracking). The Definition Model captures what the product commits to; the schema details live below the waterline. See DR-021.

---

### Q60: Why is Batch a distinct interaction pattern alongside Command, Query, Event, and Callback?

Batch operations have genuinely different SLO profiles, error semantics, and consumer workflows from per-request interactions. SLOs focus on processing window and throughput rather than per-request latency. Error handling involves partial success, rejection reports, and reconciliation — not atomic success/failure. Consumer workflow is multi-step (prepare → upload → wait → download results), not request-response. Batch has natural bidirectionality: inbound (consumer submits bulk data) and outbound (product generates bulk reports). Treating batch as "many Commands bundled" would misrepresent these differences and leave batch SLOs unmodeled. See DR-021.

---

### Q61: Why is Integration Module a connector/adapter rather than another API surface?

The original proposal defined Integration Module as "APIs bundled for a scenario," which overlapped heavily with API Module (both use-case-oriented, both compose from Dim 8 modules, both expose programmatic interfaces). The sharpened distinction: Integration Module is a **pre-built bridge** to a specific external system — it includes data mappings, protocol translations, workflow adapters, and connectors between the product's model and the target system's model. API Module says "here's our interface"; Integration Module says "here's a ready-made bridge between us and SAP/Salesforce/your ERP." The design concerns diverge: data format translation, protocol bridging, polling vs. push, conflict resolution, target-system-specific error handling. If a product doesn't ship connectors, it has API Modules but no Integration Modules. See DR-021.

---

### Q62: Why a dedicated Evolve Track instead of per-track evolution entities?

Each track already has monitoring entities (Signal Monitoring, Build Monitoring, System Monitoring, Win Monitoring), but these monitor *domain outcomes* — signal pipeline health, build quality, system uptime, customer health. They do not monitor *process effectiveness* — whether entity definitions serve their purpose, whether DoD criteria are followed, whether artifacts meet quality standards. Process evolution also crosses track boundaries: a poorly defined PSD (Discovery Track process issue) causes build failures (Build Track symptom); a missing Feedback promotion path (Win Track process issue) means customer insights never reach Discovery. A dedicated Evolve Track can assess the whole system, not just one track's domain health. Per-track evolution entities would fragment this cross-cutting concern. See DR-022.

---

### Q63: Why is Track 5 called "Evolve" and not "Process" or "Improve"?

"Evolve" parallels the active-verb naming pattern of existing tracks — Discovery (discover), Build (build), Run (run), Win (win), Evolve (evolve). "Process" is a noun describing *what* is evolved, not *what the track does*. "Improve" implies the current state is always deficient; "Evolve" acknowledges that process changes may be *adaptations* to new circumstances (new product dimensions, new organizational structures, market shifts) rather than corrections of deficiencies. Evolution is neutral — it includes refinement, extension, deprecation, and restructuring. See DR-022.

---

### Q64: How does the Evolve Track connect Work Model and Operating Model?

Tracks 1–4 produce outputs that modify the Definition Model (Modeling Task updates Dims 2–9, Specification Task produces PSDs) or external systems (Deployment deploys to infrastructure, Win Activity updates CRM). Track 5 is the only track whose outputs directly modify the Work Model itself (entity definitions, artifact types, DoD criteria, assessment criteria) AND the Operating Model (guidance structures, ceremony definitions, role descriptions). This makes Track 5 the structural bridge between the two models — the mechanism by which the three-model architecture (Definition → Work → Operating) stays coherent as it evolves. The bridge relationship is real; the structural form is a track. See DR-022.

---

### Q65: Why assessment criteria on artifact types rather than just Definition of Done?

DoD defines when a *work entity* is complete — "this Deliberation is done when a PDR is produced and stakeholders have acknowledged." Assessment criteria define what makes a *specific artifact* good — "a PDR must include alternatives considered, consequences stated, and affected dimensions identified." These are complementary but distinct: DoD ensures the right artifacts are produced; assessment criteria ensure those artifacts are produced *well*. Without assessment criteria, a team can satisfy DoD (produce a PDR) while producing a poor artifact (a PDR with no alternatives considered). Assessment criteria close this gap. They belong in the Work Model (as properties of the artifact type) rather than the Operating Model (as team practices) because a poorly reasoned PDR is poor regardless of which team produced it. See DR-022.

---

### Q66: Why does Dim 7 need its own Operational Persona, Job, and Journey instead of widening Dim 4?

Dim 4 is the "User-Centric Dimension" — it models the *customer's* experience. Dim 7 is the "Operational Dimension" — it models the *vendor's* infrastructure reality. They share the same analytical pattern (persona → job → journey → module) but serve different domains with different stakeholders, concerns, quality criteria, and relationships. Operational Job connects to SLOs and Run Track work; JTBD connects to Business Outcomes and Value Streams. Merging them would dilute both: Dim 4's user-centric focus would absorb operational concerns it doesn't own, and operational jobs would lose their connections to Operational Targets and Deployment Environments. This follows the same principle that keeps Delivery Friction (Dim 2) independent from Pain (Dim 3) and Developer Persona (Dim 6) independent from User Persona (Dim 4). Structural parallels inform design but do not create shared entities. See DR-023.

---

### Q67: Why is Tenant a Run Track work entity rather than a Dim 7 Definition Model entity?

A Tenant is something that is provisioned, configured, monitored, scaled, and eventually decommissioned — it is the result of operational work, not a structural definition. The Definition Model captures "what the product IS" (including that it supports multi-tenancy, via Tenancy Architecture on Infrastructure Model and Deployment Environment). The Run Track captures "what work EXISTS" to create and manage individual tenants within that architecture. This follows the standard Definition → Work separation: Dim 8 defines Capability, Build Track implements it; Dim 2 defines Win Outcome, Win Track achieves it; Dim 7 defines Deployment Environment with Tenancy Architecture, Run Track manages Tenants within it. Additionally, Tenant carries the customer-facing purpose (Production, UAT, Sandbox), cleanly separating it from the environment's vendor purpose — a design that requires Tenant to be a distinct operational entity, not a field on the Definition Model's Deployment Environment. See DR-023.

---

### Q68: Why is Operational Quality a taxonomy not an entity set?

Reliability, Performance, Security, Compliance, Cost Efficiency, Observability, Scalability — initially proposed as standalone "Operational Quality Attribute" entities. Reconsidered because they are a categorization framework, not individual entities with fields, statuses, and lifecycles. The parallel is AAARRR in Dim 2: Awareness, Acquisition, Activation, Retention, Revenue, Referral are not individual entities — they are a classification axis used to type Win Outcomes, Win Stakeholders, and Business KPIs. Similarly, the quality taxonomy types Operational Targets (Availability SLO, Cost SLO), Operational Personas (Reliability Operator, Security Operator), Operational Constraints (Compliance Boundary, Security Standard), and Operational Pains (by quality domain). The vocabulary appears as enumerated types on entities, not as standalone rows. See DR-023.

---

### Q69: Why does Operational Target carry Achievement Levers?

Without achievement levers, Operational Targets exist in isolation — "99.99% availability" is a number without a strategy for achieving it. Achievement Levers (Product or Operational) force the question at modeling time: "Is this primarily a product engineering problem (build circuit breakers, improve error handling) or an operational problem (add redundancy, improve incident procedures), or both?" This parallels Win Outcome (Dim 2), which carries Achievement Levers from the Business Model's Lever Portfolio. Making Operational Targets lever-aware connects Dim 7 into the Initiative/Objective planning cycle: an Initiative with Operational lever weight drives Run Track and Operating Model work to improve operational targets; Operational Pains feed the Signal pipeline, driving Initiatives with appropriate lever mixes. Without this connection, operational improvements happen outside the strategic planning framework. See DR-023.

---

### Q70: What is the relationship between Dim 7 Operational Target, Dim 6 API Operation SLOs, and Dim 3 Service Commitment?

Three layers of the same commitment, progressively more specific: **Service Commitment (Dim 3)** is the customer-facing SLA — "99.9% uptime" promised in the contract. **API Operation SLO (Dim 6)** is the per-operation target — "Create Payment: 99.95% availability, p99 < 500ms" committed to Developer and Programmatic User Personas. **Operational Target (Dim 7)** is the infrastructure-level objective — "payments-service compute availability 99.99% in Production US-East" that backs both higher layers. Each layer has different owners (Commercial/PM → API/Platform → SRE/DevOps), different measurement points (contract → API gateway → infrastructure), and different remediation paths. The Definition Model captures all three as distinct entities with explicit "backs" relationships. Actual measured values are operational state tracked by System Monitoring (Track 3). See DR-023.

---

### Q71: Why deprecate Cluster/Host and Container/Process?

Cluster/Host and Container/Process are at a specific technology level (Kubernetes clusters, Docker containers) that may not apply universally, and they lacked strategic framing — no relationships, no fields, no lifecycle. By the same waterline logic that deprecated Touchpoint (Dim 4) and Payload Schema (Dim 6): the Definition Model captures strategic operational decisions (environments, targets, constraints, readiness); specific compute infrastructure choices (cluster sizing, container configuration, pod specs) belong in PSD/Run Track artifacts. The expanded Deployment Environment entity captures the strategic infrastructure decisions that Environment originally hinted at; the specifics of how compute is organized within an environment are work artifacts. See DR-023.

---

### Q72: How are infrastructure cost targets modeled?

Cost is modeled through three complementary entities rather than a dedicated FinOps entity: **Infrastructure Model** carries a Cost Model field — the overall cost strategy (reserved instances, spot, committed spend, cost allocation approach). **Operational Target** of type Cost sets specific targets — "infrastructure cost per 1K transactions < $0.50" or "cloud spend growth must not exceed 1.5x traffic growth." **Operational Pain** surfaces cost suffering — "cloud spend grew 3x while traffic grew 1.5x, $200K/month over budget." This connects to Dim 2: Business KPI of type Cost includes "Infrastructure Cost per Customer" — the commercial view of the same cost reality. The Dim 7 Operational Target (Cost) is the infrastructure-level objective; the Dim 2 Business KPI (Cost) is the commercial-level metric derived from it. See DR-023.

---

### Q73: Why Operational Readiness at System scope rather than in Evolve Track?

Evolve Track (Track 5) assesses *process* effectiveness: "Are our entity definitions serving their purpose? Are DoD criteria followed? Are artifacts meeting quality standards?" Operational Readiness assesses *System* readiness: "Is this System ready for production in this environment?" Different scope (System vs. process), different assessors (Run Track ops team vs. Process Leads), different triggers (deployment planning vs. quarterly review cycles), different criteria (observability, security, performance vs. DoD compliance, artifact quality). Operational Readiness criteria are a Definition Model concern because "what makes a System production-ready" is a product-level standard — it applies regardless of which team operates it. The assessment work (evaluating a specific System against criteria) is Run Track activity. Module-level readiness ("is the Payments capability ready?") is a derived view that aggregates across constituent Systems. See DR-023, DR-026.

---

### Q74: Why reframe Dim 5 from code structure to technical model?

The original Dim 5 entities (Subsystem/Service, Class/Component, Function/Method) mapped to C4 architecture levels but at the wrong abstraction for the Definition Model. Code-level structure (classes, functions) is below the waterline — same principle that deprecated Touchpoint (Dim 4), Payload Schema (Dim 6), and Cluster/Host (Dim 7). Meanwhile, the product's actual technical model — its architectural strategy, systems, technology choices, dependencies, and interaction flows — had no representation. The reframe elevates Dim 5 from "how the code is organized" to "how the product is architected" — the right level for a Definition Model that captures strategic technical decisions, not implementation details. See DR-024.

---

### Q75: What is the Dim 8 / Dim 5 duality and why does the model need both?

Dim 8 (Structural/Topology) provides the *functional* view: Product → Module → Capability → Feature, with Value Streams flowing horizontally. Dim 5 (Technical & Architectural) provides the *technical* view: Architecture Model → System → Component, with Interaction Flows showing how Systems communicate. Same product, two lenses, different audiences. Dim 8 serves PM and business stakeholders ("the product has a Payments Module with Cross-Border Payments capability"). Dim 5 serves architects and engineering leadership ("Payments is implemented by payments-service in Java/Spring Boot, communicating via Kafka events, depending on PostgreSQL"). Neither is complete without the other — Dim 8 alone can't answer "which systems need to change to add this capability?" and Dim 5 alone can't answer "what business capabilities does this system serve?" The explicit many-to-many mapping between them makes this relationship traceable. See DR-024.

---

### Q76: Why is System-to-Module mapping many-to-many?

Functional decomposition (Modules — what the product does) and technical decomposition (Systems — how the product is built) are independent. A Dim 8 Module "Payments" may be implemented by multiple Systems (payments-api, payments-processor, payments-scheduler — different deployment units serving one functional domain). A shared Dim 5 System (notification-service) may serve multiple Modules (Payments, Compliance, Onboarding — one technical service supporting many functional domains). Forcing 1:1 alignment would either fragment Modules into too-granular functional units (creating a "Notification Module" just because a notification-service exists) or bloat Systems into monolithic technical units (cramming all payments logic into one service). The many-to-many mapping reflects reality and enables impact analysis in both directions. See DR-024.

---

### Q77: Why ADR as a separate entity from PDR?

PDR (Dim 1) captures *product* decisions: "Go on LATAM market," "Add mobile channel," "Adopt event-driven architecture" (when the decision is product-strategic). ADR (Dim 5) captures *technical/architectural* decisions: "Use PostgreSQL for transactional data," "Split payments monolith into three services," "Adopt OpenTelemetry for tracing." Different dimensions (Dim 1 vs. Dim 5), different audiences (PM vs. architect), different governance (product deliberation vs. architecture review), different lifecycles (PDR: Draft → Final → Superseded; ADR: Proposed → Accepted → Deprecated → Superseded). They cross-reference each other: PDR triggers ADR(s) when product decisions have architectural implications; ADR constrains PDR when architectural reality limits product options. Together they provide full decision traceability from product strategy through technical implementation. Merging them would overload PDR with technical detail and dilute its product-level focus. See DR-024.

---

### Q78: Why are technology choices fields rather than standalone entities?

A technology choice has two parts: WHAT was chosen (the technology) and WHY it was chosen (the rationale). The "what" naturally lives as fields on System and Component — language, framework, runtime, data store, protocols are properties of the technical unit. The "why" naturally lives in ADRs — the decision record explains the context, alternatives considered, and trade-offs. A standalone "Technology Choice" entity would duplicate both: it would restate the technology (already on the System) and the rationale (already in the ADR). The UPIM avoids entities that don't carry their own independent fields, statuses, and lifecycle. Technology stack fields make choices visible; ADRs make the reasoning traceable. See DR-024.

---

### Q79: Why deprecate Subsystem/Service, Class/Component, Function/Method?

Subsystem/Service is subsumed by the expanded System entity — same concept (deployable technical unit) but with technology stack fields, many-to-many Module mapping, Deployment Environment reference, and a full relationship set. Class/Component (code-level classes and modules) and Function/Method (executable code blocks) are below the Definition Model waterline by the same logic that deprecated Touchpoint (Dim 4), Payload Schema (Dim 6), Cluster/Host (Dim 7), and Container/Process (Dim 7). The Definition Model captures strategic technical decisions visible in architecture diagrams; code-level structure belongs in PSD specifications and Build Track artifacts. The new Component entity (Dim 5) replaces Class/Component at the architectural level — significant building blocks within Systems (processing engines, adapters, rule evaluators), not code-level classes. See DR-024.

---

### Q80: Why Technical Knowledge Base as a per-System assessment?

Documentation gaps are operational and commercial risks. A System with no runbook means the Run Team relies on tribal knowledge for incident response. A System with stale integration guide means the Win Team gives prospects inaccurate technical information. Making these gaps visible in the Definition Model (rather than as implicit Work Model concerns) gives them strategic weight. The per-System assessment pattern parallels Operational Readiness (Dim 7, per-System × per-Environment): both are single-instance-per-scope assessments with quality dimensions and coverage status. Technical Knowledge Base covers knowledge dimensions (architecture docs, runbooks, release notes, integration guides, Win technical guides, troubleshooting playbooks); Operational Readiness covers operational dimensions (observability, security, performance, operability, DR, compliance). The actual documents are Work Model artifacts — Build Track produces them, Run Track and Win Track consume them. Technical Knowledge Base tracks "does the knowledge exist and is it current?" — an assessment, not the knowledge itself. See DR-024.

---

### Q81: Why introduce ODR as a separate decision record from PDR and ADR?

PDR (Dim 1) captures product strategy decisions; ADR (Dim 5) captures architectural/technical decisions; ODR (Dim 7) captures operational/infrastructure decisions. Each has a different audience (PM vs. architect vs. SRE), different governance (product council vs. architecture review vs. operations review), and different scope (what to do vs. how to build vs. how to run). Operational decisions like "choose AWS MSK over self-managed Kafka," "archive transaction data to Glacier after 24 months," or "adopt blue-green deployment for payment services" don't fit in PDR (not product strategy) or ADR (not architecture design-time). They are operational, runtime decisions with their own context, alternatives, and consequences. The three-record triad provides complete decision traceability across the product lifecycle. See DR-025.

---

### Q82: What is the PDR → ADR → ODR trigger chain?

Decisions cascade across levels, each refining the previous with domain-specific expertise. "Go on LATAM market" (PDR) triggers "Deploy LATAM services in sa-east-1 with event-driven architecture" (ADR) triggers "LGPD-compliant encryption, MSK 3-AZ, dedicated tenancy for Tier-1 banks, 4-hour RTO" (ODR). The chain also works in reverse as constraints: an ODR ("4-hour RTO") constrains ADR choices ("active-active isn't justified"), and an ADR ("batch architecture") constrains PDR options ("can't offer real-time FX"). Each record type has four relationship patterns: triggered by upstream, exists independently, triggers downstream, constrains upstream. See DR-025.

---

### Q83: Why do data governance and archival decisions belong in ODR (Dim 7) rather than Dim 9?

Dim 9 (Data & Information, to be detailed) will capture the structural/domain view of data — what data the product manages and makes available, domain boundaries, ownership, schema, relationships. ODR captures the operational aspects — retention periods, archival policies, encryption requirements, access control models, backup strategies. These are runtime decisions about how data is governed, not structural decisions about what data exists. The split mirrors the Dim 8 / Dim 5 pattern: Dim 8 defines functional structure, Dim 5 defines technical realization. Similarly, Dim 9 will define data structure, ODR governs data operationally. See DR-025.

---

### Q84: Why does ODR have dual provenance (Discovery Track + Run Track)?

Some operational decisions are strategic and planned: cloud provider selection, tenancy architecture, initial DR strategy — these originate from Discovery Track Deliberations during product strategy work. Other operational decisions emerge from operational experience: changing deployment strategy after incident patterns, increasing data retention after regulatory change, adjusting capacity after load testing — these originate from Run Track work. Both paths produce the same Dim 7 entity; provenance is tracked through relationships. This gives the Run Track its own decision-making capability, paralleling Build Track's ADR production (DR-024). Previously, only Discovery (PDR) and Build (ADR) tracks formally produced decision records. See DR-025.

---

### Q85: Why are Epics Module-scoped (Dim 8) and Technical Tasks System-scoped (Dim 5)?

This reflects how work is actually planned and implemented. PMs and Tech Leads plan at the Module level ("Build the FX Rate Locking feature for the FX Module") — Modules are functional boundaries meaningful to product stakeholders. Developers implement at the System level ("Implement gRPC endpoint in fx-service") — Systems are deployable technical units meaningful to engineers. The Module-to-System many-to-many mapping means a single Story (Module-scoped) may spawn Technical Tasks in multiple Systems. This is natural: a functional increment ("lock FX rate for 24 hours") often requires changes in several Systems (fx-service for rate locking, payments-service for rate lock client, Redis for TTL). Stories bridge the two: they speak Module language but are implemented by System-scoped Technical Tasks. See DR-026.

---

### Q86: Why three-tier versioning (System Version → Module Version → Product Version)?

The original two-tier model (Module Version → Product Version) had two problems. First, "Module Version" was misnamed — the Build Track builds Systems (Dim 5), not Modules (Dim 8). `payments-service v2.3.3` is a System Version. Second, there was no integration verification layer between individual System Versions and the full Product Version. The three-tier model addresses three distinct needs:

**Verification and deployment scope:** (1) Systems are built and deployed independently as System Versions via SDDs (atomic deployment unit); (2) Systems within a Module are verified to work together as Module Versions and deployed as Module Packages via MDDs (integrated deployment unit); (3) the full product composition is certified as a Product Version and deployed as a Product Package via PDDs (complete deployment unit). All three tiers are deployable at their composition level. Module-scoped verification is O(k) within a Module rather than O(n²) across all Systems.

**Composite system nature:** Each tier is a system in its own right. Module Version is a composite system with emergent properties (end-to-end latency, integrated failure modes, cross-system data consistency) that do not exist at the individual System level. Product Version is a higher-order composite system with product-level emergent properties (end-to-end user journeys, cross-module workflows, product-wide compliance posture). All three tiers are operable and observable — they are not verification checkpoints.

**Communication bridge:** Each tier provides a shared vocabulary at progressively broader organizational scope. System Version is the Build+Run vocabulary (engineers + SREs). Module Version bridges Build+Run+Product — PMs reason in Modules ("Payments capability v4.1"), SREs monitor integrated capability health, Build teams know which Systems compose it. Product Version is the ubiquitous language across all teams and customers — Win teams, compliance, and customers all reference "Product v3.2." Without these tiers, cross-functional teams resort to ad-hoc translation between service names, feature names, and marketing labels.

See DR-026. See also `stories/versioning-alternatives-analysis.md` for how alternative approaches (monorepo, contract testing, GitOps, release trains) address these challenges and where they leave gaps.

> **DR-029 update:** Module Package → Module Package Version; Product Package → Product Package Version (Work Model artifacts). Deployment is refactored as an artifact produced by Deployment Task. See DR-029.

---

### Q87: Why are Integration Epic and Integration Story separate entities from regular Epics and Stories?

Integration work has fundamentally different characteristics from feature work: it spans multiple Systems (potentially from different Modules), it validates Interaction Flows (Dim 5) end-to-end, and it produces integration contracts and test suites rather than feature code. Conflating integration work into feature Epics hides the cross-cutting nature from planning — integration "issues" surface late and delay releases. Separate entities make integration work visible from Release Planning onward. Integration Epics reference the PSD-derived Epics/Stories they integrate, maintaining traceability to feature work. The integration output (verified contracts, test suites) feeds Module Version verification. See DR-026.

---

### Q88: Why is Design Deliberation distinct from Discovery Track Deliberation?

Both produce ADRs, but the scope and context differ. Discovery Track Deliberation is strategic — it addresses questions that shape the product's direction ("should we adopt event sourcing?", "should we support multi-currency?") and may produce PDRs, ADRs, or ODRs. Design Deliberation is tactical — it addresses questions that arise during implementation ("should we use gRPC or REST for this specific service-to-service call?", "how should we handle cache invalidation?"). Design Deliberation makes architectural decision-making during build work explicit and traceable. Without it, implementation-time ADRs have no structured origin — they exist but "came from nowhere." The ADR entity (Dim 5) is the same regardless of provenance; the deliberation process differs. See DR-026.

---

### Q89: Why is Technical Debt a work artifact, not a work entity?

Technical Debt Items are *things produced by work* — documentation of accumulated shortcomings discovered during development. They are not *work to be done* in themselves. When debt is prioritized for resolution, it is addressed through existing work entities: an Epic (if the debt is significant, e.g., "migrate from synchronous to async bank integration") or a Story (if the debt is contained). This prevents proliferating work entity types — debt resolution uses the same planning and tracking mechanisms as feature work. The artifact captures the debt's existence, category, impact, and resolution path; the Epic/Story captures the resolution work. See DR-026.

---

### Q90: Why does Bug have a provenance field (Build / Run / Win)?

Bugs originate from three distinct sources, and each source implies different traceability needs. Build-provenance Bugs are found during development (unit testing, code review, Story implementation) — they trace to Stories and Technical Tasks. Run-provenance Bugs originate from production Incidents — they trace to Incident records (Track 3), enabling "how often do incidents produce bugs?" analysis. Win-provenance Bugs originate from customer complaints or escalations in Win Cases (Track 4) — they trace to Win Case records, enabling "how often do customer complaints reveal product defects?" analysis. Without provenance, all three categories are indistinguishable, and cross-Track feedback loops are broken. See DR-026.

---

### Q91: Why rename "Interaction Pattern" to "Interaction Flow" (Dim 5)?

"Pattern" connotes an abstract, reusable template — something you *could* apply. But the entity's structure (ordered steps, source-to-target Systems, protocols, timeouts, error handling) describes concrete, sequential execution: *what actually happens* when a Value Stream is technically realized. "Flow" conveys committed motion, not abstract possibility. It also creates clean linguistic symmetry: Value Stream (Dim 8) describes the functional flow; Interaction Flow (Dim 5) describes the technical flow. Same motion, different lens. The Dim 6 concept of "interaction pattern" (Command, Query, Event, Callback, Batch) — used for API Operation classification — is unaffected; that usage describes the *style* of a single operation, not a multi-System execution path.

---

### Q92: Why do Epics/Stories feel like specification entities while Technical Tasks feel like execution entities?

Because the Build Track naturally contains two layers. The **specification/commitment layer** — Epics, Stories, Integration Epics, Integration Stories — defines *what* to build in Module (Dim 8) language. These entities carry product intent (decomposed from PSDs), acceptance criteria, and Module-scoped scope. They are defined and prioritized by PMs and Tech Leads. The **execution layer** — Technical Tasks — defines *how* to implement in System/Component (Dim 5) language. These entities are assigned to individual developers, scoped to specific Systems, and speak engineering language (write code, write tests, configure infrastructure).

This two-layer structure is a strength, not a deficiency. Story sits at the junction: it speaks Module language ("lock FX rate for 24 hours") but decomposes into System-scoped Technical Tasks ("implement rate-lock endpoint in fx-service," "add rate-lock event to Kafka topic," "write integration test for rate-lock timeout"). The layer boundary is where functional specification meets technical execution. Note that the two layers are *not* separate tracks — they are both within the Build Track. The specification layer narrows PSDs into committed scope; the execution layer implements that commitment through engineering work. See DR-027 (C8).

---

### Q93: How do we distinguish System, Module, and Product as "systems"?

Through **Composition Levels** — a formal hierarchy of deployable systems:

| Composition Level | Entity | What it is | Deployment Granularity |
|---|---|---|---|
| **Atomic** | System (Dim 5) | An independently buildable, deployable, operable technical unit | System Version → deployed via SDD |
| **Integrated** | Module (Dim 8) | A composite system of Systems with emergent operational properties | Module Package → deployed via MDD |
| **Complete** | Product | The highest-order composite system of Modules | Product Package → deployed via PDD |

"System" without qualification always refers to the Dim 5 atomic level — the System entity. When we say "Module Version is a composite system" or "Product Version is a higher-order composite system," we use "system" in the **systems-thinking sense**: a whole composed of interacting parts with emergent properties that don't exist at the constituent level. Module Version has end-to-end latency, integrated failure modes, and cross-system data consistency. Product Version has end-to-end user journeys, cross-module workflows, and product-wide compliance posture. These emergent properties make Module and Product operationally real — SREs monitor them, PMs reason about them, customers experience them.

The composition-level framing prevents confusion: Technical Tasks are scoped to **atomic** Systems (Dim 5). Module Packages are **integrated** deployment units. Product Packages are **complete** deployment units. The word "system" appears at all three levels, but each level has its own distinct entity name and composition semantics. See DR-027 (C1).

---

### Q94: Why is Module Package a separate entity from Module Version?

Because what is *deployed* includes both the tenant-serving assembly (Module Version) and operator-facing support systems (Module Package Version). Module Version is a Build Track artifact — it certifies that product System Versions integrate correctly within a Module boundary, with binding configuration that constrains the composition to its legal form. The Run Track adds operator-facing systems (custom probes, reconciliation jobs, dashboards, log shippers, cert rotation automation) and operational wiring (probe-to-system mappings, automation triggers, operational service mesh routes) to produce Module Package Version — an environment-independent deployable composition. Environment-specific configuration (monitoring thresholds, scaling policies, deployment scripts) is specified separately in the MDD (Module Deployment Descriptor), which references the Module Package and targets a specific environment. See DR-028.

Without Module Package, two things go wrong:
1. **Operational systems are invisible.** The probes, reconcilers, and automation scripts that SREs build have no composition entity. They exist as loose deployments alongside product systems, with no formal relationship to the Module they serve.
2. **Module Version becomes overloaded.** If we put operational systems on Module Version, we conflate build-time concerns (integration verification, binding configuration) with run-time concerns (operator-facing systems). Build Track produces Module Version; Run Track produces Module Package — clean ownership boundary.

The naming also reflects the semantic: Module Version is a *version* (a verified snapshot of the composition). Module Package is a *package* (an enriched, deployable bundle). Versions are verified; packages are deployed. See DR-027.

> **DR-029 update:** Module Package is now a Dim 7 specification; the Work Model artifact is renamed Module Package Version.

---

### Q95: Why does the Run Track have its own Epics and Stories?

Because the Run Track is an engineering track, not just an operational track. Custom probes, reconciliation jobs, cert rotation automation — these are legitimate Systems (Dim 5) with code, repos, CI/CD pipelines, tests, and System Versions. Building them requires the same work decomposition as product engineering: scope the work (Run Epic, Module-scoped), break it into increments (Run Story), implement with Run Track Technical Tasks scoped to operational Systems. Technical Task is a per-track concept — each engineering track owns its Technical Tasks with the same entity structure but distinct track ownership.

Run Epics mirror Build Track Epics: they are Module-scoped (Dim 8), produce System Versions, and can be planned and tracked. But they differ in three ways:
1. **Purpose.** Build Track Epics deliver product functionality (serving end-user Personas). Run Epics deliver operational capability (serving Operational Personas).
2. **Trigger.** Build Track Epics are decomposed from PSDs. Run Epics are triggered by Operational Readiness gaps, Incidents, improvement initiatives, or new Module Version readiness.
3. **Decision artifact.** Build Track Design Deliberations produce ADRs (Dim 5). Run Track Deliberations produce ODRs (Dim 7).

Without Run Epics and Run Stories, operational engineering work is informal and invisible. SRE time is conflated with incident response — there is no distinction between "operate existing systems" and "build new operational systems." This matters for capacity planning (how much SRE time goes to engineering vs. operations), for skill profiles (SREs who build operational systems need development skills), and for organizational design (should operational engineering be a separate squad or embedded within SRE?). See DR-027.

---

### Q96: Why are deployment descriptors (SDD, MDD, PDD) separate from Module Package and Product Package?

Because *what is deployed* and *how it is deployed to a specific environment* are different concerns that change at different rates. Module Package defines the composition (Module Version + operational systems + operational wiring) — this is environment-independent and changes when operational systems change. The MDD defines how that composition is deployed to a specific environment (resource sizing, monitoring thresholds, deployment scripts, runtime artifact references) — this changes when deployment configuration changes, even when the Module Package has not changed.

Without this separation, three problems arise:
1. **Version confusion.** A monitoring threshold change in production-latam is not a Module Package change (no new systems, no new wiring), but there is no entity to version deployment configuration independently.
2. **Environment coupling.** A Module Package targeting production-latam cannot be reused for production-us without creating a separate Package, even though the composition is identical.
3. **Missing deployment logic.** Pre-rollout scripts (database migrations), validation scripts (health checks), and rollback scripts (state restoration) have no structured home — they exist alongside deployments, not within a versioned specification.

The separation yields three independent version streams at the integrated level: Module Version (functional — what product code changes), Module Package (operational — what operational systems are included), MDD (deployment — how it deploys to this environment). Each evolves on its own timeline. See DR-028. See also `stories/deployment-artifacts-analysis.md` for the full four-layer model.

> **DR-029 update:** Deployment descriptors are now applied by Deployment Tasks (not Deployments). See DR-029.

---

### Q97: Why are Modules flat (no Module-within-Module nesting)?

The Product → Module → Capability → Feature hierarchy is deliberately one level deep at the Module tier. Modules are direct children of Product with no self-referential nesting. This is a structural simplicity choice with three motivations:

**Composition model clarity.** The three-tier versioning model (System Version → Module Version → Product Version) maps cleanly to the flat hierarchy: System Versions are atomic deployables, Module Versions compose System Versions within one Module, Product Versions compose Module Versions. If Modules could nest, a fourth tier would emerge (child Module Version → parent Module Version), complicating integration verification, deployment coordination, and the communication-bridge semantics that make Module Version useful across Build, Run, and Product teams.

**Decomposition discipline.** When a Module feels too large, the answer is to split it into peer Modules — not to introduce sub-modules. "Payments" containing both domestic and cross-border concerns is better modeled as two peer Modules ("Domestic Payments," "Cross-Border Payments") than as a parent "Payments" with two children. Peer Modules have independent versioning, independent integration verification, and independent Module Packages. A parent Module would need to compose its children, adding structural complexity with little informational gain.

**Grouping belongs elsewhere.** If teams need to group related Modules for organizational purposes ("the Payments domain includes Domestic Payments, Cross-Border Payments, and Settlement Modules"), that grouping belongs in the Operating Model (domain ownership, team structure) or as a lightweight tagging mechanism — not as structural nesting in the Definition Model. The Definition Model captures what the product *is*; organizational grouping captures how the org *thinks about* the product.

---

### Q98: Why is Module Package both a Definition Model entity and a Work Model artifact?

Module Package (Dim 7) is the specification/template — it defines which operational systems and wiring enrich a Module. Module Package Version (Track 3) is the versioned instance — specific System Versions assembled at a specific point in time. This follows the same Definition → Work pattern as Module (Dim 8) → Module Version (Track 2), and Product (Dim 8) → Product Version (Track 2). The specification is stable and reusable; the version is specific and changing. The specification lives in Dim 7 (not Dim 8) because package composition is an operator-facing concern (probes, dashboards, reconcilers — not tenant-serving systems), not visible to customers. See DR-029, D1-D3.

---

### Q99: Why is Deployment an artifact and not a work entity?

A Deployment records that something happened — a descriptor was applied to an environment, producing a result. It is not work to be done. The "work to be done" is the Deployment Task (Ready → Executing → Complete/Failed). The Deployment (artifact) has durable statuses (Active → Superseded → Rolled Back) that persist long after the task completes. This separation is consistent with every other track: Specification Task produces PSD (not the task itself), Research Task produces evidence (not the task itself). See DR-029, D7-D8.

---

### Q100: Why are Change Requests only for deployment-related changes?

Change Requests govern the formal change management workflow: approval → deployment planning → deployment execution → verification → completion. This workflow is specific to applying deployment descriptors to environments. Maintenance Tasks may need change management, but through different processes (they don't require Deployment Plans, Deployment Tasks, or Verification Tasks). Keeping Change Requests scoped to deployment-related changes prevents the entity from becoming a catch-all that dilutes its precision. See DR-029, D12.

---

### Q101: How does a Deployment Train relate to a Customer Release?

A single Customer Release may span multiple Deployment Trains when different modules follow different promotion paths. For example, an "LATAM Expansion" release might include payment modules on a PCI Regulated Train (72h soak, CAB approval) and a marketing portal on a Fast-Track Train (automated promotion, no soak). The Customer Release is the commercial unit; the Deployment Train is the operational promotion unit. They are associated but not constrained to a 1:1 relationship. See DR-029, D13.

---

### Q102: Why is Verification Task standalone rather than a subtype?

Verification Task is distinct from Maintenance Task (recurring/preventative), Run Track Technical Task (serves Run Stories), and Deployment Task (applies descriptors). Making it a subtype under a generic "Operational Task" would blur these distinct responsibilities. Verification Tasks produce evidence, are required for Change Request closure, and are created during Deployment Planning or added directly to Change Requests. Their lifecycle and purpose are specific enough to warrant a standalone entity. See DR-029, D9.

---

### Q103: Why is Incident a work artifact and not a work entity?

An Incident records *what happened* — unplanned service degradation. It is an observation, not a task. The work of *handling* the incident is modeled by Incident Response Task (triage-through-resolution), Post-Incident Review (structured learning), and Customer Communication Task (stakeholder communication). This parallels the Deployment pattern (DR-029): Deployment Task (work entity) produces Deployment (artifact/record). The separation enables: (1) independent assessment of what happened vs. how well the organization responded, (2) incident correlation (parent/child) at the artifact level without conflating with response work, (3) the Incident artifact as a referenceable evidence entity for SLA breach tracking, error budget consumption, and readiness assessment. See DR-030, D1.

---

### Q104: How do incidents feed back into Run Track planning?

Incident history is a first-class input to three Run Track planning entities:

1. **Deployment Planning Task** — incident history for a Module/System informs deployment risk assessment. A Module with recent SEV-1 incidents may warrant a more cautious deployment strategy (canary, drill) or may block promotion at a Station.
2. **Capacity Planning Task** — capacity-related incidents (resource saturation, throttling failures) directly inform capacity forecasting and scaling requirements.
3. **Run Epic scoping** — incident patterns inform operational engineering prioritization. "3 SEV-2 incidents from manual cert rotation" justifies an automation Run Epic without waiting for Discovery to process it as a Signal.

This is in addition to Post-Incident Review (backward-looking learning) and Discovery Track (systemic pattern recognition). Run Track planning looks forward operationally. See DR-030, D10.

---

### Q105: Why SEV-0 through SEV-4 instead of P1/P2/P3?

P1/P2 is overloaded across organizations — some use P for priority, some for severity. SEV-N is unambiguous: it labels severity specifically. SEV-0 is reserved for total service outage (all tenants affected, no workaround), providing a level above SEV-1 for catastrophic events. The Work Model defines default severity definitions; the Operating Model may refine them for the organization's context. See DR-030, D2.

---

### Q106: Who owns incident communication — Run Track or Win Track?

The Run Track owns incident communication via Customer Communication Task because SRE/DevOps has real-time technical context (blast radius, mitigation progress, ETA). Status page updates, affected-tenant notifications, and resolution summaries are produced by the Run Track. The Win Track consumes summarized or enhanced views of incidents in their regular communication routines — Win Reviews, QBRs, and proactive customer outreach. The Win Track does not duplicate incident communication; it references Run Track outputs. See DR-030, D7.

---

### Q107: How do hotfixes flow through the model?

A SEV-0/SEV-1 Incident triggers an Incident Response Task (DR-030) which may produce a Bug (provenance: Run). This Bug defaults to P0 at triage, which signals sprint-boundary bypass — the Technical Task is allocated immediately outside normal sprint capacity.

The resulting System Version uses the **Emergency gate profile** (DR-031): peer review, security scan, and smoke tests are non-negotiable; full regression, performance benchmarks, and static analysis may be deferred. The System Version is then deployed via an **Emergency-Technical Change Request** (DR-029) with abbreviated soak times and documented waivers.

The critical safeguard is the **deferred-gate obligation**: the Bug stays at `Fixed` (not `Closed`) until a subsequent Standard System Version passes all deferred gates. This prevents emergency hotfixes from permanently lowering quality standards. The full chain is: Incident → IRT → Bug (P0) → Technical Task → System Version (Emergency) → SDD → Emergency-Technical CR → Deployment Task → Deployment → Verification Task.

The hotfix branch strategy (branch from release tag, cherry-pick to main, etc.) is an Operating Model concern — the Work Model captures the `Git Reference` on System Version but does not prescribe branching.

---

### Q108: Why is FIR a work entity and not a work artifact?

FIR has a lifecycle (Created -> Triaged -> In Progress -> Resolved -> Closed), is triaged by the Win team, and actively routes work to other tracks. The triage decision is substantive work — determining "this customer report is actually a service degradation + a product gap" requires investigation, correlation with monitoring data, and routing decisions. This is work entity behavior, not artifact behavior. An Incident, by contrast, is a passive observation record (artifact) that records what happened. FIR records what happened *and* orchestrates what to do about it. See DR-032 D1.

---

### Q109: Why must every Win Case originate from an FIR?

Universal intake ensures complete coverage. If Win Cases can be created without an FIR, there is a bypass path that breaks the traceability chain — a CS Manager creates a complaint directly during a QBR with no FIR parent, no record of the original report, and it doesn't count toward FIR volume metrics. The overhead of creating an FIR for a trivial query is minimal (FIRs support direct resolution at triage with zero sub-items), and the traceability benefit is significant. FIR volume metrics become the single authoritative measure of total feedback burden. See DR-032 D2.

---

### Q110: Can Run teams create FIRs?

Yes. Run teams (SREs detecting alerts, operators observing degradation), Build teams (QA observing regressions), and Win teams (customer support receiving complaints) all create FIRs. The `Provenance` field distinguishes the creator context: `External`, `Run`, `Build`, `Internal`. If only the Win team created FIRs, monitoring alerts and QA observations would bypass universal intake and PFR-Win would be incomplete. Auto-routing is permitted for monitoring alerts — the FIR is auto-created with Provenance: Run and auto-routed to create an Incident. See DR-032 D3 and D4.

---

### Q111: Why separate roles (Definition Model) from agents (WFR)?

"The product needs a Pre-Sales Engineer function" is a product definition statement — it belongs in the Definition Model alongside other structural descriptions. "John Smith is a Pre-Sales Engineer and is also filling the CS Manager role this quarter" is a workforce statement — it belongs in WFR. Conflating them makes the Definition Model fragile (it changes every time someone joins, leaves, or changes roles) and makes WFR confusing (mixing "what the product requires" with "who is available"). The triad is: Role (Definition Model) -> Agent (WFR) -> Work (WR). See DR-034 D1 and D2.

---

### Q112: Why introduce OPR instead of keeping deployment artifacts in CAR?

Deployment descriptors, incident records, and operational artifact versions have different ownership (SRE/DevOps vs. developers), different lifecycle (deployment progression vs. build progression), and different governance (change management vs. CI/CD). CAR should hold source code and build artifacts only. The verification evidence also splits along this line: QVS for build-time quality evidence (tests, scans, benchmarks), OPR for run-time quality evidence (deployment verification, post-deployment SLA checks). See DR-033 D4 and D6.

---

### Q113: Why is ESR a reference layer, not a system of record?

The system of record for customer data remains the organization's CRM/subscription management system. Duplicating full customer records into ESR would create synchronization burdens and data governance risks. ESR holds the minimum identity and reference pointers needed by the UPIM — organization name, segment classification, primary contacts, and a pointer back to the authoritative source system. This makes ESR lightweight, easy to synchronize periodically, and focused on its purpose: providing consistent external stakeholder references across FIR reporters, Win Case customers, Incident affected tenants, and Customer Release targets. See DR-033 D3.

---
