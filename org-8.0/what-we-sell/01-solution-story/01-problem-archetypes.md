# Chapter 01: Problem Archetypes

---

**Key Question**: What types of enterprise problems support large solution businesses?

> *This chapter provides a structural taxonomy of enterprise problem types. Deeper treatment of specific problem archetypes — with industry-specific case studies and detailed economic analysis — would require a companion volume.*

---

## Taxonomy of Enterprise Problem Types

Not all enterprise problems are equal in their capacity to support durable solution businesses. Five categories recur across industries, each creating a distinct type of demand.

**Cost reduction.** The enterprise spends too much on operations that could be automated, consolidated, or re-architected. A bank running forty-year-old batch systems that consume 70% of its IT budget on maintenance has a cost reduction problem. The solution is not a cheaper contract — it is a new architecture that eliminates the structural cost.

**Regulatory compliance.** External authorities impose requirements that the enterprise cannot meet with its current capabilities. When a regulator mandates real-time transaction reporting and the bank's infrastructure processes in overnight batches, the compliance gap is architectural, not procedural. The enterprise must build or buy new capabilities to remain in operation.

**Technology transitions.** The enterprise's technology estate was built for a previous era and cannot support current or emerging requirements. Mainframe-to-cloud migration, monolith-to-microservices re-architecture, on-premises-to-SaaS transformation — each represents a structural transition that cannot be achieved by patching the existing systems.

**Capability gaps.** The enterprise lacks an institutional capability that its strategy requires. A bank that wants to launch embedded finance products but has no API layer, no real-time processing, and no partner integration framework has a capability gap. The gap is not a missing feature — it is a missing organizational ability.

**Strategic differentiation.** The enterprise needs to do something its competitors cannot. This goes beyond operational improvement — it requires building a capability that creates competitive advantage. A bank that wants to offer hyper-personalized lending decisions in real time, using proprietary data models, needs infrastructure that does not exist in off-the-shelf products.

These five categories are not mutually exclusive. The most compelling enterprise solution opportunities address two or three simultaneously — a regulatory mandate that also enables cost reduction, a technology transition that also closes a capability gap. Multi-category problems justify larger budgets, sustain longer engagements, and create deeper vendor dependencies.

---

## The Critical Filter — What Makes a "Solution Problem"

Every enterprise has problems. Only a subset of those problems sustain solution businesses. The critical filter distinguishes three categories of enterprise problems based on their structural characteristics.

### Product Problems

The problem is well-defined, bounded, and repeatable across customers without significant variation. A team needs to manage its sales pipeline. A department needs to track support tickets. An organization needs to manage employee expenses. The solution is a standardized product that the customer configures, adopts, and operates with minimal vendor involvement after purchase.

Product problems are characterized by low variance across customers, high volume of potential buyers, self-serve evaluation and adoption, and value that is realized through usage rather than through a transformation process. These are the natural domain of B2B SaaS companies. Salesforce, Zendesk, Expensify — each addresses a product problem. The customer does not need the vendor to help them reimagine their operations. They need software that works.

### Consulting Problems

The problem is unique to the enterprise, requires deep diagnostic analysis, and produces recommendations or deliverables that are specific to that institution's situation. A bank needs a strategy for entering a new market. A healthcare system needs an operating model redesign after a merger. A government agency needs a regulatory impact assessment.

Consulting problems are characterized by high uniqueness, low repeatability, and value that resides in the expertise of the people doing the work rather than in any technology artifact. There is no "product" to build because the output is advice, analysis, or a bespoke deliverable. The work does not compound — each engagement starts substantially from scratch. These are the natural domain of management consulting firms and systems integrators.

### Solution Problems

The problem sits in the space between product problems and consulting problems. It is complex enough that a standardized product cannot address it without significant configuration, integration, and organizational change. But it is repeatable enough that the technology built to solve it for one customer can be leveraged — with adaptation — for the next.

Solution problems have four defining characteristics:

**Structural complexity.** The problem spans multiple systems, processes, organizational boundaries, and stakeholder groups. It cannot be solved by deploying a single application. It requires architecture, integration, data migration, process redesign, and change management.

**Industry repeatability.** The same structural problem appears across multiple enterprises in the same industry, driven by common regulatory requirements, competitive dynamics, or technological constraints. The problem is not idiosyncratic to one institution — it is endemic to the industry.

**Co-development requirement.** The solution cannot be fully specified in advance. It must be shaped through diagnostic engagement with the customer, because the customer's specific environment — legacy systems, regulatory posture, organizational structure, risk appetite — determines how the solution is configured and delivered.

**Leverageable IP.** Despite the need for customer-specific adaptation, the core technology, architecture patterns, and delivery methodology can be reused across engagements. Each delivery makes the next one faster, cheaper, and more predictable. This is what distinguishes a solution business from a consulting business: something technological compounds from one customer to the next.

The distinction matters because it determines the business model. Product problems support SaaS economics — high gross margins, low marginal cost per customer, product-led growth. Consulting problems support services economics — revenue proportional to headcount, high utilization targets, no technology leverage. Solution problems support a hybrid model — platform revenue plus implementation services, with margins that improve as the platform matures and delivery becomes more repeatable.

Companies that misclassify their problem type build the wrong business. A company that treats a solution problem as a product problem will build a product that cannot be deployed without extensive services — but will price, staff, and organize as if services were unnecessary. A company that treats a solution problem as a consulting problem will deliver custom solutions that work brilliantly for individual clients but never compound into a platform — and will be trapped in a headcount-driven business with no leverage.

---

## The Four-Archetype Contrast

| Dimension | Consumer Product | B2B SaaS | Enterprise Solutions | SI/Consulting |
|---|---|---|---|---|
| **Problem source** | Observed user friction — something is slow, annoying, or missing in daily life. The problem is felt individually. | Observed workflow inefficiency — a business process is manual, fragmented, or poorly tooled. The problem is felt by a team or department. | Structural industry gap — a systemic condition affecting multiple enterprises, driven by regulation, technology obsolescence, or competitive dynamics. The problem is institutional. | Client-articulated need — the enterprise defines the problem and seeks help solving it. The problem is already named before the firm arrives. |
| **Validation method** | Build it and measure adoption. If users download, use, and return — the problem was real. Validation is behavioral and quantitative. | Launch and measure conversion. If businesses sign up, activate, and renew — the problem was real. Validation is commercial. | Diagnostic engagement with multiple enterprises. If three or more institutions exhibit the same structural gap and will fund its resolution — the problem is real. Validation is relational and diagnostic. | Win the engagement. If the client issues an RFP and awards the work — the problem was real enough for them. Validation is transactional. |
| **Problem scope** | Narrow and well-defined. One user, one friction, one solution. Scope is deliberately constrained to enable product focus. | Moderate and bounded. One workflow, one team, one tool. Scope may expand through land-and-expand but starts contained. | Broad and multi-dimensional. Multiple systems, multiple stakeholders, multiple phases. Scope is inherently large because the problem is institutional. | Variable and client-defined. Scope ranges from a focused advisory engagement to a multi-year transformation program, but is always defined by the client, not the firm. |

---

## In Banking

Core banking modernization is the canonical example of a solution problem — and examining why it is *not* a product problem or a consulting problem clarifies the taxonomy.

**It is not a product problem.** A bank cannot modernize its core systems by purchasing software and deploying it. The bank's legacy environment — decades of accumulated integrations, custom workflows, regulatory adaptations, and data structures — makes every modernization unique in its execution, even if the target architecture is common. No two banks have the same starting point, the same integration landscape, or the same regulatory posture. A vendor that offers a "product" without delivery capability will find that the product sits undeployed, because the bank cannot bridge the gap between the product's capabilities and the bank's operational reality without deep technical assistance. This is why core banking vendors that attempted pure SaaS models — "sign up and configure" — have consistently underperformed vendors that pair a platform with structured delivery.

**It is not a consulting problem.** A consulting firm can diagnose the modernization challenge, recommend an architecture, and even manage the program. But without a technology platform that embodies the target architecture, the consulting firm must either build custom technology for each client (expensive, slow, non-leverageable) or integrate third-party products (creating dependency on vendors the firm does not control). The consulting approach works for the first engagement. It does not compound. The second bank gets a new team, a new architecture, and a new set of custom integrations — with no leverage from the first.

**It is a solution problem.** Core banking modernization requires a technology platform (the repeatable IP), diagnostic engagement to understand each bank's specific environment (the co-development requirement), structured delivery to migrate from legacy to modern (the complexity), and the problem appears across hundreds of banks globally (the industry repeatability). The vendor that builds a core banking platform and pairs it with delivery methodology creates leverage: each deployment refines the platform, improves the delivery playbook, and produces reference customers that accelerate the next sale.

This is why the core banking market is dominated by enterprise solutions companies — Temenos, Thought Machine, Mambu, 10x Banking — rather than by SaaS companies or consulting firms. The problem's structural characteristics select for the solutions model. Companies that approach it with the wrong archetype's playbook — building a product and expecting self-serve adoption, or delivering custom solutions with no platform leverage — will underperform structurally, regardless of their technical talent or market investment.

The taxonomy is not academic. It determines what to build, how to sell, how to deliver, and how to measure success. Misclassifying the problem is the original sin of enterprise solutions strategy — and every subsequent decision inherits the error.

---

*Not every enterprise problem is a solution opportunity. The discipline of enterprise solutions strategy begins with correctly classifying the problem — and having the honesty to walk away from problems that belong to a different archetype.*
