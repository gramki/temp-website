# The Hub Way

*How Zeta thinks about work in banking domains*

---

## Why This Framework Exists

Banking is a network of business domains — payments, credit, servicing, compliance, risk — each with its own commitments to the outside world, its own internal disciplines, many kinds of participants, and systems that do the actual processing. None of these exist in isolation. They interact, depend on each other, and evolve at different rates.

The challenge is not building any one of these domains. The challenge is modeling all of this coherently — so that business leaders, domain experts, and technology teams see the same reality. And doing it in a way that lets the bank gradually shift from human-operated to AI-augmented, one piece of work at a time, without rebuilding the model.

## The Core Idea

Every piece of work in a domain is a goal. Someone — or something — resolves that goal. A millisecond payment authorization, resolved by a machine agent. A month-long dispute investigation, resolved by a team of humans and AI working together. A nightly interest computation, resolved by an automated process with no human involvement. The Hub Way models all work this way: as goals resolved by agents, using tools from the systems the bank runs, interacting through surfaces appropriate to each participant.

The bank controls a dial for each piece of work — fully human on one end, fully automated on the other, with every combination in between. Moving the dial does not change the model. It changes who resolves the work and how much autonomy they have. The bank decides the pace, one piece of work at a time, with no disruption to the rest.

---

## Hubs: The Domain Fabric

Every bank organizes its operations around business domains. Payments is one domain. Credit cards are another. Customer servicing, merchant acquiring, compliance — each has its own rules, its own participants, its own rhythm.

In the Hub Way, each of these domains is a **Hub** — a bounded business domain where agents collaborate to operate a coherent area of banking. A Hub is not a replacement for the systems a bank already runs. It is an operations and collaboration fabric that sits on top of those systems, bringing them together. A Payments Hub integrates with the bank's existing payment rails, core banking systems, and fraud engines. It does not replace them. It provides the structure — the goals, the governance, the collaboration model — that lets human and AI agents work together to operate that domain.

Zeta's product lines — Tachyon for processing, Neutrino for digital experiences, Electron for lifecycle management — integrate natively into Hubs. But a Hub works equally well with third-party systems. The fabric is system-agnostic. What makes it valuable is not which systems it connects to, but how it organizes the work those systems support.

---

## Streams: What the Bank Promises

When a customer applies for a credit card, the bank has made a commitment. When a merchant submits a payment for processing, when a regulator requests a filing, when a partner initiates a chargeback — each of these represents an obligation that the bank must fulfill.

The Hub Way calls this coordinated set of work a **Stream**. A Stream is not a workflow with predetermined steps. It is a series of goals — each modeled as a **Scenario** — that must be resolved to honor the commitment. Some goals may be resolved in parallel. Some may not arise at all, depending on what agents discover along the way. The path is not rigid; the commitment is.

This aligns with how banking actually works. A credit card application does not follow the same path every time. Some applications sail through decisioning in minutes because a machine agent resolves the risk assessment cleanly. Others require a human analyst to review documentation, a compliance agent to verify identity, and weeks of coordinated effort. The path varies because agents exercise judgment at each step — not because a workflow branches. The commitment — "we will process your application and give you a decision" — is constant.

Streams may span multiple Hubs when a commitment requires coordination across domains. A credit card application might involve the Credit Card Hub for decisioning, the Payments Hub for card provisioning, and the Servicing Hub for welcome communications. Every Stream produces an observable trace — a record of what happened, who decided what, what data was used, and what the outcome was. In banking, this trace is not optional. It is the audit trail that regulators, compliance officers, and the bank itself rely on.

---

## Loops: How the Bank Keeps Itself Honest

Not all work in a banking domain is triggered by an external request. Interest must be computed nightly. Accounts must be reconciled daily. Fraud patterns must be monitored continuously. Compliance must be verified without waiting for a regulator to ask.

The Hub Way calls this internally driven work a **Loop** — a ritual or routine that keeps a domain healthy, honest, and improving. Loops encompass analytical work (funnel analysis, customer segmentation), computational work (interest accrual, fee calculation), integrity work (reconciliation, cross-system validation), and compliance work (policy monitoring, regulatory reporting).

Some Loops are resolved entirely by machine agents — a nightly batch process that computes interest across millions of accounts, with no human in the loop. Others involve human-AI teams — a fraud analyst reviewing patterns surfaced by an AI detection system. The model is the same. The dial position differs. The bank chooses how much is automated and how much involves human judgment, and can change that choice as confidence grows.

Loops and Streams form a feedback system. Streams produce data — every commitment fulfilled generates a trace of decisions, outcomes, and exceptions. Loops consume that data — analyzing it for patterns, checking it against policies, computing derived values. And Loops may trigger new Streams — when fraud monitoring detects suspicious activity, it initiates a customer notification and account freeze, creating a new external commitment. Each cycle makes the domain more intelligent, more compliant, and more efficient.

---

## Channels: How Participants Interact

Banking involves many kinds of participants — customers, agents, supervisors, compliance officers, AI assistants, partner systems, regulatory systems. Each participates through an interaction surface appropriate to their needs.

The Hub Way calls these interaction surfaces **Channels**. A Channel is not just a user interface. It embodies identity (who is participating), authentication (how they prove it), access control (what they are authorized to do), and the interaction model appropriate to the context. A customer might interact through a web portal. An operations agent works through a task-oriented desk application. An AI agent connects through the Model Context Protocol. A partner system integrates through REST APIs.

Each Hub configures which Channels are available for its goals. A single goal may involve multiple Channels simultaneously — a dispute resolution might have the customer on a voice call, a human agent on a desk application, and an AI assistant providing real-time transaction analysis, all participating in the same work through different surfaces with appropriate access control.

Because a single persona — say, a customer — may need a cohesive experience spanning multiple Hubs, the Hub Way supports **Channel Products**: organization-scoped composites that weave components from multiple Hubs into a unified experience. The customer's mobile banking app provides access to payments, credit cards, and servicing in one place — not because a single Hub owns all of it, but because the Channel Product assembles it coherently.

---

## Teams: Who Does the Work

Every goal needs someone to resolve it. In the Hub Way, that someone is a **Team** — a combination of human and AI agents assembled to do the work.

A dispute investigation team might include a human analyst, an AI research assistant that gathers transaction history and precedent, and a supervisor who approves the final resolution. A nightly interest computation might have no human team at all — the application that runs it is itself an agent, perceiving account states, computing accruals, and posting results.

The composition of the team is the dial. For a given piece of work, the bank decides: how many humans, how much AI, how much autonomy. One team might be entirely human today and shift to AI-assisted next quarter. Another might start fully automated from day one. The bank can move the dial for each piece of work independently, at its own pace, without changing the model around it.

---

## Machines: What the Bank Works With

Agents need tools. Transaction lookup, risk scoring, payment authorization, account management — these capabilities come from the systems the bank runs. The Hub Way calls them **Machines**.

An application orchestrates how agents use these tools within each goal. That application might be a traditional workflow, a batch process, or an AI agent itself — perceiving the situation, deciding what to do, and acting through the tools available. The Hub does not care which systems provide the tools. Zeta products and third-party systems are equally valid Machines. When a bank modernizes a system, it replaces the Machine connection in the Hub, not the Hub itself.

This separation matters. The work model — goals, agents, governance — stays stable even as the technology underneath evolves. Banks modernize at their own pace, system by system, without disrupting the operational structure built on top.

---

## The Complete Picture

Six constructs, one coherent model. A **Hub** is the domain. **Streams** are the commitments to the outside world. **Loops** are the internal disciplines. **Channels** are the surfaces through which participants interact. **Teams** are the agents — human and AI — who resolve the work. **Machines** are the tools they use to do it.

Every piece of work is a goal. Agents resolve it. They use tools from the systems around them, interacting through surfaces designed for each kind of participant. The bank controls how much is human, how much is AI, how much is automated — and can change that answer for each piece of work, at its own pace. The model stays the same. Only who does the work changes.

---

## Why This Matters

**Operational visibility.** When every external commitment is modeled as a Stream and every internal discipline as a Loop, the bank can see its operations clearly. What are we committed to? How are we performing? Where are the gaps?

**Domain-expert modeling.** The Hub Way does not prescribe rigid structures. Domain experts — the people who understand payments, credit, compliance, servicing — decide how to model their domains. How many Streams does the Payments Hub need? What Loops does Credit Card require? Which Channels should Servicing expose? These are decisions made by people who understand the business, not imposed by the platform.

**Transformation at the bank's pace.** Because all work is modeled as goals resolved by agents, the bank can move the dial from human to AI for any piece of work — without changing the model. Start with human teams. Introduce AI assistants. Gradually increase autonomy. Go fully automated where it makes sense. One Scenario at a time, at whatever pace the bank is comfortable with.

**System-agnostic integration.** Hubs work with whatever systems the bank runs — Zeta products, third-party platforms, legacy systems, partner integrations. The operational fabric sits on top. The work model is independent of the technology underneath.

---

## Zeta's Hubs of Prominence

The domains where Zeta brings deep expertise and pre-built capabilities:

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
