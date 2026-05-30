# DR-025: Operations Decision Record (ODR) — Completing the Decision Record Triad

**Status:** Accepted
**Date:** 2026-02-15

## Context

The Definition Model had two formal decision record entities — PDR (Strategy, product strategy decisions) and ADR (Technical, architectural/technical decisions) — but no equivalent for operational and infrastructure decisions. Significant operational decisions (cloud provider selection, deployment strategy, data governance policies, DR/BCP configuration, tenancy isolation, compliance zone setup, data archival) were either captured ad-hoc in ADRs (where they don't naturally belong), or remained undocumented tribal knowledge.

Operational already had an Infrastructure Model (root entity), Deployment Environments, Operational Targets, and Operational Constraints — but no entity to record *why* these were configured as they are. The Infrastructure Model says "Multi-region AWS SaaS" but doesn't explain why AWS was chosen over GCP, or why active-passive DR was selected over active-active. ADR says "Adopt event-driven architecture with Kafka" but doesn't record "AWS MSK over self-managed Kafka in 3-AZ deployment" — that's an operational decision, not an architectural one.

The PDR → ADR → ODR trigger chain was identified: product decisions (PDR) cascade to architectural decisions (ADR) which cascade to operational decisions (ODR). Each level has different decision makers, different governance, and different consequences. The boundary is clean: ADR = how it's *built* (design-time), ODR = how it's *run* (runtime/operational).

Additionally, operational data governance decisions (retention periods, archival policies, encryption requirements, access control models) needed a home. These are operational decisions about data — distinct from Data, which will capture the *structural* data view (what data exists, domains, ownership, schema). The split: Data = what data the product manages; Operational/ODR = how that data is governed operationally.

## Decisions

### D1: Introduce ODR as an Operational entity, completing the PDR / ADR / ODR triad

Operations Decision Record (ODR) is a formal, referenceable record of a significant operational or infrastructure decision. It is the Operational counterpart of PDR (Strategy) and ADR (Technical), completing the decision record triad:
- **PDR:** What should the product *do*? (Strategy & Intent, Strategy)
- **ADR:** How should the product be *built*? (Architecture & Engineering, Technical)
- **ODR:** How should the product be *run*? (Operations & Infrastructure, Operational)

### D2: ODR scope — ten categories of operational decisions

ODR covers: Cloud Provider & Services, Deployment Strategy, Tenancy & Isolation, DR & BCP, Data Governance, Data Archival, Observability & Tooling, Compliance Zone, Capacity & Scaling, Cost Optimization. This Category field provides structured classification without requiring separate entities per category.

### D3: Four relationship patterns for ODR (paralleling ADR)

1. PDR triggers ODR(s): Product decision with operational implications
2. ADR triggers ODR(s): Architectural decision requiring operational provisioning
3. ODR exists independently: Purely operational decisions
4. ODR constrains ADR/PDR: Operational reality limiting architectural or product options

### D4: ODR has dual provenance — Discovery and Run

ODRs can be produced by both the Discovery Track (Deliberation-driven — strategic infrastructure planning like cloud provider selection) and the Run Track (operationally-driven — decisions emerging from operational experience, Post-Incident Reviews, capacity reviews). Both paths produce the same Operational entity.

### D5: Data governance and archival as ODR scope, not Data dimension

Operational aspects of data (retention, archival, encryption, access control, backup policies) belong in ODR (Operational). Data will capture the structural/domain view of data — what data exists, domain boundaries, ownership, schema. This maintains the Build-vs-Run split consistent with ADR (how data is structured) vs. ODR (how data is governed).

## Rationale

**Why not extend ADR to cover operational decisions?** ADR and ODR have different audiences (architect vs. SRE), different governance (architecture review vs. operations review), different dimensions (Technical vs. Operational), and different scopes (design-time vs. runtime). Forcing operational decisions into ADR would overload the entity and blur the architecture/operations boundary. The same reasoning that justified separating PDR from ADR applies to separating ADR from ODR.

**Why not just use PDR?** PDR is for product-level decisions (strategy, market, feature). "Archive transaction data after 24 months" and "Use MSK over self-managed Kafka" are not product decisions — they're operational decisions. Forcing them into PDR would dilute PDR's strategic focus and change its governance model.

**Why the Category field?** Operational decisions span diverse domains (cloud, data, deployment, DR). The Category enum provides structured classification and filtering without creating separate entity types per domain, keeping the model simple.

**Why dual provenance?** Some operational decisions are strategic and planned (cloud provider selection during product strategy deliberation). Others emerge from operational experience (changing deployment strategy after incident patterns). Both are legitimate sources of ODR; the provenance is tracked through relationships.

## Consequences

**Positive:**
- The decision record triad (PDR/ADR/ODR) provides complete decision traceability across product, architecture, and operations
- Infrastructure Model, Deployment Environments, Operational Targets, and Operational Constraints now have decision records justifying their configuration
- Data governance decisions have a formal home — retention, archival, encryption, access control are documented and referenceable
- The PDR → ADR → ODR trigger chain makes cross-level decision cascading explicit
- Run Track gains decision-making capability parallel to Build Track's ADR production

**Negative:**
- Adds one more entity to Operational (now 10 entities)
- The ADR/ODR boundary requires judgment — some decisions (e.g., "use Kafka") span both architecture and operations
- ODR dual provenance (Discovery + Run) adds complexity to the artifact production model

**Mitigations:**
- Entity count (10) is proportional to Operational's domain complexity
- ADR/ODR boundary guidance: ADR captures "what technology and why" (design-time); ODR captures "how to provision, configure, and govern it" (runtime). When in doubt, the decision should live where its primary audience is
- Run Track ODR production will be detailed incrementally (same approach as Build Track ADR production)

---
