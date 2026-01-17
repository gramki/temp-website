# Scenario-Oriented Thinking: The Core Argument

> **Status**: 🟢 Design Complete  
> **Target Audience**: All (APOs, PAs, Developers)  
> **Purpose**: The central thesis — why normative-first paradigm shift matters for AI-driven automation

---

## The Problem with Current Automation Platforms

**All automation platforms focus on HOW to automate, leaving out:**
- **WHY** — the purpose, the problem being solved
- **WHAT** — the situation, the goals to be achieved

BPM gives you workflow orchestration. Low-code gives you visual flow builders. Temporal gives you durable execution. All assume you know WHAT you want — they help with HOW.

**But where does the WHAT live?**
- In requirements documents that get written once and forgotten
- In analysts' heads
- In emails and meeting notes
- Eventually, buried in code as implementation details

**To leverage AI effectively, we must fundamentally change the approach:** Put the normative (WHY, WHAT, goals) at the center. Let AI handle the HOW.

---

## Why This Matters Now

### 1. AI Needs Structured Input to Generate Automation

AI can write code. But from WHAT input?

| Current State | Problem |
|---------------|---------|
| Requirements in Confluence | AI can't reliably extract intent |
| Rules in people's heads | AI has no access |
| Business logic in scattered emails | No structured input |
| SOPs in PDF documents | Not machine-actionable |

Structured normative specifications give AI what it needs:
- Clear goals
- Explicit decision criteria
- Defined roles and responsibilities
- Compliance constraints

**Without normative specs, AI-generated automation is guesswork. With them, it's derivation.**

### 2. The Bottleneck is Shifting

| Era | Bottleneck | Platform Focus |
|-----|------------|----------------|
| **Pre-automation** | Manual execution | Digitize processes |
| **Early automation** | Coding is expensive | Make coding easier (BPM, workflow tools) |
| **Low-code era** | Developers are scarce | Let non-developers build |
| **AI era** | WHAT should happen | **Normative specifications** |

When AI can generate code, the value shifts to: **clear articulation of goals, rules, constraints.**

Platforms that don't capture normative become commodity execution layers. The differentiation moves to who has the best articulation of WHAT should happen.

### 3. Business-Tech Alignment is Structurally Broken

**Current model:**
```
Requirements (business) → Translation → Code (developers) → Drift → "Legacy"
```

- Business can't read code
- Developers become bottlenecks for rule changes
- Translation introduces errors
- Drift is inevitable
- Knowledge leaves when people leave

**Normative-first model:**
```
Normative (business-owned) → Derivation (AI-assisted) → Automation → Validation against normative
```

- Business owns the authoritative source
- AI translates, humans review
- Derivation, not duplication
- Normative IS the documentation

**This is a structural fix, not a process improvement.**

### 4. The Evolution Problem is Real

Every organization has processes where:
- The code does something, but no one knows WHY
- Regulations change, and finding what to update is archaeology
- The person who knew the rules left years ago
- Changing anything is terrifying

**If rules are in code:** Change requires developers, reverse-engineering, hope.

**If normative drives automation:** Change means updating the spec; derivation handles the rest.

---

## Addressing Concerns

### "Normative specs will become stale, just like requirements docs"

**The structural difference:**
- Requirements docs are TRANSLATED into code, then forgotten
- Normative specs DRIVE automation — they're not an intermediate artifact

**Bidirectional verification:**
- When normative is co-located with automation, you can detect drift in BOTH directions
- AI can flag when implementation diverges from normative
- Reverse correlation is possible: code ↔ normative

**The incentive changes:**
- If automation derives from normative, stale normative = broken automation
- The system makes drift visible, not hidden

### "AI-generated automation isn't mature enough"

**AI as validator, not just generator:**
- AI doesn't just generate FROM normative — it validates AGAINST normative
- AI is significantly better when it can cross-verify its work
- Normative spec becomes acceptance criteria for generated automation

**Continuous verification:**
- Not "generate once and forget"
- AI can continuously check: does automation still match normative?
- Humans remain in the loop, but AI does more with a spec to validate against

**Preparing for the trajectory:**
- AI capability is improving rapidly
- The model prepares for where AI is going, not just where it is
- Even partial AI assistance is valuable with good normative input

### "Some domains don't need this structure"

**Domain coherence over per-scenario optimization:**
- The value isn't just per-scenario efficiency
- Keeping domain context together enables comprehension of the whole business domain
- Trade-offs should be assessed at domain level, not per automation need

**Where the structure adds most value:**
- Processes that evolve over time (most of them)
- Multiple stakeholders with distinct concerns
- Audit and compliance requirements
- AI-assisted automation is part of the strategy

**Where structure may be overhead:**
- Genuinely one-off scripts that will never change (rare in practice)
- Single person owns everything end-to-end (temporary state)
- Speed to first deployment matters more than long-term evolution (short-term thinking)

**The honest assessment:** Most "simple" processes eventually need to evolve. Most "one-off" scripts become production. The structure is investment in sustainability.

### "Existing platforms could add normative layers"

**This is a thinking model, not a product claim.**
- Nothing implies no one else can or will do this
- Others can implement the paradigm
- The value is in the paradigm shift, not exclusive capability

**However, adding it as an afterthought is different from designing around it:**
- Bolted-on requirements management ≠ normative as source of truth
- The paradigm shift is fundamental: WHAT drives HOW
- Retrofitting this onto execution-focused platforms changes their architecture

### "The problem is organizational, not technical"

**Acknowledged — bad requirements aren't fixed by any alternative.**

But consider:
- Tooling shapes behavior
- If the platform REQUIRES normative specs, they get created
- Making normative first-class changes incentives
- Explicit, verifiable requirements are better than implicit, scattered ones

**The question is:** Does the approach make requirements better or worse?
- At minimum: makes them explicit and verifiable
- With AI: makes them actionable for derivation and validation
- Over time: creates institutional memory in specs, not heads

### "Adoption barrier is real"

**Reframe:** This isn't because scenario-oriented thinking is unsuitable. It's because switching may not be valuable enough in specific contexts.

**Inertia is real but separate:**
- "We've always done it this way" is not an argument against the model
- "Switching cost exceeds benefit" is a valid assessment in some contexts

**Where switching is most valuable:**
- Organizations investing in AI-assisted automation
- Domains with significant evolution and compliance needs
- Teams with business-tech alignment problems
- Long-term thinking about maintainability

**Where switching may not be worth it:**
- Stable, simple processes with no evolution pressure
- Contexts where the current approach genuinely works
- Short time horizons where upfront structure can't pay off

---

## The Paradigm Shift in Summary

| Current Paradigm | Normative-First Paradigm |
|------------------|--------------------------|
| Platforms focus on HOW | Model focuses on WHAT, HOW is derived |
| Requirements → translate → code | Normative → derive → automation |
| Business rules in code | Business rules in normative specs |
| Developer bottleneck for changes | Business updates normative, AI regenerates |
| Drift is inevitable | Bidirectional verification catches drift |
| AI guesses from scattered docs | AI derives from structured normative |
| Knowledge in people's heads | Knowledge explicit in specifications |

**This is not incremental improvement. It's a fundamental change in what the source of truth is.**

---

## Related Documentation

- [Entry Point](./scenario-oriented-thinking.md) — Overview and reading guide
- [Core Concepts](./scenario-oriented-thinking-core.md) — Foundations and specifications
- [Examples](./scenario-oriented-thinking-examples.md) — Concrete use cases
- [Comparison with Alternatives](./scenario-oriented-thinking-alternatives.md) — How this compares

---

[← Back to Entry Point](./scenario-oriented-thinking.md)
