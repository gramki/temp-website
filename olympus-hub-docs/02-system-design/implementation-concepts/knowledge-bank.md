# Knowledge Bank

> **Category:** Data Architecture

---

## Overview

**Knowledge Bank** provides document storage and semantic retrieval (RAG) capabilities for Hub Applications. Unlike Memory Services (learned context), Knowledge Bank stores curated documents, SOPs, policies, and reference materials that applications and agents use for informed decision-making.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Knowledge Base** as curated information repositories. Knowledge Bank implements this with document management and semantic search.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Knowledge Base | Knowledge Bank | Document-based knowledge store |
| Knowledge retrieval | RAG queries | Semantic search for relevant content |

### Gap This Fills

The ontology describes knowledge conceptually. Knowledge Bank specifies:
1. **Document management**: How are documents stored?
2. **Retrieval**: How is relevant knowledge found?
3. **Chunking**: How are large documents handled?
4. **Access control**: Who can access what knowledge?

---

## Definition

**Knowledge Bank** is a document management and retrieval service that:
- Stores documents with metadata and embeddings
- Chunks documents for efficient retrieval
- Provides semantic (RAG) query interface
- Supports workbench-scoped access control

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-scoped (can share across workbenches) |
| **Lifecycle** | Documents curated by architects; queried by apps |
| **Ownership** | Process Architect manages content |
| **Multiplicity** | Multiple knowledge banks per workbench |

---

## Rationale

### Why This Design?

Dedicated knowledge bank enables:
1. **Curated quality**: Documents reviewed before inclusion
2. **Semantic retrieval**: Find by meaning
3. **Shared knowledge**: Multiple scenarios use same knowledge
4. **Governance**: Clear ownership and access control

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **External search engines** | No Hub integration; access control issues |
| **Per-application storage** | Duplicated; inconsistent |
| **Memory Services only** | Different purpose (learned vs curated) |

---

## Structure

### Knowledge Bank Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: KnowledgeBankConfig
metadata:
  name: dispute-knowledge
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  # Embedding configuration
  embedding:
    model: text-embedding-3-small
    dimensions: 1536
    
  # Chunking configuration
  chunking:
    strategy: semantic          # semantic | fixed | paragraph
    max_chunk_size: 512
    overlap: 50
    
  # Access
  shared_with:
    - workbench: fraud-ops-prod
      access: read
```

### Document Structure

```json
{
  "document_id": "doc-sop-dispute",
  "knowledge_bank_id": "dispute-knowledge",
  
  "metadata": {
    "title": "Dispute Investigation SOP",
    "type": "sop",
    "version": "2.0.0",
    "author": "process-architect",
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-05T00:00:00Z",
    "tags": ["dispute", "investigation", "compliance"]
  },
  
  "content": {
    "format": "markdown",
    "source_url": "git://...",
    "hash": "sha256:..."
  },
  
  "chunks": [
    {
      "chunk_id": "chunk-001",
      "content": "When investigating disputes...",
      "embedding": [0.1, 0.2, ...],
      "position": 0
    }
  ],
  
  "status": "active"   // active | archived | draft
}
```

### Document Types

| Type | Purpose | Examples |
|------|---------|----------|
| **sop** | Standard Operating Procedures | Investigation steps |
| **policy** | Business policies | Refund policy |
| **reference** | Reference material | Product catalog |
| **training** | Training materials | Agent onboarding |
| **compliance** | Regulatory docs | Reg E requirements |

---

## Behavior

### How It Works

**Document Ingestion:**
```
1. Process Architect uploads document
2. Knowledge Bank:
   ├── Validates document format
   ├── Extracts text content
   ├── Applies chunking strategy
   ├── Generates embeddings per chunk
   └── Stores with metadata
3. Document available for queries
```

**Knowledge Query (RAG):**
```
1. Application needs context for decision
2. Queries Knowledge Bank:
   ├── Natural language query
   ├── Optional filters (type, tags)
   └── Limit
3. Knowledge Bank:
   ├── Generate query embedding
   ├── Semantic search across chunks
   ├── Rank and filter results
   └── Return relevant chunks with source
4. Application uses in context (prompt augmentation)
```

### Chunking Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **semantic** | LLM-based semantic boundaries | Rich documents |
| **fixed** | Fixed token count | Uniform documents |
| **paragraph** | Natural paragraph breaks | Structured docs |

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Hub Applications | ← queried by | Apps retrieve knowledge |
| Seer Runtime | ← used by | AI agents query knowledge |
| Process Architect | ← managed by | Content curation |
| Git Repository | ← synced from | Document source |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Workbench scoped** | Default access within workbench |
| **Explicit sharing** | Cross-workbench requires config |
| **Versioned documents** | Changes create new versions |
| **Embedding consistency** | Same model for all chunks |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Semantic search** | Find by meaning |
| ✅ **Curated quality** | Reviewed content |
| ✅ **Shareable** | Cross-workbench access |
| ✅ **Versioned** | Track document changes |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Curation effort** | Clear ownership; review process |
| ⚠️ **Embedding costs** | Efficient chunking; batch processing |

---

## Examples

### Example 1: Querying Knowledge in Application

```python
class DisputeHandler(HubApplication):
    async def handle_request(self, update):
        dispute_type = update.payload.dispute_type
        
        # Query relevant SOP
        sop_results = await self.knowledge_bank.query(
            query=f"How to investigate {dispute_type} disputes",
            filters={"type": "sop"},
            limit=3
        )
        
        # Use in AI context
        sop_context = "\n".join([r.content for r in sop_results])
        
        decision = await self.ai.decide(
            prompt=f"Based on the following SOP:\n{sop_context}\n\n"
                   f"Analyze this dispute: {update.payload}"
        )
```

### Example 2: Document Upload

```bash
# Upload SOP document
hub knowledge upload \
  --bank dispute-knowledge \
  --file dispute-investigation-sop.md \
  --type sop \
  --tags dispute,investigation,compliance
```

---

## Implementation Notes

### For Developers

- Query knowledge at decision points
- Use specific queries for better results
- Combine multiple sources when needed
- Handle no-result gracefully

### For Process Architects

- Keep documents focused and well-structured
- Use appropriate chunking for document type
- Review and update regularly
- Tag consistently for filtering

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Memory Services](./memory-services.md) | Different: learned vs curated |
| [Application Data Store](./application-data-store.md) | Different: docs vs transactional |
| [Scenario Specification Types](./scenario-specification-types.md) | SOPs linked in Normative spec |

---

## References

- [Knowledge Services Subsystem](../../04-subsystems/cognitive-services/knowledge-services.md)
- [RAG Implementation](../../04-subsystems/cognitive-services/rag.md)

