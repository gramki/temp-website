# What Changes — And Why Each Change Is Achievable

The [thesis](thesis.md) distills the [structural problem](problems.md) and the [enterprise AI adoption challenge](enterprise-ai-adoption.md) into four core concerns and seven governing principles. What follows is what concretely gets better when those principles are applied — and why each benefit is achievable, not aspirational.

## What Changes for the Problems Banks Live With

These benefits map directly to the eight felt problems that bank executives deal with routinely.

### Technology spend starts producing returns

**Today.** The bank spends billions on technology — vendor licenses, systems integrators, transformation programs, engineering headcount. Every year there is more technology spend. Every year the operational cost is the same or higher. The board keeps asking: where is the return?

**What changes.** Each technology investment enriches the domain model rather than adding to the maintenance burden. The investment trajectory reverses: instead of each change adding complexity that makes the next change more expensive, each change adds structure that makes the next change cheaper. Over time, the proportion of spend going to maintenance shrinks and the proportion going to evolution grows. The cost-to-income ratio improves because the denominator — recurring maintenance cost — is structurally reduced.

**Why this is achievable.** When work is the stable abstraction and systems register their capabilities through declared contracts, new capabilities plug into the existing model. There is no new bespoke integration to maintain. The model absorbs the new capability; the maintenance surface does not grow. Because each investment compounds on the model, the cumulative effect is an accelerating return on technology spend rather than a growing maintenance burden.

---

### Change velocity decouples from integration complexity

**Today.** Launching a new product takes months when it should take weeks. Modifying an existing product — changing pricing, adding a feature, adjusting eligibility — ripples through multiple systems and requires engineering effort disproportionate to the business change.

**What changes.** Business changes become specification edits. A product modification — new pricing for a segment, an additional eligibility criterion, a reordered sequence of checks — is expressed in the domain model and takes effect through existing capability contracts. The change is proportional to the business intent, not to the integration complexity underneath. Business moves at business speed.

**Why this is achievable.** When operational intelligence is declarative, business logic lives in specifications, not in code fused to vendor APIs. Changing the business logic means editing the specification — a domain expert activity — not re-engineering integrations across multiple systems. The specification change propagates through existing contracts without requiring modification of the integrations themselves. The business change and the technology change are the same thing.

---

### Compliance becomes structural, not programmatic

**Today.** Every new regulation triggers a program. Find the data — scattered across systems. Trace the decisions — buried in integration logic. Build the reports — requiring manual assembly. Prove the controls — when the controls are embedded in plumbing nobody fully understands. Compliance programs cost multiples of what they should.

**What changes.** Every piece of work produces a governed trace by design — from the commitment that triggered it, through every decision and capability invocation, to the resolution and its outcome. The regulator's questions — who made this decision, what information was used, can you trace from intent to resolution — are answered by the architecture, not reconstructed after the fact. New regulations map to existing work and governance structures; they require model updates, not discovery programs.

**Why this is achievable.** When every piece of work is modeled with declared governance, the audit trail is a structural byproduct of operations, not a separate reporting effort. The model knows what work exists, who resolved it, what capabilities were invoked, and what the outcome was. Compliance reporting draws from this structural record. When a new regulation arrives, the question is: "Which of our existing work does this affect, and what governance adjustments are needed?" — not "Where is the data and who touched it?"

---

### Migrations become bounded

**Today.** Changing any significant vendor system triggers a multi-year re-engineering effort. The system itself is the easy part. The hard part is re-engineering all the bespoke integration connected to it — reverse-engineering years of accumulated operational knowledge from brittle code, then re-encoding it for the new system. Migrations take years and cost multiples of the new system's license fee.

**What changes.** Migrations become rebinding decisions. The work specification says what capability is needed — "I need a fraud assessment," "I need a credit decision." Which vendor provides it is a binding in the capability contract. Changing the vendor means updating the contract — the data shapes, the timing expectations, the error handling for the new system. The work specifications, the governance, and the operational intelligence do not change because they were never fused to the old vendor.

**Why this is achievable.** When operational intelligence is in declarative specifications rather than vendor-fused code, the knowledge survives the vendor change. The specification says what needs to happen in domain terms. The capability contract translates that into vendor-specific interactions. Swapping the vendor means writing a new contract — a bounded task — not reverse-engineering and rebuilding the entire integration layer. The bank can even run both vendors in parallel during transition, routing a percentage of work to the new system and comparing outcomes before committing. Migration risk drops because the operational intelligence is preserved, not rebuilt.

---

### Customer experience becomes fixable

**Today.** The bank knows its customers see inconsistency across channels and products. Every fix is a new layer on top of the same disconnected backend. The mobile app, the website, the contact center each connect to different backend systems, have different feature sets, and present inconsistent information. Nobody owns the coherent cross-channel experience.

**What changes.** The work and its state are channel-independent. Channels become views into domain work — surfaces through which participants interact with the same underlying model. A customer who starts a process on mobile and continues in the contact center sees the same state because the state lives in the work model, not in the channel. Cross-domain experiences are composable: the customer's relationship across payments, credit, and servicing can be assembled from domain-scoped views without requiring domains to merge their backends.

**Why this is achievable.** When the work model owns the state of each piece of work, channels read from and write to the same model. Channel fragmentation was caused by each channel connecting to different backend systems with different state. When the state is in the model, channels become presentation choices — different interaction paradigms over the same operational reality. Cross-domain composition works because each domain's model is independent but interoperable; a composite view assembles the customer's relationship from multiple domains without requiring architectural unification.

---

### Traceability is built in

**Today.** An outage, a compliance miss, a pattern of customer complaints — tracing from symptom to root cause crosses multiple systems and teams. The post-mortem takes weeks. The root cause is often in the connections between systems — the part nobody owns.

**What changes.** Every piece of work produces a trace from intent to resolution — what was the goal, what steps were taken, what capabilities were invoked, what decisions were made, what the outcome was. Root cause analysis follows the work model, not the plumbing. When something goes wrong, the trace shows exactly where the work deviated — which capability returned an unexpected result, which step stalled, which governance constraint was violated. Post-mortems take hours, not weeks.

**Why this is achievable.** When every piece of work is modeled with explicit state and governance, the trace is produced structurally by the model, not assembled forensically from logs across multiple systems. The work model owns the overall state of the operation — unlike the current reality where nobody owns the cross-system state. Traceability is not a feature that needs to be built; it is a consequence of modeling the work.

---

### Engineering capacity shifts from maintenance to evolution

**Today.** The engineers who understand how the bank's systems work together spend most of their time keeping existing things running — fixing breakages from vendor upgrades, maintaining compensating logic, supporting the shadow architecture of workarounds. They are not available for new work. When they leave, the knowledge leaves with them.

**What changes.** Operational intelligence moves from engineer-dependent code to declarative specifications. The knowledge of how the bank's domain works is in the model — examinable, maintainable, and independent of any individual engineer. When someone leaves, the specifications remain. Engineers shift from maintaining bespoke plumbing to evolving domain capabilities — modeling new work, refining specifications, expanding AI's role, registering new capabilities. The work becomes more interesting and the talent retention problem eases.

**Why this is achievable.** When operational intelligence is declarative and the model compounds, the maintenance burden structurally shrinks over time. Each piece of plumbing that is "unbuilt" — replaced by a declarative specification — removes a permanent maintenance obligation. The specification doesn't break when a vendor upgrades because it expresses domain intent, not vendor-specific API calls. The engineers who previously spent 80% of their time on maintenance can progressively shift toward evolution as the model absorbs the complexity that used to live in their heads and in their code.

---

### M&A rationalization becomes a domain conversation

**Today.** When the bank acquires another bank, integrating the operations takes years. Two sets of everything — systems, integrations, processes, workarounds — must be rationalized. The integration program consumes all technology capacity for years.

**What changes.** Both banks' work is modeled in domain terms. Rationalization becomes a domain-level conversation: which work streams does each bank have? Which recurring disciplines? Where do they overlap? Which teams can be consolidated? Which systems can be shared? The conversation is about the work — not about re-engineering plumbing between incompatible systems. The underlying systems can be rationalized incrementally, domain by domain, while both banks continue to operate on their own models.

**Why this is achievable.** When work is the stable abstraction and each domain evolves independently, two banks' domain models can be compared structurally. "Bank A's credit card domain has these work streams and disciplines; Bank B has these. Here is the overlap, here are the unique elements." The rationalization plan emerges from the domain comparison, not from reverse-engineering two sets of plumbing. Systems are rationalized by rebinding capability contracts — gradually, domain by domain — rather than through a monolithic integration program.

---

## What Changes in Integration Economics

These benefits address the specific costs of integration that consume the bank's money, time, and engineering talent.

### Integration cost becomes proportional to capabilities, not connections

**Today.** Adding a new system creates bespoke integration edges to every existing system it interacts with. Complexity grows combinatorially — a bank with 12 systems has 66 possible edges. Each edge carries the full cost of data preparation, timing orchestration, error handling, state management, security, and permanent operational support.

**What changes.** A new system registers its capabilities through standardized contracts. It does not create edges to every other system. Work that needs the new capability invokes it through the contract. The integration cost is proportional to the number of capabilities the system provides — not the number of other systems in the estate. Adding the 13th system is no harder than adding the 3rd.

**Why this is achievable.** Capability contracts standardize the integration surface. The contract declares what the capability provides — data shapes, timing expectations, error behavior, security model — in domain terms. The work specifies what it needs. The connection between them is the contract, not bespoke code. Because contracts are reusable and each investment compounds, a contract for "fraud assessment" serves every piece of work that needs fraud assessment. One contract, many consumers — not one bespoke edge per consumer.

---

### Data contracts replace bespoke data preparation

**Today.** Assembling the right data, in the right shape, at the right time, with the right freshness is the bulk of integration work. Every pair of systems has different data models. The preparation is bespoke for every edge and must be continuously maintained.

**What changes.** Capability contracts declare the data shapes they accept and produce. Data transformation happens at the contract boundary — declared once, maintained in one place. When a source system's data model changes, the contract adaptation is updated once; every piece of work that uses the capability automatically gets the updated data path.

**Why this is achievable.** When contracts include data shape declarations, the data translation is part of the contract, not scattered across bespoke code in every integration edge. The contract is the single point of truth for how this capability's data relates to the domain model. Changes propagate through the contract, not through dozens of independent integration scripts.

---

### Temporal orchestration is declared, not coded

**Today.** The core banking system runs batch overnight. The fraud engine needs real-time. The CRM updates on demand. Coordinating across different speeds and consistency guarantees is where most integration complexity lives.

**What changes.** Capability contracts declare timing expectations — latency, consistency guarantees, batch windows. The orchestration layer coordinates work across capabilities using declared temporal contracts rather than bespoke timing logic coded per integration edge. The timing complexity is managed centrally against declarations, not scattered across ad-hoc coordination code.

**Why this is achievable.** When timing is a declared property of the capability contract, the orchestration layer can reason about temporal coordination structurally. "This capability provides batch-overnight results; this work needs near-real-time; here is the reconciliation contract that bridges them." The temporal complexity doesn't disappear, but it moves from bespoke per-edge code into declared contracts that can be reasoned about, monitored, and evolved.

---

### Error handling becomes specified, not discovered

**Today.** The happy path takes 20% of the effort. The other 80% is compensating logic for every failure mode — retries, rollbacks, fallbacks, manual intervention queues. This logic is the most undocumented and least tested part of the integration.

**What changes.** Error handling and compensation strategies are part of the capability declaration. When a capability fails, the behavior is specified in domain terms — retry with exponential backoff, fall back to a manual queue, escalate to a supervisor, roll back the upstream steps. The compensation logic is visible, testable, and governable.

**Why this is achievable.** When error contracts are declared rather than coded, compensation strategies become examinable specifications rather than hidden code paths. The specification says: "If the fraud engine is unavailable, hold the transaction and alert the operations team." That is a domain-level statement that domain experts can review, not a code-level implementation that only the integration engineer understands. When the compensation strategy needs to change — "now we have a fallback fraud engine" — it's a specification edit, not a code change across multiple integration points.

---

### State ownership becomes explicit

**Today.** A business operation touches five systems over hours or days. Each has its own state. Nobody owns the overall state. Cross-system state management is the most fragile and least documented part of the bank's technology.

**What changes.** The work model owns the state of each piece of work. The overall state of a business operation — what has been done, what is pending, what is blocked, what the next step is — is a first-class concept in the model, not an emergent property of plumbing. When something stalls, the model shows exactly where and why.

**Why this is achievable.** When every piece of work is modeled, its state is managed by the model, not by ad-hoc cross-system tracking. Individual systems still have their own internal state, but the overall business state belongs to the work model. This eliminates the most common source of operational fragility — the gap between where individual systems think things are and where the business operation actually stands.

---

### Operational intelligence becomes portable and reusable

**Today.** The bank's technology IP — how it employs vendor capabilities to fulfill domain commitments — is encoded as bespoke integration code fused to specific vendors. It is fragile, undocumented, dependent on a few engineers, and rebuilt from scratch by every bank that faces the same problem.

**What changes.** The bank's operational intelligence transforms from code into specifications. These specifications are portable — they can survive vendor changes. They are reusable — the same domain knowledge applies across similar work, across domains, and potentially across banks. They are examinable — domain experts can review and improve them. And they are agent-interpretable — AI can read, reason about, and execute against them.

**Why this is achievable.** When operational intelligence is declarative, the knowledge exists independently of the vendor systems it references. A specification for "onboard a customer in the credit card domain" describes the work in domain terms — commitments, steps, capabilities needed, governance rules, compensation strategies. That specification is the bank's IP in a portable form. When a vendor changes, the specification survives. When a similar bank faces the same problem, the specification is a starting point. When AI enters, the specification is what the agent reads to understand the work. The bank's most valuable knowledge finally exists in its most durable and useful form.

---

## What Changes in the Modernization Dynamics

These benefits address the structural forces that currently make modernization self-defeating.

### The modernization curve accelerates instead of decelerating

**Today.** Each successive modern system takes longer to integrate than the last. Engineering teams spend increasing time maintaining existing integrations. The more the bank modernizes, the slower it gets. The cost-efficiency cycle — high cost, pressure to minimize, more patching, higher cost — accelerates the decline.

**What changes.** The curve reverses. Each domain investment enriches the model. The next change is cheaper because the model absorbs complexity rather than producing it. The cost-efficiency cycle becomes a value-compounding cycle: each investment reduces the cost of the next, which frees capacity for more investment, which further enriches the model.

**Why this is achievable.** When each investment compounds, the math changes fundamentally. Under the current model, adding a system with *N* existing systems creates up to *N* new bespoke edges. Under the thesis, adding a system registers its capabilities into the existing model — the integration cost is proportional to the capabilities provided, independent of the system count. The 13th system is no harder than the 3rd. Over time, the model becomes richer, the contracts more comprehensive, and each new addition finds more of its integration surface already declared. The curve accelerates.

---

### The systems gap becomes closable

**Today.** Banks are strong in recording transactions and enforcing rules but weak in engagement, intelligence, influence, identity, memory, product composition, innovation, and operational orchestration. The ones they have are treated as surrounds. Core-systems thinking limits possibilities to what the core can express.

**What changes.** Every system — whether a decades-old ledger or a new AI prediction service — registers its capabilities into the model on equal terms. There is no hierarchy. The system of record and the system of intelligence are equally legitimate providers of capabilities. New systems are introduced by registering capabilities through declared contracts, not by rewiring the architecture. The systems gap becomes a gap in available capabilities, closable incrementally by registering new systems.

**Why this is achievable.** When the model treats every system uniformly as a capability provider and each new registration compounds on the model, the architectural barrier to closing the systems gap dissolves. The bank can add an intelligence platform, an engagement system, or a product composition engine by registering each as a capability provider — without the combinatorial integration explosion that makes such additions prohibitively expensive under the current architecture. The gap closes incrementally, system by system, at the pace the bank can absorb.

---

### Domain-by-domain evolution matches how banks actually operate

**Today.** Enterprise-wide modernization programs fail because they assume a uniform starting point that does not exist. Each domain has its own unique mix of system maturity, integration depth, and technical debt.

**What changes.** Each domain is modeled independently. Each starts where it is. Each evolves at its own pace. Patterns learned in one domain — work designs, discipline categories, capability contracts, governance structures — transfer to the next domain as starting points, not mandates. The bank's unique mix of gaps and starting points is respected rather than overridden.

**Why this is achievable.** When each domain operates independently and each investment compounds, the bank gets the benefits of enterprise-scale thinking without the risks of enterprise-scale programs. The payments domain can model its work and begin AI absorption while the mortgage domain is still mapping its systems. Lessons from payments — contract patterns, work designs, governance structures — become reusable assets for the mortgage domain. The enterprise benefits from coherence without requiring simultaneity.

---

## What Changes for AI

These benefits address the specific challenges of enterprise AI adoption.

### AI investments compound

**Today.** Each AI project builds its own integration, governance, and scope. The 50th agent costs as much to integrate as the 1st. There is no platform effect. The bank has recreated the plumbing problem in AI form.

**What changes.** The 50th agent reuses the same domain model, the same capability contracts, the same governance framework as the 1st. It is genuinely cheaper. The agent doesn't need to build its own integration to the fraud engine, its own connection to the core, its own governance model — all of that exists in the domain model. The agent needs to know what work it's participating in and which capabilities it should use. The platform effect is real.

**Why this is achievable.** When agents operate within a shared model of the work, using declared capability contracts, and each investment compounds, the integration cost per agent drops with each addition. The model provides the context, the contracts provide the capabilities, the governance provides the guardrails. Each new agent extends the model's coverage rather than building a standalone island. The 50th agent is cheaper than the 5th because the model is richer, the contracts more comprehensive, and the governance more mature.

---

### Domain-level outcomes become visible and measurable

**Today.** When an executive asks "what has AI done for us?", the answers are project-shaped. Nobody can answer: what fraction of our payments domain is AI-augmented? How many applications can we retire? Is our cost-to-serve actually improving?

**What changes.** The full work of a domain is enumerable. For each piece of work, the model shows: who resolves it — human, AI, or combination. Where the dial is today. Where it could move. What the outcome of moving it would be — fewer people needed, applications retirable, accuracy improved. The executive gets domain-level visibility, not just project metrics. Progress is measurable against the denominator — total work in the domain — not just the numerator of AI projects shipped.

**Why this is achievable.** When work is modeled and the model tracks who resolves each piece of work, domain-level visibility is a structural property. The model knows: here is all the work in this domain, here is how each piece is currently resolved. Aggregating from individual work to work streams to domain gives the executive a view that was previously impossible: the denominator exists, progress is measurable, and the return on AI investment is evaluable at the level that matters.

---

### Applications can actually be retired

**Today.** AI agents connect to existing systems rather than replacing the need for them. The legacy workflow engine, the case management tool, the middleware layer are all still running. AI was added. Nothing was removed.

**What changes.** Work is specified independently of the systems that currently resolve it. When agents resolve work directly — interpreting the specification, invoking capabilities, managing the state, producing the trace — they don't need the legacy workflow engine to sequence them. They don't need the case management tool to track state. They don't need the middleware to translate between systems. These applications become redundant and can be decommissioned. The legacy infrastructure actually comes down.

**Why this is achievable.** When work is the stable abstraction and agents progressively absorb work, there comes a point for each legacy application where the work it managed is fully resolved by agents operating within the model. The workflow engine was necessary because humans needed a system to route and sequence tasks. Agents don't — they interpret the specification directly. The case management tool was necessary because humans needed a place to track state. Agents don't — the work state is in the model. Each retired application removes a permanent cost: license fees, maintenance, operational support, security patching.

---

### Structure creates the environment AI excels in

**Today.** The bank's operational environment is hostile to AI agents. The automation that exists — middleware, ETL jobs, glue scripts, compensating layers — is imperative, unstructured, and opaque. AI agents can automate individual tasks but cannot participate in the broader work of the domain.

**What changes.** The structured model — enumerated work, declared capability contracts, explicit work state, governance rules — is precisely the environment where AI agents are most effective. AI agents excel at navigating structured models, invoking capabilities through declared contracts, tracking state toward goals, and following explicit governance rules. The structure doesn't just allow AI to operate; it allows AI to *excel* — to take on progressively more complex work, to collaborate with other agents and humans, to produce governed outcomes at scale.

**Why this is achievable.** When work is modeled and capability contracts are declared, a virtuous cycle emerges — the inverse of the current vicious cycle. Structure enables AI to operate effectively. Effective AI produces better outcomes. Better outcomes justify further investment in structure. More structure enables AI to take on more complex work. Each cycle produces more value at lower cost. The bank moves from a decelerating modernization curve to an accelerating capability curve.

---

## What AI Enables Beyond Execution

These benefits describe AI's role not just as a worker within the domain, but as a partner in understanding and improving the domain itself.

### AI discovers invisible work

**Today.** Much of the work in a domain was never modeled. The coordination between systems, the compensating logic, the informal routines — all handled by humans implicitly. Invisible to management, invisible to measurement, invisible to AI.

**What changes.** AI operating within the structured model observes operational patterns that reveal unmodeled work. A daily manual reconciliation between two systems is surfaced as a candidate recurring discipline. A repeated handoff pattern between teams is identified as an unmodeled work step. Compensation logic that engineers perform informally is flagged for formalization. The invisible becomes visible progressively, with AI as a discovery partner rather than requiring exhaustive human enumeration.

**Why this is achievable.** When even a partial model exists and AI participates in discovery, the model becomes self-extending. AI can analyze operational logs, trace patterns, and compare actual behavior against the declared model to identify discrepancies — work that is happening but not modeled. Each discovery enriches the model, which gives AI a richer baseline for the next round of discovery. The bootstrapping problem — "how do I model everything?" — dissolves. You model what you know. AI helps uncover what's in the seams. The model grows organically.

---

### AI reasons about gaps and completeness

**Today.** Gaps in the bank's operational model are discovered through incidents — something goes wrong because a step was missing — or through audits — a regulator asks "where is your X?" and the bank realizes it doesn't have one.

**What changes.** Given stated goals and partially defined work, AI reasons about what is missing. If the work for customer onboarding covers identity verification, credit check, and account creation — but there is no fraud screening step, no welcome communication, no regulatory disclosure — AI identifies those gaps before they manifest as incidents or audit findings. Gap discovery shifts from reactive (incident-driven) to proactive (reasoning-driven).

**Why this is achievable.** When work is modeled with stated goals and governance requirements and AI participates in reasoning, completeness analysis becomes automated. AI compares the modeled work against the stated goals and known requirements — regulatory, operational, experiential — and flags where the coverage is incomplete. "This work fulfills a commitment to onboard a customer, but the model does not include a step for regulatory disclosure. Banks in this jurisdiction are typically required to provide this. Is it handled elsewhere, or is this a gap?" The question is precise because the model provides the context.

---

### AI brings industry knowledge to the domain

**Today.** Best practice advice is generic. Consultants recommend "you should have better fraud detection" or "you should modernize your customer engagement." The advice is not connected to the bank's specific operational reality. Implementing it requires translation from generic recommendation to specific action — a process that is expensive, slow, and often loses the intent.

**What changes.** AI draws on industry best practices, regulatory standards, vendor capabilities, and community patterns — and maps them directly to the bank's specific domain model. The advice is situated and actionable: "Your fraud detection discipline runs end-of-day batch. Banks with similar transaction profiles have found that adding an intra-day observational discipline with real-time velocity monitoring reduced false positive rates significantly. Here is how that discipline would fit your current model, which systems already provide the required capabilities, and where the gap would need to be filled." The recommendation is precise because it references the bank's actual work, actual systems, and actual gaps.

**Why this is achievable.** When the domain model is structured and AI participates in advisory, external knowledge becomes actionable internal improvement. The model provides the context that makes generic knowledge specific. "Add real-time fraud monitoring" is generic. "Add an observational discipline of this type, consuming signals from the fraud engine (capability: transaction velocity score, already registered) and core banking (capability: account activity feed, needs registration), producing alerts that feed into the existing fraud triage work" is an actionable specification. The structured model is what makes the translation from generic to specific possible.

---

## The Compound Effect

These benefits are not independent improvements. They compound on each other, creating a trajectory that is fundamentally different from the current one.

The current trajectory is a vicious cycle:

- Each change adds integration burden → higher maintenance cost → less capacity for evolution → pressure to minimize each change → more patching → more burden → each cycle makes the next harder

The thesis trajectory is a virtuous cycle:

- Each investment enriches the model → lower cost for the next change → more capacity for evolution → richer model → more AI leverage → AI discovers more work and gaps → model grows → each cycle makes the next easier and more valuable

Compliance improves because traceability is structural. Migrations become bounded because intelligence is portable. Customer experience becomes fixable because state is channel-independent. AI investments compound because the model provides the shared context. And AI itself helps the model grow — discovering work, reasoning about gaps, bringing industry knowledge — which accelerates every other benefit.

The overall trajectory is an accelerating capability curve — the structural inverse of the decelerating modernization curve that defines the bank's current reality. Each benefit creates the conditions for the others. The compound effect is what turns incremental improvements into structural transformation.

---

*Previous: [The Thesis](thesis.md) · [Reading Order](README.md) · Next: [The Hub Way](../the-hub-way/README.md)*
