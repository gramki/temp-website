# FAQ

Audience: All.

---

## Classification Questions

### How do I know if something is a Stream or a Loop?

Apply the trigger-origin rule: Did something from outside the Hub cause this work? Stream. Did something inside the Hub cause this work? Loop. Don't classify by work type (analytical, transactional, etc.) — classify by where the trigger came from.

### What about standing obligations like "keep accounts accessible"?

That's an objective, not a piece of work. Objectives decompose into actionable Streams and Loops. "Keep accounts accessible" becomes: System Health Monitoring (Loop — internal discipline), Incident Response (Stream — triggered when an outage creates external commitments), Account Recovery (Stream — triggered when a specific customer is affected). The Hub Way classifies work, not objectives.

### What if a regulatory change arrives — Stream or Loop?

The change itself is an external trigger arriving at a Compliance Hub — that's a Stream (Regulatory Change Stream). The resulting policy updates that need to be propagated to other Hubs may be modeled as Streams in a DevOps Hub or an operational change management Hub. Each Hub sees a clear trigger at its own boundary.

### Can a Loop trigger a Stream?

Yes. This is expected and desirable. When internal discipline reveals something requiring an external commitment (fraud detected → customer notification, compliance violation → remediation), the Loop triggers a new Stream. This boundary crossing IS the business reality — it should be visible, auditable, and governed. Don't try to hide it.

### Can work be both a Stream and a Loop?

No. The trigger-origin rule is binary. But a Scenario (the execution unit) could theoretically serve both a Stream and a Loop if modeled that way — this is a modeling choice, not a framework ambiguity.

### What is the difference between "what mandates the work" and "what triggers the work"?

A regulatory mandate may require quarterly compliance checks. The mandate comes from outside (regulator), but the work is triggered internally by the Hub's own compliance schedule. The trigger origin is internal → it's a Loop. The mandate explains WHY the Loop exists, but doesn't make it a Stream.

---

## Boundary Questions

### How do I decide Hub boundaries?

Follow DDD bounded context practices. The Hub Way inherits, doesn't replace them. Use existing heuristics: Context Maps, event-storming, team cognitive load, Conway's Law alignment. A Hub should have a recognizable business domain name — "Payments," "Credit Card," not "Processing Hub."

### When should I create an aggregation Hub?

When cross-cutting analysis (compliance, fraud, customer intelligence) needs to span multiple product Hubs. The aggregation Hub's Loops consume data from product Hubs. It may also have its own Streams (regulatory filings, audit responses).

### How do I know my boundaries are wrong?

Warning signs:

- **Hub Boundary Churn:** constantly reorganizing Hubs
- **Streams that don't share any Loops or Channels:** may be two Hubs forced together
- **God Hub:** too many unrelated Streams and Loops
- **Mirror Hubs:** two Hubs sharing all their Streams
- **Empty Hub:** Streams but no Loops — not a real bounded domain
- **Island Hub:** no cross-Hub connections

---

## Channel Questions

### How is a Channel different from a UI?

A Channel embodies identity, authentication, access control, and interaction model — not just visual presentation. A UI is one possible presentation within a Channel. An API Channel has no UI at all. An MCP Channel is AI-native. A voice Channel is telephony-based.

### What about a mobile app that spans multiple Hubs?

That's a Channel Product — an Organization-scoped composite experience delivered through the Neutrino suite. It composes Channels from multiple Hubs (Payments, Credit Cards, Servicing) into a single cohesive experience for a persona. A Hub's Channel is Hub-scoped; a Channel Product is Organization-scoped.

### Who decides which Channels a Hub needs?

Domain modelers, based on the personas who interact with the Hub and their interaction paradigms. Start with: who are the personas? What interaction model suits each? Task-oriented (desk), conversational (chat/voice), programmatic (API), AI-native (MCP)?

---

## Team Questions

### How do Teams differ from Personas?

Personas are interaction archetypes — they define how someone interacts with the Hub (customer experience, agent workflow, supervisor oversight). Teams are the specific agents enrolled to resolve work. A Persona determines what Channels are available; a Team determines who is assigned to Scenarios. The same person can be part of multiple Teams and interact through different Persona-Channel combinations.

### Do Teams change when we automate?

Yes — Team composition evolves as the dial moves. A dispute investigation Team today might be three human analysts and an AI assistant. Next year, it might be one human supervisor and two AI agents. The Stream and Loop models stay the same; the Team changes. This is by design: the model separates what work exists from who resolves it.

### Are Teams Hub-scoped?

Yes, Teams are enrolled per Workbench. An individual agent (human or AI) may be enrolled in multiple Workbenches, but their Team membership is Hub-scoped. Cross-Hub Streams coordinate across Teams in different Hubs, but each Hub manages its own enrollment.

### What happens in Pure Automation — is there a Team?

In Pure Automation, there is no human Team. The Hub Application invokes Machine Tools directly without delegating tasks to agents. The "team" is effectively the Machines and the orchestrating Application. When the Application is a Seer Case Orchestration Agent, the AI agent is both the orchestrator and the sole Team member.

---

## Machine Questions

### How is a Machine different from a Channel?

Both are Hub-relative concepts. A Channel is how collaborators interact with this Hub — the participation surface. A Machine is a system this Hub uses for Tools — the capability source. Another Hub can be both: the Payments Hub might be a Machine to the Credit Card Hub (providing payment tools) and also have its own Channels that Credit Card Hub's Channel Product composes.

### Does changing a Machine affect Streams and Loops?

No. The Tool contract is the stable interface. If the bank replaces its fraud engine with a new vendor, the Machine registration changes but the Streams and Loops that use fraud scoring tools remain unchanged. This is why The Hub Way models work around Tool contracts, not system identity.

### What about AI Agents as Applications?

When the runtime is Seer, the Hub Application IS an AI Agent — the Seer Case Orchestration Agent. This agent perceives the situation, decides what to do, and acts through the Tools available from Machines. It is simultaneously a Team member (resolving the Scenario) and the Application (orchestrating the resolution). This is the Application-Agent convergence described in the Teams and Machines enablement docs.

### Can a Hub be a Machine to another Hub?

Yes. This is the Hub-as-Machine pattern (Workbench-as-Machine in Olympus Hub). A Hub can expose Tools that other Hubs consume. For example, a Shared Validation Services Hub might provide validation Tools consumed by Payments, Credit Card, and Merchant Hubs. The consuming Hub registers the providing Hub as a Machine in its Machine Registry.

---

## Scope Questions

### Does The Hub Way cover data architecture?

No. The Hub Way is an operational work modeling framework. Data architecture, product architecture, commercial architecture, integration governance, and temporal architecture are complementary concerns. The Hub Way doesn't replace or address them.

### Does The Hub Way replace DDD or AOSM?

No. It extends both. Hub = Bounded Context (DDD). Scenario = AOSM execution model. The Hub Way adds work classification (Stream/Loop) and collaboration surfaces (Channel). A DDD practitioner should recognize every Hub Way concept as consistent with their existing practice, plus additional dimensions.

---

## Modeling Pitfalls

### Don't model objectives as Streams

"Maintain customer satisfaction" is an objective. Decompose it into actionable Streams (Complaint Resolution) and Loops (Customer Satisfaction Analytics) first.

### Don't skip Stream Trace design

In banking, you can't audit what you can't observe. Every Stream should have a designed Trace — not just runtime logs, but a purposeful record of commitment fulfillment.

### Don't create Loops with no consumers

Every Loop should produce something someone uses — reports that are read, alerts that are acted on, corrections that are applied. If nothing changes because the Loop ran, it's the Inert Loop anti-pattern.

### Don't classify by work type

"This is analytical work, so it's a Loop." Wrong. Some analytical work is triggered externally (audit request → Stream). Classify by trigger origin, not by what the work does.

### Don't confuse "what mandates the work" with "what triggers the work"

A regulation mandates compliance checks. But if the bank's own schedule initiates them, they're Loops. The mandate explains why; the trigger origin determines classification.

### Don't build Channels without considering personas

Start with who interacts with the Hub, not what technology is available. Different personas have different interaction paradigms — forcing all personas through one Channel is the Monolith Channel anti-pattern.

---

## Related Documents

- [The Hub Way Framework Reference](../README.md) — authoritative definitions
- [Framework and Rationale](01-framework-and-rationale.md) — design principles and scope
- [Modeling Streams](02-modeling-streams.md) — Stream anti-patterns and heuristics
- [Modeling Loops](03-modeling-loops.md) — Loop anti-patterns and heuristics
- [Modeling Hubs](04-modeling-hubs.md) — Hub anti-patterns and heuristics
- [Modeling Channels](05-modeling-channels.md) — Channel anti-patterns and heuristics
- [Modeling Teams](06-modeling-teams.md) — Team anti-patterns and heuristics
- [Modeling Machines](07-modeling-machines.md) — Machine anti-patterns and heuristics
- [Worked Examples](10-examples.md) — anti-pattern avoidance in practice
