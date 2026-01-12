# Open Points: Machines Produce Signals

> **Status:** 🟡 Draft  
> **Purpose:** Summary of open questions and TBD items for Machine signal emission  
> **Source:** [machines-produce-signals.md](./machines-produce-signals.md)

---

## Summary

This document captures all open points, questions, and TBD items from the Machine signal emission documentation. Resolved items have been moved to the "Resolved Decisions" section below.

---

## Resolved Decisions

The following items have been resolved and incorporated into the documentation:

### 1.1 Multi-Provider Support
**Status:** ✅ Resolved

**Decision:** Machines can emit signals through multiple providers simultaneously. Hub does not deduplicate or acknowledge signals from multiple providers as the same or redundant. Each signal is processed independently.

### 1.2 Provider Selection Logic
**Status:** ✅ Resolved

**Decision:** Provider selection is the Machine's choice and is outside Hub's scope. Machines are represented in Hub, not defined in Hub (often external systems). The Machine decides which provider(s) to use based on its own logic and requirements.

### 1.3 Signal Schema Validation Location
**Status:** ✅ Resolved

**Decision:** Signal schema validation occurs at the Signal Provider during normalization. Each provider validates according to its protocol requirements (OpenAPI for Webhook, CloudEvents for Atropos, File Format Spec for SFTP).

### 2.1 Endpoint Scoping
**Status:** ✅ Resolved

**Decision:** 
- Hub ingress endpoints are subscription-scoped and per-workbench
- Endpoints are provisioned by tenant admin or authorized developers as resources when required
- Endpoint pattern: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`

### 2.2 Endpoint Authentication
**Status:** ✅ Resolved

**Decision:** Per-provider authentication mechanisms are used. Each Signal Provider has its own authentication requirements and mechanisms.

### 3.1 Hub-Hosted Topic/Endpoint Naming
**Status:** ✅ Resolved

**Decision:** 
- Hub-hosted topics/endpoints use pattern: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- Topics/endpoints are configured (not auto-generated)
- Topics are dedicated to machine instance

### 3.2 Automatic Conversion
**Status:** ✅ Resolved

**Decision:** Pull-to-push conversion is automatic when endpoints are appropriately provisioned and specified. Signal-pulling applications handle the conversion automatically.

### 3.3 Error Handling for Pull Operations
**Status:** ✅ Resolved

**Decision:** Sound defaults for error handling will be implemented. Specific error handling strategies will be defined per provider and pull mechanism.

### 4.1 Subscription Management
**Status:** ✅ Resolved

**Decision:** 
- Signal-pulling application registers as subscriber with Atropos using configured credentials
- Atropos manages all subscription aspects (consumer groups, offsets, etc.)
- Subscriber only needs to acknowledge processed messages

### 4.2 Hub-Hosted Topic Lifecycle
**Status:** ✅ Resolved

**Decision:** 
- Topic is dedicated to machine instance
- Topic is auto-provisioned with machine instance
- Tenant admin manages the topic lifecycle

### 5.1 Kafka Connect Integration
**Status:** ✅ Resolved

**Decision:** 
- Hub runs Kafka Connect connectors internally
- Connectors are provisioned with machine instance
- Connector lifecycle is tied to machine instance lifecycle

### 5.2 Schema Compatibility
**Status:** ✅ Resolved (TBD for implementation)

**Decision:** Schema transformation is kept as TBD in documentation. Transformation should be possible but not specified at this stage.

### 6.1 File Polling Mechanism
**Status:** ✅ Resolved

**Decision:** 
- Polling schedule is specified in the pull configuration
- Hub polls on a configurable schedule
- File filters are applied during poll

### 6.2 File Processing
**Status:** ✅ Resolved

**Decision:** 
- Files are pushed immediately after full read completion
- Processing of pushed files follows the push endpoint configuration

### 6.3 SFTP Pull Signal Schema
**Status:** ✅ Resolved

**Decision:** 
- Pull mechanism does not validate files
- Pull mechanism reads file fully, then pushes to Hub Dia SFTP
- File validation happens at the push endpoint (Hub Dia SFTP)

---

## 1. Architecture & Design Decisions

### 1.1 Multi-Provider Support
**Question:** Can a Machine emit signals through multiple providers simultaneously?

**Example Scenario:** Critical events via Atropos AND Heracles for redundancy

**Status:** ⬜ To Resolve

> Not acknowledged as same or redundant singals by Hub

---

### 1.2 Provider Selection Logic
**Question:** How does a Machine choose which provider to use?

**Options to Consider:**
- Configured per Machine instance?
- Determined by signal type?
- Based on environment/workbench?
- Automatic selection based on signal characteristics?

**Status:** ⬜ To Resolve

> This is the nature of Machine. The choice is made by machines is outside the scope of Hub. The machine is being represented in Hub not defined in Hub more often than not.

---

### 1.3 Signal Schema Validation Location
**Question:** Where does signal schema validation occur?

**Options:**
- At Machine (before emission)?
- At Signal Provider (during normalization)?
- At Signal Exchange (after normalization)?
- Multiple validation points?

**Status:** ⬜ To Resolve

> At Signal Provider

---

## 2. Hub Ingress Endpoints

### 2.1 Endpoint Scoping
**Questions:**
- Are Hub ingress endpoints tenant-scoped or subscription-scoped?
- Are endpoints per-workbench or shared?
- How are endpoints discovered/configured?

**Status:** ⬜ To Resolve

> subscription scoped
> per-workbench
> tenant admin provisions them as resources as when required or authorized developers can also provision them

---

### 2.2 Endpoint Authentication
**Question:** What authentication is required at Hub ingress?

**Considerations:**
- Per-provider authentication mechanisms
- Machine identity (SPIFFE)?
- API keys, OAuth, mTLS?

**Status:** ⬜ To Resolve

> Per-provider authentication mechanisms
---

## 3. Pull-to-Push Conversion

### 3.1 Hub-Hosted Topic/Endpoint Naming
**Questions:**
- How are Hub-hosted topics/endpoints named? 
  - Pattern: `hub.{workbench_id}.{machine_id}.{signal_type}`?
  - Other naming conventions?
- Are they auto-generated or can they be configured?
- Are they unique per Machine Instance or shared?

**Status:** ⬜ To Resolve

> They are configured. They have "/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}"

---

### 3.2 Automatic Conversion
**Question:** Is the pull-to-push conversion automatic (handled by signal-pulling applications) or does it require explicit configuration?

**Status:** ⬜ To Resolve

> automatic, provide the edpoints are appropriately provisioned and specified
---

### 3.3 Error Handling for Pull Operations
**Questions:**
- What happens if Hub cannot connect to Machine-provided endpoint?
- What happens if messages fail to queue to Hub-hosted topic?
- Retry logic and dead-letter handling?
- Alerting mechanisms?

**Status:** ⬜ To Resolve

> Invent sound defaults.
---

## 4. Atropos Subscription Pull

### 4.1 Subscription Management
**Questions:**
- How does Hub manage subscriptions to Machine-provided topics?
- Consumer group naming and management?
- Offset management (start from beginning, latest, or specific offset)?
- How to handle reconnection and offset recovery?

**Status:** ⬜ To Resolve

> The signal-pulling application registers as a subscriber with the credential configured
> Atropos subscription manages all the aspects. A subscriber need to just ack the messages processed.
---

### 4.2 Hub-Hosted Topic Lifecycle
**Questions:**
- Is the Hub-hosted topic created automatically when Machine Instance is configured?
- Who manages the Hub-hosted topic lifecycle (creation, deletion, cleanup)?
- Can multiple Machine Instances share the same Hub-hosted topic?
- Topic retention and cleanup policies?

**Status:** ⬜ To Resolve
> Topic is dedidcated to machine instance.
> Tenant admin manages the lifecycle. Auto provisioned with instance.
---

## 5. Kafka Connect Pull

### 5.1 Kafka Connect Integration
**Questions:**
- Does Hub run Kafka Connect connectors internally?
- Or does Hub use external Kafka Connect cluster?
- How are connectors configured and managed?
- Connector lifecycle management (create, update, delete)?

**Status:** ⬜ To Resolve

> Yes, internally. 
> Provisioned with machine instance. ties to machine instance lifecycle.
---

### 5.2 Schema Compatibility
**Questions:**
- Are there any schema transformations needed between Machine topic and Hub topic?
- Or is it pass-through with CloudEvents compliance?
- Schema registry integration?

**Status:** ⬜ To Resolve

> Keep it as a TBD in the documentation. Transformation should be possible but not specified at this stage.
---

## 6. SFTP Pull

### 6.1 File Polling Mechanism
**Questions:**
- How frequently does Hub poll Machine SFTP for new files?
- Does Hub monitor for file changes or poll on schedule?
- How are file naming patterns handled?
- File filtering and selection criteria?

**Status:** ⬜ To Resolve
> Specified in the pull config
> schedule
> configuration; filter applied on poll

---

### 6.2 File Processing
**Questions:**
- Are files processed immediately upon pull?
- Or are they queued for batch processing?
- What happens to files after they're uploaded to Hub Dia SFTP?
- File retention and cleanup policies?

**Status:** ⬜ To Resolve
> pushed immediately after completion of full
> processing of pushed files is as per the push endpoint config
---

### 6.3 SFTP Pull Signal Schema
**Question:** What is the signal schema for SFTP pull?

**Options:**
- File metadata only?
- File content (parsed according to file format spec)?
- Both metadata and content?

**Note:** Similar to SFTP Push protocol, should reference [File Format Specification](../../04-subsystems/signal-providers/dia/file-format-specification.md)

**Status:** ⬜ TBD - To be defined
> Pull doesn't validate the file. it just sees that the file is fully read and then it is pushed
---

## 7. Authentication & Authorization

### 7.1 Machine Endpoint Access
**Questions:**
- How are credentials for Machine-provided endpoints managed?
- Are credentials per-Machine Instance or shared?
- How are credentials rotated?
- Credential storage (Vault, secrets management)?

**Status:** ⬜ To Resolve

---

### 7.2 Hub Endpoint Access
**Questions:**
- Who can access Hub-hosted topics/endpoints?
- Are they workbench-scoped or tenant-scoped?
- Access control policies?
- Audit logging requirements?

**Status:** ⬜ To Resolve

---

### 7.3 Per-Provider Authentication
**Question:** How are Machine credentials managed for each provider?

**Options:**
- Per-provider credentials?
- Shared credentials?
- Machine identity (SPIFFE)?
- Hybrid approach?

**Status:** ⬜ To Resolve

---

## 8. Error Handling & Resilience

### 8.1 Signal Emission Failures
**Questions:**
- What happens if signal emission fails?
- Retry at Machine level?
- Dead letter queue?
- Alerting mechanisms?
- Failure notification to Machine?

**Status:** ⬜ To Resolve

---

### 8.2 Outbound Signals
**Question:** The documentation mentions Signal Providers can handle "outbound" signals. How do Machines receive responses/updates?

**Options:**
- Via same provider (bidirectional)?
- Via different mechanism?
- Webhook callbacks?
- Polling for responses?

**Status:** ⬜ To Resolve

---

## 9. Signal-Pulling Applications

### 9.1 Application Inventory
**Status:** ⬜ To Document

**Applications to Document:**
- REST API Poller
- Database Poller
- File Watcher
- Message Queue Consumer
- Webhook Receiver
- GraphQL Query
- gRPC Client
- Event Bus Subscriber
- SFTP Poller
- Change Data Capture (CDC)

**For Each Application, Document:**
- Pull mechanism details
- Configuration schema
- Use cases
- Examples

---

### 9.2 Application Characteristics
**Questions:**
- Configurable polling intervals?
- Filtering and transformation capabilities?
- Error handling and retry logic?
- Rate limiting to avoid overwhelming source Machines?
- Signal normalization to Signal Exchange format?
- Observability (metrics, logs, traces)?

**Status:** ⬜ To Elaborate

---

## 10. Documentation Updates

### 10.1 Machine Registry Documentation
**Status:** ⬜ To Update

**Required Updates:**
- Add "Signal Emission Configuration" section
- Document `signal_emission` configuration schema
- Provide examples for each provider type
- Link to Signal Providers documentation

---

### 10.2 Signal Providers Documentation
**Status:** ⬜ To Update

**Required Updates:**
- Enhance "Architectural Role" section
- Add explicit statement: "Machines emit signals through Signal Providers"
- Show Machine → Signal Provider flow diagram
- Clarify that Signal Providers are Machines themselves

---

### 10.3 Machine Definition Schema
**Status:** ⬜ To Update

**Required Updates:**
- Add `signal_emission` fields to Machine Definition schema
- Add `signal_emission` fields to Machine Instance schema
- Update example configurations

---

### 10.4 Integration Guide
**Status:** ⬜ To Create

**Required Content:**
- "Configuring Machine Signal Emission" guide
- Step-by-step for each provider
- Common patterns
- Troubleshooting

---

### 10.5 Signal Provider Examples
**Status:** ⬜ To Add

**Required:**
- Add examples to each Signal Provider documentation
- Show Machine → Signal Provider integration
- Configuration examples

---

## 11. Implementation Tasks

### 11.1 Schema Design
**Status:** ⬜ To Design

**Tasks:**
- Design `signal_emission` schema for Machine Definition
- Design `signal_emission` schema for Machine Instance
- Design signal schema formats for each protocol
- Design file format specification integration

---

### 11.2 Signal-Pulling Applications
**Status:** ⬜ To Design

**Tasks:**
- Design signal-pulling application architecture
- Design application configuration schemas
- Design pull-to-push conversion mechanism
- Design error handling and retry logic

---

## Priority Classification

### High Priority (Remaining)
1. **Authentication & Authorization Details** (7.1, 7.2, 7.3) - Security requirement (specific mechanisms to be detailed)
2. **Error Handling Defaults** (8.1, 8.2) - Resilience requirement (specific defaults to be defined)

### Medium Priority (Remaining)
1. **Signal-Pulling Application Details** (9.1, 9.2) - Feature completeness (additional applications to be documented)

### Low Priority (Remaining)
1. **Documentation Updates** (10.x) - Can be done incrementally (most updates completed)
2. **Implementation Tasks** (11.x) - Follows design decisions

---

## Next Steps

1. ⬜ **Resolve High Priority Items** - Architecture team review
2. ⬜ **Design Schemas** - Based on resolved decisions
3. ⬜ **Elaborate Pull Mechanisms** - Complete SFTP pull specification
4. ⬜ **Document Signal-Pulling Applications** - List and describe each application
5. ⬜ **Update Formal Documentation** - Machine Registry, Signal Providers docs
6. ⬜ **Create Integration Guide** - Step-by-step configuration guide

---

## Related Documentation

- [Machines Produce Signals (Main Document)](./machines-produce-signals.md)
- [Machine Registry](../04-subsystems/registry-services/machine-registry.md)
- [Signal Providers](../04-subsystems/signal-providers/README.md)
- [File Format Specification](../04-subsystems/signal-providers/dia/file-format-specification.md)
