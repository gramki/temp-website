---
name: DDD Spring Boot Guide
overview: Create a multi-file guide at org-8.0/domain-products-with-ddd, with one Markdown file per major section (9 sections + README). Content covers DDD modeling, Spring Boot implementation without ORM, anemic domain, risks/mitigations, and testability.
todos: []
isProject: false
---

# Plan: DDD with Spring Boot Guide (Multi-File)

## Target location

All files under **[org-8.0/domain-products-with-ddd](org-8.0/domain-products-with-ddd)**. The directory does not exist yet and will be created.

## Structure: one file per section

Each main section from the approved TOC becomes a single Markdown file. The README serves as the entry point and table of contents.


| File                                       | Section                             | Purpose                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **README.md**                              | —                                   | Entry point: audience, scope, TOC with links to all section files, how to use the guide.                                                                                                                                                                                                                                                                                                    |
| **01-introduction.md**                     | §1 Introduction                     | Purpose, audience (developers, principal engineers), scope (DDD + Spring Boot, no ORM, one app per domain), how to use the guide.                                                                                                                                                                                                                                                           |
| **02-ddd-concepts.md**                     | §2 DDD concepts (reference)         | Domain, ubiquitous language, bounded context; entity, value object, aggregate, aggregate root, domain event; repository; Domain Service vs Application Service (and why domain service has no CRUD/repository); context map. Full concept tables and definitions so the guide is self-contained.                                                                                            |
| **03-mapping-product-to-ddd.md**           | §3 Mapping product to DDD           | Use cases → application services and domain model; value streams → bounded contexts and context map; product requirements → DDD checklist. Value-stream vs bounded-context diagram. Practitioner mapping tables.                                                                                                                                                                            |
| **04-one-app-per-domain.md**               | §4 One app = one domain/subdomain   | **Clarification:** subdomain vs bounded context; context map as source of truth (ownership, consistency boundary, deployment unit); criteria for "one app per X"; when not to split (avoid nanoservices); when to split (avoid monolith); governance to stick to the rule.                                                                                                                  |
| **05-spring-boot-mapping.md**              | §5 Spring Boot mapping (no ORM)     | Package layout (domain, application, infrastructure); repository interface in domain + JDBC impl; persistence model (domain ↔ persistence model ↔ DB); Domain/Application Service placement; domain events; dependency rule and no Spring in domain.                                                                                                                                        |
| **06-anemic-domain.md**                    | §6 Anemic domain (thorough)         | Definition and symptoms; why it's a slippery slope (Spring defaults, getters/setters, "services do everything"); rich vs anemic with examples; where behavior belongs (invariants in aggregates, behavior on entities, domain services only when needed); **stringent guidelines** and forbidden patterns; code review checklist; refactoring from anemic to rich.                          |
| **07-risks-and-mitigations.md**            | §7 Risks and mitigations            | Each risk with description, mitigation, and guideline: domain + Spring; aggregate reconstitution; schema/mapping and N+1; domain service + repositories; transaction boundary and cross-app; persistence model. Summary table: risk → mitigation → guideline.                                                                                                                               |
| **08-testability-and-testing-patterns.md** | §8 Testability and testing patterns | Why testability matters; unit testing domain (no Spring); unit testing application services (mocks); integration testing repository (Testcontainers, persistence model, mapper); integration testing application service + real repo; testing domain events; testing persistence/ACL; test pyramid and what to mock; guidelines (domain tests framework-free, when to use @SpringBootTest). |
| **09-summary-and-checklist.md**            | §9 Summary and checklist            | Implementation checklist (domain, application, infrastructure, deployment); quick reference table (DDD concept → Spring Boot artifact, no ORM, one app per domain); references (Evans, Vernon, internal).                                                                                                                                                                                   |


## Reader flow and narrative continuity

- **Intended reading sequence:** 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09. Each section assumes the reader has read (or can reference) earlier sections. Avoid forward dependencies that require later sections to understand the current one.
- **Placement of integrated content:** Put all building blocks and “Domain Service vs Application Service” (including “who does CRUD”) in **02-ddd-concepts** so 03 and 05 can refer back. Put use cases/value streams and practitioner mapping in **03-mapping-product-to-ddd** (depends only on 02; no Spring yet). Put “service is not a process boundary,” K8s vs DDD layers, and persistence model in **05-spring-boot-mapping**, with explicit links to 02 (“as defined in DDD concepts”). Put risk mitigations in **07-risks-and-mitigations** referencing 02 and 05 only; no new concept definitions there.
- **Avoiding patchiness:** Integrate scratchpad material so each file reads as one continuous narrative. Use short cross-references (e.g. “as defined in [DDD Concepts](02-ddd-concepts.md)”) instead of repeating long blocks. When merging, rephrase for consistency with Evans-style guidelines and the section’s role in the flow.
- **Durable reference:** (1) No references to scratchpad, draft, or internal temporary docs. (2) Define every term on first use. (3) Use stable section titles and file names; avoid “current” or date-bound phrasing in headings. (4) Keep tool/framework advice in dedicated sections (e.g. Spring Boot in 05, 08) so conceptual parts (02, 03, 04, 06) remain valid if tooling changes.

## Integrating existing content

- **Source to integrate:** The content in `org-8.0/product-line-engineering/scratchpad/thinking-domain-products-using-ddd.md` is to be **merged into** the guide following the placement in "Reader flow and narrative continuity" above: concepts and Domain vs Application Service in 02; use cases/value streams in 03; "service is not a process boundary" and K8s in 05; practitioner checklist in 03 and 07. That content is merged into those section files (02, 03, 05, 07) as described in the placement above. Adapt and extend for depth and narrative flow; do not copy verbatim.
- **No scratchpad references in the guide:** The published guide must stand alone. Do not cite, link to, or mention the scratchpad or “temporary draft” in any file under `domain-products-with-ddd`. The guide is the single source of truth for this material.
- **Additional content** (beyond the integrated doc): §4 full clarification (subdomain, context map, one app per X); §6 anemic domain (full section); §7 risks table; §8 entire testability section; §5 persistence model and no-ORM details; README and §9.

## Implementation order

1. Create directory **org-8.0/domain-products-with-ddd**.
2. Add **README.md** (TOC, links to 01–09, audience, scope).
3. Add section files **01-introduction.md** through **09-summary-and-checklist.md** in sequence, so later sections can reference earlier ones by file name if needed.
4. Use consistent heading levels: one H1 per file (title), then H2 for main subsections, H3 for sub-subsections; internal cross-references as “see [Section Title](filename.md).”

## Writing style (Evans-aligned)

Write so the guide feels close to Eric Evans’ *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Apply the following:

- **Definitions first:** Define each term precisely before use. Use consistent wording for core concepts (e.g. “entity,” “aggregate root,” “bounded context”) so the guide is referenceable and quotable.
- **Problem–solution:** Motivate patterns and decisions by the problem or force they address (e.g. “When an operation doesn’t naturally fit on a single entity…”; “When persistence shape and domain shape diverge…”). Avoid introducing a pattern without stating why it exists.
- **Conceptual before technical:** Explain DDD ideas in an implementation-agnostic way first; then map to Spring Boot (e.g. in 02 and 03, stay conceptual; in 05 and 08, add Spring/Java). The reader should understand the *what* and *why* before the *how* in code.
- **Calm, authoritative tone:** No hype or “you must always.” Prefer “when X, consider Y,” “this often leads to…,” “the team should…” so the guide reads as durable guidance, not a one-time opinion.
- **Pattern-like treatment for key decisions:** For Domain Service, Application Service, Repository, persistence model, and aggregate reconstitution: give a short context (when it applies), the approach (what to do), and the consequence (what you get or avoid). Optional: name–context–solution–consequence where it helps.
- **Ubiquitous language:** Use the same terms in prose as in the model (Order, aggregate root, bounded context). Avoid mixing jargon (e.g. “service” only in the DDD sense in conceptual sections; clarify “process” vs “design boundary” where needed).
- **Minimal, illustrative examples:** Use a consistent running example where helpful (e.g. ordering, claims). Keep examples short; they should clarify the idea, not teach Spring or Java.
- **Collaboration with the domain:** Where relevant (e.g. mapping product to DDD, ubiquitous language), mention that the model is refined through dialogue with domain experts and that the language is shared—align with Evans’ emphasis on discovery and collaboration.

## Conventions

- Markdown only; no Jekyll/Confluence-specific syntax unless already used in org-8.0.
- Links between section files: relative, e.g. `[DDD Concepts](02-ddd-concepts.md)`.
- Tables and code blocks where they aid clarity (e.g. concept tables, package layout, risk table).
- Mermaid only where it adds value (e.g. context map or test pyramid); follow project mermaid rules (no spaces in node IDs, no HTML in labels).

## Suitability for purpose

- **Audience signposting:** In README (or 01), briefly indicate which sections are especially relevant for **developers** (e.g. 05 Spring Boot mapping, 06 anemic domain, 08 testability) vs **principal engineers** (e.g. 04 one app per domain, 07 risks and mitigations, boundary and governance decisions) so each audience can navigate efficiently. State that the full sequence 01–09 is recommended for both when adopting the approach.
- **Positioning in the organisation:** In 01 or README, state how this guide relates to the organisation’s product-line or domain-product model (e.g. supports domain products, aligns with meta-model or PCMM where applicable) so the guide is clearly positioned for org use. If there is a parent doc (e.g. PLE overview), add one sentence and an optional link; the guide remains self-contained.
- **Trade-offs and rationale:** Where the guide is prescriptive (no ORM, no Spring in domain, one app per domain), state the **trade-off** or **rationale** in one or two sentences so principal engineers can apply or adapt the guideline to their context (e.g. “No ORM: avoids bloat and keeps persistence explicit; trade-off is more mapping code and schema ownership in infrastructure”).
- **Findability:** Treat **02-ddd-concepts** as the single definition source for DDD terms used in the guide. In README, add a short “Key terms” or “Find a concept” line pointing to 02 (e.g. “For definitions of bounded context, aggregate, Domain Service, see [DDD Concepts](02-ddd-concepts.md)”). In 09, the quick-reference table already supports “look up DDD concept → Spring artifact”; no separate glossary file unless the guide grows significantly.
- **When to use this guide:** In README, briefly state when the guide applies (e.g. “Use when implementing or reviewing domain products with Spring Boot”) and optionally when to look elsewhere (e.g. PLE overview, team structure) so the scope is clear for someone discovering the doc.

## Out of scope

- No code repository or sample Spring Boot project; the guide is documentation only.
- No changes to existing files under product-line-engineering or scratchpad (the scratchpad file may remain as draft material; the guide does not reference it).

