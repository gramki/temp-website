To build a rigorous and highly structured Information Model, we must formally define the archetypes for **Products** (the business boundary), **Modules** (the functional boundary), **Capabilities** (the specification boundary), and **Components** (the deployment boundary).

---

### Part 1: Product Archetypes (The Business Composite)

A Product Archetype defines *what* is being sold, *who* is buying it, and *how* it generates value.

To define a Product Archetype, we map it across three primary dimensions:

#### Dimension 1: Target Market (Audience Axis)

Who extracts the primary business value and who signs the check?

* **B2B (Business-to-Business):** Designed to solve organizational friction. High contract value, multiple stakeholders (users vs. buyers), strict compliance requirements (e.g., Salesforce, Workday).
* **B2C (Business-to-Consumer):** Designed to solve personal friction or provide entertainment. High volume, low individual contract value (e.g., Spotify, Netflix).
* **B2B2C (Business-to-Business-to-Consumer):** A platform sold to a business, which uses it to serve its own consumers (e.g., Shopify, Stripe).
* **Internal / Enterprise IT:** Built exclusively for employees. Focuses on operational cost reduction; no external sales mechanism.

#### Dimension 2: Delivery Model (Cloud Stack Axis)

How much of the operational burden does the vendor carry?

* **SaaS:** Vendor manages everything. Customer just logs in (e.g., Google Workspace).
* **PaaS:** Vendor provides runtime and OS. Customer brings applications and data (e.g., Heroku).
* **IaaS:** Vendor provides raw compute/storage/networking. Customer manages OS and above (e.g., AWS EC2).
* **On-Premise / Self-Hosted:** Customer runs everything on their own infrastructure.

#### Dimension 3: Go-To-Market Strategy (Growth Axis)

* **PLG (Product-Led Growth):** Product drives its own adoption through freemium, self-serve, viral loops (e.g., Slack, Notion).
* **SLG (Sales-Led Growth):** Requires human sales intervention (e.g., Oracle ERP).

**Example Product Archetypes:**

* *Enterprise SaaS:* (B2B + SaaS + SLG). Focuses heavily on the Business Value — Customer ROI dimension.
* *Consumer App:* (B2C + SaaS + PLG). Focuses heavily on the User-Centric dimension.
* *Developer Platform:* (B2B + PaaS + PLG). Focuses heavily on the Ecosystem & Extensibility dimension.

---

### Part 2: Module Functional Classification (The Customer Value Category)

A Module's Functional Classification describes *what the Module does for the customer* — the customer-value domain it serves. This is distinct from technical implementation patterns.

Classification is drawn from the **Twelve System Types** framework — a vocabulary for classifying enterprise systems by the business capability they provide. These twelve types are FinTech/banking-specific:

| Classification | What this Module does |
|---|---|
| `Record` | Maintains the authoritative state of business objects (payments, accounts, transactions). System of record — source of truth. |
| `Enforcement` | Applies rules, limits, thresholds, or compliance checks that must pass before an action proceeds (compliance screening, policy enforcement, risk controls). |
| `Data` | Aggregates, transforms, and surfaces data for reporting, analytics, or export. Primarily a read/analytical surface. |
| `Engagement` | Delivers interactive experiences directly to users — dashboards, portals, notifications, communication flows. |
| `Action` | Executes operations against external systems on behalf of the product (payment rails, bank APIs, partner networks). |
| `Intelligence` | Applies computation, modelling, or enrichment to produce derived outputs (FX rate calculation, risk scoring, ML-based classification). |
| `Identity` | Manages identity, authentication, authorization, and access control across the product. |
| `Influence` | Shapes customer or partner behaviour through incentive structures, pricing nudges, loyalty mechanics, or recommendation engines. |
| `Memory` | Provides temporal storage and retrieval of operational state or user preferences (not the system of record — ephemeral or session-scoped). |
| `Product` | Composes and packages capabilities from other modules into a coherent, configurable product experience for a customer segment. |
| `Innovation` | Hosts experimental or emerging capabilities not yet classified into a stable functional category. |
| `Integration` | Bridges between systems or external partners — transformation, protocol adaptation, routing. |

> **Note:** Module Functional Classification answers the PM's question: "what does this module do for the customer?" It does not prescribe technical implementation. A single Module may be realized by multiple Systems of multiple types. The technical deployment concerns are captured in Technical (System, Component).

**Example:** Core Payment Gateway modules:

| Module | Functional Classification | Rationale |
|---|---|---|
| Payments Module | Record | Authoritative state of payment transactions |
| FX Module | Intelligence | Computes, enriches, and caches FX rates |
| Compliance Module | Enforcement | Applies OFAC, AML, and limits checks |
| Settlement Module | Record | Authoritative state of settlement reconciliation |
| Customer Portal Module | Engagement | User-facing dashboard and interaction surface |
| Bank Connectivity Module | Integration | Bridges to bank payment rails and SWIFT |

---

### Part 3: Capability Templates (PM Specification Guides)

A Capability Template is a PM-facing specification guide applied at the **Capability level** within a PSD. Templates are selected per Capability, not per PSD — a single Module may contain Capabilities of different types.

Three templates are available. See `psd-templates/` for full template content.

| Template | When to use | PM specifies |
|---|---|---|
| `Experience` | Capability's primary expression is direct human interaction | User persona, user journey, UX channel, screens, accessibility |
| `Integration` | Capability is consumed programmatically | Consumer persona, API intent, contract shape, SLO, backward compatibility |
| `Processing` | Capability is realized through background computation | Trigger, input data, processing intent, output, SLA, error handling |

> **Decoupling note:** Capability Templates are decoupled from Component Archetypes. A PM selecting "Experience" is not prescribing a Web Application Component. The Architect independently maps Capabilities to Systems and Components in the Technical Review phase of the PSD.

---

### Part 4: Component Archetypes (Deployment Artifact Types)

A Component Archetype classifies the deployment artifact type of a Technical Component. See `dim5-component.md` for the full Component definition and examples.

| Archetype | Description |
|---|---|
| `API Service` | Synchronous request-response service (REST, gRPC, GraphQL) |
| `Web Application` | Browser-served frontend |
| `Event-Driven Worker` | Consumes events/messages from queue or stream |
| `Batch Job` | Runs on schedule or trigger; bulk data processing |
| `Data Store` | Managed data store artifact (schema package, cache config) |
| `Integration Adapter` | Connects to external system via its specific protocol |
| `Gateway` | Proxy/router managing traffic across Components |
| `CLI/SDK` | Command-line tool or language-specific library |

> The Component Archetype taxonomy can be enriched over time with FinTech-specific subtypes as patterns emerge.

---

### The Synthesis: A Product is a Constellation of Modules, Realized by Systems of Components

```
Product (B2B SaaS SLG)
  ├── Payments Module [Record]
  │     Realized by: payments-system
  │       ├── payments-service (API Service)
  │       ├── payment-reconciler (Batch Job)
  │       └── payment-notification-worker (Event-Driven Worker)
  ├── FX Module [Intelligence]
  │     Realized by: fx-system
  │       ├── fx-engine (API Service)
  │       └── fx-rate-cache (Data Store)
  ├── Compliance Module [Enforcement]
  │     Realized by: compliance-system
  │       ├── compliance-service (API Service)
  │       ├── ofac-screening-adapter (Integration Adapter)
  │       └── compliance-event-consumer (Event-Driven Worker)
  └── Customer Portal Module [Engagement]
        Realized by: customer-portal-system
          ├── portal-web-app (Web Application)
          └── portal-bff (API Service)
```

By separating these four classification layers — Product Archetype (market fit), Module Functional Classification (customer value), Capability Templates (PM specification language), and Component Archetypes (deployment artifact types) — the model serves each audience with the right vocabulary:

- **Business Analyst / PM:** sees Market (Product Archetype) and Value (Module Functional Classification + Capability Templates)
- **Architect:** sees Deployment Topology (Component Archetypes, System groupings)
- **SRE/Ops:** sees Deployment Boundaries (Systems and their Components)
