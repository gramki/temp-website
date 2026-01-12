---
name: Analytics Supervisor Health Design
overview: Create C2-level (Container) design documentation for Agent Analytics, Agent Session Supervisor, Agent Health Monitor, and Observability Extensions to Watch subsystems. Follow patterns from previous designs with C2-level conceptual design and C3-level detail for critical mechanisms. Agent Analytics is a data mart (like Hub Analytics), Observability Extensions to Watch is a separate subsystem (like cipher-iam-extensions), and both Supervisor and Health Monitor follow lifecycle manager patterns.
todos:
  - id: analytics-operational-data
    content: Create C2-level design for Operational Data Service covering data collection from Watch, Sidecar, Model Gateway, Runtime, and aggregation
    status: completed
  - id: analytics-data-mart
    content: Create C2-level design for Data Mart Service covering data mart construction, ETSL integration, data product creation, LakeStack Pontus integration
    status: completed
  - id: analytics-report-integration
    content: Create C2-level design for Report Integration Service covering LakeStack Report Center integration, catalog sync, access mapping, context injection
    status: completed
  - id: analytics-scope
    content: Create SCOPE.md for agent-analytics with coverage summary, design status, intended depth
    status: completed
    dependencies:
      - analytics-operational-data
      - analytics-data-mart
      - analytics-report-integration
  - id: analytics-readme
    content: Update agent-analytics/README.md with design documents table, architecture diagram, key design decisions
    status: completed
    dependencies:
      - analytics-scope
  - id: watch-ext-extension-layer
    content: Create C2-level design for Watch Extension Layer covering extension infrastructure, deployment model, dashboard JSONs, Prometheus rules, Alertmanager configs
    status: completed
  - id: watch-ext-persona-dashboards
    content: Create C2-level design for Persona Dashboards covering AI Platform Engineer, LLMOps Engineer, SRE for Agentic Systems, Security Architect dashboards
    status: completed
  - id: watch-ext-alert-templates
    content: Create C2-level design for Alert Templates covering pre-built alert definitions, routing, severity levels
    status: completed
  - id: watch-ext-operational-tools
    content: Create C2-level design for Operational Tools covering agent isolator, credential revoker, guardrail configurator, audit log viewer
    status: completed
  - id: watch-ext-scope
    content: Create SCOPE.md for observability-extensions-to-watch with coverage summary, design status, intended depth
    status: completed
    dependencies:
      - watch-ext-extension-layer
      - watch-ext-persona-dashboards
      - watch-ext-alert-templates
      - watch-ext-operational-tools
  - id: watch-ext-readme
    content: Create observability-extensions-to-watch/README.md with design documents table, architecture diagram, key design decisions
    status: completed
    dependencies:
      - watch-ext-scope
  - id: migrate-watch-ext-content
    content: Migrate content from agent-analytics/observability-extensions-to-watch.md to new observability-extensions-to-watch subsystem structure
    status: completed
    dependencies:
      - watch-ext-extension-layer
      - watch-ext-persona-dashboards
      - watch-ext-alert-templates
      - watch-ext-operational-tools
  - id: supervisor-spec-manager
    content: Create C2-level design for Supervisor Spec Manager covering spec structure, validation, deployment configuration, SupervisorSpec CRD
    status: completed
  - id: supervisor-realtime-service
    content: Create C2-level design for Realtime Supervisor Service covering SX event observation, OPA policy evaluation, real-time observation generation
    status: completed
  - id: supervisor-analytical-service
    content: Create C2-level design for Analytical Supervisor Service covering templated SQL execution on analytics data mart, periodic execution, analytical observation generation
    status: completed
  - id: supervisor-observation-service
    content: Create C2-level design for Observation Service covering Cronus Observations/Exceptions generation, Cronus Gateway integration
    status: completed
  - id: supervisor-operators
    content: Create C2-level design for Supervisor Operators covering lifecycle management, state transitions, deployment via Seer Operator
    status: completed
  - id: supervisor-levers
    content: Create C2-level design for Supervisor Levers covering runtime controls, enable/disable, suspend, emergency controls
    status: completed
  - id: supervisor-directory
    content: Create C2-level design for Supervisor Directory covering registry, search, version tracking, deployment status
    status: completed
  - id: supervisor-scope
    content: Create SCOPE.md for agent-session-supervisor with coverage summary, design status, intended depth
    status: completed
    dependencies:
      - supervisor-spec-manager
      - supervisor-realtime-service
      - supervisor-analytical-service
      - supervisor-observation-service
      - supervisor-operators
      - supervisor-levers
      - supervisor-directory
  - id: supervisor-readme
    content: Update agent-session-supervisor/README.md with design documents table, architecture diagram, key design decisions
    status: completed
    dependencies:
      - supervisor-scope
  - id: health-spec-manager
    content: Create C2-level design for Health Spec Manager covering spec structure, SLO definitions (Cost, Behavior, Feedback), validation, HealthSpec CRD
    status: completed
  - id: health-slo-manager
    content: Create C2-level design for SLO Manager covering SLO definition and threshold management for Cost (ARE), Behavior (COS), Feedback (PA/APO) SLOs
    status: completed
  - id: health-slo-tracking
    content: Create C2-level design for SLO Tracking Service covering SLO deviation tracking using Agent Analytics data mart, threshold evaluation, metric aggregation
    status: completed
  - id: health-feedback-service
    content: Create C2-level design for Human Feedback Service covering feedback collection, routing to Training Feedback Services, feedback metric calculation
    status: completed
  - id: health-operators
    content: Create C2-level design for Health Operators covering lifecycle management, state transitions, deployment via Seer Operator
    status: completed
  - id: health-levers
    content: Create C2-level design for Health Levers covering runtime controls, enable/disable, suspend, emergency controls
    status: completed
  - id: health-directory
    content: Create C2-level design for Health Directory covering registry, search, version tracking, SLO status
    status: completed
  - id: health-scope
    content: Create SCOPE.md for agent-health-monitor with coverage summary, design status, intended depth
    status: completed
    dependencies:
      - health-spec-manager
      - health-slo-manager
      - health-slo-tracking
      - health-feedback-service
      - health-operators
      - health-levers
      - health-directory
  - id: health-readme
    content: Update agent-health-monitor/README.md with design documents table, architecture diagram, key design decisions
    status: completed
    dependencies:
      - health-scope
  - id: update-subsystems-readme
    content: Update subsystems/README.md to add observability-extensions-to-watch as separate subsystem and update status for all four subsystems
    status: completed
    dependencies:
      - analytics-readme
      - watch-ext-readme
      - supervisor-readme
      - health-readme
---

# Agent Analytics, Session Supervisor, Health Monitor & Watch Extensions Design

Create comprehensive C2-level design documentation for four subsystems: **Agent Analytics**, **Agent Session Supervisor**, **Agent Health Monitor**, and **Observability Extensions to Watch**. Follow the patterns established by previous subsystem designs.

## Subsystem 1: Agent Analytics

Agent Analytics is a **data mart** (analogous to Hub Analytics) that houses operational data for agents. It answers questions based on historic health, cost, effectiveness, feedback, and behavior of agents—not runtime observability.

### Architecture Pattern

```mermaid
flowchart TB
    subgraph AgentAnalytics[Agent Analytics]
        ODS[Operational Data Service]
        DMS[Data Mart Service]
        RI[Report Integration Service]
    end
    
    subgraph DataSources[Data Sources]
        Watch[Olympus Watch]
        SeerSidecar[Seer Sidecar Metrics]
        ModelGateway[Model Gateway]
        AgentRuntime[Agent Runtime]
    end
    
    subgraph LakeStack[Olympus LakeStack]
        Pontus[Pontus Data Infrastructure]
        ReportCenter[Report Center]
        ETSL[ETSL]
    end
    
    DataSources --> ODS
    ODS --> DMS
    DMS --> Pontus
    DMS --> ReportCenter
    RI --> ReportCenter
    DMS --> ETSL
```

### Sub-Components

| Component | Description | Key Capabilities |

|-----------|-------------|------------------|

| **Operational Data Service** | Collects and aggregates agent operational data | Data collection from Watch, Sidecar, Model Gateway, Runtime |

| **Data Mart Service** | Builds and maintains agent data marts | Data mart construction, ETSL integration, data product creation |

| **Report Integration Service** | Integrates with LakeStack Report Center | Report catalog sync, access mapping, context injection |

### Key Design Decisions

- **Data Mart Model**: Agent Analytics is a data mart, not runtime observability
- **LakeStack Integration**: Uses Pontus infrastructure for data marts and Report Center for serving
- **ETSL Integration**: Registers agent operational data as assertions into ETSL
- **Separation from Observability**: Runtime observability is in Observability Extensions to Watch

### Files to Create

| File | Description |

|------|-------------|

| `agent-analytics/operational-data-service.md` | Data collection and aggregation from multiple sources |

| `agent-analytics/data-mart-service.md` | Data mart construction, ETSL integration, data products |

| `agent-analytics/report-integration-service.md` | LakeStack Report Center integration |

| `agent-analytics/SCOPE.md` | Coverage summary, design status |

---

## Subsystem 2: Observability Extensions to Watch

Observability Extensions to Watch is a **separate subsystem** (like cipher-iam-extensions) that provides runtime observability extensions to Olympus Watch for AREs and Cognitive Operations Stewards.

### Architecture Pattern

```mermaid
flowchart TB
    subgraph WatchExtensions[Observability Extensions to Watch]
        ExtensionLayer[Watch Extension Layer]
        Dashboards[Persona Dashboards]
        Alerts[Alert Templates]
        Tools[Operational Tools]
    end
    
    subgraph Watch[Olympus Watch]
        Prometheus[Prometheus]
        Jaeger[Jaeger]
        LogAgg[Log Aggregation]
    end
    
    subgraph SeerComponents[Seer Components]
        ModelGateway[Model Gateway]
        ToolGateway[Tool Gateway]
        PolicyEngine[Policy Engine]
        AgentLifecycle[Agent Lifecycle]
        GuardrailSidecar[Guardrail Sidecar]
    end
    
    SeerComponents --> Watch
    Watch --> ExtensionLayer
    ExtensionLayer --> Dashboards
    ExtensionLayer --> Alerts
    ExtensionLayer --> Tools
```

### Sub-Components

| Component | Description | Key Capabilities |

|-----------|-------------|------------------|

| **Watch Extension Layer** | Extension infrastructure for Watch | Dashboard JSONs, Prometheus recording rules, Alertmanager configs, custom plugins |

| **Persona Dashboards** | Dashboards for AI Platform Engineer, LLMOps Engineer, SRE for Agentic Systems, Security Architect | Pre-built dashboards per persona |

| **Alert Templates** | Pre-built alert definitions | Alert rules, routing, severity levels |

| **Operational Tools** | UI tools for operational tasks | Agent isolator, credential revoker, guardrail configurator |

### Key Design Decisions

- **Separate Subsystem**: Independent subsystem like cipher-iam-extensions
- **Watch-Based**: All extensions built on Olympus Watch infrastructure
- **Persona-Focused**: Dashboards and tools organized by SRE persona needs
- **No New Infrastructure**: Extends Watch, doesn't create new observability layer

### Files to Create

| File | Description |

|------|-------------|

| `observability-extensions-to-watch/watch-extension-layer.md` | Extension infrastructure, deployment model |

| `observability-extensions-to-watch/persona-dashboards.md` | Dashboards for each SRE persona |

| `observability-extensions-to-watch/alert-templates.md` | Pre-built alert definitions and routing |

| `observability-extensions-to-watch/operational-tools.md` | UI tools for operational tasks |

| `observability-extensions-to-watch/SCOPE.md` | Coverage summary, design status |

**Note**: Existing `agent-analytics/observability-extensions-to-watch.md` should be migrated to this new subsystem structure.

---

## Subsystem 3: Agent Session Supervisor

Agent Session Supervisor provides supervisory oversight for agent sessions, managing supervisory policies, observations, and escalations. Follows lifecycle manager pattern.

### Architecture Pattern

```mermaid
flowchart TB
    subgraph Supervisor[Agent Session Supervisor]
        SSM[Supervisor Spec Manager]
        RTS[Realtime Supervisor Service]
        ASS[Analytical Supervisor Service]
        OS[Observation Service]
        SO[Supervisor Operators]
        SL[Supervisor Levers]
        SD[Supervisor Directory]
    end
    
    subgraph ExternalSystems[External Systems]
        SignalExchange[Signal Exchange]
        AgentAnalytics[Agent Analytics]
        Cronus[Cronus Gateway]
        SeerOp[Seer Operator]
    end
    
    SignalExchange --> RTS
    AgentAnalytics --> ASS
    RTS --> OS
    ASS --> OS
    OS --> Cronus
    SSM --> SeerOp
    SO --> SD
    SL --> SD
```

### Sub-Components

| Component | Description | Key Capabilities |

|-----------|-------------|------------------|

| **Supervisor Spec Manager** | Supervisor specification CRD structure, validation | Spec structure, validation, deployment configuration |

| **Realtime Supervisor Service** | Observes SX events, evaluates OPA policies | SX event observation, OPA policy evaluation, real-time observation generation |

| **Analytical Supervisor Service** | Runs templated SQL queries on analytics data mart | Periodic execution, SQL template evaluation, analytical observation generation |

| **Observation Service** | Generates Cronus Observations/Exceptions | Observation/Exception creation, Cronus integration |

| **Supervisor Operators** | Lifecycle management via Seer Operator | Registration, validation, deployment, state transitions |

| **Supervisor Levers** | Runtime controls for supervisors | Enable/disable, suspend, emergency controls |

| **Supervisor Directory** | Registry of supervisors | Search, version tracking, deployment status |

### Key Design Decisions

- **Two Supervisor Types**: Realtime (SX + OPA) and Analytical (SQL on data mart)
- **Cronus Integration**: Generates Observations/Exceptions via Cronus Gateway (Hub model)
- **Deployment Model**: Supervisors deployed via Deployment CRDs referencing Spec CRDs
- **Lifecycle Pattern**: Follows same pattern as Trained/Employed Agent lifecycle managers

### Files to Create

| File | Description |

|------|-------------|

| `agent-session-supervisor/supervisor-spec-manager.md` | Spec structure, validation, deployment configuration |

| `agent-session-supervisor/realtime-supervisor-service.md` | SX event observation, OPA policy evaluation |

| `agent-session-supervisor/analytical-supervisor-service.md` | SQL template execution on analytics data mart |

| `agent-session-supervisor/observation-service.md` | Cronus Observations/Exceptions generation |

| `agent-session-supervisor/supervisor-operators.md` | Lifecycle management, state transitions |

| `agent-session-supervisor/supervisor-levers.md` | Runtime controls, enable/disable, suspend |

| `agent-session-supervisor/supervisor-directory.md` | Registry, search, version tracking |

| `agent-session-supervisor/SCOPE.md` | Coverage summary, design status |

---

## Subsystem 4: Agent Health Monitor

Agent Health Monitor tracks and enforces health-related Service Level Objectives (SLOs) for agents, including cost SLOs (ARE), behavior SLOs (COS), and feedback SLOs (PA/APO). Follows similar structure to Supervisor.

### Architecture Pattern

```mermaid
flowchart TB
    subgraph HealthMonitor[Agent Health Monitor]
        HSM[Health Spec Manager]
        SLOM[SLO Manager]
        SLOT[SLO Tracking Service]
        HFS[Human Feedback Service]
        HO[Health Operators]
        HL[Health Levers]
        HD[Health Directory]
    end
    
    subgraph ExternalSystems[External Systems]
        AgentAnalytics[Agent Analytics]
        TrainingFeedback[Training Feedback Services]
        AgentSessionSupervisor[Agent Session Supervisor]
        SeerOp[Seer Operator]
    end
    
    AgentAnalytics --> SLOT
    SLOT --> SLOM
    HFS --> TrainingFeedback
    SLOM --> AgentSessionSupervisor
    HSM --> SeerOp
    HO --> HD
    HL --> HD
```

### Sub-Components

| Component | Description | Key Capabilities |

|-----------|-------------|------------------|

| **Health Spec Manager** | Health specification CRD structure, validation | Spec structure, SLO definitions, validation |

| **SLO Manager** | SLO definition and threshold management | Cost SLOs (ARE), Behavior SLOs (COS), Feedback SLOs (PA/APO) |

| **SLO Tracking Service** | Tracks SLO deviations using Agent Analytics | Deviation detection, threshold evaluation, metric aggregation |

| **Human Feedback Service** | Collects, routes, and calculates feedback metrics | Feedback collection, routing to Training Feedback Services, metric calculation |

| **Health Operators** | Lifecycle management via Seer Operator | Registration, validation, deployment, state transitions |

| **Health Levers** | Runtime controls for health monitoring | Enable/disable, suspend, emergency controls |

| **Health Directory** | Registry of health specs | Search, version tracking, SLO status |

### Key Design Decisions

- **SLO Types**: Cost (ARE), Behavior (COS), Feedback (PA/APO)
- **No Enforcement**: Only definition and tracking—no automatic enforcement actions
- **Agent Analytics Integration**: Uses Agent Analytics data mart for SLO evaluation
- **Supervisor Integration**: SLO deviations can trigger supervisors (if defined)
- **Lifecycle Pattern**: Follows same pattern as Supervisor lifecycle management

### Files to Create

| File | Description |

|------|-------------|

| `agent-health-monitor/health-spec-manager.md` | Spec structure, SLO definitions, validation |

| `agent-health-monitor/slo-manager.md` | SLO definition and threshold management |

| `agent-health-monitor/slo-tracking-service.md` | SLO deviation tracking using Agent Analytics |

| `agent-health-monitor/human-feedback-service.md` | Feedback collection, routing, metric calculation |

| `agent-health-monitor/health-operators.md` | Lifecycle management, state transitions |

| `agent-health-monitor/health-levers.md` | Runtime controls, enable/disable, suspend |

| `agent-health-monitor/health-directory.md` | Registry, search, version tracking |

| `agent-health-monitor/SCOPE.md` | Coverage summary, design status |

---

## Integration Points

### Agent Analytics

| Integration | Direction | Purpose |

|-------------|-----------|---------|

| Olympus Watch | Inbound | Collect operational metrics |

| Seer Sidecar | Inbound | Collect guardrail, policy, quota metrics |

| Model Gateway | Inbound | Collect model usage, cost metrics |

| Agent Runtime | Inbound | Collect deployment, health metrics |

| LakeStack Pontus | Outbound | Data mart construction, ETSL integration |

| LakeStack Report Center | Outbound | Report serving |

### Observability Extensions to Watch

| Integration | Direction | Purpose |

|-------------|-----------|---------|

| Olympus Watch | Extends | Dashboard, alert, tool extensions |

| Seer Components | Inbound | Metric sources (Model Gateway, Tool Gateway, Policy Engine, etc.) |

### Agent Session Supervisor

| Integration | Direction | Purpose |

|-------------|-----------|---------|

| Signal Exchange | Inbound | SX event observation for Realtime Supervisor |

| Agent Analytics | Inbound | Data mart queries for Analytical Supervisor |

| Cronus Gateway | Outbound | Generate Observations/Exceptions |

| Seer Operator | Outbound | CRD reconciliation |

### Agent Health Monitor

| Integration | Direction | Purpose |

|-------------|-----------|---------|

| Agent Analytics | Inbound | SLO evaluation using data mart |

| Training Feedback Services | Outbound | Route feedback for improvement |

| Agent Session Supervisor | Outbound | Trigger supervisors on SLO deviations (if configured) |

| Seer Operator | Outbound | CRD reconciliation |

---

## Content Migration

### From `agent-observability.md`

- **Platform-level observability content** → Migrate to `observability-extensions-to-watch/` subsystem
- **Cognitive Operations Desk references** → Keep in observability-extensions-to-watch (UI tool)
- **SDK content** → Already migrated to `seer-agent-sdk/` (observability-apis.md)

### From `agent-analytics/observability-extensions-to-watch.md`

- **Migrate entire content** → Move to `observability-extensions-to-watch/` subsystem structure
- **Split into sub-components**: Extension Layer, Persona Dashboards, Alert Templates, Operational Tools

---

## Implementation Details Deferred

Following the pattern from other subsystem designs:

- Detailed CRD schemas
- Complete API specifications (REST/gRPC endpoints)
- Storage backends and indexing strategies
- Specific algorithm implementations
- Error code taxonomies
- Wire format details
- SQL template syntax for Analytical Supervisor
- OPA policy schema for Realtime Supervisor