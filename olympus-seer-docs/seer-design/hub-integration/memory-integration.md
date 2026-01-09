# Agent Memory Integration

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Seer-Hub Integration](./README.md)

---

## Overview

Seer agents access **Hub Agent Memory Services** for session-scoped persistence. Memory stores are provisioned at employment time, and all reads/writes are scoped to the current Request.

---

## Memory Model for Seer Agents

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      SEER AGENT MEMORY MODEL                                  │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    Employed Agent                                    │   │
│   │                                                                       │   │
│   │   Memory Stores (provisioned at employment)                          │   │
│   │   ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐       │   │
│   │   │Conversation│ │  KV Store  │ │    Log     │ │ Documents  │       │   │
│   │   │   Store    │ │            │ │   Store    │ │   Store    │       │   │
│   │   └────────────┘ └────────────┘ └────────────┘ └────────────┘       │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                            │                                                 │
│                            │ All reads/writes scoped to Request             │
│                            ▼                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    Per-Request Isolation                             │   │
│   │                                                                       │   │
│   │   Request A: /tenant/workbench/scenario/request-a/agent/store/...   │   │
│   │   Request B: /tenant/workbench/scenario/request-b/agent/store/...   │   │
│   │   Request C: /tenant/workbench/scenario/request-c/agent/store/...   │   │
│   │                                                                       │   │
│   │   Stores are constant per Employed Agent                             │   │
│   │   Isolation is per (tenant, workbench, scenario, request, agent)     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Declaration and Provisioning

### Declaration in TrainingSpec

```yaml
# In Seer TrainingSpec
spec:
  memoryConfig:
    stores:
      - name: case-dialog
        type: conversation
        compaction:
          strategy: summarize
          tokenBudget: 4000
      - name: case-entities
        type: kv
      - name: session-audit
        type: log
        ragEnabled: true
```

### Mapping in HubApplicationSpec

```yaml
# In HubApplicationSpec
spec:
  hubConfig:
    memoryRequirements:
      agentMemory:
        stores:
          - type: conversation
            name: case-dialog
            compaction: summarize
          - type: kv
            name: case-entities
          - type: log
            name: session-audit
```

### Binding in ScenarioDeployment

```yaml
# In ScenarioDeployment
spec:
  applicationDeployments:
    - appRef: fraud-case-analyst
      memoryBindings:
        - name: case-dialog
          workbenchStore: disputes-conversation-store
        - name: case-entities
          workbenchStore: disputes-kv-store
        - name: session-audit
          workbenchStore: disputes-log-store
```

---

## Access Patterns

Seer agents access memory via **SDK** or **Tools**:

### SDK Access

```python
from hub_memory_sdk import AgentMemory

memory = AgentMemory.from_environment()

# KV Store
memory.kv.put("case-entities", "fraud_assessment", {
    "score": 0.87,
    "factors": ["velocity", "new_device"]
})

assessment = memory.kv.get("case-entities", "fraud_assessment")

# Conversation Store
memory.conversation.append("case-dialog", {
    "role": "assistant",
    "content": "I've analyzed the transaction..."
})

history = memory.conversation.get_last("case-dialog", n=10)

# Log Store with RAG
memory.log.append("session-audit", {
    "action": "fraud_check",
    "result": "suspicious"
})

relevant = memory.log.rag_search("session-audit", 
    query="what fraud checks were performed?",
    limit=5
)
```

### Tool Access

```python
# Using memory as a tool (LLM-invocable)
tools = [
    {
        "name": "save_entity",
        "tool": "agent_memory.kv.save",
        "parameters": {
            "store": "case-entities",
            "key": "string",
            "value": "object"
        }
    },
    {
        "name": "recall_entity",
        "tool": "agent_memory.kv.recall",
        "parameters": {
            "store": "case-entities",
            "key": "string"
        }
    }
]
```

---

## Memory vs Enterprise Memory

| Aspect | Agent Memory | Enterprise Memory |
|--------|--------------|-------------------|
| **Scope** | Request/Session | Organizational |
| **Lifetime** | Session + retention | 7+ years |
| **PII** | Permitted (encrypted) | Prohibited |
| **Access** | Direct SDK/Tools | Via Access Tools |
| **Write Path** | Direct to store | Via Signal Exchange |
| **Cross-Session** | ❌ No | ✅ Yes |

### When to Use Which

| Use Case | Memory Type |
|----------|-------------|
| Conversation history (current session) | Agent Memory (Conversation) |
| Extracted entities (current case) | Agent Memory (KV) |
| Session audit trail | Agent Memory (Log) |
| Decision records (for compliance) | Enterprise Memory (Episodic) |
| Learned patterns (cross-case) | Enterprise Memory (Semantic) |
| User preferences (persistent) | Enterprise Memory (Preference) |

---

## Compound Agent Memory

For Raw Agents with internal sub-agents:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      COMPOUND AGENT MEMORY                                    │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    Raw Agent Container                               │   │
│   │                                                                       │   │
│   │   ┌───────────────────────────────────────────────────────────────┐ │   │
│   │   │                   Orchestrator                                 │ │   │
│   │   │                                                                 │ │   │
│   │   │   Memory Scope: /agent/{employed_agent_id}/...                 │ │   │
│   │   └───────────────────────────────────────────────────────────────┘ │   │
│   │                            │                                         │   │
│   │             ┌──────────────┼──────────────┐                         │   │
│   │             ▼              ▼              ▼                         │   │
│   │   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                  │   │
│   │   │  Sub-Agent  │ │  Sub-Agent  │ │  Sub-Agent  │                  │   │
│   │   │      A      │ │      B      │ │      C      │                  │   │
│   │   │             │ │             │ │             │                  │   │
│   │   │ Can access  │ │ Can access  │ │ Can access  │                  │   │
│   │   │ parent's    │ │ parent's    │ │ parent's    │                  │   │
│   │   │ memory      │ │ memory      │ │ memory      │                  │   │
│   │   └─────────────┘ └─────────────┘ └─────────────┘                  │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│   Sub-agents share the parent's memory scope                                 │
│   Hub sees only one Employed Agent                                           │
└──────────────────────────────────────────────────────────────────────────────┘
```

- **Orchestrator and sub-agents** share the same memory scope
- **Hub** sees one Employed Agent with one memory allocation
- **Internal coordination** is the Raw Agent's responsibility

---

## Security Model

### Encryption

| Aspect | Configuration |
|--------|---------------|
| **Layer** | Application-layer encryption |
| **Keys** | Unique per (agent, session) |
| **Derivation** | From Workbench-scoped root key |
| **Visibility** | Values not logged, not retrievable outside session |

### Isolation

```
Memory Key Pattern:
/{tenant}/{workbench}/{scenario}/{request_id}/{agent_id}/{store}/{key}

Example:
/acme/disputes/dispute-resolution/req-123/emp-001/case-entities/fraud_assessment
```

---

## Lifecycle

### Provisioning (Employment Time)

1. EmploymentSpec maps declared stores to workbench resources
2. Seer Operator provisions store access credentials
3. Agent receives environment variables with endpoints

### Runtime (Request Time)

1. Request created → memory scope established
2. Agent reads/writes within request scope
3. All operations encrypted before persistence

### Cleanup (Session End + Retention)

1. Request completed/cancelled
2. Retention period expires
3. Encryption keys deleted
4. Data becomes unrecoverable

---

## CAE Integration

Context Assembly Engine can pull from Agent Memory:

```python
from seer_sdk import ContextAssemblyEngine

cae = ContextAssemblyEngine.from_environment()

context = cae.compile(
    request_id=request.id,
    retrievers=[
        {
            "type": "agent_memory",
            "store": "session-audit",
            "query": "recent actions",
            "limit": 20
        },
        {
            "type": "agent_memory",
            "store": "case-entities",
            "keys": ["fraud_assessment", "customer_profile"]
        }
    ]
)
```

---

## Related Documentation

- [Agent Memory Services](../../../olympus-hub-docs/04-subsystems/memory-services/agent-memory/README.md) — Full specification
- [Agent Memory SDK](../../../olympus-hub-docs/04-subsystems/memory-services/agent-memory/sdk.md) — SDK reference
- [Agent Memory Developer Guide](../../../olympus-hub-docs/10-guides/agent-memory-developer-guide.md) — Best practices
- [Context Assembly](./context-assembly.md) — CAE + Memory integration

---

*Agent Memory provides session-scoped persistence for Seer agents, with strict isolation and encryption.*

