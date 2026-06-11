# Document Governance

[← Back to ERE Guide](../README.md)

All Engagement and Exploration documentation follows a **strict governance model** that separates customer-facing documents from internal working documents.

---

## Core Principle

The fundamental principle is clear separation by document purpose and audience:

| Document Type | Location | Format | Examples |
|---------------|----------|--------|----------|
| **Shared BY customer** | SharePoint | Office (Word, Excel, PPT) | Customer requirements docs, RFPs, data files, contracts |
| **Shared WITH customer** | SharePoint | Office (Word, Excel, PPT) | Proposals, SOWs, status reports, presentations |
| **Internal working documents** | Git | Markdown | Requirements analysis, architecture decisions, planning docs, meeting notes |

This separation ensures:

- **Customers work in familiar formats** — Office documents they can edit, comment on, and share internally
- **Internal teams work in version-controlled, AI-friendly formats** — Markdown enables tooling, search, and automation
- **Clear ownership boundaries** — customer-provided content stays in SharePoint; analysis and decisions stay in Git
- **Audit trail** — Git provides history and accountability for all internal decisions

---

## Why This Approach

### The Problem We're Solving

Without structure, Engagement documentation becomes chaotic:

- Documents scattered across email, Teams, SharePoint, personal drives
- No single source of truth — which version is current?
- Can't find what was decided or why
- Knowledge is lost when people leave or Engagements complete
- No ability to automate, search across Engagements, or build tooling on top

### Why Two Systems Instead of One

**Why not just SharePoint?**

Office formats are poor for internal working documents:
- No meaningful version control — "Final_v3_FINAL_revised.docx"
- Can't diff changes between versions
- Binary formats block automation and AI processing
- Can't build validators, dashboards, or compliance tools on top

**Why not just Git?**

Customers expect Office documents:
- Proposals, status reports, contracts must be professionally formatted
- Customers can't edit or comment on markdown files
- Legal and commercial documents require industry-standard formats

**So we need both** — with a clear boundary and a bridge between them.

### Why Git + Markdown for Internal Work

| Benefit | How Git/Markdown Delivers |
|---------|--------------------------|
| **AI-assisted drafting** | Markdown is the native output format of LLMs. First drafts that took an afternoon can be generated, reviewed, and reshaped in minutes. The author's time shifts from typing to judgment — deciding what is right, what is missing, what to cut. |
| **Diff-based review** | When requirements change, an assistant proposes the update, and the author reviews a diff instead of rewriting pages. |
| **Version control** | Full history of every change, who made it, when. Branches for parallel work. PRs for approval workflows on documents. |
| **Portability** | Same source files render in an IDE, compile to a static site, or feed a search index. Content is not locked to any one tool. |
| **Longevity** | Plain text survives tool migrations. Markdown files written today will still open cleanly in whatever editor exists a decade from now. |
| **Tooling** | Build validators, generators, compliance dashboards, and search indexes on top of plain text. |

### Why SharePoint for Customer-Facing

| Benefit | How SharePoint/Office Delivers |
|---------|-------------------------------|
| **Customer familiarity** | They already use Word, Excel, PowerPoint |
| **Professional deliverables** | Branded templates, polished formatting |
| **Collaboration** | Comments, track changes, co-editing |
| **Permissions** | Native sharing with external parties |
| **Contracts/legal** | Industry-standard formats for signatures |

### Why the Content Bridge

Without it:
- Teams manually copy-paste between Git and SharePoint
- Creates **drift** — internal analysis doesn't match what customer sees
- Wastes time on formatting and reformatting
- RFP responses are manually parsed question-by-question
- The productivity gained in authoring is lost at the publishing step

With the [Content Bridge](../02-systems/content-bridge.md):
- **Automated conversion** while maintaining governance
- **Single source of truth** in Git; SharePoint is a rendered view
- **AI-assisted extraction** from customer documents
- **Audit trail** for what was exported and when

---

## Naming Convention

Repositories follow a consistent naming scheme that identifies the construct type and customer code. The [Engagement Registry](../02-systems/engagement-registry.md) is the authoritative source for all identifiers.

| Construct | Repo Names | Example |
|-----------|------------|---------|
| **Engagement** | `ENG-{CODE}-requirements`, `ENG-{CODE}-project` | `ENG-NXTORBIT-requirements`, `ENG-NXTORBIT-project` |
| **Exploration** | `EXP-{CODE}-exploration` | `EXP-NXTORBIT-exploration` |

The `{CODE}` is a short, unique identifier for the customer/opportunity — typically derived from the customer name or project codename. The Engagement Registry ensures IDs are globally unique and immutable.

---

## In This Section

| Document | What It Covers |
|----------|---------------|
| [Engagement Repos](engagement-repos.md) | Structure of `ENG-{CODE}-requirements` and `ENG-{CODE}-project` repositories |
| [Exploration Repos](exploration-repos.md) | Structure of `EXP-{CODE}-exploration` repository |
| [SharePoint Structure](sharepoint-structure.md) | Customer SharePoint site organization |
| [Governance Rules](governance-rules.md) | Auto-provisioning, archival, access control, PI Artifacts (SAFe) |

---

## Related Content

- [Engagement Registry](../02-systems/engagement-registry.md) — source of truth for identifiers and lifecycle
- [Bootstrap Kit](../02-systems/bootstrap-kit.md) — automated provisioning of repos and SharePoint
- [Markdown Style Guide](../reference/markdown-style-guide.md) — standardized conventions for all documentation
- [PI Artifacts Reference](../reference/pi-artifacts.md) — SAFe artifact definitions
- [Content Bridge](../02-systems/content-bridge.md) — tools that bridge Git and Office ecosystems

---

[← Previous: Knowledge Engineering](../04-knowledge-engineering/README.md) | [→ Next: Governance Enforcement](../06-governance-enforcement/README.md)
