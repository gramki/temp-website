# Section 22: Multi-Agent Topologies in Hub — Overview

## Purpose of this Section

This section demonstrates how Hub implements the multi-agent topology requirements established in Section 5.14. Complex business processes require multiple specialized agents working together, coordinating through shared state rather than explicit task assignment. Hub Composite Applications enable multiple Hub Applications to participate in the same Request, supporting topology patterns like Blackboard, Planner-Executor-Critic (PEC Loop), Market-Based, and Role-Specialized Committees.

Hub Composite Applications extend Hub's application model to support sophisticated multi-agent collaboration while maintaining governance, observability, and operational controls. They enable cross-runtime composition, allowing agents from different runtimes (Seer, Rhea, Atlantis) to collaborate on the same request.

## Core Questions Addressed

*   How do Hub Composite Applications enable multiple agents to operate on the same request?
*   What topology patterns do Hub Composite Applications support?
*   How does deployment-time resolution work for composite applications?
*   How do OPA filters route updates to appropriate agents?

## Structure of this Section

This section is organized into the following sub-sections:

*   **22.1 Hub Composite Applications**: Definition, multiple apps per request, OPA filters, and cross-runtime composition.
*   **22.2 Supported Topologies**: Blackboard, PEC Loop, Market-Based, and Role-Specialized Committees patterns.
*   **22.3 Deployment Model**: Deployment-time resolution, routing table population, and update conflict resolution.

## Relationship to Other Sections

This section implements:

*   **Section 5.14 (Multi-Agent Topology Requirements)**: Implements all topology pattern requirements.

This section integrates with:

*   **Section 16.3 (Coordination Patterns in Hub)**: Hub Composite Applications are a coordination pattern.
*   **Section 12.4 (Deep Observability)**: Composite applications maintain observability across all participating agents.

---
