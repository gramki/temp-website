# Why Seer?

**A comprehensive guide to enterprise AI agent platforms and why Seer exists.**

---

## What Is This?

This is a textbook-style documentation of Seer, Zeta's enterprise agent platform. It explains:

- **The Problem:** Why enterprise AI agents require capabilities that cloud-managed AI services don't provide
- **The Solution:** How Seer addresses these requirements with a purpose-built architecture

## Who Should Read This?

| Reader | Start Here |
|--------|------------|
| **Executives & Decision Makers** | [Preface](./00-front-matter/00-1-preface.md) → [Summary: Why Seer](./part-2-how-seer-solves/13-summary-why-seer/_section-overview.md) |
| **Enterprise Architects** | [Part 1: Background](./part-1-background/_part-overview.md) (full) |
| **Developers & Engineers** | [Part 2: How Seer Solves](./part-2-how-seer-solves/_part-overview.md) (full) |
| **Security & Compliance** | [Identity & Authority](./part-2-how-seer-solves/03-identity-authority-in-seer/_section-overview.md) + [Audit](./part-1-background/04-audit-requirements/_section-overview.md) |
| **Quick Reference** | [Glossary](./appendices/appendix-a-glossary.md) |

## Document Structure

```
why-seer/
├── 00-front-matter/           # Preface, How to Use, Table of Contents
├── part-1-background/         # The Problem Space (5 sections)
│   ├── 01-what-is-enterprise-agent-platform/
│   ├── 02-why-enterprise-agents-different/
│   ├── 03-memory-requirements/
│   ├── 04-audit-requirements/
│   └── 05-building-enterprise-agent/
├── part-2-how-seer-solves/    # The Solution (13 sections)
│   ├── 01-seer-design-philosophy/
│   ├── 02-agent-lifecycle-in-seer/
│   ├── 03-identity-authority-in-seer/
│   ├── 04-memory-knowledge-audit-in-seer/
│   ├── 05-context-assembly-in-seer/
│   ├── 06-governance-override-in-seer/
│   ├── 07-runtime-observability-in-seer/
│   ├── 08-model-gateway-in-seer/
│   ├── 09-cost-governance-in-seer/
│   ├── 10-tools-actions-in-seer/
│   ├── 11-multi-agent-patterns-in-seer/
│   ├── 12-feedback-learning-in-seer/
│   └── 13-summary-why-seer/
└── appendices/                # Glossary, References, AOSM Foundations
```

## How to Read

### Option 1: Sequential (Recommended for First-Time Readers)

1. Start with the [Preface](./00-front-matter/00-1-preface.md)
2. Read [How to Use This Book](./00-front-matter/00-2-how-to-use-this-book.md)
3. Follow Part 1 → Part 2 → Appendices

### Option 2: Problem-First

1. Start with [Part 1: Background](./part-1-background/_part-overview.md) to understand the problem
2. Then jump to specific Part 2 sections that address your concerns

### Option 3: Solution-First

1. Go directly to [Part 2: How Seer Solves](./part-2-how-seer-solves/_part-overview.md)
2. Reference Part 1 sections when you need context on "why"

### Option 4: Reference

1. Use the [Table of Contents](./00-front-matter/00-3-table-of-contents.md) to navigate
2. Consult the [Glossary](./appendices/appendix-a-glossary.md) for terminology

## Key Concepts at a Glance

| Concept | Definition | Where to Learn More |
|---------|------------|---------------------|
| **OPD Triad** | Observability, Predictability, Directability—what makes agents enterprise-ready | [Section 1.3](./part-1-background/01-what-is-enterprise-agent-platform/01-3-opd-triad.md) |
| **Raw → Trained → Employed** | The three-layer agent lifecycle model | [Section 5.1](./part-1-background/05-building-enterprise-agent/05-1-agent-lifecycle.md) |
| **ESPP Taxonomy** | Memory types: Episodic, Semantic, Procedural, Preference | [Section 3.2](./part-1-background/03-memory-requirements/03-2-espp-taxonomy.md) |
| **CAF** | Cognitive Audit Fabric—enterprise memory control plane | [Section 4.3](./part-1-background/04-audit-requirements/04-3-cognitive-audit-fabric.md) |
| **Seer + Hub** | Two-system architecture: Agent governance + Operational substrate | [Section 1.1 (P2)](./part-2-how-seer-solves/01-seer-design-philosophy/01-1-two-system-architecture.md) |

## Quick Links

| Resource | Description |
|----------|-------------|
| [📖 Full Table of Contents](./00-front-matter/00-3-table-of-contents.md) | Complete navigational index |
| [📚 Glossary](./appendices/appendix-a-glossary.md) | All terms and definitions |
| [🔗 Seer + Hub Division](./appendices/appendix-b-seer-hub-division.md) | What Seer owns vs. what Hub owns |
| [📐 AOSM Foundations](./appendices/appendix-c-aosm-foundations.md) | Theoretical foundations |
| [📎 Further Reading](./appendices/appendix-d-further-reading.md) | Links to related documentation |

## Related Documentation

- **Seer Design:** `olympus-seer-docs/seer-design/`
- **Hub Documentation:** `olympus-hub-docs/`
- **AOSM Meta-Model:** `aosm-meta-model/`

---

*This document is part of the Zeta AI Product Strategy documentation. For questions or feedback, consult the [requires-expansion-or-review.md](./requires-expansion-or-review.md) tracking document.*

