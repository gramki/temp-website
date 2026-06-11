# Knowledge Engineering

[← Back to Engagement Readiness Engineering](../README.md)

Knowledge capture is not optional overhead — it is a **first-class function** within Engagement Readiness Engineering.

## Core Principle

Every Engagement generates reusable knowledge: patterns, architectures, lessons learned, case studies. ERE treats this knowledge as an asset to be systematically captured, curated, and leveraged — not as an afterthought documented post-hoc.

## Design Philosophy

| Principle | Implementation |
|-----------|----------------|
| **Capture at the source** | Knowledge is a byproduct of work — tools capture decisions, patterns, and insights as they happen |
| **AI-assisted drafting** | Agents propose knowledge artifacts from work products; humans review and approve |
| **Quality gates** | Completeness, reusability score, findability (tagging), freshness (periodic review) |
| **Visible metrics** | Contribution tracked at individual, team, and portfolio levels |

## Knowledge Lifecycle

```
Work Product → AI Extraction → Human Review → Knowledge Base → Reuse
     ↑                                              │
     └──────────────── Feedback Loop ───────────────┘
```

## In This Section

| Document | Description |
|----------|-------------|
| [Ownership](ownership.md) | Knowledge Engineer role, Domain Steward rotation model |
| [Lifecycle Capture](lifecycle-capture.md) | Required artifacts at each phase transition |
| [Pattern Curator Agent](pattern-curator.md) | AI agent for pattern discovery, curation, and gap identification |

## Relationship to Other Sections

- **AI Architecture**: Knowledge Engineering relies on [AI agents](../03-ai-architecture/agents.md) for extraction and curation
- **Systems**: The [Knowledge & Reuse Platform](../02-systems/knowledge-platform.md) provides the tooling infrastructure
- **Governance**: Knowledge gates are enforced through [Governance Enforcement](../06-governance-enforcement/README.md)

## Tooling Principles

| Principle | How It Works |
|-----------|--------------|
| **Capture at the source** | Knowledge is a byproduct of work — Meeting Suite transcribes and extracts decisions; BRD Author prompts "What's generalizable here?" |
| **AI-assisted drafting** | Agents propose knowledge artifacts from work products; humans review and approve |
| **Quality gates** | Completeness, reusability score, findability (tagging), freshness (periodic review) |
| **Contribution metrics** | Visible at individual, team, and portfolio levels |

---

*See also: [Knowledge & Reuse Platform](../02-systems/knowledge-platform.md) | [AI Agents](../03-ai-architecture/agents.md) | [Knowledge Governance](../06-governance-enforcement/knowledge-governance.md)*

---

[← Previous: AI Architecture](../03-ai-architecture/README.md) | [→ Next: Document Governance](../05-document-governance/README.md)
