# Engagement Operating Model: Definitions, Usage, and Governance Guide

---

# 1. Purpose

This document establishes the core constructs in our operating model:

* **Engagement** (assembly construct)
* **Engagement Engineering** (assembly discipline)
* **Engagement Success** (outcome/adoption function — owned by the EPM role)
* **Exploration** (pre-commitment construct)

Together, they define how we **deliver customer-specific value** using Product Lines without drifting into a services model.

This guide provides:

* Canonical definitions
* Clear boundaries and relationships
* Leadership DOs and DON'Ts
* Staffing principles and patterns
* Style guide for consistent usage
* FAQ to address common concerns

---

# 2. Canonical Definitions

## 2.1 Engagement (Assembly Construct)

> **Engagement** is the complete collection of software artifacts — configurations, extensions, integrations, and studio-built components — that together constitute a customer-specific product instantiation derived from Product Lines. More completely, an Engagement is the **governed transformation of one banking domain**: the domain's work discovered as a **Work Model**, the customer's existing estate **inducted** into it (wrapped in Tool Contracts and registered as Machines — see The Hub Way's Modeling Machines chapter), the gaps composed from Product Lines and fabrics, and an **Agent Swarm** employed as part of the deliverable.

An Engagement is not a contract, a relationship, or a form of activity. It is a **thing**: the set of artifacts that, taken together, make up what a specific customer receives. These artifacts derive from Product Lines; they are not bespoke builds. The collection spans more than software in the narrow sense: it includes the Work Model that makes the domain's work explicit, the Tool Contracts and declarative specifications through which the customer's existing systems are enrolled rather than replaced, and the definitions, evaluation records, authority grants, and guardrail configurations of the employed Agent Swarm. There is no formal packaging mechanism today (no manifest or bill of materials) that binds these artifacts into a single deployable unit — the Engagement is the logical container that groups them.

**What it represents:**

* A **bounded artifact collection** derived from Product Lines
* A **governed domain transformation** — the domain's work made visible as a Work Model, its estate inducted, and an Agent Swarm employed to resolve work alongside the customer's people
* A **unit of delivery accountability** — who is responsible for assembling and delivering these artifacts
* A **pipeline element** (plan, sequence, prioritize across the portfolio)
* A **governed lifecycle** (Initiate → Discover → Build → Transfer → Complete) that controls how the collection is assembled and delivered

---

## 2.2 Engagement Engineering (Discipline)

> **Engagement Engineering** is the discipline of designing and assembling customer-specific product instantiations by leveraging Product Lines and studio-built components, ensuring scalable, repeatable, and high-quality delivery.  


**What it represents:**

* The **how** of assembly
* Patterns, accelerators, and architectures for reuse
* Engineering rigor across integration, orchestration, and experience layers

For a detailed breakdown of how Engagement Engineering is practiced—including boundaries, artifact groups, and operating model—see [Engagement Engineering in Practice](engagement-engineering-in-practice.md).

---

## 2.3 Engagement Success (EPM-Owned Function)

> **Engagement Success** is the function responsible for ensuring that an Engagement is successfully deployed and adopted in the customer's environment — driving readiness, orchestrating adoption, and ensuring value delivery. It is **owned by the EPM** as part of the EPM role, not a separate organizational unit.

**What it represents:**

* The **customer-side delivery** of value — beyond engineering completion
* Readiness, adoption tracking, and value delivery assessment
* A named responsibility within the EPM role — not a standalone team or function

Engagement Success is why the EPM role extends beyond traditional program management. The EPM doesn't just coordinate delivery; the EPM owns the outcome: is the customer using what was delivered, and is it delivering value? See [Roles and Responsibilities](roles.md) for the full EPM role description.

---

## 2.4 Exploration (Pre-Sales Construct)

> **Exploration** is the pre-commitment work of discovering customer needs, assessing feasibility, shaping a potential solution, and qualifying whether an Engagement should be initiated.

**What it represents:**

* All pre-sales activity (discovery, scoping, POC, technical evaluation)
* A **qualification gate** — not every Exploration becomes an Engagement
* Accountable to Sales and Pre-Sales; not to delivery squads

**Boundary:** An Exploration becomes an Engagement when a customer commitment triggers the delivery lifecycle. Until that point, it is not an Engagement.

---

# 3. Relationship to Core Constructs

| Construct                  | Role                                                                   |
| -------------------------- | ---------------------------------------------------------------------- |
| Product Line               | Source of reusable capability                                          |
| Customer Product           | Structured instantiation of Product Lines                              |
| Studio                     | Execution units (squads) building integration, extensions, experiences |
| **Engagement**             | Artifact collection that constitutes the customer-specific product instantiation |
| **Engagement Engineering** | Discipline that assembles the system                                    |
| **Engagement Success**     | EPM-owned function that ensures customer-side success (readiness, adoption, value delivery) |
| **Exploration**            | Pre-commitment work that qualifies whether an Engagement should begin  |

---

# 4. What an Engagement Includes

## 4.1 Artifact Groups

An Engagement contains five artifact groups:

* **Work Model artifacts** — the domain's Work Model (Streams, Loops, Scenarios, Teams, Machines, Channels), the Tool Contracts under which existing customer systems are inducted as Machines, and the declarative specifications extracted from the estate's operational intelligence (see The Hub Way's Modeling Machines chapter)
* **Workforce artifacts** — agent definitions for the employed Agent Swarm, training and evaluation records, authority grants delegated from accountable humans, and guardrail configurations
* **Customer Product artifacts** — Product Line configurations, extensions, platform integrations, and customer-specific business logic
* **Studio Component artifacts** — integration adapters, orchestration flows, custom experiences (UIs, workflows, applications), and operational artifacts (runbooks, escalation matrices, monitoring configurations)
* **Verification artifacts** — test environment definitions (IaC), assembly-level test suites, test data preparation tooling, CI orchestration configurations, and certification records. These are codified engineering — version-controlled and maintained with the same rigor as functional code. See [Verification and Certification](verification-and-certification.md).

Together, these artifacts make up the assembled product instantiation for a specific customer. Verification and Workforce artifacts are deliverables — they are handed over at Transfer.

## 4.2 Lifecycle Phases

An Engagement is assembled through five lifecycle phases, beginning after customer commitment (the Exploration-to-Engagement boundary):

* **Initiate** — kickoff, scope confirmation, operating model agreement
* **Discover** — detailed requirements, solution architecture, team composition, gap analysis
* **Build** — platform configuration, extensions, integrations, studio-built components, testing, go-live
* **Transfer** — handover per operating model, knowledge capture
* **Complete** — stabilization, squad release, close-out

---

# 5. What an Engagement is NOT

An Engagement is NOT:

* A contract or statement of work — Engagements may be governed by a contract, but they are not the contract itself
* A customer relationship — the relationship is between Zeta and the customer; the Engagement is the artifact collection delivered within that relationship
* A project for staffing or billing purposes
* A pool of resources assigned temporarily
* A generic client interaction
* A ticket or work item
* A purely technical deployment
* A pre-sales activity — any work performed during pre-sales phases is an **Exploration**, not an Engagement

> Engagements represent **structured product assembly**, not services execution.

---

# 6. Why These Terms

## 6.1 Engagement

* Re-purposed as a technical noun denoting the **artifact assembly** — not a contract, relationship, or activity
* Distinguishes from "project" (process-centric) and "solution" (vague, services-flavored)
* Capitalizing it creates a formal term that overrides everyday connotations
* Scales to pipeline and governance

## 6.2 Engagement Engineering

* Elevates assembly to a **repeatable engineering discipline**
* Emphasizes patterns, reuse, and architecture
* Avoids framing as ad hoc implementation

## 6.3 Engagement Success

* Anchors **ownership of outcomes and adoption** within the EPM role
* Distinguishes the EPM from a traditional program manager — the EPM owns delivery *and* adoption
* Avoids PMO/services connotations — the function is about customer outcomes, not project reporting

---

# 7. Leadership Guidelines (DOs and DON'Ts)

## 7.0 Across All Constructs

### DO

* Treat the constructs as **distinct and complementary**
* Reinforce definitions consistently
* Keep Product Lines as the primary source of capability

### DON'T

* Do NOT collapse them into a single "delivery" function
* Do NOT use them interchangeably

---

## 7.1 Engagement (Assembly Construct)

### DO

* Use as a **formal construct** (capitalize)
* Anchor every Engagement to Product Lines
* Manage **pipeline, readiness, and outcomes**

### DON'T

* Do NOT use Engagement to mean staffing or projects
* Do NOT allocate individuals dynamically across Engagements
* **Do NOT staff an Engagement directly**
* Do NOT measure success via utilization/hours
* Do NOT use Engagement for pre-sales work — the correct term is **Exploration**

---

## 7.2 Engagement Engineering (Discipline)

### DO

* Build **reusable patterns and accelerators**
* Enforce architectural alignment with Product Lines
* Treat as a **core engineering capability**

### DON'T

* Do NOT reduce to "integration-only" work
* Do NOT allow divergence from Product Line principles
* Do NOT treat as ad hoc implementation

---

## 7.3 Engagement Success (EPM Responsibility)

Engagement Success is owned by the EPM. These guidelines apply to the EPM when exercising the Success function:

### DO

* Own readiness, adoption tracking, and value delivery assessment as part of the EPM role
* Drive lifecycle progression beyond engineering completion — the Engagement isn't done when code is deployed; it's done when the customer is using it
* Collaborate with EPO (training/enablement), EA (architecture handover), and SRE Lead (operational readiness) to drive adoption

### DON'T

* Do NOT reduce the EPM role to coordination and reporting — Engagement Success is what distinguishes EPM from a traditional PM
* Do NOT treat adoption as someone else's problem — the EPM owns it
* Do NOT conflate Engagement Success with engineering delivery — ELs own squad delivery; the EPM owns the outcome

---

# 8. Behavioral Guardrails (Studio Work)

* Squads must remain stable
* Product Lines remain the primary source of capability
* **Studio work may include integration, extensions, and customer-specific experiences (UX, workflows, applications), but must remain anchored to the Customer Product and Product Lines, without creating parallel standalone systems**
* Engagements must not become open-ended custom development efforts

## 8.1 Allowed vs Anti-Patterns

| Category      | Allowed (Aligned)                               | Anti-Pattern (Drift)                                  |
| ------------- | ----------------------------------------------- | ----------------------------------------------------- |
| Integration   | Connectors/adapters to customer systems         | Rebuilding core capabilities outside Product Lines    |
| Extensions    | Business logic extending Product Line APIs      | Forking/duplicating Product Line logic                |
| Experiences   | Custom UIs/workflows on top of Customer Product | Standalone apps bypassing Customer Product            |
| Orchestration | Automation using Product Line services          | Independent orchestration replacing platform behavior |
| Data          | Mappings aligned to product schemas             | Parallel data models diverging from Product Lines     |

## 8.2 Guiding Principle

> **Extend, don't fork.**

## 8.3 Leader Test

Ask: *"Is this amplifying the Product Line, or replacing it?"*

Borderline cases are adjudicated by the **Engagement Architect** in consultation with Product Line leadership. When Product Line Squads and Customer Product Squads disagree on whether work is extension or divergence, the Engagement Architect makes the call — escalating to engineering leadership if needed.

## 8.4 Tech Debt Repatriation

Engagement-specific work that proves reusable should fold back into Product Lines via **inner source** (structured contribution from Customer Product Squads to Product Line Squads). Engagement-specific work that remains one-off must be documented and owned by the Customer Product Squad for the lifecycle of the Engagement.

---

# 9. Staffing Principles and Patterns

## 9.1 Core Principle

> **Assign engineers to squads, not to Engagements.**

* Engagements are delivered **by squads**, not staffed as containers of individually assigned resources
* Assignments exceeding **two quarters** are considered **long-term associations**

## 9.2 Engagement Role Structure

Each Engagement has a defined role hierarchy:

| Role | Responsibility |
|------|---------------|
| **Client Partner** | Senior-most per-client role; strategic client relationship; EO reports to Client Partner; assigned by ERC |
| **Engagement Owner (EO)** | Overall accountability for the Engagement; final escalation; reports to Client Partner; assigned by ERC |
| **Engagement Program Manager (EPM)** | Customer-facing contact; integrated view; Engagement Success |
| **Engagement Architect (EA)** | Architecture across the entire span; variability (Architecture or Engineering function) |
| **Assembly Verification Architect (AVA)** | Assembly certification; release authority (Architecture or Engineering function) |
| **Engagement Product Owner (EPO)** | Customer discovery; requirements; training |
| **SRE Lead** | Operational readiness |
| **Engineering Lead (EL)** | Per-squad delivery and tech leadership |
| **Squad PM** | Squad-level backlog prioritization (product role) |
| **Scrum Master** | Process facilitation (1-3 squads); reports to EPM |
| **Portfolio Program Manager (PPM)** | Cross-Engagement capacity coordination; staffing demand consolidation (ERC function) |

See the [Engagement Operating Model Guide](README.md) for full role descriptions and the escalation model.

## 9.3 Four Squad Types

```
                          Engagement
                               │
        ┌──────────┬───────────┼───────────┬──────────┐
        │          │           │           │          │
  Customer    Studio      Verification  Product Line
  Product    Components                  │
        │          │           │       ┌──┴───┐
   ┌────┴────┐    ...        AVA     PL Sq X  PL Sq Y
   │         │              Squad
 CP Sq A   CP Sq B
```

Five artifact groups make up the Engagement Assembly: **Work Model artifacts**, **Workforce artifacts**, **Customer Product artifacts**, **Studio Component artifacts**, and **Verification artifacts** (see [Section 4.1](#41-artifact-groups)). Squads assemble these artifacts; the Engagement is what they produce. CP and Studio squads are led by an **Engineering Lead (EL)**; the Verification Squad is directed by the **AVA**.

### Customer Product Squads

* Assembled to deliver the Customer Product for an Engagement
* Configure and extend Product Lines; they do not fork or own Product Line code
* Engineers are assigned from Product Line Squads; assignments >2 quarters are long-term

### Product Line Squads

* Stable, long-lived squads owning Product Line (platform) capability
* Own reusable capability evolution, platform maturity, and reliability
* Engineers may be assigned to Engagement squads for delivery

### Studio Squads

* Stable squads building integration, extensions, and customer-specific experiences (UX, workflows, applications)
* Build reusable accelerators where possible
* May include dedicated migration squads when data migration is required

## 9.4 Engagement Activation Model

* Define Customer Product
* ERC assigns Client Partner (per-client), EO, EPM, EA, AVA, and ensures CPA support for the Client Partner; PPM coordinates squad staffing demand
* Activate relevant CP, Studio, Verification, and PL Squads
* EO assigns ELs, EPO, SRE Lead; squads are staffed through PPM at Discover
* Execute lifecycle phases (Initiate → Discover → Build → Transfer → Complete)

## 9.5 Elastic Capacity (Controlled)

* Adjust squad size deliberately
* Spin up temporary, domain-aligned squads if needed
* Avoid ad hoc individual reassignment across Engagements
* EPM coordinates staffing needs; ERC Portfolio Program Manager maintains cross-Engagement view

## 9.6 Squad Capacity Prioritization

* When multiple Engagements compete for squad capacity, **prioritization is a leadership responsibility** — not resolved through ad hoc individual reassignment
* Leaders set priority based on strategic alignment, customer commitment, and contract obligations
* ERC Portfolio Program Manager supports prioritization decisions

## 9.7 Leadership Responsibilities

* Protect squad stability
* Prevent Engagement-driven fragmentation
* Maintain Product Line alignment

---

# 10. Style Guide for Usage

## 10.1 Capitalization

Always capitalize constructs:

* Engagement
* Engagement Engineering
* Engagement Success
* Exploration

Note: "engagement" is a common English word. The capitalized form **Engagement** refers exclusively to the formal assembly construct defined in this document. Lowercase "engagement" in casual conversation (e.g., "customer engagement is strong") does not carry this meaning.

## 10.2 Customer-Facing Language

"Engagement" may be used with customers when referring to the delivery lifecycle. In customer-facing contexts, ensure it is understood as the assembled product they receive — not a generic services interaction.

## 10.3 Preferred Usage

* "Engagement built on [Product Line]"
* "Engagement Engineering patterns"
* "Engagement Success milestones"

## 10.4 Avoid

* Using terms interchangeably
* "Engagement resources"
* "Assign people to Engagement"
* "Pre-sales engagement" (use **Exploration**)

## 10.5 Replace with

| Incorrect              | Correct                  |
| ---------------------- | ------------------------ |
| Engagement resources   | Squad capacity           |
| Engineering engagement | Engagement Engineering   |
| Engagement manager     | EPM (Engagement Success) |
| Pre-sales engagement   | Exploration              |

---

# 11. FAQ

**Q1: Is an Engagement a project?**
No. An Engagement is a collection of software artifacts derived from Product Lines. It has a lifecycle that governs how it is assembled, but the Engagement itself is the artifacts — not the process.

**Q2: Does Engagement mean services work?**
No. An Engagement is a set of software artifacts derived from Product Lines — not a scope of billable work. Its artifacts are configurations, extensions, and integrations of existing platforms, not bespoke custom development.

**Q3: Who owns an Engagement?**
The Engagement Owner (EO) has overall accountability for the Engagement and reports to the Client Partner. The Client Partner is the senior-most per-client role (may span multiple Engagements with the same client). Responsibilities are distributed: EPM owns customer-facing delivery and Engagement Success; EA owns architecture; AVA owns assembly verification; EPO owns requirements and training; ELs own squad delivery; SRE Lead owns operational readiness. See the [Engagement Operating Model Guide](README.md) for the full role structure.

**Q4: What does Engagement Engineering do?**
Designs and assembles customer-specific systems using Product Lines with reusable patterns.

**Q5: What does Engagement Success do?**
Ensures readiness, adoption, and value delivery in the customer environment. It is owned by the EPM as part of the EPM role — not a separate team or function. The EPM drives adoption tracking and value delivery assessment beyond engineering completion.

**Q6: How is success measured?**
By delivery outcomes, not utilization. Key metrics include: delivery velocity (time from Initiate to production), reuse ratio (proportion from Product Lines vs. net-new custom), assembly certification pass rate (AVA), customer satisfaction and adoption (EPM/Engagement Success), and handover quality.

**Q7: When does an Exploration become an Engagement?**
When a customer commitment triggers the delivery lifecycle. The Exploration-to-Engagement boundary is a formal gate: until customer commitment exists, the work is an Exploration. After commitment, the Engagement lifecycle begins with the Initiate phase.

**Q8: How do Engagement learnings flow back to Product Lines?**
Through structured review and inner source. Customer Product Squads contribute reusable patterns, extensions, and platform enhancements back to Product Line Squads via inner source contributions. Engagement retrospectives and knowledge capture feed into Product Line roadmap decisions.

**Q9: What artifacts make up an Engagement?**
Five groups: (1) Work Model artifacts — the domain's Work Model, Tool Contracts for inducted systems, and declarative specifications; (2) Workforce artifacts — agent definitions, training and evaluation records, authority grants, and guardrail configurations; (3) Customer Product artifacts — Product Line configurations, extensions, platform integrations, and customer-specific business logic; (4) Studio Component artifacts — integration adapters, orchestration flows, custom experiences, and operational artifacts (runbooks, escalation matrices, monitoring configurations); (5) Verification artifacts — IaC environment definitions, assembly-level test suites, test data preparation tooling, CI orchestration configurations, and certification records. See [Section 4.1](#41-artifact-groups).

**Q10: What changed with the role structure?**
The Customer Product Delivery Lead (CPDL) role has been retired. Its responsibilities are now distributed across specialized roles: Client Partner (senior-most per-client role; EO reports to Client Partner), Client Partner Associate (CPA) for generalist support to the Client Partner, Engineering Lead (EL) for squad delivery, Engagement Program Manager (EPM) for customer-facing coordination and Engagement Success, Engagement Product Owner (EPO) for requirements and training, Assembly Verification Architect (AVA) for assembly certification, Engagement Owner (EO) for overall Engagement accountability, and SRE Lead for operational readiness. See the [Engagement Operating Model Guide](README.md).

---

# 12. Final Positioning

We do not run projects.
We do not execute services.

> We deliver **Engagements** through **Engagement Engineering**, and the EPM ensures customer outcomes through **Engagement Success**.
>
> An Engagement is software and an employed workforce, not a service.

---

# 13. Related Documents

| Document | What It Covers |
|----------|---------------|
| [Engagement Operating Model Guide](README.md) | Complete role structure, lifecycle, governance, and practitioner guidance |
| [Why "Engagement" — Terminology Deliberation Record](whats-in-the-name.md) | Naming rationale and vocabulary system |
| [Engagement Lifecycle](../product-line-engineering/processes/engagement-lifecycle.md) | Detailed lifecycle phase activities |

---

End of Document
