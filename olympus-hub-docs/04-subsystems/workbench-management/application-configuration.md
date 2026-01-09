# Application Configuration

> **Status:** 🔴 Stub — Placeholder for expansion

Defines how Hub Applications are configured for Scenarios within Workbenches.

---

## Overview

A **Hub Application** is the automation artifact that corresponds to a Scenario. Each Automation Runtime provides specialized Hub Application types.

---

## Hub Application Types

| Automation Runtime | Hub Application Type(s) | Description |
|-------------------|------------------------|-------------|
| **Atlantis** | Procedure App | Stateless, single-step procedure |
| **Atlantis** | Decision App | ML model invocation for decisions |
| **Atlantis** | Prediction App | ML model for predictions |
| **Perseus** | File App | Single or multi-file processing |
| **Perseus** | Map-Reduce App | Parallel data processing |
| **Perseus** | Complex Event App | Event pattern detection |
| **Rhea** | Workflow App | BPMN workflow execution |
| **ChronoShift** | Durable Workflow App | Long-running durable workflows |
| **Seer** | Seer Case Orchestration Agent | AI-driven case management |

---

## Application Configuration Schema

```yaml
application:
  id: string
  name: string
  workbench_id: string
  
  # Automation Runtime
  automation_system: enum
  application_type: string
  
  # Runtime configuration
  runtime:
    # System-specific configuration
    atlantis:
      function_name: string
      runtime: string
      timeout_ms: number
    
    perseus:
      job_type: string
      parallelism: number
      checkpoint_interval: string
    
    rhea:
      process_definition_id: string
      version: string
    
    chronoshift:
      workflow_type: string
      task_queue: string
    
    seer:
      case_spec_id: string
      agent_ids: array
  
  # Resource limits
  resources:
    cpu: string
    memory: string
    timeout: duration
  
  # Scaling
  scaling:
    min_instances: number
    max_instances: number
    target_concurrency: number
  
  # Metadata
  version: string
  status: enum  # active | deprecated | disabled
```

---

## Scenario → Application Binding

Each Scenario references one Hub Application:

```yaml
scenario:
  id: "dispute-filing"
  application:
    automation_system: "seer"
    application_id: "dispute-case-agent"
    application_type: "Seer Case Orchestration Agent"
```

---

## Related Documentation

- [Workbench Management Overview](./README.md)
- [Scenario Definitions](./scenario-definitions.md)
- [Automation Runtimes](../automation-runtimes/README.md)

---

*TODO: Detailed design — per-system configuration, deployment, versioning*

