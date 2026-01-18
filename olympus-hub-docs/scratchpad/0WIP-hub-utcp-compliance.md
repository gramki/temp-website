# Hub Tool Registry UTCP Compliance

> **Status:** 🟡 Draft — Brainstorming  
> **Last Updated:** 2026-01-17  
> **Purpose:** Design UTCP-compliant Tool Registry so Hub tools are discoverable by UTCP clients/SDKs

---

## Problem Statement

**Goal:** Make Hub's Tool Registry UTCP-compliant so that:
- All tools in Tool Registry are discoverable by UTCP-compliant clients/SDKs
- Seer SDK can use Tool Registry through UTCP repository interface
- Training Spec tool whitelisting can reference tools in UTCP format
- Hub tools can be consumed by any UTCP-compliant agent framework

**Key Requirements:**
1. **UTCP Standard Compliance** — Tools must conform to UTCP manual (call template) format
2. **Repository Interface** — Tool Registry must expose UTCP repository interface
3. **Training Spec Integration** — Tool whitelisting should support UTCP tool references
4. **SDK Integration** — Seer SDK should use UTCP repository interface
5. **Backward Compatibility** — Existing Hub APIs continue to work

---

## UTCP Key Concepts

From [UTCP Python SDK](https://github.com/universal-tool-calling-protocol/python-utcp):

### Manuals (Call Templates)
- Define how tools are discovered and invoked
- Support multiple communication protocols: HTTP, CLI, MCP, Text
- Include authentication, endpoint configuration, protocol restrictions

### Communication Protocols
- **HTTP**: REST API tools (most common)
- **CLI**: Command-line tools
- **MCP**: Model Context Protocol tools
- **Text**: Text-based tools (manuals, documentation)

### Tool Discovery
- Tools registered in UTCP repository
- Clients discover tools via `list_manuals()` or `discover_tools()`
- Access control via protocol restrictions

### OpenAPI Ingestion
- Zero-infrastructure tool integration
- Convert OpenAPI 2.0/3.0 specs to UTCP tools automatically
- Supports batch processing, remote URLs, file-based specs

### Protocol Restrictions
- Security: Tools can only use allowed communication protocols
- Default: Same protocol as call template type
- Explicit: `allowed_communication_protocols` field

---

## Current Hub Tool Registry State

### Architecture
- **Two-Level Model**: Tool Protocols (abstract) + Tools (concrete instances)
- **Tool Protocols**: Part of Machine Definitions, OpenAPI specs
- **Tools**: Bound to Machines, have access control, flow control policies
- **Integration**: Machine Registry, MCP Router, Seer Context Assembly

### Current Limitations
- No UTCP manual format
- No UTCP repository interface
- Tools not discoverable by UTCP clients
- Training specs reference tools by protocol ID only

---

## Proposed Changes

### 1. Tool Registry Subsystem

#### A. Add UTCP Manual Schema

```yaml
# Enhanced Tool Schema with UTCP compliance
tool:
  id: "acme-get-account"
  name: "Get ACME Account"
  namespace: "acme-core-banking"
  
  protocol_id: "get-account"
  machine_id: "acme-core-banking"
  
  # Existing fields...
  access_control: {...}
  flow_control: {...}
  
  # NEW: UTCP compliance fields
  utcp_manual:
    # UTCP call template configuration
    call_template_type: "http"  # http | cli | mcp | text
    communication_protocol: "http"  # Required for UTCP
    
    # HTTP call template (most common)
    http_config:
      url: "https://core.acme.com/api/accounts/{accountId}"
      method: "GET"
      headers: {}
      auth:
        type: "oauth2"  # oauth2 | api_key | basic | bearer
        token_url: "https://auth.acme.com/token"
        client_id: "${CLIENT_ID}"
        client_secret: "${CLIENT_SECRET}"
        scope: "read:accounts"
    
    # MCP call template (for MCP tools)
    mcp_config:
      server_name: "acme-banking-mcp"
      transport: "stdio"
      command: ["python", "-m", "acme_mcp_server"]
      config:
        mcpServers:
          acme-banking:
            transport: "stdio"
            command: ["python", "-m", "acme_mcp_server"]
    
    # CLI call template (for command-line tools)
    cli_config:
      commands:
        - command: "curl -X GET {{url}}"
          append_to_final_output: false
        - command: "jq '.account'"
      env_vars:
        API_KEY: "${MY_API_KEY}"
      working_dir: "/tmp"
    
    # Protocol restrictions (security)
    allowed_communication_protocols: ["http"]  # Default: same as call_template_type
    
    # Tool metadata for UTCP discovery
    utcp_metadata:
      name: "get-account"  # UTCP tool name
      description: "Retrieve account details by ID"
      version: "1.0.0"
      tags: ["banking", "accounts", "read"]
      category: "data_access"
```

#### B. Implement UTCP Repository Interface

```python
# New interface in Tool Registry
from typing import List, Optional
from utcp.utcp_client import UtcpClient
from utcp.manual import Manual

class UTCPRepository:
    """UTCP-compliant repository interface for tool discovery"""
    
    async def register_manual(self, manual: Manual) -> str:
        """
        Register a tool as UTCP manual.
        Returns tool ID.
        """
        # Convert Hub Tool to UTCP Manual
        # Store in Tool Registry
        # Return tool ID
        pass
    
    async def list_manuals(self, 
                          namespace: Optional[str] = None,
                          protocol: Optional[str] = None,
                          tags: Optional[List[str]] = None) -> List[Manual]:
        """
        List all UTCP manuals (tools) discoverable by clients.
        Applies access control and protocol restrictions.
        """
        # Query Tool Registry
        # Filter by namespace, protocol, tags
        # Apply access control (workbench, role)
        # Convert Hub Tools to UTCP Manuals
        # Return list
        pass
    
    async def get_manual(self, tool_id: str) -> Manual:
        """
        Get UTCP manual for a specific tool.
        """
        # Lookup tool in registry
        # Verify access
        # Convert to UTCP Manual
        # Return
        pass
    
    async def discover_tools(self, 
                           client_context: ClientContext) -> List[Tool]:
        """
        UTCP-compliant tool discovery with access control.
        Client context includes: workbench, role, agent identity
        """
        # Get tools accessible to client
        # Filter by protocol restrictions
        # Convert to UTCP format
        # Return
        pass
    
    async def call_tool(self, 
                       tool_id: str, 
                       arguments: dict,
                       client_context: ClientContext) -> dict:
        """
        Invoke tool via UTCP protocol.
        """
        # Lookup tool
        # Verify access and protocol restrictions
        # Resolve tool instance (machine binding)
        # Invoke via appropriate protocol
        # Return result
        pass
```

#### C. Tool Protocol to UTCP Mapping

```yaml
# Tool Protocol should generate UTCP-compliant schemas
tool_protocol:
  id: "get-account"
  name: "Get Account"
  
  # Existing fields...
  protocol_type: "openapi"
  specification: {...}  # OpenAPI spec
  
  # NEW: UTCP schema generation
  utcp_schema:
    # Auto-generated from OpenAPI spec or explicit
    input_schema:  # JSON Schema compatible
      type: "object"
      required: ["accountId"]
      properties:
        accountId:
          type: "string"
          description: "Account identifier"
          pattern: "^[A-Z0-9-]+$"
    
    output_schema:  # JSON Schema compatible
      type: "object"
      properties:
        account:
          type: "object"
          properties:
            id:
              type: "string"
            name:
              type: "string"
            balance:
              type: "number"
    
    # Communication protocol metadata
    communication_protocol: "http"
    call_template_type: "http"
    
    # Default protocol restrictions
    default_allowed_protocols: ["http"]
```

#### D. OpenAPI Ingestion Integration

```python
# Leverage UTCP's OpenAPI converter
from utcp_http.openapi_converter import OpenApiConverter

class ToolRegistryOpenAPIIngestion:
    """Convert Machine OpenAPI specs to UTCP tools"""
    
    async def ingest_openapi_spec(self, 
                                  machine_id: str,
                                  openapi_spec: dict) -> List[str]:
        """
        Ingest OpenAPI spec and create UTCP tools.
        Returns list of created tool IDs.
        """
        # Use UTCP OpenAPI converter
        converter = OpenApiConverter(openapi_spec)
        manual = converter.convert()
        
        # Create Tool Protocols from manual
        # Create Tools bound to Machine
        # Register in Tool Registry
        # Return tool IDs
        pass
    
    async def batch_ingest(self, 
                          specs: List[dict]) -> dict:
        """
        Batch process multiple OpenAPI specs.
        """
        # Process each spec
        # Return mapping of spec -> tool IDs
        pass
```

---

### 2. Training Spec Tool Whitelisting

#### A. Enhanced Tool References

```yaml
# Training Spec CRD - Enhanced tool whitelisting
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: dispute-analyst-training
  version: "1.7.0"
spec:
  tools:
    protocols:
      # Option 1: Existing format (still supported)
      - protocol: "get-transaction-details"
        alias: "get_txn"
        permissions: ["read"]
        usage: "Retrieve transaction details for dispute analysis"
      
      # Option 2: UTCP manual reference by tool ID
      - utcp_manual: "acme-get-account"  # Tool ID from registry
        alias: "get_account"
        permissions: ["read"]
        usage: "Get account information"
      
      # Option 3: UTCP manual reference with namespace
      - utcp_manual: "acme-banking/get-account"
        namespace: "acme-banking"
        alias: "get_account"
        permissions: ["read"]
        # Optional: protocol restrictions
        allowed_protocols: ["http"]
      
      # Option 4: UTCP manual reference with full path
      - utcp_manual: "acme-core-banking.acme-get-account"
        alias: "get_account"
        permissions: ["read", "write"]
    
    # NEW: UTCP discovery configuration
    utcp_discovery:
      # Filter tools by UTCP metadata
      tags: ["banking", "disputes", "transactions"]
      protocols: ["http"]  # Only HTTP tools
      namespaces: ["acme-banking", "acme-disputes"]
      categories: ["data_access", "action"]  # Tool categories
      
      # Auto-discover tools matching criteria
      auto_discover: false  # If true, automatically include matching tools
      auto_discover_scope: "workbench"  # workbench | tenant | system
```

#### B. Training Spec Validation

```yaml
# Validation rules for UTCP tool references
validation_rules:
  - All tools referenced must exist in Tool Registry
  - Tools must have UTCP manual configuration
  - Protocol restrictions must be compatible with tool's allowed protocols
  - Access control policies must allow agent's role/workbench
  - Tool must be in allowed workbench tool whitelist
  - Tool status must be "active" (not deprecated/suspended)
```

#### C. Training Spec Manager Changes

```python
# Training Spec Manager - UTCP tool resolution
class TrainingSpecManager:
    """Manages Training Spec lifecycle and tool resolution"""
    
    async def resolve_tools(self, training_spec: TrainingSpec) -> List[ResolvedTool]:
        """
        Resolve tool references in training spec.
        Supports both protocol IDs and UTCP manual references.
        """
        resolved_tools = []
        
        for tool_ref in training_spec.spec.tools.protocols:
            if tool_ref.protocol:
                # Existing format: resolve by protocol ID
                tool = await self._resolve_by_protocol(tool_ref.protocol)
            elif tool_ref.utcp_manual:
                # NEW: Resolve by UTCP manual reference
                tool = await self._resolve_by_utcp_manual(
                    tool_ref.utcp_manual,
                    namespace=tool_ref.namespace
                )
            
            # Validate access and protocol restrictions
            await self._validate_tool_access(tool, training_spec)
            
            resolved_tools.append(ResolvedTool(
                tool=tool,
                alias=tool_ref.alias,
                permissions=tool_ref.permissions
            ))
        
        return resolved_tools
    
    async def _resolve_by_utcp_manual(self, 
                                      utcp_manual_ref: str,
                                      namespace: Optional[str] = None) -> Tool:
        """
        Resolve tool by UTCP manual reference.
        """
        # Parse reference (supports multiple formats)
        # Format 1: "tool-id"
        # Format 2: "namespace/tool-id"
        # Format 3: "namespace.tool-id"
        
        # Query Tool Registry
        # Return tool
        pass
```

---

### 3. Seer SDK Changes

#### A. UTCP Client Integration

```python
# Seer SDK - Hub Integration APIs
from seer_sdk import SeerSDK
from seer_sdk.hub.utcp import UTCPClient, UTCPRepository

# Initialize SDK
sdk = SeerSDK.from_environment()

# NEW: Access UTCP-compliant tool repository
utcp_client = sdk.hub.utcp

# Discover tools via UTCP
tools = await utcp_client.discover_tools(
    namespace="acme-banking",
    protocol="http",
    tags=["banking", "accounts"]
)

# Get tool manual (UTCP format)
manual = await utcp_client.get_manual("acme-get-account")

# List all manuals
manuals = await utcp_client.list_manuals(
    namespace="acme-banking"
)

# Register manual (for tools not yet in registry)
await utcp_client.register_manual({
    "name": "custom-tool",
    "call_template_type": "http",
    "url": "https://api.example.com/tool",
    "auth": {
        "auth_type": "api_key",
        "api_key": "Bearer ${API_TOKEN}",
        "var_name": "Authorization",
        "location": "header"
    }
})

# Call tool via UTCP
result = await utcp_client.call_tool(
    tool_name="acme-get-account",
    arguments={"accountId": "acc-123"}
)
```

#### B. Dual Interface Support

```python
# Option 1: Existing Hub APIs (backward compatible)
tools = await hub.tools.discover()
result = await hub.tools.invoke("get-transactions", {
    "account_id": "acc-123"
})

# Option 2: UTCP interface (new, standard)
tools = await hub.utcp.discover_tools()
result = await hub.utcp.call_tool("get-transactions", {
    "account_id": "acc-123"
})

# Option 3: UTCP repository interface (for advanced use)
repository = UTCPRepository(client=utcp_client)
manuals = await repository.list_manuals(
    namespace="acme-banking",
    protocol="http"
)
```

#### C. SDK Architecture

```python
# Seer SDK structure
seer_sdk/
  hub/
    tools.py          # Existing tool APIs
    utcp/
      __init__.py
      client.py       # UTCP client
      repository.py   # UTCP repository interface
      manual.py       # UTCP manual models
      converter.py    # Hub Tool <-> UTCP Manual conversion
```

---

### 4. MCP Channel Integration

#### A. UTCP Manual Generation for MCP Tools

```yaml
# MCP Server CRD - Enhanced with UTCP
apiVersion: hub.olympus.io/v1
kind: MCPServer
metadata:
  name: acme-banking-mcp
  namespace: acme-banking
spec:
  template_kind: "machine-template"
  
  tools:
    source: "machine"  # or "explicit"
    machine_id: "acme-core-banking"
  
  # NEW: UTCP configuration
  utcp:
    # Generate UTCP manuals for all tools
    enabled: true
    call_template_type: "mcp"  # MCP tools use MCP call template
    mcp_config:
      server_name: "acme-banking-mcp"
      transport: "stdio"
      command: ["python", "-m", "hub_mcp_server"]
      config:
        mcpServers:
          acme-banking:
            transport: "stdio"
            command: ["python", "-m", "hub_mcp_server"]
    
    # Protocol restrictions
    allowed_communication_protocols: ["mcp", "http"]  # Can expose via both
    
    # Auto-generate UTCP manuals for all tools
    auto_generate_manuals: true
```

#### B. MCP Router UTCP Endpoints

```python
# MCP Router - UTCP endpoints
# GET /utcp/manuals
# Returns: List of UTCP manuals (tools) available to client
# Query params: namespace, protocol, tags

# GET /utcp/manuals/{tool_id}
# Returns: UTCP manual for specific tool

# POST /utcp/tools/{tool_id}/call
# Body: { "arguments": {...} }
# Returns: Tool execution result

# GET /utcp/repository
# Returns: UTCP repository metadata
```

---

## Implementation Roadmap

### Phase 1: Foundation (Tool Registry)
- [ ] Add UTCP manual schema to Tool Registry CRD
- [ ] Implement UTCP repository interface in Tool Registry service
- [ ] Add tool-to-UTCP conversion logic
- [ ] Support OpenAPI → UTCP conversion (leverage UTCP's OpenAPI ingestion)
- [ ] Add protocol restrictions validation
- [ ] Update Tool Registry API to expose UTCP endpoints

### Phase 2: Training Spec Integration
- [ ] Extend Training Spec CRD with UTCP tool references
- [ ] Add validation for UTCP tool references
- [ ] Update Training Spec Manager to resolve UTCP tools
- [ ] Support auto-discovery of tools based on UTCP metadata
- [ ] Update Training Spec validation rules

### Phase 3: SDK Integration
- [ ] Add UTCP client to Seer SDK (Python)
- [ ] Implement UTCP repository interface in SDK
- [ ] Add Hub Tool <-> UTCP Manual conversion utilities
- [ ] Maintain backward compatibility with existing APIs
- [ ] Add UTCP tool discovery and invocation
- [ ] Add Java SDK support (if needed)

### Phase 4: MCP Channel Enhancement
- [ ] Add UTCP manual generation for MCP tools
- [ ] Update MCP Router to expose UTCP endpoints
- [ ] Support MCP call template type in Tool Registry
- [ ] Auto-generate UTCP manuals for machine-template tools

### Phase 5: OpenAPI Ingestion
- [ ] Integrate UTCP's OpenAPI converter
- [ ] Auto-generate UTCP manuals from Machine OpenAPI specs
- [ ] Support batch OpenAPI ingestion
- [ ] Add OpenAPI ingestion API to Tool Registry

---

## Benefits

1. **Standard Compliance** — Tools discoverable by any UTCP-compliant client
2. **Interoperability** — Works with UTCP ecosystems and frameworks
3. **Zero-Infrastructure Integration** — OpenAPI ingestion for existing APIs
4. **Security** — Protocol restrictions prevent unauthorized protocol usage
5. **Backward Compatibility** — Existing Hub APIs continue to work
6. **Developer Experience** — Standard tool discovery and invocation patterns
7. **Future-Proof** — Aligned with emerging tool calling standards

---

## Open Questions

### 1. Namespace Strategy
- **Question**: How to handle tool namespacing in UTCP?
- **Options**:
  - Use Hub's namespace (workbench/tenant)
  - Use UTCP namespace format
  - Support both with mapping
- **Recommendation**: Support both, map Hub namespace to UTCP namespace

### 2. Versioning
- **Question**: How to version UTCP manuals?
- **Options**:
  - Use tool version from Tool Registry
  - Use protocol version
  - Separate UTCP manual version
- **Recommendation**: Use tool version, support protocol version as fallback

### 3. Protocol Mapping
- **Question**: How to map Hub's protocol types to UTCP call template types?
- **Mapping**:
  - `openapi` → `http` (call_template_type)
  - `asyncapi` → `http` (with async support)
  - `grpc` → `http` (via gRPC-Web)
  - `graphql` → `http`
  - `mcp` → `mcp`
- **Recommendation**: Explicit mapping table, support custom mappings

### 4. Authentication
- **Question**: How to handle Hub's OAuth in UTCP auth config?
- **Options**:
  - Map Hub OAuth to UTCP OAuth2
  - Use API key with token injection
  - Support both
- **Recommendation**: Map Hub OAuth to UTCP OAuth2, support API key for simple cases

### 5. Tool Discovery Scope
- **Question**: What tools should be discoverable via UTCP?
- **Options**:
  - All tools in Tool Registry
  - Only tools with UTCP manual configuration
  - Tools explicitly marked as UTCP-compliant
- **Recommendation**: Only tools with UTCP manual configuration (opt-in)

### 6. Backward Compatibility
- **Question**: How to handle tools without UTCP configuration?
- **Options**:
  - Auto-generate UTCP manuals from existing tool specs
  - Require explicit UTCP configuration
  - Support both (opt-in auto-generation)
- **Recommendation**: Support both, default to auto-generation for OpenAPI tools

---

## Related Documentation

- [Tool Registry](../04-subsystems/registry-services/tool-registry.md)
- [MCP Channel](../04-subsystems/mcp-channel/README.md)
- [Training Spec CRD](../../olympus-seer-docs/seer-design/hub-integration/training-spec-crd.md)
- [Seer SDK Hub Integration](../../olympus-seer-docs/seer-design/subsystems/seer-agent-sdk/python-sdk/hub-integration-apis.md)
- [UTCP Python SDK](https://github.com/universal-tool-calling-protocol/python-utcp)
- [UTCP Documentation](https://www.utcp.io/)

---

## Next Steps

1. **Review and Refine** — Get feedback on proposed approach
2. **Design Details** — Create detailed design for each subsystem
3. **Prototype** — Build proof-of-concept for Tool Registry UTCP interface
4. **Integration Planning** — Plan integration with existing systems
5. **Documentation** — Update subsystem documentation with UTCP compliance

---

*This is a brainstorming document. Design decisions and implementation details will be refined as we progress.*
