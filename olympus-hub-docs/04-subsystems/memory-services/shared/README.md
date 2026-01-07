# Shared Memory Concepts

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Parent**: [Memory Services](../README.md)

---

## Overview

This folder contains concepts and specifications shared across both **Enterprise Memory** and **Agent Memory** services. These shared foundations ensure consistency while allowing each memory type to have its specific semantics.

---

## Documents

| Document | Description | Status |
|----------|-------------|--------|
| [ESPP Taxonomy](./espp-taxonomy.md) | Unified Episodic-Semantic-Procedural-Preference taxonomy | 🟡 Draft |
| [PII Policy](./pii-policy.md) | PII handling across memory types | 🟡 Draft |

---

## Shared Principles

### 1. ESPP Taxonomy

Both Enterprise and Agent Memory use the **ESPP (Episodic-Semantic-Procedural-Preference)** taxonomy:

| Memory Class | Anchoring | Purpose |
|--------------|-----------|---------|
| **Episodic** | Event/Time | What happened |
| **Semantic** | Entity/Domain | What we know |
| **Procedural** | Skill/Task | How to act |
| **Preference** | Subject | How to personalize |

The same classes appear in both memory types, but with different scopes and semantics.

### 2. Workbench Scoping

Both Enterprise and Agent Memory stores are **workbench-scoped**:
- Provisioned as part of Workbench specification
- Isolated between workbenches
- Tenant boundaries enforced

### 3. CAF Compatibility

Both memory types follow CAF schema conventions:
- Record ID format (UUID v4)
- Content hash for integrity (Enterprise: required; Agent: optional)
- Typed content conventions
- Hub metadata structure

### 4. Olympus Platform Integration

Both memory types use Olympus platform services:
- **Enterprise Memory**: Europa (managed OpenSearch)
- **Agent Memory**: TBD (potentially Callisto, Europa, or purpose-built)

---

## Key Differences

| Aspect | Enterprise Memory | Agent Memory |
|--------|-------------------|--------------|
| **Scope** | Organizational | Agent/Session |
| **Retention** | 7+ years | Days to months |
| **Write Path** | Signal Exchange | Direct SDK |
| **Immutability** | Yes | No |
| **PII** | Prohibited | Permitted |
| **Storage** | Europa (OpenSearch) | TBD |

---

## Related Documents

- [Enterprise Memory](../enterprise-memory/README.md)
- [Agent Memory](../agent-memory/README.md)
- [Memory Services Overview](../README.md)

