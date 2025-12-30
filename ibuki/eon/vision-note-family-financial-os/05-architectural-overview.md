# 5. Architectural Overview

## 5.1 High-Level Layered Architecture
FFOS comprises three deeply interdependent layers governed via shared policy artifacts, telemetry, and operational playbooks. Clear separation of duties prevents capability creep while allowing each layer to evolve independently under common guardrails.

### 5.1.1 Core System Services (Infrastructure Layer)
Privileged services manage identity, family graph, consent, guardrails, event ingestion, obligation detection, workflow orchestration, document handling, memory stores, feature computation, IPC/IAC, and channel adapters. They run as bank-managed microservices with hardened IAM integration, least-privilege credentials, and audited configuration baselines. These services expose APIs and events consumed by all agents; no agent bypasses this layer.

### 5.1.2 FSOS Foundation Agents (System Intelligence Layer)
Foundation agents synthesize normalized events, memories, and feature vectors into authoritative household state—cashflow posture, goal attainment, risk exposure, and operational telemetry. They publish state updates over IPC topics, persist snapshots for deterministic replay, and expose read-optimized APIs so experience agents never recompute domain logic inconsistently.

### 5.1.3 Experience & Domain Agents (Application Layer)
Think, Do, Orchestrator, Governance, and Concierge agents sit closest to channels, RM workbenches, and external I/O. They rely on core services for authentication, consent enforcement, workflow primitives, storage, and logging. Business logic remains configuration-driven per segment or market, so banks can launch new offers without duplicating security or integration effort.

## 5.2 Cross-Cutting Concerns

### 5.2.1 Security, Privacy, and Consent
IAM federation, hardware-backed secrets, consent scopes, and policy evaluation services span every layer. All IPC messages include provenance metadata, consent tokens, and policy hashes for enforcement and forensic traceability. Guardrail engines run pre- and post-action checks, and governance agents monitor threshold breaches or anomalous behavior.

### 5.2.2 Observability, Logging, and Auditability
Unified telemetry captures metrics by agent, workflow, channel, and household. Event timelines, document references, and consent artifacts feed append-only audit stores with immutable signatures. Observability dashboards expose latency, success rates, anomaly flags, and household KPIs to product, risk, and operations teams, while log lakes support forensic replay.

### 5.2.3 Performance, Scalability, and Resilience
Event pipelines, workflow schedulers, and agent runtimes scale horizontally with autoscaling policies tied to obligation calendars and campaign loads. Back-pressure controls, prioritized queues, and multi-region replication underpin resilience targets. Core memory, graph memory, and feature stores employ tiered storage, caching, and snapshotting strategies to meet sub-second SLAs for advisory and execution flows, even during failovers.
