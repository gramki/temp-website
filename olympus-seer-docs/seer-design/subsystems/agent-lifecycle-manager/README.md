# Agent Lifecycle Manager

> **Status**: 🟡 Draft — Capability outline  
> **Last Updated**: 2026-01-11

## Overview

Agent Lifecycle Manager manages the complete lifecycle of Employed Agents, including employment specification management, delegation chain synchronization, agent levers (kill switches, authority controls), ecosystem integration, and the employed agent directory.

---

## Capabilities

Based on `olympus-hub-docs/scratchpad/seer-subsystems.md`:

### Employment Spec Manager
- Authority Enforcement Controls
- Resource Quota
- Fair Usage Budget (Per Subject, Per Signal, etc.)
- Delegation Chain

### Delegation Chain Sync Service
- Synchronization when human authority changes

### Agent Levers Service
- Kill Switches
- Authority Enforcement Actions

### Agent Ecosystem Integration Services
- IAM Changes
- Subscription Policy Changes
- Workbench Policy Changes
- Agent Lifecycle Changes
- Agent Health Actions
- Platform SRE Directives
- Tools Gateway integration
- Signal Exchange integration
- Training Management integration

### Employed Agent Directory
- Profile of Agent (System Prompts (Goals, Skills, Behaviors, Guardrails), External Guardrails, Context Compiler DSL, Tools, Resources)
- Derived Skills, Capabilities
- Specified/Assigned Skill Labels, Tags
- Accountability Discovery
- Human Responsibility Span
- Agent Change Log (Employment Spec, Authority Changes, Enforcement Actions (Levers))
- Agent dependency Graph (understand agent-to-agent relationships and dependencies)

---

## Sub-Components

- `employment-spec-manager.md` - Employment specification management
- `delegation-chain-sync-service.md` - Delegation chain synchronization
- `agent-levers-service.md` - Agent levers (kill switches, authority controls)
- `agent-ecosystem-integration-services.md` - Ecosystem integration services
- `employed-agent-directory.md` - Employed agent directory

---

## Existing Content

Detailed content available in:
- `../agent-lifecycle-service.md` - Agent lifecycle service (to be migrated here)
- `../agent-lifecycle-api.md` - Agent lifecycle API (to be migrated here)

---

## Related

- `implementation-concepts/agent-lifecycle.md` - Agent lifecycle concepts
- `raw-agent-lifecycle-manager/README.md` - Raw agent lifecycle
- `trained-agent-lifecycle-manager/README.md` - Trained agent lifecycle

---

*Detailed design to be added in subsequent sessions.*
