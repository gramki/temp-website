# Persona: Developer

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Developer** builds Hub Applications and defines Triggers that connect Signals to automation. They translate Process Architect designs into working implementations.

| Attribute | Value |
|-----------|-------|
| **Category** | Hub Persona — Workbench Designer |
| **Scope** | Workbench |
| **Domain** | Tenant Identity Domain |
| **Primary Console** | IDE / Development Tools |

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

## Hub Capabilities Consumed

### Development Tools (Primary Interface)

| Capability | What It Provides |
|------------|------------------|
| **Application Development** | Build Hub Applications using runtime SDKs |
| **Trigger Designer** | Define signal matching, transformations |
| **Application Configuration** | Runtime-specific settings, environment bindings |
| **Testing & Debugging** | Local testing, integration testing |

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Workbench Management** | Create Trigger definitions, Application configurations |
| **Registry Services** | Register machines, tools; configure access policies |
| **Knowledge Services** | Define retrieval patterns for applications |
| **Memory Services** | Define memory access patterns for applications |
| **Hub Application APM** | Monitor application performance, debug issues |
| **Signal Exchange** | Test signal routing, message envelopes |

### Heracles Launcher (API Testing)

| Capability | What It Provides |
|------------|------------------|
| **API Testing** | Test Hub APIs, MCP endpoints |
| **Request Simulation** | Simulate signals, test triggers |
| **Response Inspection** | Debug response transformations |

### What They Produce

| Output | Consumed By |
|--------|-------------|
| Hub Applications | Signal Exchange (for routing) |
| Trigger Definitions | Signal Exchange (for matching) |
| Machine/Tool Registrations | Applications (for invocation) |
| Scenario Manifest | Supervisor (for deployment) |

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

