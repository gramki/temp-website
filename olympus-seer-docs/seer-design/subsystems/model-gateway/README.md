# Model Gateway

> **Status**: 🟡 Draft — Capability outline  
> **Last Updated**: 2026-01-11

## Overview

The Seer Model Gateway provides **unified LLM/SLM access** for all agents in the Hub ecosystem. It is based on Bifrost, an open-source LLM gateway, adapted for Hub's authentication, governance, and observability requirements.

**Key Capabilities:**
- Unified interface for 8+ providers, 1000+ models
- Provider fallback for high availability
- Budget enforcement at workbench and agent levels
- Virtual key management per Employed Agent
- OpenTelemetry-based observability

---

## Capabilities

Based on `olympus-hub-docs/scratchpad/seer-subsystems.md`:

- Cognitive Metrics
- Policy Enforcement Point
- Resource Budget Enforcement

---

## Existing Content

Detailed content available in:
- `../model-gateway.md` - Complete Model Gateway design (to be migrated here)

---

## Related

- `implementation-concepts/agent-observability.md` - Observability concepts
- `agent-analytics/README.md` - Agent analytics
- `olympus-hub-docs/decision-logs/0075-seer-model-gateway-bifrost.md` - ADR on Model Gateway

---

*Detailed design to be added in subsequent sessions.*
