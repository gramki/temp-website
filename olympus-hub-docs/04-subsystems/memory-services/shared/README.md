# Shared Memory Concepts

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
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

The **ESPP (Episodic-Semantic-Procedural-Preference)** taxonomy provides a conceptual framework for memory organization:

| Memory Class | Anchoring | Purpose |
|--------------|-----------|---------|
| **Episodic** | Event/Time | What happened |
| **Semantic** | Entity/Domain | What we know |
| **Procedural** | Skill/Task | How to act |
| **Preference** | Subject | How to personalize |

> **Important Applicability Difference**:
> - **Enterprise Memory**: ESPP taxonomy is **enforced** — records must be classified
> - **Agent Memory**: ESPP taxonomy is **optional** — developers use framework-native patterns
>
> See [ESPP Taxonomy](./espp-taxonomy.md) for details on applicability by memory type.

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
| **Scope** | Organizational — cross-agent, cross-session | Request/Session — per agent |
| **Retention** | 7+ years (configurable) | Session + admin-configured period (hours to days) |
| **Write Path** | Via Signal Exchange (no direct writes) | Direct SDK and Tools |
| **Read Path** | Via Memory Access Tools | SDK methods, Tools |
| **Immutability** | Yes (append-only) | No (update/delete allowed) |
| **PII** | Prohibited (entity references only) | Permitted (session scope) |
| **ESPP Taxonomy** | Enforced | Optional |
| **Storage** | Europa (OpenSearch) | TBD |
| **Encryption** | Platform-level | Application-layer, session-unique keys |

---

## Related Documents

- [Enterprise Memory](../enterprise-memory/README.md)
- [Agent Memory](../agent-memory/README.md)
- [Memory Services Overview](../README.md)

