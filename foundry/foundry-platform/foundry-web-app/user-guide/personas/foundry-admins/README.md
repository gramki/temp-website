# Foundry Admins — Jobs to be Done

**Primary Module:** Foundry Management

**Role:** Administer the Foundry Platform — configure Workshops, Workbenches, repositories, teams, agents, and tenancy.

## Prerequisites

- Foundry Admin role assigned in Olympus Cipher
- Familiarity with [Foundry onboarding journey](../../../../management/user-guide/foundry-onboarding.md)
- Understanding of [ACE hierarchy](../../../../ace/README.md) — Foundry > Workshop > Workbench

---

## Primary Jobs — Workshop & Workbench Management

### J1. Create and configure Workshops
**When** a new division/unit needs a Workshop  
**I want to** create and configure the Workshop  
**So that** it's ready for use

**Acceptance Criteria:**
- Workshop creation wizard
- Name, description, owner
- Repository allocation
- Team assignment
- Settings and policies

---

### J2. Create and configure Workbenches
**When** a new Product needs a Workbench  
**I want to** create and configure the Workbench within a Workshop  
**So that** Product evolution can begin

**Acceptance Criteria:**
- Workbench creation wizard
- Link to UPIM Product
- **GitHub Org connection** (see GitHub integration below)
- Workspace configuration (standard 6 Workspaces — see below)
- Team assignment (see team structure below)
- Repository provisioning (see repository list below)
- External tool connections (Figma, TestRail, Jira)

**GitHub Integration (at Workbench creation):**
- Specify GitHub Organization to associate with Workbench
- Workbench installs as **GitHub App** on the org
- Workbench becomes org manager (team members get repo-level access only)
- Multiple Workbenches can share one GitHub Org
- Repo tagging: FoundryID, Workshop, Workbench, Product Code
- Best practice: import existing repos (not mandated)

**Standard Workspaces (created for every Workbench):**
- Product Specification
- UX Design
- Development
- QA
- Release
- Governance

**Workbench Team Structure:**
- Every Workbench has a team associated with it
- Team members can have **Manager** role or **Member** role
- **Managers** can:
  - Manage repositories (create via Workbench, configure, access control)
  - Add Scenario Catalogs to Workspaces
- **All team members** can add components to the Workbench
- **GitHub access:** Team members get repo-level access; org management is Workbench-only

**Workbench Services (auto-provisioned):**

| Service | Purpose |
|---------|---------|
| **Metadata Service** | PI ID generation, commit tracking (all repos), code repo references |
| **Ontology Service** | Product structure, capabilities, features (independent) |
| **Quality Service** | Unified access wrapper over TestRail + Git |

**Workbench Repositories (owned by the Workbench):**

| Repository | Storage | Service Role |
|------------|---------|--------------|
| **Intent** | Git repo (GitHub Org) | Metadata Service: PI ID required; commit tracking |
| **Design** | Git repo (GitHub Org) | Metadata Service: commit tracking |
| **Code** | Multiple git repos (GitHub Org) | Metadata Service: reference management; commit tracking |
| **Ontology** | Native service | Ontology Service (auto-provisioned) |
| **Quality** | TestRail (SoT) + Git (automation) | Quality Service: unified access wrapper |
| **Operations** | Jira (JSM) | Label-filtered; linked at setup |
| **Feedback** | Jira | Label-filtered; linked at setup |
| **Work** | Jira | Label-filtered; linked at setup |
| **Evolution** | TBD | Deferred (not Phase 1) |

**Jira Integration (Operations, Feedback, Work):**
- Jira projects **not exclusive** to Workbench
- Foundry configured with **simple label filter** per Workbench
- Linked **manually** at Workbench setup
- Operations uses **JSM** (Jira Service Management) for problems/incidents

**Intent Repository Structure:**
```
intent-repo/
├── PI-001/              # PI ID from Metadata Service, created after Go/Pivot PDR
│   ├── README.md        # Intent overview
│   ├── pdr.md           # Authorizing product decision
│   ├── psd-*.md         # PSD refinement (one or more files)
│   └── mockups/         # Mockups or Figma links
├── PI-002/
└── (organized as product team sees fit)
```

**External Tool Integrations (Phase 1):**

| Tool | Integration | Notes |
|------|-------------|-------|
| **GitHub** | GitHub App | Org manager role |
| **Figma** | OAuth | Design assets |
| **TestRail** | OAuth | Quality repo SoT for test cases |
| **Jira** | OAuth | Operations (JSM), Feedback, Work repos |
| **Olympus Weave** | OAuth | Publisher; deploy, track versions, EoS |
| **Others** | URL reference | No deep integration |

Workbench ID is used as OAuth client ID for all integrations.

**Olympus Weave Integration:**
- Workbench acts as **Publisher** to Olympus Weave (deployment platform)
- **Product Code** assigned by Weave on Workbench creation
- **Olympus Product Module code** assigned by Weave per System (when registered in Ontology)
- Deployment tracking: Weave → Foundry webhook + Foundry polls Weave
- Tracks which version deployed where (multi-region)
- EoS/deprecation metadata owned by Weave, surfaced in Foundry

**Shared Repositories (referenced from Workshop/Foundry):**

| Repository | Purpose | Scope |
|------------|---------|-------|
| **Domain** | Domain knowledge, glossaries, business rules | Workshop-shared |
| **Practices** | Standards, templates, policies | Workshop-shared |
| **Workforce** | Agents, humans, role bindings, skills | Foundry-shared |
| **Stakeholders** | External stakeholder registry | Workshop-shared |

---

### J3. Provision and manage repositories
**When** repositories need setup or maintenance  
**I want to** provision, configure, and manage repositories  
**So that** Workspaces have the data substrate they need

**Acceptance Criteria:**

*Git-based repositories (Intent, Design, Code, Quality automation):*
- Create repos via Workbench interface (ensures proper tagging)
- Repos created in associated GitHub Org
- Access control at repo level (via GitHub)
- Backup/retention via GitHub settings

*Service-based repositories (Ontology, Quality Service):*
- Auto-provisioned on Workbench creation
- Configuration via Workbench admin UI
- Health monitoring dashboard

*Quality repository (hybrid):*
- Link TestRail project (source of truth for test cases)
- Create Git repo for automation code
- Quality Service provides unified access

*Jira-based repositories (Operations, Feedback, Work):*
- Link existing Jira/JSM projects
- Configure label filter for Workbench
- Operations uses JSM for problems/incidents

*Code repositories (multiple per Workbench):*
- Create new code repo for System/Component
- Metadata Service tracks all code repo references
- All repos tagged with FoundryID, Workshop, Workbench, Product Code

*Olympus Weave connection:*
- Connect Workbench as Publisher to Weave
- Weave assigns Product Code
- Register Systems → Weave assigns Olympus Product Module codes

*Shared repositories (Domain, Practices, Workforce, Stakeholders):*
- Managed at Workshop or Foundry level
- Workbenches reference but don't own

**Note:** Workbench Managers (not just Foundry Admins) can create code repos via Workbench interfaces.

---

## Primary Jobs — Team & User Management

### J4. Configure teams, roles, and permissions
**When** people need access  
**I want to** configure teams, assign roles, and set permissions  
**So that** the right people have the right access

**Acceptance Criteria:**
- Team creation/management
- Role definitions
- Permission matrix
- Workspace access control
- Workbench access control

---

### J5. Onboard new users
**When** new builders join  
**I want to** onboard them to the Foundry  
**So that** they can start working

**Acceptance Criteria:**
- User creation/invitation
- Team assignment
- Workbench assignment
- Role assignment
- Onboarding checklist

---

### J6. Manage agent configurations and skill assignments
**When** agents need setup  
**I want to** configure agents and assign skills  
**So that** they can execute Scenarios

**Acceptance Criteria:**
- Agent configuration
- Skill assignment
- Availability settings
- Cost/quota configuration
- Performance thresholds

---

## Primary Jobs — Tenancy Management

### J7. Configure tenancy
**When** the platform serves multiple tenants  
**I want to** configure tenant isolation and settings  
**So that** tenants are properly separated

**Acceptance Criteria:**
- Tenant creation
- Isolation boundaries
- Resource quotas
- Tenant-specific settings
- Billing/cost allocation

---

### J8. Manage tenant onboarding
**When** a new tenant joins  
**I want to** onboard them to the platform  
**So that** they can use Foundry

**Acceptance Criteria:**
- Tenant provisioning workflow
- Admin user creation
- Initial Workshop setup
- Configuration templates

---

## Primary Jobs — Platform Operations

### J9. Monitor platform health
**When** operating the platform  
**I want to** see health dashboards  
**So that** I can ensure availability

**Acceptance Criteria:**
- Platform health dashboard
- Service status
- Error rates
- Latency metrics
- Capacity utilization

---

### J10. View observability dashboards
**When** investigating issues  
**I want to** access logs, traces, and metrics  
**So that** I can diagnose problems

**Acceptance Criteria:**
- Link to observability tools
- Key metric summaries
- Alert management
- Incident history

---

### J11. View platform usage and capacity
**When** planning capacity  
**I want to** see usage trends and capacity  
**So that** I can scale appropriately

**Acceptance Criteria:**
- Usage dashboard
- User counts
- Work Order volumes
- Storage consumption
- Compute utilization

---

## Supporting Jobs — Knowledge & Scenarios

### J12. Manage knowledge bases and practices repositories
**When** organizational knowledge needs curation  
**I want to** manage Domain and Practices repositories  
**So that** knowledge is current

**Acceptance Criteria:**
- Knowledge repository browser
- Content management
- Version control
- Access control

---

### J13. Manage platform-level Scenario catalogue
**When** new Scenarios are developed for the platform  
**I want to** publish them to the platform Scenario catalogue  
**So that** Workbench Managers can add them to their Workspaces

*(Note: Foundry Admin manages the **platform catalogue**. Workbench Managers add Scenario Catalogs to their Workspaces — that is a Workbench Manager job, not a Foundry Admin job.)*

**Acceptance Criteria:**
- Platform Scenario catalogue management
- Publish/unpublish Scenarios
- Scenario versioning
- Scenario metadata and documentation
- Skill/agent mapping

---

## Supporting Jobs — Integrations & Troubleshooting

### J14. Manage platform-level integrations
**When** external systems need platform-wide connection  
**I want to** configure platform-level integrations  
**So that** Workbenches can leverage them

**Acceptance Criteria:**

*Platform-level integration setup:*
- Configure OAuth app credentials for supported tools (GitHub, Figma, TestRail, Jira)
- Set up platform-wide defaults and policies

*Workbench-level integrations (handled by Workbench Managers):*
- GitHub Org association (via GitHub App installation)
- OAuth connection to Figma, TestRail, Jira using Workbench ID
- URL references for unsupported tools

*Monitoring:*
- Integration health dashboard
- OAuth token status
- Sync status for connected tools

**Note:** Foundry Admins manage platform-level OAuth app setup; Workbench Managers connect their Workbenches to tools.

---

### J15. Troubleshoot user/agent access issues
**When** access problems occur  
**I want to** diagnose and resolve them  
**So that** work isn't blocked

**Acceptance Criteria:**
- Access audit log
- Permission checker
- Impersonation (for debugging)
- Quick-fix actions

---

### J16. Manage platform settings
**When** global settings need adjustment  
**I want to** update platform configuration  
**So that** the platform behaves correctly

**Acceptance Criteria:**
- Settings management UI
- Environment-specific settings
- Feature flags
- Change audit trail

---

## Related

- [Admin Console](../../../platform-developer-guide/pages/consoles/settings/admin-console.md) — Workbench administration
- [Agent Console](../../../platform-developer-guide/pages/consoles/workforce/agent-console.md) — Agent configuration
- [Foundry onboarding](../../../../management/user-guide/foundry-onboarding.md) — First-time setup walkthrough
- [Workbench provisioning](../../../../management/user-guide/workbench-provisioning.md) — Creating Workbenches
- [Agent lifecycle](../../../../agent-fabric/user-guide/agent-lifecycle.md) — Agent configuration journey

## Open Questions

- What's the self-service vs admin-assisted boundary for Workshop/Workbench creation?
- How are agent costs/quotas managed and billed?
- What's the disaster recovery and backup strategy?
- How are platform upgrades managed?
