# Signal Configuration Guide

> **Audience:** Process Architects, Developers  
> **Prerequisites:** Workbench created, I/O Gateways configured

This guide walks through configuring Signals and Triggers to enable your Workbench to respond to external events, API calls, file arrivals, and scheduled events.

---

## Overview

In Olympus Hub, **Signals** are external stimuli that trigger automation. You don't "create" signals directly — signals **arrive** from external systems via I/O Gateways. Your role is to:

1. **Define Signal Definitions** — Specify which signals your Scenario should respond to
2. **Configure Triggers** — Transform matching signals into Requests for Hub Applications

```
External System → I/O Gateway → Normalized Signal → Signal Definition (filter) → Trigger (transform) → Request
```

---

## Understanding Signals

### What is a Signal?

A **Signal** is an external event or stimulus that arrives at Hub through an I/O Gateway:

| Signal Source | I/O Gateway | Example |
|---------------|-------------|---------|
| Business Events | **Atropos** (Event Bus) | `payment.disputed`, `account.overdraft` |
| API Calls | **Heracles** (API Gateway) | POST `/api/disputes`, GET `/api/status` |
| File Arrivals | **Dia** (File Gateway) | Settlement file, batch upload |
| Scheduled Events | **Kale** (Scheduler) | Daily reconciliation, monthly reports |
| Business Exceptions | **Cronus** | Fraud alert, compliance observation |
| Chat Messages | **MS Teams** | User message in bot channel |

### Signal Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SIGNAL FLOW                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   EXTERNAL SYSTEM                                                            │
│        │                                                                     │
│        │ Protocol-specific format (HTTP, Kafka, SFTP, etc.)                 │
│        ▼                                                                     │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │                    I/O GATEWAY                                      │    │
│   │                                                                     │    │
│   │   1. Receive signal in protocol-specific format                    │    │
│   │   2. Authenticate & authorize                                      │    │
│   │   3. Transform to Normalized Signal DTO                            │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│        │                                                                     │
│        │ Normalized Signal DTO                                              │
│        ▼                                                                     │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │                   SIGNAL EXCHANGE                                   │    │
│   │                                                                     │    │
│   │   4. Match against Signal Definitions (filters)                    │    │
│   │   5. Execute matching Triggers (transformations)                   │    │
│   │   6. Create or update Request                                      │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│        │                                                                     │
│        ▼                                                                     │
│   HUB APPLICATION                                                            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## The Normalized Signal DTO

All signals arrive at Signal Exchange in a **normalized format**, regardless of the originating protocol. Understanding this format is essential for defining filters and transformations.

### Signal Structure

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "signal_id": "sig-12345",
    "signal_type": "payment_event",
    "timestamp": "2026-01-06T10:00:00Z",
    "correlation_id": "corr-67890",
    "idempotency_key": "idem-22222"
  },
  "payload": {
    "content_type": "application/json",
    "data": {
      // Signal-specific data
    }
  },
  "metadata": {
    "source_system": "temenos-core",
    "source_event_id": "evt-99999",
    "trace_id": "trace-abc123"
  },
  "additional_fields": {
    // I/O Gateway-specific fields
  }
}
```

### Signal Header Fields

| Field | Required | Description |
|-------|----------|-------------|
| `tenant_id` | ✅ | Tenant scope — identifies your organization |
| `subscription_id` | ✅ | Subscription scope — identifies the Hub subscription |
| `signal_id` | ✅ | Unique identifier for this signal |
| `signal_type` | ✅ | Type of signal (used in filtering) |
| `timestamp` | ✅ | When the signal occurred |
| `correlation_id` | ❌ | Link to existing Request (for updates) |
| `idempotency_key` | ❌ | Prevents duplicate processing |

### Payload Structure

| Field | Description |
|-------|-------------|
| `content_type` | `application/json` or `application/base64` |
| `data` | The actual signal data (structure depends on signal type) |

---

## Step 1: Define Signal Types

Before creating Signal Definitions, identify the signal types your Workbench needs to handle.

### Access Signal Type Registry

```
Workbench Studio → [Workbench] → Signals → Signal Types
```

### Register Signal Types

For each type of signal you expect:

```yaml
signal_type:
  id: "payment-disputed"
  name: "Payment Disputed"
  description: "Card network dispute filed against a transaction"
  
  # Source I/O Gateway
  source_gateway: atropos
  source_topic: "card-network.disputes"
  
  # Expected payload schema
  payload_schema:
    type: object
    required:
      - transaction_id
      - dispute_reason
      - amount
    properties:
      transaction_id:
        type: string
        description: "Original transaction identifier"
      dispute_reason:
        type: string
        enum: ["FRAUD", "NOT_RECEIVED", "NOT_AS_DESCRIBED", "DUPLICATE", "OTHER"]
      amount:
        type: number
        description: "Disputed amount in cents"
      customer_id:
        type: string
      dispute_date:
        type: string
        format: date
```

### Signal Type Examples by Gateway

#### Atropos (Event Bus) Signal Types

```yaml
# Core Banking Events
signal_types:
  - id: "account-overdraft"
    source_gateway: atropos
    source_topic: "core-banking.accounts"
    payload_schema:
      properties:
        account_id: { type: string }
        overdraft_amount: { type: number }
        current_balance: { type: number }
        
  - id: "transaction-posted"
    source_gateway: atropos
    source_topic: "core-banking.transactions"
    payload_schema:
      properties:
        transaction_id: { type: string }
        amount: { type: number }
        type: { type: string, enum: ["DEBIT", "CREDIT"] }
```

#### Heracles (API Gateway) Signal Types

```yaml
# API Request Signal Types
signal_types:
  - id: "dispute-submission"
    source_gateway: heracles
    source_endpoint: "POST /api/v1/disputes"
    payload_schema:
      properties:
        transaction_id: { type: string, required: true }
        reason: { type: string, required: true }
        description: { type: string }
        supporting_documents: 
          type: array
          items: { type: string, format: uri }
          
  - id: "status-inquiry"
    source_gateway: heracles
    source_endpoint: "GET /api/v1/disputes/{id}/status"
    payload_schema:
      properties:
        dispute_id: { type: string }
```

#### Dia (File Gateway) Signal Types

```yaml
# File Arrival Signal Types
signal_types:
  - id: "settlement-file-arrived"
    source_gateway: dia
    file_pattern: "settlements/*.csv"
    payload_schema:
      properties:
        file_name: { type: string }
        file_size: { type: integer }
        file_path: { type: string }
        row_count: { type: integer }
        
  - id: "document-uploaded"
    source_gateway: dia
    file_pattern: "documents/{request_id}/*"
    payload_schema:
      properties:
        document_type: { type: string }
        file_name: { type: string }
        mime_type: { type: string }
```

#### Kale (Scheduler) Signal Types

```yaml
# Scheduled Signal Types
signal_types:
  - id: "daily-reconciliation"
    source_gateway: kale
    schedule: "0 2 * * *"  # Daily at 2 AM
    timezone: "UTC"
    payload_schema:
      properties:
        batch_date: { type: string, format: date }
        batch_type: { type: string }
        
  - id: "monthly-report"
    source_gateway: kale
    schedule: "0 6 1 * *"  # 1st of each month at 6 AM
    payload_schema:
      properties:
        report_month: { type: string }
        report_type: { type: string }
```

---

## Step 2: Create Signal Definitions

A **Signal Definition** is a filter that identifies signals your Scenario should process.

### Access Signal Definition Editor

```
Workbench Studio → [Workbench] → Signals → Signal Definitions → Create
```

### Signal Definition Structure

```yaml
signal_definition:
  id: "sig-def-high-value-dispute"
  name: "High Value Dispute Signal"
  description: "Disputes over $10,000 requiring special handling"
  
  # Associated signal type
  signal_type_id: "payment-disputed"
  
  # Filter conditions (must all match)
  filter:
    # Filter on signal header
    signal_header:
      signal_type: "payment_event"
      
    # Filter on payload data
    payload:
      data:
        dispute_reason:
          $in: ["FRAUD", "NOT_RECEIVED"]
        amount:
          $gt: 1000000  # Over $10,000 (in cents)
          
    # Filter on metadata (optional)
    metadata:
      source_system: "visa-network"
```

### Filter Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `$eq` | Equals (default) | `status: "ACTIVE"` |
| `$ne` | Not equals | `status: { $ne: "CLOSED" }` |
| `$gt` | Greater than | `amount: { $gt: 1000 }` |
| `$gte` | Greater than or equal | `priority: { $gte: 3 }` |
| `$lt` | Less than | `days_open: { $lt: 30 }` |
| `$lte` | Less than or equal | `score: { $lte: 50 }` |
| `$in` | In array | `type: { $in: ["A", "B"] }` |
| `$nin` | Not in array | `status: { $nin: ["CANCELLED"] }` |
| `$exists` | Field exists | `optional_field: { $exists: true }` |
| `$regex` | Pattern match | `code: { $regex: "^ERR-" }` |

### Signal Definition Examples

#### Example 1: Fraud Dispute Signal

```yaml
signal_definition:
  id: "sig-def-fraud-dispute"
  name: "Fraud Dispute"
  
  signal_type_id: "payment-disputed"
  
  filter:
    payload:
      data:
        dispute_reason: "FRAUD"
```

#### Example 2: Large Transaction Alert

```yaml
signal_definition:
  id: "sig-def-large-transaction"
  name: "Large Transaction Alert"
  
  signal_type_id: "transaction-posted"
  
  filter:
    payload:
      data:
        amount:
          $gt: 5000000  # Over $50,000
        type: "DEBIT"
```

#### Example 3: VIP Customer File Upload

```yaml
signal_definition:
  id: "sig-def-vip-document"
  name: "VIP Customer Document Upload"
  
  signal_type_id: "document-uploaded"
  
  filter:
    payload:
      data:
        document_type: "SUPPORTING_EVIDENCE"
    metadata:
      customer_segment: "VIP"
```

#### Example 4: Weekend API Request

```yaml
signal_definition:
  id: "sig-def-weekend-submission"
  name: "Weekend Dispute Submission"
  description: "Disputes submitted on weekends (may need Monday review)"
  
  signal_type_id: "dispute-submission"
  
  filter:
    signal_header:
      # Custom expression evaluated at runtime
      $expr:
        $in:
          - { $dayOfWeek: "$timestamp" }
          - [0, 6]  # Sunday = 0, Saturday = 6
```

---

## Step 3: Create Triggers

A **Trigger** transforms a matching signal into a Request for a Hub Application.

### Access Trigger Editor

```
Workbench Studio → [Workbench] → Triggers → Create
```

### Trigger Structure

```yaml
trigger:
  id: "trg-fraud-dispute-resolution"
  name: "Fraud Dispute Resolution Trigger"
  description: "Creates dispute resolution request for fraud cases"
  
  # Link to Signal Definition
  signal_definition_id: "sig-def-fraud-dispute"
  
  # Target Scenario
  scenario_id: "fraud-dispute-resolution"
  
  # Action type
  action: create_or_update  # create_new | update_existing | create_or_update
  
  # Correlation for finding existing requests
  correlation:
    key_expression: "$.payload.data.transaction_id"
    
  # Transformation from Signal → Request
  transformation:
    type: low_code  # low_code | code
    
    mapping:
      # Request metadata
      request_type: "BusinessRequest"
      priority: "high"
      
      # Subject (who the request is about)
      subject:
        type: "customer"
        id: "$.payload.data.customer_id"
        
      # Object (what the request is about)
      object:
        type: "transaction"
        id: "$.payload.data.transaction_id"
        
      # Request payload (data for the application)
      payload_mapping:
        dispute_reason: "$.payload.data.dispute_reason"
        transaction_id: "$.payload.data.transaction_id"
        disputed_amount: "$.payload.data.amount"
        dispute_date: "$.signal_header.timestamp"
        customer_id: "$.payload.data.customer_id"
```

### Transformation Types

#### Low-Code Transformation

Use JSONPath expressions to map signal fields to request fields:

```yaml
transformation:
  type: low_code
  
  mapping:
    request_type: "BusinessRequest"  # Static value
    priority: "$.payload.data.priority"  # Dynamic from signal
    
    subject:
      type: "customer"
      id: "$.payload.data.customer_id"
      
    payload_mapping:
      # Direct mappings
      account_id: "$.payload.data.account_id"
      amount: "$.payload.data.amount"
      
      # With default values
      currency:
        source: "$.payload.data.currency"
        default: "USD"
        
      # Computed fields
      is_high_value:
        $expr:
          $gt: ["$.payload.data.amount", 1000000]
```

#### Code Transformation

For complex transformations, use a code handler:

```yaml
transformation:
  type: code
  code_ref: "trigger-handlers/fraud-dispute-handler"
  
  # Handler receives:
  # - signal: The normalized signal DTO
  # - context: Tenant, subscription, workbench context
  # Handler returns:
  # - Request Mutation DTO
```

Example handler (JavaScript):

```javascript
// trigger-handlers/fraud-dispute-handler.js
export function transform(signal, context) {
  const payload = signal.payload.data;
  
  // Calculate priority based on amount and customer segment
  let priority = "medium";
  if (payload.amount > 1000000) priority = "high";
  if (payload.customer_segment === "VIP") priority = "urgent";
  
  // Determine if expedited handling needed
  const isExpedited = payload.dispute_reason === "FRAUD" && 
                      payload.amount > 500000;
  
  return {
    request_type: "BusinessRequest",
    scenario_id: "fraud-dispute-resolution",
    priority: priority,
    
    subject: {
      type: "customer",
      id: payload.customer_id
    },
    
    object: {
      type: "transaction", 
      id: payload.transaction_id
    },
    
    payload: {
      dispute_reason: payload.dispute_reason,
      transaction_id: payload.transaction_id,
      disputed_amount: payload.amount,
      dispute_date: signal.signal_header.timestamp,
      customer_id: payload.customer_id,
      is_expedited: isExpedited,
      calculated_priority: priority
    }
  };
}
```

### Trigger Action Types

| Action | Description | Use Case |
|--------|-------------|----------|
| `create_new` | Always creates a new Request | One-time events, reports |
| `update_existing` | Updates existing Request only | Status updates, follow-ups |
| `create_or_update` | Creates if no match, updates if found | Most common — handles both initiation and updates |

### Correlation Configuration

Correlation determines how to find existing Requests for updates:

```yaml
correlation:
  # Simple key - single field
  key_expression: "$.payload.data.transaction_id"
  
  # Compound key - multiple fields
  # key_expression: "$.payload.data.customer_id + '-' + $.payload.data.account_id"
  
  # Lookup strategy
  strategy: UPDATE_OR_CREATE  # UPDATE_OR_CREATE | UPDATE_ONLY | CREATE_ONLY
  
  # Match scope
  scope:
    workbench_id: true  # Match within same workbench
    scenario_id: true   # Match within same scenario
    status:
      $in: ["ACTIVE", "PENDING"]  # Only match non-terminal requests
```

---

## Step 4: Configure Trigger Settings

### Priority and Ordering

```yaml
trigger:
  id: "trg-high-priority-fraud"
  
  # Trigger priority (higher = processed first when multiple triggers match)
  priority: 100
  
  # Ordering within same priority
  order: 1
  
  # Stop processing other triggers if this one matches
  exclusive: true
```

### Trigger Conditions

Add additional conditions beyond the Signal Definition:

```yaml
trigger:
  id: "trg-business-hours-only"
  
  signal_definition_id: "sig-def-api-request"
  
  # Additional runtime conditions
  conditions:
    - type: time_window
      start: "09:00"
      end: "17:00"
      timezone: "America/New_York"
      days: ["MON", "TUE", "WED", "THU", "FRI"]
      
    - type: feature_flag
      flag: "new-dispute-flow-enabled"
      
    - type: expression
      expr: "$.context.workbench.settings.accept_new_disputes == true"
```

### Error Handling

```yaml
trigger:
  id: "trg-with-error-handling"
  
  error_handling:
    on_transformation_error:
      action: log_and_skip  # log_and_skip | fail_signal | fallback_trigger
      fallback_trigger_id: "trg-default-handler"  # If action = fallback_trigger
      
    on_request_creation_error:
      action: retry
      max_retries: 3
      backoff: exponential
      
    dead_letter:
      enabled: true
      queue: "trigger-errors-dlq"
```

---

## Step 5: Test Your Configuration

### Signal Simulator

Test your Signal Definitions and Triggers using the built-in simulator:

```
Workbench Studio → [Workbench] → Signals → Simulator
```

#### Simulate a Signal

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "signal_id": "test-sig-001",
    "signal_type": "payment_event",
    "timestamp": "2026-01-06T10:00:00Z"
  },
  "payload": {
    "content_type": "application/json",
    "data": {
      "transaction_id": "txn-12345",
      "dispute_reason": "FRAUD",
      "amount": 1500000,
      "customer_id": "cust-67890"
    }
  }
}
```

#### Simulator Output

```
Signal Simulation Results
─────────────────────────────────────────────────────────────────────────────

Signal ID: test-sig-001
Signal Type: payment_event

Matching Signal Definitions:
  ✅ sig-def-fraud-dispute (Fraud Dispute)
  ✅ sig-def-high-value-dispute (High Value Dispute Signal)
  ❌ sig-def-merchandise-dispute (filter: dispute_reason ≠ "NOT_RECEIVED")

Triggered:
  ✅ trg-fraud-dispute-resolution
     → Scenario: fraud-dispute-resolution
     → Action: create_or_update
     → Correlation Key: txn-12345
     → Would CREATE new Request (no existing match)

Generated Request Preview:
  {
    "request_type": "BusinessRequest",
    "scenario_id": "fraud-dispute-resolution",
    "priority": "high",
    "subject": { "type": "customer", "id": "cust-67890" },
    "object": { "type": "transaction", "id": "txn-12345" },
    "payload": {
      "dispute_reason": "FRAUD",
      "transaction_id": "txn-12345",
      "disputed_amount": 1500000,
      "dispute_date": "2026-01-06T10:00:00Z",
      "customer_id": "cust-67890"
    }
  }
```

### Trigger Debugging

Enable debug mode for detailed logs:

```yaml
trigger:
  id: "trg-fraud-dispute-resolution"
  
  debug:
    enabled: true
    log_signal: true
    log_transformation: true
    log_output: true
    retention_days: 7
```

---

## Complete Configuration Examples

### Example 1: Event-Driven Dispute Resolution

**Scenario:** Automatically create dispute cases when card network events arrive.

```yaml
# Signal Type
signal_type:
  id: "card-network-dispute"
  source_gateway: atropos
  source_topic: "card-network.disputes"

# Signal Definition
signal_definition:
  id: "sig-def-visa-dispute"
  signal_type_id: "card-network-dispute"
  filter:
    metadata:
      source_system:
        $in: ["visa-network", "mastercard-network"]
    payload:
      data:
        dispute_type:
          $in: ["CHARGEBACK", "PRE_ARB", "ARB"]

# Trigger
trigger:
  id: "trg-visa-dispute"
  signal_definition_id: "sig-def-visa-dispute"
  scenario_id: "card-dispute-resolution"
  action: create_or_update
  
  correlation:
    key_expression: "$.payload.data.arn"  # Acquirer Reference Number
    
  transformation:
    type: low_code
    mapping:
      request_type: "BusinessRequest"
      priority: 
        $switch:
          - case: { $gt: ["$.payload.data.amount", 5000000] }
            then: "urgent"
          - case: { $gt: ["$.payload.data.amount", 1000000] }
            then: "high"
          - default: "medium"
            
      subject:
        type: "customer"
        id: "$.payload.data.cardholder_id"
        
      object:
        type: "transaction"
        id: "$.payload.data.transaction_id"
        
      payload_mapping:
        arn: "$.payload.data.arn"
        dispute_type: "$.payload.data.dispute_type"
        amount: "$.payload.data.amount"
        reason_code: "$.payload.data.reason_code"
        merchant_name: "$.payload.data.merchant.name"
        due_date: "$.payload.data.response_due_date"
```

### Example 2: API-Initiated Self-Service

**Scenario:** Allow customers to submit disputes via API.

```yaml
# Signal Type
signal_type:
  id: "customer-dispute-api"
  source_gateway: heracles
  source_endpoint: "POST /api/v1/disputes"

# Signal Definition  
signal_definition:
  id: "sig-def-customer-dispute"
  signal_type_id: "customer-dispute-api"
  filter: {}  # Accept all valid API submissions

# Trigger
trigger:
  id: "trg-customer-dispute"
  signal_definition_id: "sig-def-customer-dispute"
  scenario_id: "customer-dispute-handling"
  action: create_new
  
  transformation:
    type: low_code
    mapping:
      request_type: "BusinessRequest"
      priority: "medium"
      
      subject:
        type: "customer"
        id: "$.context.authenticated_user_id"
        
      object:
        type: "transaction"
        id: "$.payload.data.transaction_id"
        
      payload_mapping:
        transaction_id: "$.payload.data.transaction_id"
        reason: "$.payload.data.reason"
        description: "$.payload.data.description"
        documents: "$.payload.data.supporting_documents"
        
  # Response configuration for synchronous API
  response:
    type: sync
    mapping:
      status: "$.request.status"
      request_id: "$.request.id"
      message: "Dispute submitted successfully"
```

### Example 3: Scheduled Batch Processing

**Scenario:** Process settlement files daily.

```yaml
# Signal Type
signal_type:
  id: "daily-settlement"
  source_gateway: kale
  schedule: "0 2 * * *"

# Signal Definition
signal_definition:
  id: "sig-def-daily-settlement"
  signal_type_id: "daily-settlement"
  filter: {}

# Trigger
trigger:
  id: "trg-daily-settlement"
  signal_definition_id: "sig-def-daily-settlement"
  scenario_id: "settlement-processing"
  action: create_new
  
  transformation:
    type: low_code
    mapping:
      request_type: "SystemRequest"  # No human subject
      priority: "low"
      
      payload_mapping:
        batch_date: "$.signal_header.timestamp"
        batch_type: "DAILY_SETTLEMENT"
```

### Example 4: File Upload Continuation

**Scenario:** Continue processing when customer uploads documents.

```yaml
# Signal Type
signal_type:
  id: "dispute-document-upload"
  source_gateway: dia
  file_pattern: "disputes/{request_id}/documents/*"

# Signal Definition
signal_definition:
  id: "sig-def-document-upload"
  signal_type_id: "dispute-document-upload"
  filter:
    payload:
      data:
        mime_type:
          $in: ["application/pdf", "image/jpeg", "image/png"]

# Trigger - Updates existing request
trigger:
  id: "trg-document-received"
  signal_definition_id: "sig-def-document-upload"
  scenario_id: "customer-dispute-handling"
  action: update_existing  # Only update, don't create new
  
  correlation:
    # Extract request_id from file path
    key_expression: "$.payload.data.file_path.match(/disputes\\/([^/]+)\\//)[1]"
    
  transformation:
    type: low_code
    mapping:
      update_type: "DOCUMENT_RECEIVED"
      
      payload_mapping:
        document_type: "$.payload.data.document_type"
        file_name: "$.payload.data.file_name"
        file_path: "$.payload.data.file_path"
        file_size: "$.payload.data.file_size"
        uploaded_at: "$.signal_header.timestamp"
```

---

## Configuration Checklist

```
□ Signal Types
  □ Identify all signal sources (events, APIs, files, schedules)
  □ Register signal types with payload schemas
  □ Document expected data structures

□ Signal Definitions
  □ Create filter for each signal type
  □ Define matching criteria
  □ Test filters with sample data

□ Triggers
  □ Link Signal Definitions to Scenarios
  □ Configure correlation keys
  □ Define transformations (low-code or code)
  □ Set priorities for overlapping triggers
  □ Configure error handling

□ Testing
  □ Use Signal Simulator for each signal type
  □ Verify Request payload generation
  □ Test correlation/update scenarios
  □ Validate error handling paths

□ Deployment
  □ Review trigger order and priorities
  □ Enable monitoring and alerting
  □ Document signal contracts for external systems
```

---

## Troubleshooting

### Common Issues

| Issue | Possible Cause | Resolution |
|-------|----------------|------------|
| Signal not triggering | Filter too restrictive | Relax filter conditions, check field names |
| Wrong trigger fires | Multiple matching triggers | Adjust priorities, use exclusive flag |
| Transformation fails | Invalid JSONPath | Verify path expressions in simulator |
| Duplicate requests created | Missing correlation | Add correlation key configuration |
| Updates not applied | Correlation key mismatch | Check key expression and existing data |

### Debug Checklist

1. **Verify signal format** — Is the signal in normalized DTO format?
2. **Check filter conditions** — Use simulator to test matching
3. **Validate JSONPath expressions** — Test paths against sample data
4. **Review correlation logic** — Ensure keys are consistent
5. **Check trigger priority** — Higher priority triggers execute first

---

## Related Documentation

- [Signal Exchange](../04-subsystems/signal-exchange/README.md) — Technical reference
- [Signal Provider Interactions](../04-subsystems/signal-exchange/signal-provider-interactions.md) — DTO formats
- [I/O Gateways](../04-subsystems/signal-providers/README.md) — Signal sources
- [Workbench Setup Guide](./workbench-setup-guide.md) — Complete workbench configuration
- [Scenario Development Journey](../08-personas-and-journeys/journeys/scenario-development.md) — End-to-end scenario setup


