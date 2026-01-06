# Memory Services

> **Category:** Data Architecture

---

## Overview

**Memory Services** provides cognitive memory capabilities for Hub Applications and agents. Unlike Application Data Stores (transactional), Memory Services stores learned context, preferences, and behavioral patterns across three scopes: Enterprise Memory (organization-wide), Agent Memory (per agent), and User Memory (per end user).

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Memory** as persistent experience that influences future behavior. Memory Services implements this across multiple scopes.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Memory | Memory Services | Three-scoped memory implementation |
| Learning | Memory accumulation | Experience captured as memory |

### Gap This Fills

The ontology describes memory conceptually. Memory Services specifies:
1. **Memory scopes**: Whose memory is it?
2. **Memory types**: What kinds of things are remembered?
3. **Retrieval**: How is relevant memory accessed?
4. **Governance**: How is memory managed and audited?

---

## Definition

**Memory Services** is a cognitive storage subsystem that:
- Stores contextual memory at enterprise, agent, and user scopes
- Provides semantic retrieval of relevant memories
- Supports memory lifecycle (create, update, expire, delete)
- Integrates with Cognitive Audit Fabric for governance

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Three levels: Enterprise, Agent, User |
| **Lifecycle** | Created during operations; managed via policies |
| **Ownership** | Platform provides; governed by CAF |
| **Multiplicity** | One service; many memory entries |

---

## Rationale

### Why This Design?

Scoped memory enables:
1. **Personalization**: Agent and user-specific context
2. **Organizational learning**: Enterprise-wide insights
3. **Continuity**: Context preserved across sessions
4. **Appropriate access**: Right memory at right scope

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single memory store** | No scope separation |
| **Per-application memory** | Inconsistent; siloed |
| **No persistent memory** | Loses valuable context |

---

## Structure

### Memory Scopes

| Scope | What's Stored | Access |
|-------|---------------|--------|
| **Enterprise Memory** | Organization-wide learnings, policies, patterns | All applications in workbench |
| **Agent Memory** | Individual agent preferences, history, skills | Agent and their applications |
| **User Memory** | End-user context, preferences, history | User's interactions |

### Memory Entry

```json
{
  "memory_id": "mem-12345",
  "scope": "agent",
  "scope_id": "agent-alice",
  
  "type": "preference",           // preference | insight | observation | skill
  "category": "communication",
  
  "content": {
    "summary": "Agent prefers detailed email summaries",
    "details": {
      "preference_type": "notification_format",
      "value": "detailed",
      "confidence": 0.85
    }
  },
  
  "metadata": {
    "source": "task-completion-001",
    "created_at": "2026-01-06T10:00:00Z",
    "expires_at": null,
    "access_count": 15
  },
  
  "embedding": [0.1, 0.2, ...]     // For semantic retrieval
}
```

### Memory Service Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: MemoryServicesConfig
metadata:
  name: dispute-ops-memory
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  enterprise_memory:
    enabled: true
    retention_days: 365
    
  agent_memory:
    enabled: true
    retention_days: 180
    max_entries_per_agent: 1000
    
  user_memory:
    enabled: true
    retention_days: 90
    consent_required: true
    
  embedding_model: text-embedding-3-small
```

---

## Behavior

### How It Works

**Memory Creation:**
```
1. Application/Agent completes interaction
2. Identifies memory-worthy insight
3. Calls Memory Services to store:
   ├── Scope (enterprise/agent/user)
   ├── Type (preference/insight/observation)
   ├── Content
   └── Metadata
4. Memory Services:
   ├── Validates against CAF policies
   ├── Generates embedding
   └── Stores in memory store
```

**Memory Retrieval:**
```
1. Application needs context for decision
2. Queries Memory Services:
   ├── Scope (which memories to search)
   ├── Query (what context needed)
   └── Filters (type, recency, etc.)
3. Memory Services:
   ├── Semantic search via embedding
   ├── Apply access controls
   └── Return ranked memories
4. Application uses memories in context
```

### Memory Types

| Type | Purpose | Example |
|------|---------|---------|
| **preference** | User/agent preferences | "Prefers SMS notifications" |
| **insight** | Learned pattern | "Disputes from merchant X often fraudulent" |
| **observation** | Captured fact | "Customer mentioned address change" |
| **skill** | Agent capability | "Can handle Spanish language disputes" |

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Hub Applications | ← used by | Apps read/write memory |
| Cognitive Audit Fabric | → governed by | Policies and audit |
| Embedding Service | → uses | Generate embeddings |
| Knowledge Bank | ↔ complements | Memory vs knowledge |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Scope isolation** | Cannot access higher scope memories inappropriately |
| **CAF governance** | All operations logged and policy-checked |
| **Consent for user memory** | User consent required where configured |
| **Retention limits** | Memory expires per retention policy |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Contextual awareness** | Applications use relevant history |
| ✅ **Personalization** | Agent and user-specific experiences |
| ✅ **Learning** | Organization improves over time |
| ✅ **Semantic retrieval** | Find by meaning, not keywords |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Privacy concerns** | CAF governance; consent mechanisms |
| ⚠️ **Memory accuracy** | Confidence scores; review capabilities |

---

## Examples

### Example 1: Agent Using Memory

```python
class DisputeHandler(HubApplication):
    async def handle_request(self, update):
        customer_id = update.payload.customer_id
        
        # Retrieve relevant user memories
        user_memories = await self.memory.query(
            scope="user",
            scope_id=customer_id,
            query="previous dispute history preferences",
            limit=5
        )
        
        # Use memories in context
        if any(m.type == "preference" and 
               m.content.get("prefers_phone_contact") 
               for m in user_memories):
            # Customer prefers phone contact
            await self.schedule_callback(customer_id)
```

### Example 2: Storing Enterprise Insight

```python
# After analyzing dispute patterns
await self.memory.store(
    scope="enterprise",
    type="insight",
    category="fraud_detection",
    content={
        "summary": "Disputes from merchant 'XYZ Store' have 78% fraud rate",
        "details": {
            "merchant_id": "merchant-xyz",
            "fraud_rate": 0.78,
            "sample_size": 150,
            "time_period": "2025-Q4"
        }
    }
)
```

---

## Implementation Notes

### For Developers

- Query memory at start of complex decisions
- Store insights that will be valuable later
- Use appropriate scope for each memory
- Include confidence scores for learned insights

### For Operators

- Monitor memory storage growth
- Review CAF audit logs
- Manage retention policies
- Handle deletion requests

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Knowledge Bank](./knowledge-bank.md) | Knowledge vs Memory |
| [Cognitive Audit Fabric](./cognitive-audit-fabric.md) | Governs Memory Services |
| [Application Data Store](./application-data-store.md) | Different purpose |

---

## References

- [Memory Services Subsystem](../04-subsystems/cognitive-services/memory-services.md)
- [Cognitive Audit Fabric](../04-subsystems/cognitive-services/caf.md)

