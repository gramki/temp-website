# Gates and Checkpoints

[← Back to Governance Enforcement](README.md) · [ERE Guide](../README.md)

ERE tools enforce (progressively) governance at lifecycle transitions. Each gate combines delivery requirements with knowledge capture requirements.

---

## Lifecycle Gates

| Lifecycle Phase | Delivery Gate | Knowledge Gate | Enforced By |
|-----------------|---------------|----------------|-------------|
| **Exploration → Initiate** | Qualification criteria met; Exploration artifacts complete | Exploration summary and qualification rationale captured | Proposal Repository + Estimation Workbench |
| **Initiate** | Charter signed; roles assigned; operating model confirmed | — | Engagement Registry + Bootstrap Kit |
| **Discover** | Solution architecture reviewed; staffing committed; test strategy agreed | Architecture decisions documented; gap analysis captured | BRD Validator + People Assignment Tracker |
| **Build** | Increment certification; go-live criteria met | Variability documentation complete; inner source PRs submitted with learning notes | Governance Prep Suite + AVA integration |
| **Transfer** | Handover checklist complete; verification module delivered | Retrospective captured; lessons learned documented | Governance Prep Suite + Customer Portal |
| **Complete** | Stabilization criteria met; inner source complete | Case study draft submitted; reusable patterns tagged | Retrospective Synthesizer + Case Study Generator |

---

## Delivery Gates Detail

### Exploration → Initiate

| Requirement | Description |
|-------------|-------------|
| Qualification complete | Go/no-go decision documented with rationale |
| Commercial alignment | Pricing and terms agreed |
| Archetype identified | Applicable archetype(s) confirmed |
| Staffing feasibility | Initial staffing confirmed available |
| Customer commitment | LOI or contract signed |

### Initiate

| Requirement | Description |
|-------------|-------------|
| Charter signed | Engagement charter approved by EO and customer |
| Roles assigned | EPM, EA, AVA, EPO, ELs confirmed |
| Operating model | Governance structure, meeting cadence, escalation paths documented |
| Repos provisioned | `ENG-{CODE}-requirements` and `ENG-{CODE}-project` created |
| SharePoint ready | Customer SharePoint folders created |

### Discover

| Requirement | Description |
|-------------|-------------|
| Solution architecture | Architecture reviewed and approved |
| Staffing committed | Squad composition confirmed |
| Test strategy | Verification approach agreed with AVA |
| Gap analysis | Platform and archetype gaps documented |
| ADRs | Key architecture decisions recorded |

### Build

| Requirement | Description |
|-------------|-------------|
| Increment certification | Each increment passes AVA certification |
| Go-live criteria | Defined go-live criteria documented and tracked |
| Variability documented | All configuration points documented |
| Inner source | Required inner source contributions submitted |

### Transfer

| Requirement | Description |
|-------------|-------------|
| Handover checklist | All handover artifacts delivered |
| Verification module | Customer can independently verify the assembly |
| Training complete | Customer team training delivered |
| Runbooks delivered | Operational runbooks in place |
| Retrospective | Engagement retrospective completed |

### Complete

| Requirement | Description |
|-------------|-------------|
| Stabilization | Post-go-live stabilization period complete |
| Inner source merged | All inner source PRs accepted to Product Lines |
| Case study | Draft case study submitted |
| Patterns tagged | Reusable patterns identified and tagged |
| Repos archived | Both repos marked read-only |

---

## Knowledge Gates Detail

Knowledge gates follow the same progressive model: initially flagged (Assistance), evolving to blocking (Mandatory Gate) as tooling matures.

### Phase-by-Phase Knowledge Requirements

| Phase Transition | Required Knowledge Artifact | Owner |
|------------------|----------------------------|-------|
| Exploration → Initiate | Exploration summary, qualification rationale | Exploration Lead |
| Discover → Build | Solution architecture, gap analysis, archetype decisions | EA |
| Build → Transfer | Variability documentation, inner source contributions with learning notes | EA + ELs |
| Transfer → Complete | Retrospective, lessons learned, pattern candidates | EPM |
| Complete (exit) | Case study draft, reusable artifacts tagged | EPM + Knowledge Engineer |

### Knowledge Quality Criteria

Each knowledge artifact is evaluated against:

| Criterion | What It Measures |
|-----------|------------------|
| **Completeness** | All required sections populated |
| **Reusability** | Content structured for future reuse (not Engagement-specific jargon) |
| **Findability** | Proper tagging and categorization |
| **Freshness** | Content reviewed within policy period |

---

## Gate Enforcement Modes

| Mode | Behavior | Appropriate When |
|------|----------|------------------|
| **Guidance** | Dashboard shows compliance; no enforcement | Early adoption, tooling unproven |
| **Assistance** | Non-compliance flagged; exceptions documented | Moderate adoption, tooling mostly accurate |
| **Mandatory** | Transition blocked until compliant | Mature adoption, tooling reliable |

### Current Gate Modes

> [!NOTE]
> Gate modes will be configured as tooling matures. Initial deployment will use Guidance mode for all gates.

---

## Exception Process

When an Engagement cannot meet a gate requirement:

1. **Document the exception** — reason, impact, mitigation
2. **Escalate appropriately** — based on gate severity
3. **Track for resolution** — exception appears on compliance dashboard
4. **Review pattern** — repeated exceptions trigger gate policy review

Exception authority:

| Gate Severity | Exception Authority |
|---------------|---------------------|
| Standard | EPM with EO approval |
| Critical (go-live, certification) | EO with ERC notification |

---

## Related Content

- [Compliance Dashboards](compliance-dashboards.md) — visibility into gate compliance
- [Knowledge Governance](knowledge-governance.md) — knowledge contribution requirements
- [Document Governance](../05-document-governance/README.md) — artifact structure and location
