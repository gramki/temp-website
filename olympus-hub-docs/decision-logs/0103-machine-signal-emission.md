# ADR-0103: Machine Signal Emission Through Signal Providers

## Status

Accepted

## Date

2026-01-15

## Context

Machines in the Hub Environment need to emit signals to Hub for Scenario processing. The current Machine Registry documentation indicates that Machines can produce signals (`capabilities.produces_signals: true`) and defines signal schemas, but it does not explain:

1. **How** Machines emit signals (what mechanism/protocol)
2. **Which** Signal Providers (I/O Gateways) Machines can use
3. **How** Machines are configured to emit through specific Signal Providers
4. **The flow** from Machine → Signal Provider → Signal Exchange

Additionally, we need to support:
- Multiple protocols (Webhook, Atropos, SFTP)
- Both push and pull models for signal delivery
- Various Machine capabilities and constraints

### Example Use Cases

1. **Payment Switch** — Emits payment events via Atropos Event Bus for real-time processing
2. **Customer Portal** — Sends dispute submissions via HTTP Webhook to Heracles
3. **Settlement System** — Uploads batch files via SFTP to Dia for daily processing
4. **External Payment System** — Hub subscribes to external Kafka topic via Atropos Subscription
5. **Legacy System** — Hub polls legacy system's SFTP for files via SFTP Poller

### Challenge

Without a clear specification:
- Developers understand Machines *can* produce signals, but not *how* to configure or use this capability
- No standardized way to configure signal emission across different protocols
- Ambiguity about push vs pull models and when to use each
- Unclear endpoint provisioning and authentication mechanisms

### Question

How should Machines emit signals to Hub, and what mechanisms should Hub support for receiving signals from Machines?

## Decision

**Machines emit signals through Signal Providers (I/O Gateways), which serve as Hub ingress endpoints.** Signal Providers normalize signals and forward them to Signal Exchange for trigger evaluation.

### Push Model

Machines actively send signals to Hub ingress endpoints:

| Protocol | Signal Provider | Description |
|----------|----------------|-------------|
| **Webhook** | Heracles | HTTP POST to gateway endpoint |
| **Atropos Inbox** | Atropos | Publish events to Event Bus topic (CloudEvents v1.0) |
| **SFTP** | Dia | Upload files to SFTP endpoint |

### Pull Model

Hub uses signal-pulling applications (native Hub applications) to retrieve signals from Machines:

| Protocol | Signal Provider | Signal-Pulling Application |
|----------|----------------|---------------------------|
| **Atropos Subscription** | Atropos | Atropos Subscriber |
| **Kafka Connect** | Atropos | Kafka Connect Puller |
| **SFTP Poll** | Dia | SFTP Poller |

### Hub Ingress Endpoints

Hub ingress endpoints are:
- **Scoped**: Subscription-scoped and per-workbench
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Provisioning**: Provisioned by tenant admin or authorized developers as resources when required
- **Authentication**: Per-provider authentication mechanisms

### Signal Schema Validation

**Signal schema validation occurs at the Signal Provider during normalization:**
- **Webhook (Heracles)**: Validates against OpenAPI specification for POST request body
- **Atropos Inbox**: Validates CloudEvents v1.0 compliance
- **SFTP (Dia)**: Validates file format specification (CSV/TSV/Fixed-Width)

### Pull-to-Push Conversion

All pull mechanisms follow a **pull-to-push conversion pattern**:
1. Hub pulls signals from Machine-provided endpoints/topics
2. Hub routes pulled signals to Hub-hosted topics/endpoints
3. Signals are then processed as push semantics (from Hub-hosted resources)
4. This ensures consistent signal processing regardless of original delivery method

**Hub-hosted topics:**
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Dedicated**: Each topic is dedicated to a machine instance
- **Auto-Provisioned**: Topics are auto-provisioned with machine instance
- **Lifecycle Management**: Tenant admin manages topic lifecycle (creation, deletion, cleanup)
- **Tied to Instance**: Topic lifecycle is tied to machine instance lifecycle

### Multi-Provider Support

Machines can emit signals through multiple providers simultaneously. **Hub does not deduplicate or acknowledge signals from multiple providers as the same or redundant.** Each signal is processed independently.

### Provider Selection

Provider selection is the Machine's choice and is outside Hub's scope. Machines are represented in Hub, not defined in Hub (often external systems). The Machine decides which provider(s) to use based on its own logic and requirements.

### Machine Registry Configuration

Machine Registry supports `signal_emission` configuration in both Machine Definition and Machine Instance:

**Machine Definition** (abstract):
- Signal schemas per protocol (OpenAPI, CloudEvents, File Format Spec)
- Supported push/pull protocols per signal type

**Machine Instance** (concrete):
- Concrete endpoint configurations
- Authentication credentials
- Protocol-specific settings

## Consequences

### Positive

- **Clear Configuration Model**: Standardized way to configure Machine signal emission across all protocols
- **Flexibility**: Support for both push and pull models accommodates various Machine capabilities
- **Protocol Diversity**: Multiple protocols (Webhook, Atropos, SFTP) support different integration patterns
- **Consistent Processing**: Pull-to-push conversion ensures all signals processed with push semantics
- **Scalability**: Hub-hosted topics enable reliable signal processing

### Negative

- **Complexity**: Multiple protocols and models increase configuration complexity
- **Endpoint Management**: Requires endpoint provisioning workflow and lifecycle management
- **Signal-Pulling Applications**: Need to develop and maintain native Hub applications for pull model
- **Schema Validation**: Each provider must implement protocol-specific validation

### Neutral

- **Machine Choice**: Provider selection is outside Hub scope (may require Machine-side documentation)
- **Multi-Provider**: No deduplication means potential duplicate processing (by design)

## Related ADRs

- [ADR-0001](./0001-signal-normalization.md) - Normalize signal format between Signal Providers and Signal Exchange
- [ADR-0003](./0003-signal-exchange-responsibility-boundaries.md) - Signal Exchange routes to Applications, not tasks or agents

## Implementation Notes

### Machine Registry Schema

Machine Registry must support `signal_emission` configuration:
- Machine Definition: Signal schemas and supported protocols
- Machine Instance: Concrete endpoint configurations and credentials

### Signal Providers Documentation

Signal Providers must document:
- Hub ingress endpoint patterns and provisioning
- Machine signal emission configuration examples
- Protocol-specific schema requirements

### Signal-Pulling Applications

Native Hub applications needed:
- Atropos Subscriber (for Atropos subscription pull)
- Kafka Connect Puller (for Kafka Connect pull)
- SFTP Poller (for SFTP pull)
- Additional applications as needed (REST API Poller, Database Poller, etc.)

### Endpoint Provisioning

Workflow required for:
- Tenant admin provisioning Hub ingress endpoints
- Authorized developer provisioning endpoints
- Endpoint lifecycle management

## References

- [Machine Registry](../04-subsystems/registry-services/machine-registry.md)
- [Signal Providers](../04-subsystems/signal-providers/README.md)
- [Machine Signal Emission Guide](../10-guides/machine-signal-emission-guide.md)
- [Signal-Pulling Applications](../04-subsystems/hub-native-utilities/signal-pulling-applications.md)
