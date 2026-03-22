# Corporate Payments by Design

**Entities, Archetypes, and Operating Models for the Tachyon–Electron Platform**

---

## What This Book Is

A practitioner-authoritative reference for Zeta product managers building and evolving the corporate payments platform. The book defines the entities, relationships, control models, and lifecycle patterns that constitute the corporate payments domain — as seen through three distinct lenses: **Bank**, **ESP**, and **Corporate**.

The central argument: a bank sees products, a corporate sees workflow controls, and an ESP translates between the two. Every entity in this book is placed in exactly one of those three domains, with its ownership, authority boundaries, and interaction patterns made explicit.

## How to Read It

The book is structured as a progressive build-up, but each chapter also works as a standalone reference.

**Cover-to-cover** — read Parts I through V in order. Part I establishes the problem space and conceptual tools (Spend Archetypes, Spend Mandates). Part II defines every entity in the ontology. Parts III–V show how each actor uses those entities.

**By role** — jump to the part that matches your current work:

| If you are working on… | Start with |
|---|---|
| Understanding the domain from scratch | [Part I — The Problem Space](01-problem-space/) → [Part II — The Ontology](02-ontology/) |
| Bank platform (Tachyon) capabilities | [Part III — The Bank's Foundation](03-bank-foundation/) |
| ESP platform (Electron) product design | [Part IV — The ESP's Playbook](04-esp-playbook/) |
| Corporate portal and program operations | [Part V — The Corporate's Playbook](05-corporate-playbook/) |
| A specific entity definition | [Part II — The Ontology](02-ontology/) (find the chapter below) |
| State models and lifecycle transitions | [Appendix](06-appendix/) |

## Running Example

Three fictitious entities appear throughout every chapter:

| Entity | Role | Platform |
|---|---|---|
| **Commonwealth National Bank** | Bank — underwrites Credit Facilities, creates Account Products and Virtual Card Products | Tachyon |
| **Apex Payments** | ESP — creates Corporate Payment Products, onboards corporates, manages billing | Electron |
| **Meridian Industries** | Corporate — configures Programs, enrolls members, operates spend workflows | Electron (corporate portal) |

Meridian operates across three legal entities (US, UK, India), four Spend Archetypes, and multiple currencies — designed to exercise every concept in the book. See *The Running Example* for full details.

---

## Table of Contents

### Front Matter

| # | Chapter | File |
|---|---|---|
| — | Purpose, Audience, and Scope | [`00-front-matter/01-purpose-audience-scope.md`](00-front-matter/01-purpose-audience-scope.md) |
| — | The Running Example | [`00-front-matter/02-running-example.md`](00-front-matter/02-running-example.md) |

### Part I — The Problem Space

| # | Chapter | File |
|---|---|---|
| 1 | The Corporate Payments Problem | [`01-problem-space/01-corporate-payments-problem.md`](01-problem-space/01-corporate-payments-problem.md) |
| 2 | Existing Solutions and Their Limitations | [`01-problem-space/02-existing-solutions.md`](01-problem-space/02-existing-solutions.md) |
| 3 | Two Lenses — Why the Gap Exists | [`01-problem-space/03-two-lenses.md`](01-problem-space/03-two-lenses.md) |
| 4 | Spend Archetypes — Four Workflow Patterns | [`01-problem-space/04-spend-archetypes.md`](01-problem-space/04-spend-archetypes.md) |
| 5 | Spend Mandates — The Authorization Envelope | [`01-problem-space/05-spend-mandates.md`](01-problem-space/05-spend-mandates.md) |
| — | Bridge: From Concepts to Entities | [`01-problem-space/06-bridge.md`](01-problem-space/06-bridge.md) |

### Part II — The Ontology

| # | Chapter | File |
|---|---|---|
| 6 | Corporate, Legal Entity, Organizational Unit, and Members | [`02-ontology/01-corporate-legal-entity-ou-members.md`](02-ontology/01-corporate-legal-entity-ou-members.md) |
| 7 | Account Product and Virtual Card Product | [`02-ontology/02-account-product-virtual-card-product.md`](02-ontology/02-account-product-virtual-card-product.md) |
| 8 | ESP Variants and Corporate Payment Product | [`02-ontology/03-esp-variants-corporate-payment-product.md`](02-ontology/03-esp-variants-corporate-payment-product.md) |
| 9 | Credit Facility, Budget, and Account | [`02-ontology/04-credit-facility-budget-account.md`](02-ontology/04-credit-facility-budget-account.md) |
| 10 | Corporate Payment Program | [`02-ontology/05-corporate-payment-program.md`](02-ontology/05-corporate-payment-program.md) |
| 11 | Card Profile | [`02-ontology/06-card-profile.md`](02-ontology/06-card-profile.md) |
| 12 | Spend Policy and Controls | [`02-ontology/07-spend-policy-controls.md`](02-ontology/07-spend-policy-controls.md) |
| 13 | Booking Profile and Settlement Profile | [`02-ontology/08-booking-settlement-profile.md`](02-ontology/08-booking-settlement-profile.md) |
| 14 | Users and Roles | [`02-ontology/09-users-roles.md`](02-ontology/09-users-roles.md) |
| 15 | Members, Eligibility, and Enrollment | [`02-ontology/10-members-eligibility-enrollment.md`](02-ontology/10-members-eligibility-enrollment.md) |
| 16 | Transaction Posting and Data | [`02-ontology/11-transaction-posting-data.md`](02-ontology/11-transaction-posting-data.md) |
| 17 | Multi-Currency, Residency, and Cross-Border | [`02-ontology/12-multi-currency-residency.md`](02-ontology/12-multi-currency-residency.md) |

### Part III — The Bank's Foundation

| # | Chapter | File |
|---|---|---|
| 18 | Account Products and Virtual Card Products — The Bank's Building Blocks | [`03-bank-foundation/01-account-card-products.md`](03-bank-foundation/01-account-card-products.md) |
| 19 | Onboarding — ESP and Corporate Legal Entities | [`03-bank-foundation/02-onboarding.md`](03-bank-foundation/02-onboarding.md) |
| 20 | Processing, Authorization, and Controls | [`03-bank-foundation/03-processing-authorization-controls.md`](03-bank-foundation/03-processing-authorization-controls.md) |

### Part IV — The ESP's Playbook

| # | Chapter | File |
|---|---|---|
| 21 | ESP-Wide Concerns | [`04-esp-playbook/01-esp-wide-concerns.md`](04-esp-playbook/01-esp-wide-concerns.md) |
| 22 | Designing the Supplier Payments Product | [`04-esp-playbook/02-supplier-payments-product.md`](04-esp-playbook/02-supplier-payments-product.md) |
| 23 | Designing the Employee & Department Spend Product | [`04-esp-playbook/03-employee-spend-product.md`](04-esp-playbook/03-employee-spend-product.md) |
| 24 | Designing the Travel & Booking Payments Product | [`04-esp-playbook/04-travel-payments-product.md`](04-esp-playbook/04-travel-payments-product.md) |
| 25 | Designing the Central Recurring Merchant Payments Product | [`04-esp-playbook/05-central-recurring-product.md`](04-esp-playbook/05-central-recurring-product.md) |

### Part V — The Corporate's Playbook

| # | Chapter | File |
|---|---|---|
| 26 | Corporate-Wide Concerns | [`05-corporate-playbook/01-corporate-wide-concerns.md`](05-corporate-playbook/01-corporate-wide-concerns.md) |
| 27 | Operating the Supplier Payments Program | [`05-corporate-playbook/02-supplier-payments-program.md`](05-corporate-playbook/02-supplier-payments-program.md) |
| 28 | Operating the Employee & Department Spend Program | [`05-corporate-playbook/03-employee-spend-program.md`](05-corporate-playbook/03-employee-spend-program.md) |
| 29 | Operating the Travel & Booking Payments Program | [`05-corporate-playbook/04-travel-payments-program.md`](05-corporate-playbook/04-travel-payments-program.md) |
| 30 | Operating the Central Recurring Merchant Payments Program | [`05-corporate-playbook/05-central-recurring-program.md`](05-corporate-playbook/05-central-recurring-program.md) |

### Appendix

| # | Chapter | File |
|---|---|---|
| — | State Models | [`06-appendix/01-state-models.md`](06-appendix/01-state-models.md) |

---

## Key Concepts at a Glance

| Concept | Domain | Defined In |
|---|---|---|
| Spend Archetype | Conceptual | Ch 4 |
| Spend Mandate | Conceptual | Ch 5 |
| Corporate / Legal Entity / OU | Corporate | Ch 6 |
| Member (Employee, Supplier, Contractor, Client) | Corporate | Ch 6, 15 |
| Account Product / Virtual Card Product | Bank (Tachyon) | Ch 7 |
| ESP Account Variant / ESP Virtual Card Variant | ESP (Electron) | Ch 8 |
| Corporate Payment Product | ESP (Electron) | Ch 8 |
| Credit Facility / Budget / Account | Dual (Bank + Corporate) | Ch 9 |
| Corporate Payment Program | Corporate | Ch 10 |
| Card Profile | Corporate | Ch 11 |
| Spend Policy / AMC | Cascading (ESP → Corporate → Card) | Ch 12 |
| Booking Profile / Settlement Profile | Corporate | Ch 13 |
| Users and Roles | Corporate | Ch 14 |

## Conventions

- **Cross-references** between chapters use *italicized chapter titles*.
- **Mermaid diagrams** are used throughout for entity relationships, state models, and operational flows.
- **Running-example values** (Credit Facility amounts, Budget allocations, member names) are consistent across all chapters. Canonical values: US $50M, UK £12M, India ₹400M.
- **Entity definitions** appear in Part II. Parts III–V reference those definitions without repeating them.
