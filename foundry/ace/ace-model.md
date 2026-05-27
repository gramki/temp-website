ACE: Agent Centric Engineering
An Agent Centric Product Development System
For the Engineers, By the Engineers

----
ACE defines foundry as a place where Software Products are crafted

Foundry 
* is governed by Product Model, Work Model, and Operating Model

Foundry
* hosts multiple Workshops

Workshop
* is the body of work owned by a product team, product suite, or organization (not a single Product)
* has multiple Repositories
    Domain Knowledge Repository
    Practitioner Repository
    Skill Repository
    Product Intent Repository
    Product Ontology Repository
    Design Repository
    Product Evolution Repository
    Feedback Repository
    Source Repository
    Artifact Repository
    Quality & Verification Repository
    Work Repository
    Workforce Repository
* hosts multiple Workbenches

Workbench
* corresponds to a Product in UPIM — the venue where that Product is evolved (not the Product itself)
* is where work happens
* has multiple Workspaces, each for a distinct functional team
* types of workspaces:
    Product Specification Workspace
    UX Design Workspace
    Development Workspace
    QA Workspace
    Release Workspace
    Governance Workspace

Workspace
* has Human-Agent Team and Tools
* is interfaced by Humans using an IDE
* has well-defined Scenarios
* each Scenario creates Tasks
* Tasks are completed by Human-Agent Team of the Workspace
* uses and updates Repositories


Product Evolution Cycle
* Discovery and product decisions establish or update Product Intent
* Release Workspace renews Product Intent for the next cycle
* Product Intent triggers Scenarios in Product Specification Workspace
* PSDs refine Product Intent into buildable specification
* Product Intent moves from Product Specification to UX Design Workspace
* Product Intent moves from UX Design Workspace to Product Specification Workspace
* Product Intent moves from Product Specification Workspace to Development Workspace and Quality Assurance Workspace
* Product Intent moves from Development Workspace to Quality Assurance Workspace
* Product Intent moves from Quality Assurance Workspace to Release Workspace as Product Delivery
* Optionally Product Intent can move from Development, QA Workspaces to Product Specification Workspace as well

Governance Workspace 
* Every transition of Product Intent invokes Scenarios in Governance Workspace
