# Perseus - Batch Processing Engine

> **Status:** 🔴 Stub — Placeholder for expansion

Perseus is the Automation Runtime for **batch processing operations**—file applications, map-reduce jobs, and complex event processing applications.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Operation Types** | File Applications, Map-Reduce Jobs, Complex Event Applications |
| **Execution Model** | Batch, parallel processing |
| **State Management** | Job-level state, checkpoint/restart |
| **Integration** | Dia (file inputs), Atropos (event streams) |

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **File Processing** | Process settlement files, reconciliation files, bulk imports |
| **Map-Reduce** | Large-scale data transformation, aggregation, filtering |
| **Complex Event Processing** | Pattern detection across event streams |
| **Batch ETL** | Extract-transform-load operations |
| **Report Generation** | Scheduled report generation and distribution |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        PERSEUS                                   │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   JOB SCHEDULER                          │    │
│  │   (Job queue, priority, dependencies, parallelism)       │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │                   EXECUTION ENGINE                       │    │
│  │                                                          │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐   │    │
│  │  │  File    │  │Map-Reduce│  │  Complex Event       │   │    │
│  │  │  Apps    │  │  Engine  │  │  Processing          │   │    │
│  │  └──────────┘  └──────────┘  └──────────────────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              STATE & CHECKPOINT MANAGER                  │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Job** | A unit of batch work to be executed |
| **Task** | A subdivision of a Job (e.g., processing one partition) |
| **Checkpoint** | Saved state for restart after failure |
| **Partition** | Data division for parallel processing |
| **Pipeline** | Sequence of processing stages |

---

## Job Types

### File Application
- Processes files from Dia
- Single-file or multi-file operations
- Output to Dia or downstream systems

### Map-Reduce Application
- Splits input into partitions
- Map phase: transform each partition
- Reduce phase: aggregate results
- Supports custom mappers and reducers

### Complex Event Application
- Subscribes to Atropos event streams
- Applies pattern detection rules
- Generates derived events or Requests

---

## Integration Points

| System | Integration |
|--------|-------------|
| **Dia** | File input/output |
| **Atropos** | Event stream input, event publishing |
| **Task Management** | Manual review tasks for failed records |
| **CAF** | Audit trail for batch decisions |

---

## Job Lifecycle

```
[Submitted] → [Queued] → [Running] → [Completed]
                              │
                              ├─→ [Failed] → [Retrying] → [Running]
                              │
                              └─→ [Cancelled]
```

---

## Related Documentation

- [Automation Runtimes Overview](./README.md)
- [Dia - File Gateway](../signal-providers/dia-file-gateway.md)
- [Atropos - Event Bus](../signal-providers/atropos-event-bus.md)

---

*TODO: Detailed design — job definition schema, parallelism strategies, checkpoint mechanisms, monitoring*

