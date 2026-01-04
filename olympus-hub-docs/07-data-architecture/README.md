# Data Architecture

This section covers the data architecture for Olympus Hub, including the layered storage model, cognitive services, and application data stores.

---

## Core Principle

Hub separates data by **ownership**, **purpose**, and **cognitive classification**:

| Category | Owner | Purpose |
|----------|-------|---------|
| **System Data** | Platform (Zeta) | Blueprints, registries, industry knowledge |
| **Tenant Spec** | Tenant Admins | Configuration, definitions, schemas |
| **Operations Data** | Hub | Requests, tasks, activities, signals |
| **Application Data** | Hub Applications | Business domain entities |
| **Memory Services** | Hub (semantic) | Enterprise, Agent, User memory (incl. decisions) |
| **Knowledge Services** | Hub (semantic) | RAG, curated enterprise knowledge |

> **Note:** CAF (Cognitive Audit Fabric) is the **control plane** for Enterprise Memory — it governs how decisions, evidence, and explanations are structured and accessed. It is not a separate storage layer.

---

## Key Distinction: Cognitive vs Operational vs Domain Data

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA CLASSIFICATION                       │
│                                                              │
│   ┌───────────────────────────────────────────────────────┐ │
│   │              COGNITIVE DATA                            │ │
│   │   "What do we know, remember, and learn?"              │ │
│   │                                                        │ │
│   │      Memory Services      │      Knowledge Services    │ │
│   │   (Control Plane: CAF)    │                            │ │
│   └───────────────────────────────────────────────────────┘ │
│                                                              │
│   ┌───────────────────────────────────────────────────────┐ │
│   │              OPERATIONAL DATA                          │ │
│   │   "What is happening in the Hub?"                      │ │
│   │                                                        │ │
│   │   Requests │ Tasks │ Activities │ Actions │ Sessions   │ │
│   └───────────────────────────────────────────────────────┘ │
│                                                              │
│   ┌───────────────────────────────────────────────────────┐ │
│   │              DOMAIN DATA                               │ │
│   │   "What business entities does my application manage?" │ │
│   │                                                        │ │
│   │   Ganymede (Relational) │ Callisto (KV) │ Europa (Search) │
│   └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Storage Architecture](./storage-architecture.md) | Layered storage model with selection guide | 🟡 WIP |
| [Application Data Stores](./application-data-stores.md) | Ganymede, Callisto, Europa for applications | 🔴 Stub |
| [Storage FAQ](./storage-faq.md) | Common questions for architects and developers | ✅ Complete |

---

## Quick Reference: Where to Store What

| Data Type | Store | Why |
|-----------|-------|-----|
| Policies, SOPs, rules | Knowledge Services | Curated, governed truth |
| Decisions, precedents | Enterprise Memory (via CAF) | Institutional learning |
| Agent learning | Agent Memory | Operational continuity |
| User preferences | User Memory | Personalization |
| Requests, tasks | Operations Data | Hub-managed lifecycle |
| Business entities | Ganymede | Relational, transactional |
| Entity state cache | Callisto | Fast key-value |
| Search, logs, analytics | Europa | Full-text, aggregation |

---

*Status: 🟡 WIP - Structure defined with storage selection guidance*
