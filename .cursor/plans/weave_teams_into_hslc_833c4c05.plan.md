---
name: Weave Teams into HSLC
overview: "Introduce \"Teams\" as a core constituent of a Hub across the HSLC documentation suite: a new enablement document (05b), updates to the narrative, framework reference, and all enablement docs that reference Hub composition. Teams represent the human and AI agents who collaborate to resolve Scenarios within Streams and Loops, grounded in AOSM's HAT concept and Olympus Hub's collaborator/agent model."
todos:
  - id: create-05b
    content: "Create new enablement/05b-modeling-teams.md with full structure: definition, composition, Streams/Loops relationship, assignment, Resolution Models, cross-Hub, anti-patterns, heuristics"
    status: pending
  - id: update-narrative
    content: Add Teams section to narrative.md between Channels and The Complete Picture; update The Complete Picture and closing
    status: pending
  - id: update-readme
    content: Add Teams subsection to README.md; update heading, scope, AOSM alignment, Hub inventory
    status: pending
  - id: update-enablement-index
    content: Add 05b to enablement/README.md audience paths and document map
    status: pending
  - id: update-01-framework
    content: "Update 01-framework-and-rationale.md: Hub-as-system table, orthogonal concerns, AOSM alignment"
    status: pending
  - id: update-04-hubs
    content: "Update 04-modeling-hubs.md: Hub aspects table, What a Hub Contains, Hub-Workbench mapping, summary"
    status: pending
  - id: update-streams-loops-channels
    content: "Light updates to 02-modeling-streams.md, 03-modeling-loops.md, 05-modeling-channels.md: Team references and Related Documents links"
    status: pending
  - id: update-06-ontology
    content: "Update 06-hslc-and-hub-ontology.md: What HSLC Adds, Agent Model bridge, Summary Mapping"
    status: pending
  - id: update-07-implementing
    content: "Update 07-implementing-hslc-in-hub.md: frame agent pools as Teams, update summary"
    status: pending
  - id: update-08-examples
    content: Add Teams tables to all 3 example Hubs and update summary checklist in 08-examples.md
    status: pending
  - id: update-09-faq
    content: Add Team Questions section to 09-faq.md
    status: pending
isProject: false
---

# Weave Teams into HSLC Documentation

## Concept Definition

**Teams** are the human and AI agents who collaborate to resolve Scenarios within Streams and Loops. They are integral constituents of a Hub -- not external operators, but the people and agents whose skills, roles, and collaboration patterns make the work possible. Teams bring together the "who" for every piece of work a Hub performs.

HSLC Teams ground in:

- **AOSM**: Human-AI Team (HAT) -- shared context, task interoperability, seamless handoff, human oversight
- **Olympus Hub**: Collaborators (Agent, Supervisor, Process Architect, Developer, APO, Administrator, Auditor), Agent Pools (human + AI + groups), Task Queues, Escalation Matrices, Resolution Models, Persona Twins

## Files to Create

### 1. New: [enablement/05b-modeling-teams.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/05b-modeling-teams.md)

Structure (following the style of existing modeling docs -- definition, tables, examples, anti-patterns, heuristics, summary, related docs):

- **Section 1: Teams as Hub Constituents** -- Teams are not external to the Hub; they are its essential participants. A Hub without Teams is an empty specification. Define Team as the set of collaborators (human and AI agents) enrolled in a Hub to resolve its Scenarios.
- **Section 2: What a Team Comprises** -- Table mapping human agent types (Operator/Agent, Supervisor, Process Architect, Developer) and AI agent types (Capable AI, Skilful AI, Scenario-as-Agent, Hub Application Agent, Persona Twins). Reference Olympus Hub's agent spectrum from `olympus-hub-docs/02-system-design/agent-model.md`.
- **Section 3: Teams in Streams and Loops** -- Teams are the "who" for each Scenario. A Stream's Scenarios require specific teams (dispute analysts for disputes, credit officers for applications). A Loop's Scenarios may require different teams (reconciliation ops for integrity loops, data engineers for preparatory loops) or no team at all (fully automated). The Resolution Model determines team involvement.
- **Section 4: Team Assignment and Structure** -- How agents are matched to work: skill-based pools, task queues, escalation matrices, allocation algorithms. Reference Olympus Hub's task allocation from `olympus-hub-docs/02-system-design/implementation-concepts/task-allocation.md`.
- **Section 5: Teams and Resolution Models** -- Link Teams to the 9 Resolution Models. Pure Automation = no team involvement. Human-AI Teaming = mixed team. AI-Autonomous = AI team within governance. The Resolution Model determines the team composition for a Scenario.
- **Section 6: Cross-Hub Teams** -- A person may participate in multiple Hubs (agent works in Payments and Servicing). Teams are Hub-scoped (enrolled per Workbench), but individuals span Hubs. Aggregation Hubs have their own teams.
- **Section 7: Team Anti-Patterns** -- The Phantom Team (Scenarios with no enrolled agents), The Monolith Team (one team for all Scenarios regardless of skill needs), The Invisible Team (work modeled without considering who resolves it), The Siloed Team (no cross-Hub collaboration paths when Streams span Hubs).
- **Section 8: Team Heuristics** -- "Every Scenario should answer: who resolves this?", "Start with Streams and Loops, then ask who participates", "Match Resolution Model to team composition", "Design for gradual automation: today's human team may become tomorrow's AI team".
- **Summary and Related Documents**

## Files to Modify

### 2. [narrative.md](org-8.0/what-we-sell/hubs-streams-loops-channels/narrative.md)

**Add a new section "Teams: Who Makes It Work" between "Channels" (line 53) and "The Complete Picture" (line 73).** Approximately 10-12 lines. Narrative style -- flowing prose, no tables. Key message: Streams and Loops define what work exists and how it is classified. Channels define how participants interact. But none of this works without the people and AI agents who actually do the work. Teams are the human and AI collaborators who bring skills, judgment, and capability to each Scenario.

Example flow:

- A dispute resolution Stream requires investigators, supervisors, AI analysts
- An interest computation Loop may require no human team at all -- fully automated
- The composition of the team determines how the work gets done: Pure Automation, Human-AI Teaming, or any point along the spectrum
- Teams evolve: today's human-heavy team becomes tomorrow's AI-augmented team, without changing the Stream or Loop model

**Update "The Complete Picture" (line 73-77)** to include Teams: "...All work executes through Scenarios -- goal-oriented definitions resolved by **Teams** of human and AI agents collaborating within governance structures through Channels."

**Update the final line (107)** to include "Teams" alongside Streams, Loops, and Channels.

### 3. [README.md](org-8.0/what-we-sell/hubs-streams-loops-channels/README.md)

- **Update heading "The Four Concepts" (line 7)** to "The Core Concepts" (keeping it neutral since naming is deferred)
- **Add a new subsection "Team -- The Collaborators" after Channel (line 64)**: concise authoritative definition (~8-10 lines). A Team is the set of human and AI agents enrolled in a Hub to resolve its Scenarios. Teams are Hub-scoped. A Hub configures which agents participate through task queues, escalation matrices, and agent pools. Reference AOSM's HAT and Resolution Models.
- **Update Scope section (line 103-108)**: add "How collaborators are structured (Teams)" to the "covers" list
- **Update Relationship to DDD and AOSM (line 111-117)**: add AOSM alignment for Teams -> HAT
- **Update Hub and Loop inventory references**: each Hub has Streams, Loops, Channels, **and Teams**

### 4. [enablement/README.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/README.md)

- Add `05b-modeling-teams.md` to both audience paths and the document map table
- Insert between row 05 (Channels) and row 06 (Ontology)

### 5. [enablement/01-framework-and-rationale.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/01-framework-and-rationale.md)

- **Section 2 "Hub-as-System Metaphor" (line 22)**: add a "Teams" row to the table: Teams | Agents/actors | Who does the work -- human and AI agents that resolve Scenarios
- **Section 3 "Four Orthogonal Concerns" (line 35)**: add Teams row to the table. Update surrounding prose to reference five concerns.
- **Section 8 "Relationship to AOSM and DDD" (line 163)**: add Teams -> HAT alignment row in the AOSM table

### 6. [enablement/04-modeling-hubs.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/04-modeling-hubs.md)

- **Section 1 table (line 11)**: add row "Collaborators / Teams | Who participates -- human and AI agents enrolled to resolve Scenarios"
- **Section 4 "What a Hub Contains" table (line 53)**: add row "Teams | Human and AI agents enrolled in the Hub, organized into pools, assigned via task queues and escalation matrices"
- **Section 7 "Hub and Workbench" table (line 112)**: add row "Teams | Agent Pools, Task Queues, Escalation Matrices"
- **Summary (line 190)**: mention Teams

### 7. [enablement/02-modeling-streams.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/02-modeling-streams.md)

- **Section 4 "Scenarios Within a Stream" (line 78)**: add a brief paragraph noting that Scenarios within a Stream are resolved by Teams -- human and AI agents collaborating through Channels. The Team composition may vary per Scenario (credit decisioning needs different skills than document collection).
- **Related Documents**: add link to 05b-modeling-teams.md

### 8. [enablement/03-modeling-loops.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/03-modeling-loops.md)

- **Section 5 "Execution Model" (line 65)**: reinforce that Loops execute as Scenarios resolved by Teams. Some Loops have no human team (Pure Automation). Others involve agents. The Resolution Model determines team involvement.
- **Related Documents**: add link to 05b-modeling-teams.md

### 9. [enablement/05-modeling-channels.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/05-modeling-channels.md)

- **Section 5 "Channel and Scenario" (line 85)**: strengthen the connection -- "Teams collaborate through Channels to resolve Scenarios." Channels are the surfaces; Teams are the participants.
- **Related Documents**: add link to 05b-modeling-teams.md

### 10. [enablement/06-hslc-and-hub-ontology.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/06-hslc-and-hub-ontology.md)

- **Section 2 "What HSLC Adds" (line 39)**: add a row for Teams -- "Collaborator structuring / Teams / The ontology defines Agent types but does not provide a Hub-level modeling vocabulary for how agents are organized as teams for work"
- **Section 3 "Agent Model Unchanged" (line 97)**: add a bridging note: HSLC's Team concept uses the ontology's Agent types unchanged but elevates the *organization of agents into teams* as a modeling concern.
- **Section 8 "Summary Mapping Table" (line 234)**: add row "Team | Maps to Agent Pools, Task Queues, Escalation Matrices. Aligns with AOSM HAT."

### 11. [enablement/07-implementing-hslc-in-hub.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/07-implementing-hslc-in-hub.md)

- **Section 1.2 or 1.3**: add a brief note connecting agent pools and task queues to the Teams concept. This doc already has detailed implementation content for agent pools (lines 101-139); add a framing sentence: "Agent pools implement the HSLC Team concept at the platform level."
- **Summary (line 622)**: mention Teams

### 12. [enablement/08-examples.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/08-examples.md)

- For each of the 3 example Hubs (Payments, Credit Card, Enterprise Compliance), add a **Teams** table after the Channels table showing:
  - Team roles (e.g., Dispute Analyst, Fraud Investigator, Reconciliation Operator)
  - Agent types (Human, AI, Mixed)
  - Which Streams/Loops they serve
- **Summary Checklist table (line 149)**: add row "Teams | Who resolves Scenarios? What agent types? What skills? What Resolution Model?"

### 13. [enablement/09-faq.md](org-8.0/what-we-sell/hubs-streams-loops-channels/enablement/09-faq.md)

Add a **Team Questions** section with 3-4 entries:

- "How do Teams differ from Personas?" -- Personas describe interaction archetypes (Agent, Supervisor, Customer). Teams describe the *specific composition* of agents enrolled to resolve work in a Hub.
- "Do Teams change when we automate?" -- Team composition evolves with Resolution Model. A Scenario moving from Human-AI Teaming to AI-Autonomous changes the team, not the Stream or Loop.
- "Are Teams Hub-scoped or can they span Hubs?" -- Teams are Hub-scoped (enrolled per Workbench). Individuals may participate in multiple Hubs. Cross-Hub Streams are coordinated through context sharing, not shared teams.

### 14. [critique.md](org-8.0/what-we-sell/hubs-streams-loops-channels/critique.md)

- No substantive change needed. Teams are an addition to the framework, not a response to a critique concern.

## Style Consistency Notes

- **Narrative**: flowing prose, `---` dividers, no tables, bold for key terms on first use, banking examples
- **README (framework ref)**: concise authoritative definitions, tables for structure, minimal prose
- **Enablement docs**: section-numbered, tables for comparison/examples, anti-patterns as H3 with Problem/Sign/Remedy structure, heuristics as tables, Summary paragraph, Related Documents section
- **Capitalize**: Hub, Stream, Loop, Channel, Team, Scenario (as framework terms)

