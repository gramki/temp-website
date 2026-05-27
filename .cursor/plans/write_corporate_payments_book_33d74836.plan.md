---
name: Write Corporate Payments Book
overview: Write all 30 chapters + front matter + appendix of the Corporate Payments Concepts book using parallel agents, with part-level subfolders for maintainability.
todos:
  - id: agent-1-frontmatter
    content: "Agent 1: Write 00-front-matter/ (01-purpose-audience-scope.md, 02-running-example.md)"
    status: completed
  - id: agent-2-part1-narrative
    content: "Agent 2: Write 01-problem-space/ Ch 1,3,4,5 + 06-bridge.md"
    status: completed
  - id: agent-3-part1-research
    content: "Agent 3: Write 01-problem-space/02-existing-solutions.md (with web research)"
    status: completed
  - id: agent-4-part2-bank-esp
    content: "Agent 4: Write 02-ontology/ Ch 6,7,8 (01-03)"
    status: completed
  - id: agent-5-part2-financial
    content: "Agent 5: Write 02-ontology/ Ch 9,10,11,12 (04-07)"
    status: completed
  - id: agent-6-part2-profiles
    content: "Agent 6: Write 02-ontology/ Ch 13-17 (08-12)"
    status: completed
  - id: agent-7-part3-bank
    content: "Agent 7: Write 03-bank-foundation/ Ch 18-20 (01-03)"
    status: completed
  - id: agent-8-part4-esp
    content: "Agent 8: Write 04-esp-playbook/ Ch 21-25 (01-05)"
    status: completed
  - id: agent-9-part5-corporate
    content: "Agent 9: Write 05-corporate-playbook/ Ch 26-30 (01-05)"
    status: completed
  - id: agent-10-appendix
    content: "Agent 10: Write 06-appendix/01-state-models.md"
    status: completed
isProject: false
---

# Write Corporate Payments Concepts Book

## Source Files (every agent must read these)

- **Outline**: [suggested-outline-draft.md](us-bank-commercial-card/suggested-outline-draft.md) — writing style (lines 1-45), chapter specs, running example
- **Domain knowledge**: [overview.md](us-bank-commercial-card/overview.md) — 1675 lines of raw concepts, writing instructions, and clarifications
- **Q&A clarifications**: [open-questions.md](us-bank-commercial-card/open-questions.md) — 64 answered questions resolving ambiguities

## Output Directory and Folder Structure

```
us-bank-commercial-card/corporate-payments-book/
  00-front-matter/
    01-purpose-audience-scope.md
    02-running-example.md
  01-problem-space/
    01-corporate-payments-problem.md
    02-existing-solutions.md
    03-two-lenses.md
    04-spend-archetypes.md
    05-spend-mandates.md
    06-bridge.md
  02-ontology/
    01-corporate-legal-entity-ou-members.md
    02-account-product-virtual-card-product.md
    03-esp-variants-corporate-payment-product.md
    04-credit-facility-budget-account.md
    05-corporate-payment-program.md
    06-card-profile.md
    07-spend-policy-controls.md
    08-booking-settlement-profile.md
    09-users-roles.md
    10-members-eligibility-enrollment.md
    11-transaction-posting-data.md
    12-multi-currency-residency.md
  03-bank-foundation/
    01-account-card-products.md
    02-onboarding.md
    03-processing-authorization-controls.md
  04-esp-playbook/
    01-esp-wide-concerns.md
    02-supplier-payments-product.md
    03-employee-spend-product.md
    04-travel-payments-product.md
    05-central-recurring-product.md
  05-corporate-playbook/
    01-corporate-wide-concerns.md
    02-supplier-payments-program.md
    03-employee-spend-program.md
    04-travel-payments-program.md
    05-central-recurring-program.md
  06-appendix/
    01-state-models.md
```

Files are numbered within each part-folder. Adding/removing a chapter only affects numbering within that folder. Cross-references in content use chapter titles (e.g., "see *Credit Facility, Budget, and Account*") rather than file numbers.

## Agent Plan — 10 Parallel Agents

### Agent 1: Front Matter

- **Folder**: `00-front-matter/`
- **Files**: `01-purpose-audience-scope.md`, `02-running-example.md`
- **Outline sections**: Lines 48-107 (Part 0, Running Example)
- **Content notes**: Purpose/audience/scope sets up who the book is for (Zeta PMs), why it exists (two-lens problem), Zeta's role (Tachyon + Electron), assumed knowledge (four-party model), and out-of-scope items. Running Example defines Meridian Industries (3 LEs, OU trees, 18K employees, four spend needs), Apex Payments (ESP on Electron, 4 archetypes, 40+ corporates, AMCs), Commonwealth National Bank (on Tachyon, creates products, underwrites CFs). Include mermaid diagram showing three-actor interaction model and platform mapping.

### Agent 2: Part I Narrative + Bridge (Ch 1, 3, 4, 5 + Bridge)

- **Folder**: `01-problem-space/`
- **Files**: `01-corporate-payments-problem.md`, `03-two-lenses.md`, `04-spend-archetypes.md`, `05-spend-mandates.md`, `06-bridge.md`
- **Outline sections**: Lines 110-193
- **Overview sections to read**: Spend Lanes (section 20), Spend Mandate concepts, control archetypes per lane (section 3), reconciliation per lane (section 6), ESP role (section 9)
- **Content notes**: Most narrative part of the book. Ch 1 establishes Meridian's pain across four different teams. Ch 3 uses concrete dissonance examples (Commonwealth packages products one way, Meridian evaluates them completely differently). Ch 4 defines four Spend Archetypes with mermaid diagrams comparing control models, card lifecycles, and enrollment patterns. Ch 5 unpacks eight mandate components with enforceable-vs-auditable split. Bridge is short — maps Archetypes and Mandates to their system entity counterparts with a mapping diagram. Forward-references to Parts IV and V.

### Agent 3: Part I Ch 2 — Existing Solutions (RESEARCH REQUIRED)

- **Folder**: `01-problem-space/`
- **Files**: `02-existing-solutions.md`
- **Outline sections**: Lines 129-146
- **Content notes**: This chapter needs web research on how banks (JPMorgan, Citi, US Bank), networks (Visa, Mastercard, Amex), and fintechs currently package virtual card / commercial card products. Categorize by: AP/supplier payment programs, commercial/purchasing cards, travel virtual cards, lodge/ghost cards, embedded/API issuance. Research what works (rich controls, real-time auth, improving data) and what doesn't (bank-centric packaging, reconciliation as afterthought, workflow gap). Include mermaid diagram showing the gap between bank product taxonomy and corporate workflow taxonomy. Use Meridian as example of a corporate trying to adopt these products.

### Agent 4: Part II — Corporate Foundation + Bank + ESP Domain Entities (Ch 6, 7, 8)

- **Folder**: `02-ontology/`
- **Files**: `01-corporate-legal-entity-ou-members.md`, `02-account-product-virtual-card-product.md`, `03-esp-variants-corporate-payment-product.md`
- **Outline sections**: Lines 197-261
- **Overview sections to read**: Sections 1 (Corporate/OU model), 7 (Supplier/Merchant distinction), 9 (ESP role), 22 (Bank products, Variants, assembly), Q&A 1-3 (Corporate/OU), Q&A 11-13 (ESP), Q&A 28-29 (Member, Client Contract), Q&A 48-60 (bank products, variants, redistributability, override model)
- **Content notes**: Reference-style. Each chapter opens with bold one-sentence definition per entity. Ch 6 needs mermaid ER diagram for Corporate→Legal Entity→OU→Member hierarchy, with Meridian's 3 LEs and OU trees as example. Ch 7 needs entity definition for Account Product and Virtual Card Product with Commonwealth's catalog as example. Ch 8 needs assembly diagram: Account Product → Account Variant → CPP ← Virtual Card Variant ← Virtual Card Product, plus full component program lists, override model, notification programs, commercial terms. Apex's variant setup as example.

### Agent 5: Part II — Financial Hierarchy + Program + Card + Controls (Ch 9, 10, 11, 12)

- **Folder**: `02-ontology/`
- **Files**: `04-credit-facility-budget-account.md`, `05-corporate-payment-program.md`, `06-card-profile.md`, `07-spend-policy-controls.md`
- **Outline sections**: Lines 263-326
- **Overview sections to read**: Sections 1-2 (Account, CF, Budget definitions), 3 (roles, controls per lane), 5 (mandate enforcement), Q&A 4-10 (Account/Budget cardinality, sharing, hierarchy), Q&A 19-20 (pending spend, refunds), Q&A 27 (Card Profile structure), Q&A 30-32 (Spend Policy entity, controls per lane), Q&A 44 (AMC in Spend Policy)
- **Content notes**: Ch 9 needs bank-domain vs corporate-domain mapping table and mermaid diagram of CF→Budget→Account→Card hierarchy, with state models for each. Ch 10 needs Product-vs-Program comparison and state model (Draft→Active→Suspended→Closed). Ch 11 needs Card Profile structure diagram (Cardholder Profile, Spend Policy, Fee Overrides, Tags with detailed sub-components). Ch 12 needs cascading policy diagram (Product→Program→Card, tighten-only), Merchant/AMC definitions, enforceable vs auditable controls. Meridian examples with specific CF amounts, budget allocations.

### Agent 6: Part II — Profiles, People, Data, Cross-Border (Ch 13, 14, 15, 16, 17)

- **Folder**: `02-ontology/`
- **Files**: `08-booking-settlement-profile.md`, `09-users-roles.md`, `10-members-eligibility-enrollment.md`, `11-transaction-posting-data.md`, `12-multi-currency-residency.md`
- **Outline sections**: Lines 328-368
- **Overview sections to read**: Section 4 (posting data, statements), 6 (reconciliation per lane), 8 (residency, FX, billing, settlement), Q&A 16-20 (profiles, disputes, refunds), Q&A 34-38 (enrollment, physical/virtual cards, approval engine, FX, billing), Q&A 43 (Users vs Members), Q&A 45-46 (data capture forms, settlement timing)
- **Content notes**: Ch 13 needs Booking Profile rules flow diagram (static defaults + dynamic overrides) and Settlement Profile one-account-per-program constraint. Ch 14 is short — Users/Roles scope diagram showing access to OUs, Programs, Products, Budgets. Ch 15 needs eligibility→enrollment→card issuance flow diagram with KYC steps and approval engine. Ch 16 needs L1/L2/L3 data structure diagram with three-source model (network, merchant, payer). Ch 17 needs multi-currency flow diagram. Meridian examples throughout.

### Agent 7: Part III — Bank Foundation (Ch 18, 19, 20)

- **Folder**: `03-bank-foundation/`
- **Files**: `01-account-card-products.md`, `02-onboarding.md`, `03-processing-authorization-controls.md`
- **Outline sections**: Lines 372-422
- **Overview sections to read**: Section 22 (full bank role including products, variants, processing, controls), Q&A 48-60 (all bank-related questions), Q&A 61-64 (notification programs)
- **Content notes**: Narrative + reference hybrid. Ch 18 provides narrative context for why the bank creates Account Products and Virtual Card Products (companion to Ch 7 entity reference) — covers catalogs, redistributability, what bank retains vs exposes. Ch 19 needs onboarding journey diagram (ESP onboarding → LE KYB → CF extension) with Commonwealth onboarding Apex and KYB'ing Meridian's three LEs. Ch 20 needs authorization flow diagram showing bank enforcement of all policies with optional ESP/Corporate participation, rewards/rebates computation split, bank-side non-overridable controls list, notification boundary. All illustrated with Commonwealth.

### Agent 8: Part IV — ESP Playbook (Ch 21, 22, 23, 24, 25)

- **Folder**: `04-esp-playbook/`
- **Files**: `01-esp-wide-concerns.md`, `02-supplier-payments-product.md`, `03-employee-spend-product.md`, `04-travel-payments-product.md`, `05-central-recurring-product.md`
- **Outline sections**: Lines 426-503
- **Overview sections to read**: Section 9 (ESP role), 22 (variants, product assembly, Notification Programs), Q&A 11-13 (ESP multi-corporate, entity model, ESP replacement), Q&A 23-24 (commercial terms per Product not Program), Q&A 29 (Client Contract), Q&A 50-53 (variant composition, assembly, reuse)
- **Content notes**: Ch 21 needs ESP operational flow diagram (Client Contract → Variant creation → CPP assembly → Relationship-level terms → Corporate onboarding → Billing). Covers variant creation, branding, product assembly rule (1+1=1). Ch 22-25: each archetype product chapter needs a design decision summary table covering baseline Spend Policy, Card Profile template, fees, settlement mechanics, control capabilities, data/reporting. Each needs a mermaid diagram of the product's control model and card lifecycle. Use Apex building products for Commonwealth as running example.

### Agent 9: Part V — Corporate Playbook (Ch 26, 27, 28, 29, 30)

- **Folder**: `05-corporate-playbook/`
- **Files**: `01-corporate-wide-concerns.md`, `02-supplier-payments-program.md`, `03-employee-spend-program.md`, `04-travel-payments-program.md`, `05-central-recurring-program.md`
- **Outline sections**: Lines 507-616
- **Overview sections to read**: Sections 1-8 (all corporate domain concepts), Q&A 1-10 (Corporate/OU/Budget/Account), Q&A 31-33 (per-lane control archetypes and reconciliation)
- **Content notes**: Ch 26 needs corporate administration diagram covering OUs, Budgets, Settlement Accounts, Members, Users, notification customization, settlement operations. Ch 27-30 each follow the Reference + Program Journey structure from the outline. Each needs: a reference box (control archetype, eligibility model, cardholder, reconciliation pattern) and a full program journey as a numbered sequence (10-12 steps) with a mermaid sequence diagram. Detailed Meridian examples: specific program names, dollar amounts, OU assignments, supplier/employee names, cost centers, GL codes. Each journey covers creation → configuration → enrollment → card issuance → transaction → clearing → billing → settlement → booking → reconciliation.

### Agent 10: Appendix — State Models

- **Folder**: `06-appendix/`
- **Files**: `01-state-models.md`
- **Outline sections**: Line 624
- **Overview sections to read**: Q&A 26 (state models needed), Q&A 59 (variant state models in scope)
- **Content notes**: Consolidated reference. Cover state models for: Credit Facility, Budget, Account, Card, Corporate Payment Program, ESP Account Variant, ESP Virtual Card Variant. Each entity gets a mermaid stateDiagram and a transition table (from-state, event/trigger, to-state). Account Product and Virtual Card Product state models are out of scope (bank-internal). Research reasonable state transitions for each entity.

## Agent Instructions Template

Every agent receives this instruction preamble:

1. Read the Writing Style section (lines 1-45) of `suggested-outline-draft.md` FIRST — it defines voice, tone, terminology discipline, and per-part calibration
2. Read the Running Example (lines 58-106) for the three fictitious entities used throughout
3. Read the assigned outline sections for your specific chapters
4. Read the relevant sections of `overview.md` and `open-questions.md` for detailed domain content and clarifications
5. Write each chapter as a standalone markdown file in the assigned subfolder
6. Use mermaid diagrams extensively — at least one per chapter, more for complex topics
7. Use Meridian/Apex/Commonwealth with concrete, detailed examples (specific numbers, configurations, decisions)
8. Follow practitioner-authoritative style: declarative, precise, active voice, third person, no meta-narration
9. Cross-reference other chapters by title (e.g., "see *Credit Facility, Budget, and Account*") not by file number
10. Each Part II (02-ontology/) chapter opens with a bold one-sentence definition block for each entity defined in that chapter

## Execution Strategy

All 10 agents launch in parallel. No sequential dependencies because:

- The outline provides complete specifications for every chapter
- Cross-references use chapter titles (refactoring-safe)
- Each agent reads source files independently
- The writing style is defined once and shared

