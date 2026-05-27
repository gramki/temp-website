---
name: Business Model Narrative
overview: Transform the structured business-model.md into a Simon Sinek-style narrative memo for senior management, following the Why-How-What arc.
todos:
  - id: write-narrative
    content: Write business-model-narrative.md following the confirmed outline
    status: completed
isProject: false
---

# Business Model Narrative — Outline

**Source:** [business-model.md](org-8.0/what-we-sell/business-model.md)
**Target:** `org-8.0/what-we-sell/business-model-narrative.md`
**Style:** Simon Sinek — Start with Why, written as a leadership memo to be read
**Length:** 3-4 pages

---

## Proposed Structure

### 1. The Tension (opening — 1-2 paragraphs)

- Banks are caught between two forces: the pressure to innovate and the weight of legacy technology
- The cost of standing still is rising (obsolescence, customer expectations, regulatory complexity, competitive pressure from fintechs)
- Most technology vendors offer banks more features; few offer them genuine leverage

*Purpose: create the problem space that makes the "Why" inevitable*

### 2. Why We Exist (the core belief — 1-2 paragraphs)

- "Democratize Banking" — the belief that every bank, not just the largest, should have the technology to innovate, reduce cost, improve accessibility, and increase reach
- This is not a product pitch. It is the organizing principle behind every decision we make: what we build, how we sell, who we hire, how we engage

*Purpose: establish the Sinek "Why" — the cause that precedes the business*

### 3. Who We Serve (the three conversations — ~1 page)

Three distinct personas, each with their own version of the same question: "Why should I trust Zeta?"

- **The CIO/CTO conversation**: technology control, cost of ownership, scalability, migration safety, integration, deployment flexibility, AI assurance, talent availability
- **The Business team conversation**: speed to market, competitive differentiation, customer experience, revenue growth, partner ecosystems, lifecycle management
- **The Risk/ISG/Procurement conversation**: compliance assurance, regulatory certification, data governance, security posture, third-party risk management, proof of enterprise readiness

Each framed as a narrative paragraph (not bullet lists), showing how the same underlying belief — democratize banking — manifests differently for each stakeholder.

*Purpose: show that we understand the buyer, not just the product*

### 4. The Gap: Why This Is Hard to Find (the market reality — 2-3 paragraphs)

Before describing what Zeta delivers, establish *why buyers struggle to find it*. The market is structured in a way that fragments what banks actually need:

- **Core banking vendors** (Temenos, FIS, Fiserv) offer breadth but are legacy-heavy, slow to evolve, and lock banks into rigid upgrade cycles. They sell features, not leverage.
- **Fintech point solutions** (Marqeta, Galileo, nCino) are modern but narrow — they solve one domain and leave integration, compliance, and lifecycle management to the buyer.
- **Cloud/platform vendors** (AWS, Azure) offer infrastructure but no banking domain knowledge. Banks still have to build everything themselves or hire an SI.
- **Systems integrators** (Accenture, TCS, Infosys) offer delivery capacity but no product IP. Every engagement starts from scratch; nothing compounds.

What banks actually need is the intersection: modern product IP with deep banking domain expertise, delivered through an engineering methodology that transfers knowledge and control — not a vendor that does one of these well and ignores the rest. This combination is rare because building it requires sustained investment across all four dimensions simultaneously.

The result: banks compromise. They pick the vendor that's best at *one* of these dimensions and accept weakness in the others. Or they assemble a patchwork of vendors that don't compose. Either way, they don't get leverage — they get complexity.

*Purpose: create the "aha" moment — the buyer's frustration is structural, not incidental. Position Zeta's model as the answer to a real gap, not a marketing claim.*

### 5. How We Deliver: The Leverage Model (the "How" — ~1.5 pages)

Introduce "Zeta Leverage" as the central concept — not just cheaper or faster, but a compounding structural advantage across five layers:

- **Infrastructure Leverage** (Estate, Cipher, LakeStack, Foundry): compliance-by-design, zero-trust security, privacy engineering, reliable runtimes, agentic operations. Names the platforms but explains what they *mean* for the buyer rather than listing acronyms.
- **Integration Leverage** (Hub): the Hubs, Streams, and Loops framework. Banks don't just need applications — they need composable business domains (Hubs), connected value streams (Streams), and autonomous improvement cycles (Loops). Reference the specific banking hubs (Payments, Credit Cards, CLM, Servicing, etc.)
- **Frameworks Leverage** (Product Factory, CLCM, Digital Experiences): the reusable business capability layer — product lifecycle management, customer lifecycle management, servicing and experience orchestration. This is what turns infrastructure into bank-ready capability.
- **Product Line Leverage** (Tachyon, Neutrion, Electron): the ready-to-deploy banking products that sit on top of the stack. Reference the specific product lines to ground the abstraction.
- **Engagement Engineering Leverage**: the methodology that activates everything above for a specific customer. This is not professional services — it is a repeatable engineering discipline. An Engagement is an *assembly construct*: the complete collection of configurations, extensions, integrations, and studio-built components that form a customer-specific product instantiation derived from Product Lines. Key elements to narrate:
  - **Lifecycle discipline** (Initiate, Discover, Build, Transfer, Complete) — every engagement follows the same governed phases
  - **Squad model** (Customer Product Squads, Studio Squads, Verification Squads) — engineers are assigned to squads, not to projects; staffing is deliberate, not opportunistic
  - **Three artifact groups** — Customer Product artifacts, Studio Component artifacts, and Verification artifacts — verification is a deliverable, not an afterthought
  - **Ownership boundary** — Engagement squads own the derived product; Product Line squads own the platform. This keeps the platform clean and the engagement focused.
  - **Inner source** — reusable work flows back to Product Lines through governed contribution, so every engagement strengthens the platform for the next one
  - **Behavioral guardrails** — extend don't fork, no parallel systems, studio work stays anchored to Product Lines
  - This is the lever that competitors cannot replicate by buying technology alone — it requires building an organizational discipline

The key narrative point: each layer amplifies the one below it. Infrastructure makes frameworks reliable. Frameworks make product lines fast to build. Product lines make engagement assembly fast and repeatable. Engagement Engineering is what delivers the compounding leverage *to the customer*. Without it, the other four layers are potential energy. With it, they become outcomes.

*Purpose: show the "How" as a system, not a list of capabilities. Engagement Engineering is the connective tissue that makes the leverage real.*

### 6. How We Sustain (the durability argument — 2-3 paragraphs)

- Operations maturity as competitive moat (SRE, DevOps, AI Ops)
- Human-AI teams as the way work gets done
- Continuous evolution of Engagement Engineering practices — the methodology itself improves with each engagement
- Inner source philosophy — every engagement enriches the platform
- Academies, certifications, and training programs

Framed as: leverage that isn't sustained isn't leverage — it's a temporary advantage. Here's how we make it durable.

*Purpose: answer the unasked question — "will this still be true in 3 years?"*

### 6. Close (1 paragraph)

Return to the Why. The revised business model isn't a new strategy — it's a clearer articulation of what we've always believed. Democratizing banking means giving every bank the leverage to act like the best-funded bank in the world. That's what we sell.

---

## Key Narrative Principles

- No bullet lists in the final document — everything in flowing prose
- Technical concepts named but explained in outcome terms (e.g., "zero-trust security architecture" not "CSPM, DLP, XDR")
- Product names used to ground abstractions (Tachyon, Neutrion, Electron, Hub, Cipher, Estate, LakeStack)
- Each section builds on the previous — the reader should feel a logical inevitability
- Sinek's signature move: repetition of the core belief as a through-line ("This is what it means to democratize banking")

