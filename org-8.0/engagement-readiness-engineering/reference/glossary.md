# Glossary

[← Back to ERE Guide](../README.md)

Terms and acronyms used throughout the Engagement Readiness Engineering documentation.

---

## ERE-Specific Terms

| Term | Definition |
|------|------------|
| **Engagement Readiness Engineering (ERE)** | The function within ERC responsible for building and operating the systems, tools, and applications that make the Engagement lifecycle efficient, reliable, and consistent. |
| **Engagement Engineering** | The discipline of designing and assembling customer-specific product instantiations by leveraging Product Lines and studio-built components. ERE builds infrastructure that enables Engagement Engineering to be practiced at scale. |
| **Engagement Registry** | The central system of record for all Engagements and Explorations. Manages identity (`ENG-{CODE}`, `EXP-{CODE}`), lifecycle state transitions, resource indexing, and governance enforcement. All other systems reference the Registry as their source of truth. |
| **Bootstrap Kit** | Tool that auto-provisions resources (Git repos, SharePoint folders, Jira projects, Teams channels) for Explorations and Engagements. Uses the Engagement Registry to validate entities before provisioning. |
| **Engagement Concierge** | AI agent paired with the Customer Portal that answers questions, accepts requests, and provides proactive guidance based on lifecycle phase. |
| **Knowledge Engineer** | Role that owns the knowledge base system, taxonomy, quality standards, and curation workflows. Not responsible for content creation — that comes from across the organization. |
| **Domain Steward** | Rotating SME role that validates and enriches domain-specific knowledge content. |
| **Pattern Curator Agent** | AI agent that scans artifacts for patterns, identifies duplicates, flags gaps, and proposes taxonomy updates. |
| **Progressive Enforcement** | Governance model where tools evolve from Guidance → Assistance → Mandatory Gate based on adoption maturity and tooling reliability. |

---

## Roles and Entities

| Acronym | Full Name | Definition |
|---------|-----------|------------|
| **ERC** | Engagement Readiness Council | Governs the Engagement pipeline; assigns Engagement-level roles; houses PPM function; provides framework guidance and archetype references. |
| **EPM** | Engagement Program Manager | Primary customer-facing contact; owns integrated view and Engagement Success; directs ELs and Scrum Masters. |
| **EPO** | Engagement Product Owner | Owns customer discovery, requirements, and training. |
| **EA** | Engagement Architect | Owns architecture across the entire Engagement span; peer to AVA; responsible for engineering quality standards. |
| **AVA** | Assembly Verification Architect | Owns verification architecture, assembly certification, and release authority; directs Verification Squad. |
| **EO** | Engagement Owner | Overall accountability for the Engagement; reports to Client Partner. |
| **EL** | Engineering Lead | Per-squad delivery accountability; reports to EPM. |
| **PAC** | Platform Architecture Council | Governs architecture standards, practice sharing, pattern extraction, and variability across Product Lines. |
| **PPM** | Portfolio Program Manager | Function within ERC for capacity coordination across Engagements. |
| **SRE Lead** | Site Reliability Engineering Lead | Owns operational readiness and release coordination. |
| **CPA** | Client Partner Associate | Generalist support for Client Partner: governance prep, stakeholder coordination, commercial tracking. |

---

## Lifecycle and Process Terms

| Term | Definition |
|------|------------|
| **Exploration** | Pre-commitment phase: discovering customer needs, assessing feasibility, qualifying whether an Engagement should be initiated. |
| **Engagement** | The complete collection of software artifacts (configurations, extensions, integrations, studio-built components, verification artifacts) constituting a customer-specific product instantiation. |
| **Assembly Construct** | The construct-type label for Engagement — emphasizing that what we produce is an assembled artifact, not a service. |
| **Engagement Success** | Function responsible for ensuring an Engagement is successfully deployed and adopted — readiness, adoption, value delivery. Owned by EPM. |
| **Knowledge Gate** | Checkpoint requiring specific knowledge artifacts before phase transition proceeds. |
| **Delivery Gate** | Checkpoint requiring delivery criteria before lifecycle phase transition. |

---

## SAFe Terms

| Term | Definition |
|------|------------|
| **PI** | Program Increment — a timebox (typically 8-12 weeks) during which Agile Release Trains deliver incremental value. |
| **PI Planning** | Event where teams plan the upcoming PI: objectives, features, dependencies, risks. |
| **PI Objectives** | Committed outcomes for a PI, written in SMART format. |
| **Program Board** | Visual representation of features, dependencies, and milestones for a PI. |
| **ROAM** | Risk status model: Resolved, Owned, Accepted, Mitigated. |
| **Confidence Vote** | End-of-planning assessment where teams rate their confidence (1-5) in achieving PI objectives. |
| **Inspect & Adapt** | Retrospective event at PI end to identify improvements. |
| **Iteration** | A smaller timebox (typically 2 weeks) within a PI. |

---

## AI and Tooling Terms

| Term | Definition |
|------|------------|
| **Assistive** | AI autonomy level where agents draft, suggest, and flag — humans review and approve. |
| **Automative** | AI autonomy level where agents execute routine actions autonomously, with human escalation for exceptions. |
| **Agent Accuracy** | Percentage of agent outputs accepted without modification. |
| **Escalation Rate** | Percentage of agent requests escalated to humans. |
| **Autonomy Utilization** | Percentage of available automative capacity actually used. |

---

## Document Governance Terms

| Term | Definition |
|------|------------|
| **ENG-{CODE}** | Naming prefix for Engagement repositories and SharePoint folders. |
| **EXP-{CODE}** | Naming prefix for Exploration repositories and SharePoint folders. |
| **ADR** | Architecture Decision Record — documents a significant architecture decision with context and rationale. |
| **CR** | Change Request — documents a scope change with impact analysis. |
| **Content Bridge** | Tools that convert between Git (Markdown) and Office (SharePoint) formats. |

---

## Quality and Metrics Terms

| Term | Definition |
|------|------------|
| **Contribution Rate** | Number of knowledge artifacts contributed per Engagement. |
| **Reuse Rate** | Number of times contributed artifacts are reused in other Engagements. |
| **Coverage** | Percentage of archetypes/domains with adequate knowledge artifacts. |
| **Quality Score** | Rating (1-5) based on completeness, reusability, findability, and freshness. |
| **Freshness** | Percentage of knowledge artifacts reviewed within policy period. |
| **Gate Pass Rate** | Percentage of Engagements passing gates without documented exceptions. |

---

## RFC 2119 Keywords

Used in requirements documentation:

| Keyword | Meaning |
|---------|---------|
| **MUST** / **REQUIRED** | Absolute requirement |
| **MUST NOT** | Absolute prohibition |
| **SHOULD** / **RECOMMENDED** | Strong preference; valid exceptions exist |
| **SHOULD NOT** | Strong preference against |
| **MAY** / **OPTIONAL** | Truly optional |

---

## Related Content

- [Markdown Style Guide](markdown-style-guide.md) — formatting conventions
- [PI Artifacts Reference](pi-artifacts.md) — SAFe artifact definitions
- [Engagement Operating Model](../../engagement/README.md) — full engagement lifecycle guide
