# The Hub Way

*How Zeta thinks about work in banking domains*

---

## Why This Framework Exists

The companion documents establish that mid-size and large banks face a compound structural problem: [the work in their domains has no coherent model, their operational intelligence is locked in vendor-coupled code, their architecture punishes evolution, and enterprise AI leverage depends on structural prerequisites that don't exist yet](../the-thesis/problems.md). The [enterprise AI adoption challenge](../the-thesis/enterprise-ai-adoption.md) compounds this — project-by-project AI produces tools and islands, not transformation. The [thesis](../the-thesis/thesis.md) distills these into four core concerns and proposes seven governing principles as an alternative thesis.

The Hub Way translates that thesis into a concrete, implementable model. It gives domain experts, technology teams, and business leaders a shared way to enumerate the work in a banking domain, identify who resolves it, register the tools available, define how participants interact, and progressively move from human to AI resolution — with each investment compounding on the last and AI participating in the domain's ongoing discovery and improvement.

## The Core Idea

The fundamental choice in any operational model is what to organize around. If the model is organized around systems, every system change is a structural disruption — migrations take years because the operational knowledge is fused to the systems. If it is organized around processes, every change in who does the work means redesigning the process — a vendor replacement, a team reorganization, an AI agent taking over a step, each triggers a re-engineering project rather than a configuration change.

The Hub Way organizes around the work itself — the commitments a domain must fulfill to the outside world and the internal disciplines it must maintain. Work endures. Systems change. Vendors come and go. People move on. AI arrives. But the bank will always need to process payments, onboard customers, detect fraud, reconcile accounts, comply with regulations. The work is the stable abstraction.

Every piece of work in a domain is a goal. Someone — or something — resolves that goal. A millisecond payment authorization, resolved by a machine agent. A month-long dispute investigation, resolved by a team of humans and AI working together. A nightly interest computation, resolved by an automated process with no human involvement. The Hub Way models all of this uniformly: as goals resolved by agents, using tools from the systems the bank runs, interacting through surfaces appropriate to each participant.

Because the model is about the work and not about who does it, the bank controls a dial for each piece of work — fully human on one end, fully automated on the other, with every combination in between. Moving the dial does not change the model. It changes who resolves the work and how much autonomy they have. This is what makes gradual transformation possible without architectural disruption. This is what makes compliance structural — every piece of work produces a governed trace by design. This is what makes AI investments compound — every agent operates within the same model, the same tool contracts, the same governance. The bank decides the pace, one piece of work at a time, with no disruption to the rest.

---

## Hubs: The Domain Fabric

In the Hub Way, a **Hub** is a bounded business domain — the organizing unit for all work, all participants, and all systems within a coherent area of banking. A Payments Hub. A Credit Card Hub. A Compliance Hub. Each has its own Streams, Loops, Channels, Teams, and Machines. Each is modeled independently. Each evolves at its own pace.

A Hub is not a replacement for the systems a bank already runs. It is the domain model — the shared representation of what work exists, who resolves it, what tools are available, and how participants interact. A Payments Hub connects to the bank's existing payment rails, core banking systems, and fraud engines. Those systems become Machines in the Hub — registered providers of tools. The Hub provides the structure that was missing: the goals, the governance, the collaboration model, and the governed trace that connects commitment to resolution.

The Hub is system-agnostic. Zeta's product lines and third-party systems are equally valid Machines. What makes a Hub valuable is not which systems it connects to, but the coherent model of the domain's work that it provides — and the fact that this model stays stable as systems, people, and AI evolve underneath.

---

## Streams: What the Bank Promises

When a customer applies for a credit card, the bank has made a commitment. When a merchant submits a payment for processing, when a regulator requests a filing, when a partner initiates a chargeback — each of these represents an obligation that the bank must fulfill.

The Hub Way calls this coordinated set of work a **Stream**. A Stream is not a workflow with predetermined steps. It is a series of goals — each modeled as a **Scenario** — that must be resolved to honor the commitment. Some goals may be resolved in parallel. Some may not arise at all, depending on what agents discover along the way. The path is not rigid; the commitment is.

This is the first half of making the domain's work visible. When every external commitment is modeled as a Stream, the bank can answer: what do we owe the outside world? How many commitments are active? Where are we falling behind? These questions — unanswerable today — become structural properties of the model.

This aligns with how banking actually works. A credit card application does not follow the same path every time. Some applications sail through decisioning in minutes because a machine agent resolves the risk assessment cleanly. Others require a human analyst to review documentation, a compliance agent to verify identity, and weeks of coordinated effort. The path varies because agents exercise judgment at each step — not because a workflow branches. The commitment — "we will process your application and give you a decision" — is constant.

Streams may span multiple Hubs when a commitment requires coordination across domains. A credit card application might involve the Credit Card Hub for decisioning, the Payments Hub for card provisioning, and the Servicing Hub for welcome communications. Every Stream produces an observable trace — a record of what happened, who decided what, what data was used, and what the outcome was. In banking, this trace is not optional. It is the audit trail that regulators, compliance officers, and the bank itself rely on.

---

## Loops: How the Bank Keeps Itself Honest

Not all work in a banking domain is triggered by an external request. Interest must be computed nightly. Accounts must be reconciled daily. Fraud patterns must be monitored continuously. Compliance must be verified without waiting for a regulator to ask.

The Hub Way calls this internally driven work a **Loop** — a ritual or routine that keeps a domain healthy, honest, and improving. Loops encompass analytical work (funnel analysis, customer segmentation), computational work (interest accrual, fee calculation), integrity work (reconciliation, cross-system validation), compliance work (policy monitoring, regulatory reporting), observational work (transaction velocity monitoring, anomaly detection), and preparatory work (data staging, pre-qualification runs).

This is the second half of making the domain's work visible. Loops are the work that has always existed but was rarely modeled — the disciplines that keep the domain healthy. When they are explicit, the bank can ask: are our internal disciplines actually running? Are they producing useful output? Are they keeping us healthy? And AI can discover additional Loops that should exist but don't — gaps that today surface only through incidents or audit findings.

Some Loops are resolved entirely by machine agents — a nightly batch process that computes interest across millions of accounts, with no human involvement. Others involve human-AI teams — a fraud analyst reviewing patterns surfaced by an AI detection system. The model is the same. The dial position differs. The bank chooses how much is automated and how much involves human judgment, and can change that choice as confidence grows.

Loops and Streams form a feedback system. Streams produce data — every commitment fulfilled generates a trace of decisions, outcomes, and exceptions. Loops consume that data — analyzing it for patterns, checking it against policies, computing derived values. And Loops may trigger new Streams — when fraud monitoring detects suspicious activity, it initiates a customer notification and account freeze, creating a new external commitment. Each cycle makes the domain more intelligent, more compliant, and more efficient.

---

## Channels: How Participants Collaborate

Work is resolved through collaboration — and collaboration requires interaction surfaces. A customer submits a dispute through a mobile app. A human agent investigates through a task-oriented desk application. An AI assistant analyzes transaction patterns through an API. A supervisor reviews the resolution through a management dashboard. All are participating in the same Scenario, through different surfaces, with appropriate identity, authentication, and access control.

The Hub Way calls these interaction surfaces **Channels**. A Channel is not just a UI. It is a comprehensive interaction system — embodying identity, authentication, access control, and the interaction paradigm appropriate to the participant and context. A customer interacts through a web portal. An operations agent works through a task-oriented desk application. An AI agent connects through the Model Context Protocol. A partner system integrates through REST APIs.

Each Hub defines which Channels are available for its work. This is what makes the customer experience structurally fixable. Today, channels are disconnected silos — the mobile app, the website, and the contact center each connect to different backends and present inconsistent information. When the work and its state live in the model, channels become views into the same operational reality. The customer who starts a process on mobile and continues in the contact center sees the same state because the state belongs to the Scenario, not the channel.

Because a single persona may need a cohesive experience spanning multiple domains, the Hub Way supports **Channel Products** — organization-scoped composites that weave Channels from multiple Hubs into a unified experience. The customer's mobile banking app provides access to payments, credit cards, and servicing in one place — not because a single Hub owns all of it, but because the Channel Product assembles it coherently. This is how the customer stops falling through the seams between domains.

---

## Teams: Who Does the Work

Every piece of work needs someone to resolve it. In the Hub Way, that someone is a **Team** — a combination of human and AI agents assembled for the work.

A dispute investigation team might include a human analyst, an AI research assistant that gathers transaction history and precedent, and a supervisor who approves the final resolution. A nightly interest computation might have no human involvement at all — the application that orchestrates it is itself an agent, perceiving account states, computing accruals, and posting results.

Teams are where transformation becomes concrete. When the bank decides to shift a piece of work from human-heavy to AI-augmented, it changes the Team composition — not the model. The Stream, the Scenarios, the Tool contracts, the governance — all stay the same. AI doesn't replace the team; it joins it. Over time, AI absorbs more of the coordination, more of the judgment, more of the routine steps — progressively, as confidence grows. This is what progressive absorption looks like in practice: not replacing processes, but evolving who is on the team.

---

## Machines: What the Bank Works With

Agents need tools to resolve work. Risk scoring, payment authorization, transaction lookup, document verification, account management — these capabilities come from the systems the bank runs. In the Hub Way, every such system is a **Machine** — a registered provider of tools.

A Machine exposes its capabilities through **Tool contracts** — declared interfaces that specify what the tool does, what data it needs, what it returns, its timing characteristics, and its error behavior. The fraud engine is a Machine that provides a "fraud assessment" Tool. The core banking system is a Machine that provides "account inquiry" and "balance posting" Tools. An AI prediction service is a Machine that provides a "credit risk score" Tool. Zeta systems and third-party systems are equally valid Machines.

This is where the diagnosis principle — "operational intelligence should be declarative, not imperative" — becomes concrete. Today, the bank's knowledge of how to use a fraud engine is locked in bespoke integration code fused to that specific engine. In the Hub Way, the work specification says "I need a fraud assessment." The Tool contract defines how to get one. If the bank replaces the fraud engine, it writes a new Tool contract for the new Machine. The work specification doesn't change. The operational intelligence — the domain knowledge of when and why to request a fraud assessment — survives the vendor change.

An **Application** orchestrates how agents use Tools within each Scenario. That application might be a traditional workflow engine, a batch process, or — on the Seer runtime — an AI agent itself, simultaneously orchestrating the work and participating as a team member. The Hub does not prescribe the orchestration model. It provides the stable work model and the Tool contracts; the Application decides how to resolve the goal.

---

## The Complete Picture

Six constructs compose a complete model of a banking domain. A **Hub** is the domain boundary. Within it, **Streams** represent every commitment to the outside world and **Loops** represent every internal discipline — together, they enumerate all the work. **Teams** are the human and AI agents who resolve the work. **Machines** are the systems that provide tools. **Channels** are the surfaces through which participants collaborate.

Every piece of work executes as a **Scenario** — a goal-oriented unit of resolution. Scenarios are where everything converges: a Team resolves a goal, using Tools from Machines, collaborating through Channels, producing a governed trace. The bank can see every Scenario — active, completed, stalled — and can see for each one: who resolved it, what tools were used, what decisions were made, and what the outcome was.

This is what "making work visible" looks like in practice. The domain's full operational reality — commitments, disciplines, agents, tools, interactions, traces — is enumerable, examinable, and governable. The denominator exists.

---

## How a Domain Gets Modeled

A bank starts with one domain — the one under the most pressure, the one with the clearest mandate. Domain experts enumerate the Streams — every external commitment the domain fulfills. They identify the Loops — the internal disciplines that keep the domain healthy. They register the Machines — the systems that provide tools. They define the Channels — the surfaces participants use. They describe the Teams — who currently resolves each piece of work.

This is not an exhaustive, multi-month analysis exercise. It is a structured conversation with domain experts, producing a model that is immediately useful and progressively refined. AI participates from the start — discovering work that wasn't initially captured, reasoning about gaps, bringing industry patterns as suggestions. The model grows organically. The bank doesn't need to model everything before it can act. It models what it knows, starts moving the dial where it matters most, and expands as confidence and evidence accumulate.

---

## What This Makes Possible

The six constructs — Hubs, Streams, Loops, Channels, Teams, Machines — compose into outcomes that the systems-first approach cannot produce.

**All work becomes visible.** Streams enumerate every external commitment. Loops enumerate every internal discipline. Together they are the denominator — the full scope of work in the domain. When the denominator exists, the bank can answer questions that were previously unanswerable: what fraction of our domain is AI-augmented? Where are we falling behind on commitments? Which internal disciplines are actually running? Domain-level measurement becomes a structural property of the model, not a reporting exercise.

**Compliance becomes structural.** Every Scenario produces a governed trace — from the commitment that triggered it, through every decision, every Tool invocation, every agent involved, to the resolution and its outcome. The regulator's questions — who decided, what information was used, can you trace from intent to resolution — are answered by the architecture. New regulations map to existing Streams, Loops, and governance structures. Compliance is a byproduct of operations, not a separate program.

**Migrations become bounded.** Machines register capabilities through Tool contracts. Replacing a vendor means writing a new Tool contract for a new Machine. The Streams, Loops, Scenarios, governance, and operational intelligence are unaffected — they were never fused to the old vendor. The bank can run both Machines in parallel during transition, routing work to each and comparing outcomes before committing. Migration risk drops because the knowledge survives the system change.

**Customer experience becomes fixable.** Channels read from Scenario state in the model, not from independent backends. The customer who starts on mobile and continues in the contact center sees the same state because the state belongs to the Scenario, not the channel. Channel Products compose the customer's relationship across multiple Hubs — payments, credit, servicing — without requiring backend unification. The customer stops falling through the seams between domains.

**AI investments compound.** Agents join Teams within the same model, using the same Tool contracts, the same governance. The 50th agent is genuinely cheaper than the 5th — the model provides the context, the contracts provide the capabilities, the governance provides the guardrails. Each new agent extends the model's coverage rather than building a standalone island. The platform effect is real because the shared model is real.

**Progressive absorption works.** Teams evolve — AI joins, absorbs more coordination, more judgment, more routine steps. Humans shift to higher-judgment tasks. The Streams, Loops, Tool contracts, and governance hold. The dial moves without architectural disruption. And the model makes the progression visible: for each piece of work, who resolves it today, where the dial could move next, what the outcomes of moving it would be.

**Each investment compounds.** The vicious cycle — more plumbing, higher maintenance cost, pressure to minimize each change, more patching — reverses into a virtuous cycle. Each piece of work modeled, each Tool contract declared, each Stream or Loop formalized makes everything that follows cheaper, faster, and more capable. The trajectory is an accelerating capability curve, not a decelerating maintenance burden.

The [thesis benefits document](../the-thesis/benefits.md) develops the full structural argument for these outcomes at the principle level. The enablement chapters that follow show how each construct delivers its specific share.

---

## Zeta's Hubs of Prominence

The domains where Zeta brings deep expertise and pre-built capabilities. A bank doesn't need all of these — it starts with the domain that matters most and expands at its own pace:

- **Payments** — various rails and instruments
- **Credit Card** — issuance, lifecycle, servicing
- **Customer Lifecycle Management** — offers, rewards, cross-sell, up-sell
- **Customer Servicing and Digital Journeys** — multi-channel service delivery
- **Customer IAM** — SSO, identity risk, behavioral risk
- **Merchants** — acquiring, payment facilitation, payment aggregation
- **Commercial Cards** — business and corporate card programs
- **Family Banking** — household-oriented banking experiences
- **Small Business** — SMB banking and financial services

Each of these domains is modeled as a Hub with its own Streams, Loops, Channels, Teams, and Machines — and each benefits from the compounding effect of Zeta's platform: improvements learned in one engagement strengthen the frameworks and product lines available to every subsequent engagement.
