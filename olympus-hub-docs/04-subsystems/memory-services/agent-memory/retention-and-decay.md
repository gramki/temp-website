# Agent Memory Retention & Decay

> **Status**: 🔴 Stub — Placeholder for expansion  
> **Last Updated**: 2026-01-07  
> **Parent**: [Agent Memory](./README.md)

---

## Overview

Agent Memory implements **retention policies** and **decay models** that differ from Enterprise Memory's durable, immutable approach. Agent Memory is ephemeral by design, with records expiring or decaying over time.

---

## Retention Defaults

| Memory Class | Default Retention | Rationale |
|--------------|-------------------|-----------|
| **Episodic** | Session + 24 hours | Recent context only |
| **Semantic** | 30 days | Facts may become stale |
| **Procedural** | Indefinite | Skills don't expire |
| **Preference** | 90 days | Preferences may change |

---

## Decay Models

### Time-Based Decay (Episodic)

Episodic memory decays linearly over time:
- Records lose relevance as they age
- Automatic deletion after TTL

### Usage-Based Decay (Semantic, Preference)

Semantic and Preference memory uses usage-based decay:
- Records that are accessed have TTL extended
- Records that are not accessed eventually expire
- Relevance score decreases with time since last access

---

## TODO

| Item | Priority | Notes |
|------|----------|-------|
| Define decay algorithms | P2 | Mathematical models |
| Define TTL extension rules | P2 | How access extends lifetime |
| Define bulk cleanup | P3 | Batch expiration processing |

---

*TODO: Detailed decay algorithms pending storage backend decision*

