# Derived Knowledge Artifacts vs Signals (Pre‑Knowledge)

Enterprises often conflate “where data is stored” with “what it means cognitively.”

This page separates:

- **Asserted enterprise knowledge** (truth + semantics, governed)
- **Derived knowledge artifacts** (computed, useful, but not knowledge-of-record by default)
- **Signals** (pre-knowledge inputs optimized for utility, not explanation)

## Derived knowledge artifacts

Derived artifacts are computed from events and memory to support specific consumers:

- aggregates, dashboards, reports
- interpreted fact tables
- risk scores
- feature views and feature stores

They *may* become enterprise knowledge **only when explicitly asserted and governed**.

## Signals (pre-knowledge)

Signals are high-variance inputs:

- raw features
- embeddings
- telemetry-derived signals

They are not knowledge-of-record; they require interpretation and governance before being used as binding justification.

## Practical rule

> If it is intended to **constrain behavior**, it must be promoted into asserted enterprise knowledge with ownership and review.

## Navigation

- Back: [`README.md`](./README.md)

