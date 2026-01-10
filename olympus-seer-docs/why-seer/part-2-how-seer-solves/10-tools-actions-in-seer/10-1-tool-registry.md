# 10.1 Tool Registry

The Tool Registry is Hub's centralized catalog of all tools available to agents. It provides discoverability, documentation, and governance for tool capabilities.

## What the Registry Contains

| Component | Description |
|-----------|-------------|
| **Tool Protocols** | Abstract capability definitions |
| **Tool Instances** | Concrete environment bindings |
| **Schemas** | Input/output specifications |
| **Metadata** | Descriptions, tags, owners |
| **Policies** | Access control, rate limits |

## Registry Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      TOOL REGISTRY                           │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │                 TOOL PROTOCOLS                     │    │
│   │   Abstract definitions (OpenAPI specs)             │    │
│   │                                                    │    │
│   │   get-transaction-details                          │    │
│   │   approve-refund                                   │    │
│   │   send-notification                                │    │
│   │   ...                                              │    │
│   └───────────────────────────────────────────────────┘    │
│                            │                                │
│                            │ binds to                       │
│                            ▼                                │
│   ┌───────────────────────────────────────────────────┐    │
│   │                 TOOL INSTANCES                     │    │
│   │   Concrete bindings per environment                │    │
│   │                                                    │    │
│   │   acme-transaction-service-prod                    │    │
│   │   acme-refund-api-prod                             │    │
│   │   acme-notification-service-prod                   │    │
│   │   ...                                              │    │
│   └───────────────────────────────────────────────────┘    │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │                 ACCESS POLICIES                    │    │
│   │   Who can use which tools                          │    │
│   └───────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Tool Protocol Definition

```yaml
# Tool Protocol (abstract)
apiVersion: hub.olympus.io/v1
kind: ToolProtocol
metadata:
  name: get-transaction-details
  namespace: shared-tools
  
spec:
  description: "Retrieve transaction details by ID"
  
  input:
    type: object
    required: [transaction_id]
    properties:
      transaction_id:
        type: string
        description: "Transaction identifier"
        
  output:
    type: object
    properties:
      transaction_id:
        type: string
      amount:
        type: number
      merchant:
        type: string
      status:
        type: string
        enum: [pending, settled, refunded]
        
  errors:
    - code: NOT_FOUND
      description: "Transaction not found"
    - code: ACCESS_DENIED
      description: "Not authorized to view transaction"
```

## Tool Instance Definition

```yaml
# Tool Instance (concrete)
apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: acme-transaction-service
  namespace: acme-disputes
  
spec:
  protocol: get-transaction-details
  
  binding:
    type: http
    endpoint: https://txn.acme.internal/v1/transactions/{transaction_id}
    method: GET
    
  authentication:
    type: oauth2
    credentials_ref: acme-txn-service-creds
    
  rate_limits:
    per_minute: 100
    per_hour: 1000
    
  access_policy:
    allowed_agents:
      - dispute-analyst-tier1
      - fraud-detector-v2
    allowed_workbenches:
      - dispute-ops-prod
```

## Registry Operations

### Discovery

Agents discover available tools:

```python
# List tools available to this agent
tools = await registry.list_tools(
    agent=agent_id,
    workbench=workbench_id
)

# Returns: [get-transaction-details, approve-refund, ...]
```

### Schema Retrieval

Get tool input/output schemas:

```python
schema = await registry.get_schema("get-transaction-details")
# Returns OpenAPI-compatible schema
```

### Instance Resolution

Resolve protocol to instance for environment:

```python
instance = await registry.resolve(
    protocol="get-transaction-details",
    workbench="dispute-ops-prod"
)
# Returns: acme-transaction-service (with binding details)
```

## Tool Categories

```yaml
tool_categories:
  read:
    description: "Retrieve data"
    examples: [get-transaction, get-customer, search-cases]
    risk: low
    
  write:
    description: "Modify data"
    examples: [update-case, add-note]
    risk: medium
    
  execute:
    description: "Trigger actions"
    examples: [approve-refund, send-notification]
    risk: high
    
  external:
    description: "Call external systems"
    examples: [check-fraud-score, verify-identity]
    risk: variable
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/registry-services/tool-registry.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-8-tool-action-requirements.md`

