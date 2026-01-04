# Persona: Developer

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Developer** builds Hub Applications and defines Triggers that connect Signals to automation. They translate Process Architect designs into working implementations.

| Attribute | Value |
|-----------|-------|
| **Scope** | Tenant Subscription |
| **Domain** | Tenant Identity Domain |
| **Primary Console** | Agent Studio (IDE) |

---

## Objectives

| Objective | Description |
|-----------|-------------|
| **Build Applications** | Implement Hub Applications on chosen Automation Runtimes |
| **Define Triggers** | Connect signals to applications with proper transformations |
| **Integrate Services** | Wire applications to Memory, Knowledge, and Tools |
| **Enable Monitoring** | Instrument applications for observability |

---

## Key Activities

### Build Phase

1. **Runtime Selection**
   - Choose appropriate Automation Runtime based on scenario needs
   - Configure runtime-specific application type

2. **Application Development**
   - Implement business logic
   - Honor Hub Request contracts
   - Integrate with Hub services

3. **Trigger Configuration**
   - Define signal matching conditions
   - Configure request/response transformations
   - Link to Scenario definitions

4. **Tool Integration**
   - Register machines and tools
   - Configure access policies
   - Test integrations

### Collaboration

| With | Activity |
|------|----------|
| **Process Architect** | Receive scenario designs, clarify requirements |
| **Supervisor** | Create Scenario Manifest for task delegation |
| **Administrator** | Request resources, machine registrations |

---

## Tools and Interfaces

| Tool | Purpose |
|------|---------|
| **Agent Studio** | IDE for application development |
| **Heracles Launcher** | API testing and debugging |
| **Tool Registry** | Machine and tool configuration |
| **Hub Application APM** | Monitoring and debugging |

---

## Key Journeys

- [Scenario Development](../journeys/scenario-development.md) — Primary journey (Build phase)

---

## Automation Runtimes

| Runtime | Application Type | Best For |
|---------|-----------------|----------|
| **Atlantis** | Container Application | Simple procedures, stateless logic |
| **Rhea** | Workflow Application | Structured, predictable workflows |
| **ChronoShift** | Durable Workflow | Long-running, fault-tolerant workflows |
| **Seer** | Case Orchestration Agent | AI-driven case management |
| **Perseus** | File Application | Batch processing |

---

## Related Documentation

- [Hub Applications](../../01-concepts/hub-applications.md)
- [Trigger Definitions](../../04-subsystems/workbench-management/trigger-definitions.md)
- [Registry Services](../../04-subsystems/registry-services/README.md)
- [Hub Application APM](../../04-subsystems/supporting-systems/hub-application-apm.md)

---

*TODO: Detailed responsibilities, development workflow, testing patterns*

