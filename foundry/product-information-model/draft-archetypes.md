To build a rigorous and highly structured Information Model, we must formally define the archetypes for both **Products** (the business boundary) and **Modules** (the technical boundary).

Because a Product is a composite that *contains* multiple Modules, they are measured on entirely different dimensional axes. Products are measured by market mechanics, while Modules are measured by software physics.

Here is the definitive breakdown of Product Archetypes and Module Archetypes, complete with their defining dimensions.

---

### Part 1: Product Archetypes (The Business Composite)

A Product Archetype defines *what* is being sold, *who* is buying it, and *how* it generates value. It ignores the underlying code.

To define a Product Archetype, we map it across three primary dimensions:

#### Dimension 1: The Target Market (Audience Axis)

Who extracts the primary business value and who signs the check?

* **B2B (Business-to-Business):** Designed to solve organizational friction. High contract value, multiple stakeholders (users vs. buyers), and strict compliance requirements (e.g., Salesforce, Workday).
* **B2C (Business-to-Consumer):** Designed to solve personal friction or provide entertainment. High volume, low individual contract value, single user/buyer (e.g., Spotify, Netflix).
* **B2B2C (Business-to-Business-to-Consumer):** A platform sold to a business, which that business uses to serve its own consumers (e.g., Shopify, Stripe).
* **Internal / Enterprise IT:** Built exclusively for employees within the organization. Focuses purely on operational cost reduction; no external sales mechanism (e.g., an airline's custom crew-scheduling software).

#### Dimension 2: The Delivery Model (Cloud Stack Axis)

How much of the underlying operational burden does the vendor carry versus the customer?

* **SaaS (Software-as-a-Service):** The vendor manages everything (data, runtime, middleware, OS, servers). The customer just logs in (e.g., Google Workspace).
* **PaaS (Platform-as-a-Service):** The vendor provides the runtime framework and OS. The customer brings their own applications and data (e.g., Heroku, AWS Elastic Beanstalk).
* **IaaS (Infrastructure-as-a-Service):** The vendor provides raw compute, storage, and networking. The customer manages the OS and everything above it (e.g., AWS EC2).
* **On-Premise / Self-Hosted:** The customer buys the software license and runs it entirely on their own physical or private cloud infrastructure.

#### Dimension 3: The Go-To-Market Strategy (Growth Axis)

How is the product designed to acquire and expand its user base?

* **PLG (Product-Led Growth):** The product drives its own adoption through freemium tiers, self-serve onboarding, and viral loops. UX/UI is the primary sales tool (e.g., Slack, Notion).
* **SLG (Sales-Led Growth):** Requires human intervention (Account Executives, Solution Architects) to demo, negotiate, and implement. Driven by relationships and RFP responses (e.g., Oracle ERP).

**Example Product Archetypes:**

* *Enterprise SaaS:* (B2B + SaaS + SLG). Focuses heavily on the *Business Value - Customer (ROI) Dimension*.
* *Consumer App:* (B2C + SaaS + PLG). Focuses heavily on the *User-Centric Dimension*.
* *Developer Platform:* (B2B + PaaS + PLG). Focuses heavily on the *Extensibility Dimension*.

---

### Part 2: Module Archetypes (The Technical Execution)

A Module Archetype defines *how* a specific bounded context of the product is built, deployed, and interacted with.

To define a Module Archetype, we map it across our two strict MECE (Mutually Exclusive, Collectively Exhaustive) technical dimensions:

#### Dimension 1: The Interaction Boundary (Trigger Axis)

How do data and commands enter and exit this specific module?

* **Human-Interactive (Synchronous UI):** Requires a human to provide inputs and await visual outputs.
* *Focus:* Usability, accessibility, time-to-interact.
* *Examples:* Web Dashboards, Mobile App Frontends, Command Line Interfaces (CLIs).


* **Programmatic-Interactive (Synchronous M2M):** A machine or external system sends a request and waits for a response.
* *Focus:* API contracts, latency, throughput, backward compatibility.
* *Examples:* REST APIs, GraphQL servers, gRPC endpoints.


* **Reactive / Background (Asynchronous):** Triggered by system events, message queues, or time (cron). Does not return a synchronous response to the trigger source.
* *Focus:* Queue depth, data consistency, fault tolerance, batch processing time.
* *Examples:* Kafka event consumers, nightly data warehouse ETL jobs, email notification dispatchers.



#### Dimension 2: The Deployment Topology (Packaging Axis)

How is the compiled code for this module packaged and deployed?

* **Single-Deployable Unit (Monolith):** The module's logic, UI (if applicable), and data access layer are tightly coupled and deployed as one unified artifact.
* **Multi-Deployable Unit (Distributed):** The module is broken into smaller, independently deployable artifacts that communicate over a network (Microservices, Serverless Functions/FaaS, micro-frontends).
* **Client-Distributed:** The module is built by the vendor but deployed/instantiated in the consumer's environment — user devices, user browsers, customer codebases, or customer web applications. Distributed through a channel (app store, package registry, CDN) rather than deployed to vendor infrastructure. Dim 7 (Operational) footprint is lighter: CI/CD + distribution channel + version adoption tracking rather than clusters and containers. Examples: mobile apps (app stores → user devices), PWAs (CDN → user browsers), SDKs (package registries → customer codebases), embedded widgets (CDN → customer web apps), CLI tools (package managers → developer machines). See DR-021.

**Example Module Archetypes:**

* *Web Client:* (Human-Interactive + Distributed Micro-frontend).
* *Public API Gateway:* (Programmatic-Interactive + Distributed Microservice).
* *Daily Ledger Reconciliation:* (Reactive/Background + Single-Deployable Monolith).
* *Mobile App:* (Human-Interactive + Client-Distributed).
* *Python SDK:* (Programmatic-Interactive + Client-Distributed).
* *Embeddable Payment Widget:* (Human-Interactive + Client-Distributed).

---

### The Synthesis: A Product is a Constellation of Modules

By rigidly defining these archetypes, your Information Model reflects reality.

If we look at **Zoom** as an example:

* **The Product Archetype:** Zoom is a *B2B/B2C SaaS PLG* product.
* **Its Module Archetypes:** * The Desktop App is a *Human-Interactive Monolith* module.
* The Meeting Creation API is a *Programmatic-Interactive Distributed* module.
* The Cloud Recording Video Encoder is a *Reactive Background Distributed* module.



This layered architecture ensures that when a Business Analyst looks at the model, they see Market and ROI dimensions. When an Engineer looks at the model, they see Interaction Boundaries and Deployment Topologies.
