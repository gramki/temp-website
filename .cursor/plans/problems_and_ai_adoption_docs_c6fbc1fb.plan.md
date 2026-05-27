---
name: Problems and AI adoption docs
overview: "Two-document update: (1) reframe problems.md with correct voice, honest urgency, and Zeta board audience, and (2) create a new enterprise AI adoption problem document that covers why AI requires the structural model and why project-by-project approaches won't scale."
todos:
  - id: problems-title-opening
    content: New title and opening paragraph for problems.md — Zeta voice, market framing
    status: completed
  - id: problems-voice
    content: Ground key claims in experience — light framing sentences at section openings
    status: completed
  - id: problems-urgency
    content: Completely rework Why This Matters Now — real triggers (regulatory, M&A, leadership, cost), honest framing, brief AI paragraph
    status: completed
  - id: problems-spend
    content: Add existing spend dimension — banks burning budgets on ineffective coping
    status: completed
  - id: problems-failed-approaches
    content: Elevate failed approaches to own prominent subsection
    status: completed
  - id: problems-trim-channels
    content: Trim channel section — keep felt consequences, reduce technical detail
    status: completed
  - id: problems-footnotes
    content: Reframe Hub Way footnotes as strategic positioning, not product-spec
    status: completed
  - id: problems-closing
    content: Strengthen Compound Picture closing with honest urgency and episodic buying moments
    status: completed
  - id: ai-doc-create
    content: Create enterprise-ai-adoption.md — full document covering tool-agent-enterprise progression, why projects don't compound, decision maker's visualization need, Hub Way as evaluation framework
    status: completed
isProject: false
---

# Update problems.md and Create Enterprise AI Adoption Problem Doc

Two documents, complementary arguments. The problems document establishes the structural problem banks face. The AI adoption document establishes why AI — the most significant current technology wave — makes that structural problem unavoidable.

---

## Document 1: Reframe [problems.md](org-8.0/what-we-sell/problems.md)

The analytical structure and problem depth are strong. Changes are about voice, urgency framing, and audience calibration for Zeta's board.

### 1.1 Title and opening — Zeta's voice

Replace the title with something that leads with consequence and positions Zeta's perspective. Add 2-3 opening sentences framing this as Zeta's articulation of the market it serves — grounded in what we see across engagements, not analyst observation.

### 1.2 Voice shift — ground claims in experience

Light framing at key section openings: shift from third-person assertion to first-person conviction. "Across banking domains we work in, we consistently find..." Not fake case studies — just the voice of a practitioner who has seen this pattern repeatedly. Key locations: Core Problem, Organizational Reality, Plumbing Problem, Modernization Trap openings.

### 1.3 Completely rework "Why This Matters Now"

**Remove** the analyst-grade urgency drivers (competitive pressure from neobanks, customer expectations, talent risk). These are "often cited but don't drive sufficient urgency" — they're ambient pressure, not action triggers. Banks don't lose customers easily. Product differentiation hasn't swayed fortunes.

**Replace with real triggers** — what actually makes banks move:

- **Regulatory mandates**: Non-optional. When the regulator demands operational resilience, AI explainability, or real-time surveillance, the bank must act regardless of architecture. Compliance cost is proportional to the structural mess.
- **M&A — bank or vendor**: Acquiring a bank doubles the compound problem overnight. Vendor M&A (acquisition, EOL, pricing changes) forces migration. These trigger nine-figure programs.
- **Leadership change with vision**: A new CTO/CDO/COO with a mandate and a 2-3 year window of political capital. The person who reads this document and says "this is what I came here to fix."
- **Contract renewal / vendor EOL**: Predictable, recurring decision points that surface the plumbing problem.
- **Cost pressure**: When the board asks "why is our cost-to-income ratio not improving despite all this technology spend?"
- **Major incidents**: An outage traced to brittle plumbing creates political will that didn't exist the day before.

**Add the honest framing**: Competitive responses (feature launches by peers) produce incremental reaction — more plumbing, not less. Each tactical response deepens the structural problem while creating the illusion of progress. Transformational needs are opportunistic, not seasonal. The compound problem grows slowly, but the buying moments are sudden and time-limited. When the door opens, you have to be ready.

**Brief AI paragraph** (not elaborated — defer to Document 2): AI is the first technology wave that requires the structural model rather than tolerating its absence. Previous waves (internet, mobile, cloud) were channel innovations — bolt them on, add plumbing. AI is a work execution innovation — it changes who resolves the work, and you can't hand work to an AI agent if you haven't modeled what the work is. Brief statement, pointer to the full AI adoption argument.

### 1.4 Add existing spend dimension

Brief paragraph establishing banks are already spending heavily to cope — SI contracts, middleware, transformation programs, headcount for plumbing maintenance. Real, recurring, large-scale spend that doesn't address the root problem. The budget exists; it's being burned on ineffective approaches.

### 1.5 Elevate failed approaches

Move the ESB / iPaaS / API gateway / cloud migration paragraph from buried in Modernization Trap to its own prominent subsection. For Zeta's board: these are the approaches the market has tried. None addressed the root issue. The opportunity is still open.

### 1.6 Trim channel section

Keep felt consequences (fragmented views, inconsistent information, starting over at the branch). Reduce identity/session/trust-boundary technical detail to one sentence. Condense channel team incentive paragraph to one sentence.

### 1.7 Reframe Hub Way footnotes

Lead with strategic claim, not product-spec vocabulary. Use executive language — outcomes, not ontology. Keep Migration, Innovation, and Compensation footnotes as-is (already crisp). Rewrite the larger footnotes (Why This Matters Now, Organizational Reality, Systems Gap, Plumbing Problem, Modernization Trap) to lead with "why this is differentiated" rather than "what the concepts are."

### 1.8 Strengthen closing

Update Compound Picture to include the organizational reality dimension and the honest urgency framing. End with: universal (every bank), structural (not solvable by incremental fixes), worsening (each incremental response deepens it), currently unaddressed, and the buying moments are episodic — triggered by regulation, M&A, leadership, or cost pressure.

---

## Document 2: Create enterprise AI adoption problem doc

**New file**: [org-8.0/what-we-sell/enterprise-ai-adoption.md](org-8.0/what-we-sell/enterprise-ai-adoption.md)

This document makes the argument that AI is the first technology wave that makes the structural problem (from problems.md) unavoidable — and that the current approach to AI in banking will fail at enterprise scale.

### 2.1 The current state — AI as tools and projects

- Bank executives are under disproportionate pressure to show AI results
- The rational response: pick projects, demonstrate change, declare success
- Tech-inclined leaders see AI as an opportunity to insource — AI lets you build quickly
- Current state: AI is in the realm of tools, not enterprise capability

### 2.2 The tool-agent-enterprise progression

Three levels, with most banks stuck at the first:

- **Tool**: AI assists a person with a task. The person, process, and systems are still there. Marginal efficiency, nothing retired.
- **Isolated agent**: AI handles a task autonomously. Better — but an island with its own plumbing, governance, monitoring. Automates a task, doesn't simplify the domain.
- **Agents working together**: Multiple agents (human and AI) collaborating to resolve work at domain granularity. This is where real outcomes live — applications retired, headcount redeployed, work simplified, tech debt removed. But requires agents to know what work they're working on.

### 2.3 Why projects don't compound

Each AI project builds its own integration, its own governance, its own connection to systems. The 50th agent costs as much to integrate as the 1st. The compound problem reasserts itself in AI form — bespoke, brittle connections between agents and systems, domain knowledge encoded in code. Success at project scale doesn't guarantee success at domain scale.

### 2.4 Why AI is different from previous waves

Previous waves (internet, mobile, cloud) were channel innovations — additive, bolt-on, more plumbing. AI is a work execution innovation — it changes who resolves the work. This requires:

- A model of what the work is (you can't hand work to an agent without it)
- A stable abstraction that survives when the "who" changes (process maps encode human sequences, not goals)
- Governance at domain scale (who decided, what information was used, was AI involved)
- Composability (agents reuse the same model, same tool contracts, same governance)

This is the first technology wave where "add it to the plumbing" genuinely doesn't work.

### 2.5 The outcomes executives want — and why they're invisible

Executives want: people redeployed, work simplified, accuracy improved, tech debt removed, applications retired. These are domain-level outcomes that require domain-level visibility. Without a model of the domain's work, you can't even define the denominator — "what percentage of our operations is AI-augmented?" is unanswerable.

Three years in, 15 AI projects, and nothing measurable at domain level. Not because the projects failed — because project-level success doesn't aggregate into domain-level transformation.

### 2.6 The decision maker's need — a visualization model

Decision makers need a model to evaluate any AI approach (in-house, vendor, hybrid) against the question: "Will this work at domain scale? At org scale?"

The city plan analogy: you can build excellent buildings without a city plan, but you can't answer whether the neighborhood is coherent. The model doesn't replace the builders — it gives leadership a way to evaluate whether individual projects add up to operational transformation.

What the model must let the decision maker see:

- Here is all the work in this domain (finite, enumerable, comprehensible to a domain head)
- Here is who does the work today (the current dial: human, AI, automated, hybrid)
- Here is where AI could move the dial — and what that means in outcomes (people, applications, cost)
- Here is whether our approach compounds or fragments

### 2.7 The Hub Way as evaluation framework

Position the Hub Way not as a vendor product but as the thinking framework for evaluating any AI approach. Three requirements: simple enough for executives to hold (five concepts in two minutes), rigorous enough that the technical team can't dismiss it (maps to DDD, AOSM, established thinking), practical enough to drive action (start with one domain, enumerate work, identify dial opportunities, build first agents within the model, measure domain-level outcomes, expand).

Brief Hub Way mapping — in executive language, not ontology:

- A domain has work: commitments to the outside world, internal disciplines
- Work is resolved by teams: human and AI, working together
- Teams use tools from systems
- Teams interact through channels
- The dial determines how much is human vs. AI for each piece of work
- The model stays stable as the dial moves

### 2.8 Voice and tone

Same Zeta-practitioner voice as the updated problems.md. Not a whitepaper — a conviction document. Grounded in what we see across engagements. Executive-accessible language throughout — no systems ontology in the main narrative (technical rigor in appendix or footnotes if needed).