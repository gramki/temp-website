# Headless Access Service

> **Category:** UX Architecture

---

## Overview

A **Headless Access Service** is a backend service that provides persona-specific business logic without UI coupling. Channels (Web, MS Teams, MCP, REST) connect to these services, which handle the actual operations. This separation enables consistent behavior across channels while allowing channel-specific presentation.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address service architecture. Headless Access Services are an implementation pattern for multi-channel access.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Agent actions | Service operations | Services implement action logic |
| (not covered) | Headless pattern | Backend-frontend separation |

### Gap This Fills

The ontology focuses on operations. Headless Access Services address:
1. **Multi-channel consistency**: Same logic, different UIs
2. **Separation of concerns**: Backend logic vs presentation
3. **API organization**: Services organized by persona

---

## Definition

**Headless Access Service** is a backend service that:
- Implements persona-specific business operations
- Exposes APIs consumed by channel adapters
- Is agnostic to presentation layer
- Enforces authorization per persona

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Persona-level; one service per persona |
| **Lifecycle** | Platform-managed; always available |
| **Ownership** | Platform owns; channels consume |
| **Multiplicity** | One per primary persona |

---

## Rationale

### Why This Design?

Headless services enable:
1. **Channel flexibility**: Add new channels without service changes
2. **Consistent behavior**: All channels get same logic
3. **Independent evolution**: Channels and services evolve separately
4. **Testing**: Test business logic without UI

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Per-channel backends** | Duplicated logic; inconsistency |
| **Monolithic service** | Too large; mixed concerns |
| **Direct database access** | No business logic layer |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0009](../decision-logs/0009-headless-services-with-channel-adapters.md) | Headless services with channel adapters |

---

## Structure

### Hub Headless Services

| Service | Persona | Key Operations |
|---------|---------|----------------|
| **Agent Access Service** | Agent | Get tasks, complete tasks, add memos |
| **Supervisor Access Service** | Supervisor | View queues, reassign, escalate |
| **Admin Access Service** | Admin | Manage users, configure resources |
| **Creator Access Service** | Architect/Developer | Manage scenarios, deploy apps |
| **Business User Access Service** | Business User | Submit requests, check status |

### Service Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HEADLESS SERVICE ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   CHANNELS                          HEADLESS SERVICES                        │
│   ────────                          ─────────────────                        │
│                                                                              │
│   ┌───────────┐                    ┌─────────────────────────────────────┐  │
│   │Web Console│──┐                 │                                     │  │
│   └───────────┘  │                 │   AGENT ACCESS SERVICE              │  │
│                  │                 │                                     │  │
│   ┌───────────┐  │                 │   ┌─────────────────────────────┐   │  │
│   │ MS Teams  │──┼────────────────▶│   │ Operations                  │   │  │
│   └───────────┘  │                 │   │ • Get assigned tasks        │   │  │
│                  │                 │   │ • Start work on task        │   │  │
│   ┌───────────┐  │                 │   │ • Complete task             │   │  │
│   │   MCP     │──┤                 │   │ • Add memo/thought          │   │  │
│   └───────────┘  │                 │   │ • Request reassignment      │   │  │
│                  │                 │   │ • Get request history       │   │  │
│   ┌───────────┐  │                 │   └─────────────────────────────┘   │  │
│   │ REST API  │──┘                 │                                     │  │
│   └───────────┘                    └─────────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Service Interface

```typescript
// Agent Access Service interface
interface AgentAccessService {
  // Task operations
  getAssignedTasks(agentId: string): Promise<Task[]>;
  startWork(taskId: string, memo?: string): Promise<void>;
  completeTask(taskId: string, outcome: TaskOutcome): Promise<void>;
  
  // Memo operations
  addMemo(requestId: string, memo: Memo): Promise<void>;
  addThought(taskId: string, thought: Thought): Promise<void>;
  
  // Request operations
  getRequestHistory(requestId: string): Promise<RequestUpdate[]>;
  getRequestContext(requestId: string): Promise<RequestContext>;
}
```

---

## Behavior

### How It Works

```
1. User interacts via Channel
   └── Web click, Teams message, MCP tool call

2. Channel adapter receives interaction
   └── Translate to service call

3. Channel calls Headless Service
   ├── Include authentication context
   └── Include operation parameters

4. Service processes request
   ├── Validate authorization
   ├── Execute business logic
   └── Return result

5. Channel adapter renders response
   └── Channel-appropriate format
```

### Channel Adapters

```
Each channel has an adapter that:
├── Receives channel-native interactions
├── Translates to service calls
├── Calls appropriate Headless Service
├── Transforms response for channel
└── Renders in channel-appropriate format
```

### Authorization

```
Headless Service authorization:
├── Verify caller persona matches service
├── Check operation permission
├── Validate resource access (tenant, workbench)
└── Apply fine-grained rules (own tasks vs all tasks)
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Channel Adapters | ← called by | Channels consume services |
| Cipher IAM | → authenticates | Validate user and permissions |
| Signal Exchange | → calls | For request operations |
| Task Management | → calls | For task operations |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Persona-scoped** | Service only serves its persona |
| **Stateless** | No session state in service |
| **Authorization required** | All operations authenticated |
| **Channel-agnostic** | No channel-specific logic |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Channel flexibility** | Add channels without service changes |
| ✅ **Consistent behavior** | Same logic everywhere |
| ✅ **Testable** | Test business logic independently |
| ✅ **Maintainable** | Clear separation of concerns |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Additional layer** | Minimal overhead; clear benefits |
| ⚠️ **Interface evolution** | Versioned APIs; backward compatible |

---

## Examples

### Example 1: Agent Gets Tasks via Different Channels

```
Web Console:
1. Agent clicks "My Tasks"
2. Web adapter calls AgentAccessService.getAssignedTasks()
3. Service returns Task[]
4. Web renders task cards with full details

MS Teams:
1. Agent types "show my tasks"
2. Teams adapter calls AgentAccessService.getAssignedTasks()
3. Service returns Task[]
4. Teams renders adaptive card with summary

MCP:
1. AI agent calls hub.agent.list_tasks()
2. MCP adapter calls AgentAccessService.getAssignedTasks()
3. Service returns Task[]
4. MCP returns structured data for AI
```

### Example 2: Service Implementation

```python
class AgentAccessService:
    def __init__(self, task_client, request_client):
        self.task_client = task_client
        self.request_client = request_client
    
    async def get_assigned_tasks(self, agent_id: str) -> List[Task]:
        # Authorization checked by middleware
        tasks = await self.task_client.find_by_assignee(agent_id)
        return [self._enrich_task(t) for t in tasks]
    
    async def complete_task(
        self, 
        task_id: str, 
        outcome: TaskOutcome
    ) -> None:
        task = await self.task_client.get(task_id)
        # Validate agent can complete this task
        await self.task_client.complete(task_id, outcome)
        # Update request
        await self.request_client.add_update(
            task.request_id,
            UpdateType.TASK_COMPLETED,
            {"task_id": task_id, "outcome": outcome}
        )
```

---

## Implementation Notes

### For Developers

- Design service APIs for multiple channel consumption
- Don't include channel-specific logic in services
- Return rich data; let channels filter/format

### For Operators

- Monitor service health per persona
- Track latency per operation
- Review authorization failures

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Channel](./channel.md) | Channels consume Headless Services |
| [Persona](./persona.md) | Services organized by Persona |
| [Signal Exchange](./signal-exchange.md) | Services call SX for operations |

---

## References

- [UX Architecture](../06-ux-architecture/README.md)
- [ADR-0009: Headless Services](../decision-logs/0009-headless-services-with-channel-adapters.md)

