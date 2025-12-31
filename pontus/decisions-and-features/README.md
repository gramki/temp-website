# Decisions and Features

## What This Folder Contains

This folder contains the analysis and arguments for building **semantic infrastructure around features** — treating features as enterprise data products, enabling self-service decisions, and preparing for the agentic future.

---

## Document Overview

| Document | Purpose | Start Here If... |
|----------|---------|------------------|
| [**features-as-data-products.md**](./features-as-data-products.md) | The main problem statement and solution direction | You want to understand the core thesis |
| [**solution-approach.md**](./solution-approach.md) | How to build features as ETSL data products | You want the directional solution approach |
| [**ai-readiness-cliff.md**](./ai-readiness-cliff.md) | Deep dive on why semantic infrastructure is essential for AI agents | You're focused on the agentic future and explainability |
| [**entity-type-vs-instance-analysis.md**](./entity-type-vs-instance-analysis.md) | Analysis of how feature stores handle entity semantics | You want to understand what existing systems do (and don't) |
| [**entity-thinking-objections.md**](./entity-thinking-objections.md) | Anticipated criticisms of entity-centric thinking | You're skeptical and want to see objections addressed |
| [**questions-on-features-and-decisions.md**](./questions-on-features-and-decisions.md) | Open questions and deliberation points | You want to explore what's not yet decided |

---

## Suggested Reading Order

**For a first read:**
1. **features-as-data-products.md** — Start here. The TL;DR and Sections 1-3 cover the problem space.
2. **solution-approach.md** — The directional solution: features as ETSL data products.

**For deeper understanding:**
3. **ai-readiness-cliff.md** — Why this matters for the agentic future
4. **entity-type-vs-instance-analysis.md** — What existing systems actually provide

**For deliberation:**
5. **entity-thinking-objections.md** — Potential criticisms and responses
6. **questions-on-features-and-decisions.md** — Open questions to resolve

---

## How the Documents Relate

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DOCUMENT STRUCTURE                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │              features-as-data-products.md                           │   │
│   │              (Main Document — Problem Statement)                    │   │
│   └───────────────────────────┬─────────────────────────────────────────┘   │
│                               │                                             │
│                               ▼                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │              solution-approach.md                                   │   │
│   │              (Directional Solution — Features as ETSL Products)     │   │
│   └───────────────────────────┬─────────────────────────────────────────┘   │
│                               │                                             │
│               ┌───────────────┼───────────────┐                             │
│               │               │               │                             │
│               ▼               ▼               ▼                             │
│   ┌───────────────────┐ ┌───────────────┐ ┌───────────────────────────┐     │
│   │ ai-readiness-     │ │ entity-type-  │ │ entity-thinking-          │     │
│   │ cliff.md          │ │ vs-instance-  │ │ objections.md             │     │
│   │ (Future: Agents)  │ │ analysis.md   │ │ (Anticipated Criticism)   │     │
│   └───────────────────┘ │ (Current Gap) │ └───────────────────────────┘     │
│                         └───────────────┘                                   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │              questions-on-features-and-decisions.md                 │   │
│   │              (Open Questions — To Be Resolved)                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Themes

| Theme | Where It's Covered |
|-------|-------------------|
| **Features as data products** | features-as-data-products.md (throughout) |
| **Entity semantics** | features-as-data-products.md (Section 1.5), entity-type-vs-instance-analysis.md |
| **Composite entities** | features-as-data-products.md (Section 1.3, 1.4) |
| **Self-service decisions** | features-as-data-products.md (Section 3) |
| **Agentic future / AI-readiness** | features-as-data-products.md (Section 2), ai-readiness-cliff.md |
| **Regulatory / explainability** | ai-readiness-cliff.md (Section 2) |
| **What exists today** | features-as-data-products.md (Section 4), entity-type-vs-instance-analysis.md |
| **Solution direction** | features-as-data-products.md (Section 5), solution-approach.md |
| **ETSL integration** | solution-approach.md |
| **Open questions** | questions-on-features-and-decisions.md |

---

## Status

This is an evolving body of work. The main document (`features-as-data-products.md`) articulates the problem and solution direction. The supporting documents provide depth on specific aspects. The questions document captures what's not yet resolved.

**Next steps** are outlined in Section 8 of the main document.

