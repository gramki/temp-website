# Agent Memory SDK

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Agent Memory Services](./README.md)

---

## Overview

The Agent Memory SDK provides programmatic access to Hub's agent memory storage services. It is available to all agents — both Raw Agents built on external frameworks and Seer-based agents.

---

## SDK Access

### Installation

```python
# Included in Hub agent runtime
from hub.agent_memory import (
    kv_store,
    conversation,
    log_store,
    documents
)
```

### Initialization

The SDK is automatically initialized with the current execution context:
- Tenant
- Workbench
- Scenario
- Request/Session
- Agent

**No explicit initialization required** — the runtime provides context.

---

## Service Clients

### KV Store Client

```python
from hub.agent_memory import kv_store

class KVStore:
    async def put(
        self,
        store: str,      # Logical store name (or "." for default)
        key: str,        # Key within store
        value: Any       # JSON-serializable value
    ) -> None:
        """Store a value."""
        
    async def get(
        self,
        store: str,
        key: str
    ) -> Optional[Any]:
        """Retrieve a value. Returns None if not found."""
        
    async def delete(
        self,
        store: str,
        key: str
    ) -> bool:
        """Delete a value. Returns True if existed."""
        
    async def list(
        self,
        store: str
    ) -> List[str]:
        """List all keys in a store."""
        
    async def exists(
        self,
        store: str,
        key: str
    ) -> bool:
        """Check if key exists."""
```

### Conversation Client

```python
from hub.agent_memory import conversation

class Conversation:
    async def append(
        self,
        message: Message   # Conversation message
    ) -> None:
        """Append message to conversation. Triggers compaction if needed."""
        
    async def retrieve(
        self,
        token_budget: int = None,  # Max tokens to return
        last_n: int = None         # Last N messages
    ) -> List[Message]:
        """Retrieve conversation within constraints."""
        
    async def compact(self) -> CompactionResult:
        """Manually trigger compaction."""
        
    async def get_summary(self) -> Optional[str]:
        """Get current conversation summary (if summarization enabled)."""
        
    async def get_token_count(self) -> int:
        """Get current token count."""
```

### Log Store Client

```python
from hub.agent_memory import log_store

class LogStore:
    async def append(
        self,
        entry: LogEntry   # Log entry object
    ) -> str:
        """Append entry to log. Returns entry ID."""
        
    async def get_last(
        self,
        n: int = 10      # Number of entries
    ) -> List[LogEntry]:
        """Get last N entries."""
        
    async def rag_search(
        self,
        query: str,
        limit: int = 5,
        min_score: float = 0.0
    ) -> List[SearchResult]:
        """Semantic search over log entries."""
        
    async def get_by_id(
        self,
        entry_id: str
    ) -> Optional[LogEntry]:
        """Get specific entry by ID."""
```

### Document Storage Client

```python
from hub.agent_memory import documents

class Documents:
    async def store(
        self,
        content: bytes,
        content_type: str,
        metadata: Dict[str, Any] = None
    ) -> str:
        """Store document. Returns content-addressable URI."""
        
    async def retrieve(
        self,
        uri: str
    ) -> Document:
        """Retrieve document by URI."""
        
    async def delete(
        self,
        uri: str
    ) -> bool:
        """Delete document. Returns True if existed."""
        
    async def list(self) -> List[DocumentInfo]:
        """List all stored documents."""
        
    async def rag_search(
        self,
        query: str,
        limit: int = 5,
        min_score: float = 0.0
    ) -> List[DocumentSearchResult]:
        """Semantic search over document content."""
```

---

## Data Types

### Message

```python
@dataclass
class Message:
    role: Literal["user", "assistant", "system", "tool"]
    content: str
    timestamp: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_call_id: Optional[str] = None
    tool_name: Optional[str] = None
```

### LogEntry

```python
@dataclass
class LogEntry:
    type: str                        # Entry type (e.g., "user_message", "tool_call")
    content: Any                     # Entry content
    timestamp: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None
```

### Document

```python
@dataclass
class Document:
    uri: str
    content: bytes
    content_type: str
    metadata: Dict[str, Any]
    created_at: datetime
    size_bytes: int
```

### SearchResult

```python
@dataclass
class SearchResult:
    entry: LogEntry
    score: float                     # Relevance score (0-1)
    highlights: List[str]            # Matched snippets
```

---

## Tool Definitions

All storage services expose tools for LLM-based agents:

### KV Store Tools

```json
{
  "name": "agent_memory.kv.save",
  "description": "Save a value to agent memory key-value store",
  "parameters": {
    "store": {
      "type": "string",
      "description": "Logical store name (optional, default '.')"
    },
    "key": {
      "type": "string",
      "description": "Key to store value under"
    },
    "value": {
      "type": "any",
      "description": "Value to store (JSON-serializable)"
    }
  }
}
```

```json
{
  "name": "agent_memory.kv.recall",
  "description": "Retrieve a value from agent memory key-value store",
  "parameters": {
    "store": {
      "type": "string",
      "description": "Logical store name (optional, default '.')"
    },
    "key": {
      "type": "string",
      "description": "Key to retrieve"
    }
  }
}
```

### Conversation Tools

```json
{
  "name": "agent_memory.conversation.save",
  "description": "Save a message to conversation history",
  "parameters": {
    "message": {
      "type": "object",
      "description": "Message to save",
      "properties": {
        "role": { "type": "string", "enum": ["user", "assistant", "system"] },
        "content": { "type": "string" }
      }
    }
  }
}
```

```json
{
  "name": "agent_memory.conversation.recall",
  "description": "Retrieve conversation history within token budget",
  "parameters": {
    "token_budget": {
      "type": "integer",
      "description": "Maximum tokens to return"
    }
  }
}
```

### Log Store Tools

```json
{
  "name": "agent_memory.log.save",
  "description": "Append entry to session log",
  "parameters": {
    "entry": {
      "type": "object",
      "description": "Log entry to append"
    }
  }
}
```

```json
{
  "name": "agent_memory.log.recall",
  "description": "Retrieve from session log",
  "parameters": {
    "mode": {
      "type": "string",
      "enum": ["last_n", "rag"],
      "description": "Retrieval mode"
    },
    "n": {
      "type": "integer",
      "description": "Number of entries (for last_n mode)"
    },
    "query": {
      "type": "string",
      "description": "Search query (for rag mode)"
    },
    "limit": {
      "type": "integer",
      "description": "Max results (for rag mode)"
    }
  }
}
```

### Document Tools

```json
{
  "name": "agent_memory.documents.save",
  "description": "Store a document",
  "parameters": {
    "content_base64": {
      "type": "string",
      "description": "Base64-encoded document content"
    },
    "content_type": {
      "type": "string",
      "description": "MIME type of document"
    },
    "metadata": {
      "type": "object",
      "description": "Optional metadata"
    }
  }
}
```

```json
{
  "name": "agent_memory.documents.recall",
  "description": "Retrieve a document by URI",
  "parameters": {
    "uri": {
      "type": "string",
      "description": "Document URI"
    }
  }
}
```

---

## Error Handling

### Exceptions

```python
from hub.agent_memory.exceptions import (
    QuotaExceededException,
    StoreNotFoundException,
    KeyNotFoundException,
    InvalidStoreNameException,
    DocumentTooLargeException,
    ContentValidationException
)

try:
    await kv_store.put("preferences", "key", large_value)
except QuotaExceededException as e:
    # Handle quota exceeded
    print(f"Quota exceeded: {e.quota_limit}, used: {e.current_usage}")
except InvalidStoreNameException as e:
    # Handle invalid store name
    print(f"Invalid store name: {e.store_name}")
```

### Error Codes

| Exception | Code | Description |
|-----------|------|-------------|
| `QuotaExceededException` | `QUOTA_EXCEEDED` | Storage limit reached |
| `StoreNotFoundException` | `STORE_NOT_FOUND` | Logical store not declared |
| `KeyNotFoundException` | `KEY_NOT_FOUND` | Key doesn't exist |
| `InvalidStoreNameException` | `INVALID_STORE_NAME` | Name violates pattern |
| `DocumentTooLargeException` | `DOC_TOO_LARGE` | Document exceeds size limit |
| `ContentValidationException` | `CONTENT_INVALID` | Virus/malware detected |

---

## Usage Patterns

### Entity Extraction Pattern

```python
async def extract_and_store_entities(message: str, agent_context):
    """Extract entities from message and store in KV."""
    
    # Framework-specific entity extraction
    entities = await extract_entities(message)
    
    for entity_type, entity_value in entities.items():
        await kv_store.put("entities", entity_type, entity_value)
```

### Conversation with Token Budget

```python
async def get_context_for_llm(token_budget: int = 4000):
    """Get conversation context within token budget."""
    
    # Get conversation history
    messages = await conversation.retrieve(token_budget=token_budget - 500)
    
    # Get relevant log entries
    log_entries = await log_store.get_last(n=5)
    
    # Get key preferences
    prefs = await kv_store.get("preferences", "all")
    
    return {
        "messages": messages,
        "recent_log": log_entries,
        "preferences": prefs
    }
```

### Document Reference in Conversation

```python
async def process_uploaded_document(doc_bytes: bytes, content_type: str):
    """Store document and add reference to conversation."""
    
    # Store document
    uri = await documents.store(
        content=doc_bytes,
        content_type=content_type,
        metadata={"source": "user_upload"}
    )
    
    # Add to conversation
    await conversation.append({
        "role": "user",
        "content": f"I've uploaded a document: {uri}",
        "metadata": {"document_uri": uri}
    })
    
    return uri
```

---

## Related Documents

- [Agent Memory Services](./README.md) — Overview
- [Storage Services](./storage-services.md) — Service details
- [Context Assembly Integration](./context-assembly.md) — Seer integration
- [Design Rationale](./design-rationale.md) — Design decisions and trade-offs
- [Developer Guide](../../../10-guides/agent-memory-developer-guide.md) — Best practices

---

*The Agent Memory SDK provides unified access to all storage services with consistent error handling and typing.*
