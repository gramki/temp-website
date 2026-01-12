# Machine Signal Emission

> **Category:** Signal Architecture

---

## Overview

**Machine Signal Emission** is the mechanism by which Machines produce signals that Hub Scenarios/Applications perceive through Signal Providers (I/O Gateways). Machines can emit signals using push or pull models across multiple protocols.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Machine** as a deployed compute system that manages business entities and can emit or transform signals, and **Signal** as a message conveying information about an event or request. Machine Signal Emission is the implementation of how Machines produce signals for Hub processing.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Machine | Machine Instance with signal_emission configuration | Concrete machine that emits signals |
| Signal | Normalized Signal DTO | Signals emitted by Machines are normalized by Signal Providers |
| Sensor | Signal Provider (Hub ingress) | Signal Providers sense signals from Machines |

### Gap This Fills

The ontology describes Machines and Signals conceptually. Machine Signal Emission specifies:
1. **Mechanisms**: How Machines send signals (push vs pull)
2. **Protocols**: Which protocols are supported (Webhook, Atropos, SFTP)
3. **Configuration**: How Machines are configured to emit signals
4. **Flow**: The complete flow from Machine → Signal Provider → Signal Exchange

---

## Definition

**Machine Signal Emission** is the process by which Machines produce signals through Signal Providers (Hub ingress endpoints) for Hub Scenario/Application processing.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Per-machine instance configuration |
| **Lifecycle** | Tied to machine instance lifecycle |
| **Ownership** | Machine configuration managed by tenant admin or authorized developers |
| **Multiplicity** | Machines can emit through multiple providers simultaneously |

---

## Rationale

### Why This Design?

Machine Signal Emission enables:
1. **Protocol Diversity**: Support multiple protocols (Webhook, Atropos, SFTP) for different Machine capabilities
2. **Flexibility**: Both push and pull models accommodate various Machine constraints
3. **Consistent Processing**: Pull-to-push conversion ensures all signals processed with push semantics
4. **Scalability**: Hub-hosted topics enable reliable signal processing for pull model

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Single protocol only** | Too restrictive; doesn't accommodate diverse Machine capabilities |
| **Push-only model** | Machines without push capability cannot emit signals |
| **Pull-only model** | Real-time signals require push model |
| **Direct Machine-to-Signal Exchange** | Violates separation of concerns; no protocol abstraction |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0001](../../decision-logs/0001-signal-normalization.md) | Normalize signal format between SPs and SX |
| [ADR-0003](../../decision-logs/0003-signal-exchange-responsibility-boundaries.md) | Signal Exchange routes to Applications, not tasks or agents |
| [ADR-0103](../../decision-logs/0103-machine-signal-emission.md) | Machine Signal Emission Through Signal Providers |

---

## Structure

### Signal Emission Configuration

**Machine Definition (Abstract):**
```yaml
machine_definition:
  signal_emission:
    signals:
      - type: string
        push:
          protocols: [webhook, atropos_inbox, sftp]
          schemas:
            webhook: { openapi_spec: {...} }
            atropos_inbox: { openapi_schema: {...}, cloudevents_compliant: true }
            sftp: { file_format_spec: {...} }
        pull:
          protocols: [atropos_subscription, kafka_connect, sftp]
          schemas:
            atropos_subscription: { openapi_schema: {...}, cloudevents_compliant: true }
            kafka_connect: { openapi_schema: {...}, cloudevents_compliant: true }
            sftp: { schema: {...} }
```

**Machine Instance (Concrete):**
```yaml
machine:
  signal_emission:
    push:
      webhook:
        endpoint: string  # Workbench-scoped endpoint
        auth: { type: enum, credentials_ref: string }
      atropos_inbox:
        broker_endpoint: string
        topic: string
        auth: { type: enum, credentials_ref: string }
      sftp:
        server_endpoint: string
        folder_path: string
        auth: { type: enum, credentials_ref: string }
    pull:
      atropos_subscription:
        machine_broker: string
        machine_topic: string
        hub_topic: string  # Auto-provisioned
        auth: { type: enum, credentials_ref: string }
      kafka_connect:
        machine_broker: string
        machine_topic: string
        hub_topic: string
        connect_config: object
        auth: { type: enum, credentials_ref: string }
      sftp:
        machine_sftp: { endpoint: string, path: string, auth: {...} }
        hub_sftp: { endpoint: string, path: string, auth: {...} }
        polling: { schedule: string, file_filters: array }
```

### Hub Ingress Endpoint Patterns

Hub ingress endpoints follow this pattern:
```
/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}
```

**Examples:**
- Webhook: `https://heracles.olympus.tech/api/workbenches/payment-ops/signals`
- Atropos Topic: `/hub/acme-bank/prod-subscription/payment-ops/atropos/payment-events`
- SFTP: `sftp://dia.olympus.tech:22/inbound/settlements/payment-operations`

---

## Behavior

### Push Flow

```
Machine → Signal Provider (Hub Ingress) → Signal Exchange → Trigger → Scenario/Application
```

**Steps:**
1. Machine sends signal to Hub ingress endpoint (Webhook, Atropos Inbox, SFTP)
2. Signal Provider receives signal at Hub ingress endpoint
3. Signal Provider validates schema according to protocol requirements
4. Signal Provider normalizes to Signal Exchange DTO format
5. Signal Provider forwards to Signal Exchange
6. Signal Exchange processes signal (trigger evaluation, request creation)

### Pull Flow

```
Machine → Signal-Pulling App → Hub-Hosted Topic/Endpoint → Signal Provider → Signal Exchange → Trigger → Scenario/Application
```

**Steps:**
1. Signal-pulling application retrieves signal from Machine (subscribe, poll, connect)
2. Signal-pulling application queues signal to Hub-hosted topic/endpoint
3. Signal Provider processes from Hub-hosted resource (push semantics)
4. Signal Provider validates schema according to protocol requirements
5. Signal Provider normalizes to Signal Exchange DTO format
6. Signal Provider forwards to Signal Exchange
7. Signal Exchange processes signal (trigger evaluation, request creation)

### Pull-to-Push Conversion

All pull mechanisms follow a pull-to-push conversion pattern:
1. Hub pulls signals from Machine-provided endpoints/topics
2. Hub routes pulled signals to Hub-hosted topics/endpoints
3. Signals are then processed as push semantics (from Hub-hosted resources)
4. This ensures consistent signal processing regardless of original delivery method

**Hub-Hosted Topics:**
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Dedicated**: Each topic is dedicated to a machine instance
- **Auto-Provisioned**: Topics are auto-provisioned with machine instance
- **Lifecycle Management**: Tenant admin manages topic lifecycle
- **Tied to Instance**: Topic lifecycle is tied to machine instance lifecycle

---

## Constraints

| Constraint | Description |
|------------|-------------|
| **Provider Selection** | Provider selection is Machine's choice, outside Hub scope |
| **Multi-Provider** | Hub does not deduplicate signals from multiple providers |
| **Schema Validation** | Schema validation occurs at Signal Provider during normalization |
| **Endpoint Provisioning** | Hub ingress endpoints must be provisioned before use |
| **Workbench Scoping** | Hub ingress endpoints are per-workbench |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Protocol Diversity** | Support multiple protocols for different Machine capabilities |
| ✅ **Flexibility** | Both push and pull models accommodate various constraints |
| ✅ **Consistent Processing** | Pull-to-push conversion ensures uniform processing |
| ✅ **Scalability** | Hub-hosted topics enable reliable signal processing |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Configuration Complexity** | Clear documentation and examples |
| ⚠️ **Endpoint Management** | Provisioning workflow and lifecycle management |
| ⚠️ **No Deduplication** | By design; Machines control provider selection |

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Signal Exchange](./signal-exchange.md) | Receives normalized signals from Signal Providers |
| [I/O Gateway](./io-gateway.md) | Serves as Hub ingress endpoints for Machine signals |
| [Machine Registry](../../04-subsystems/registry-services/machine-registry.md) | Stores Machine signal emission configuration |
| [Signal-Pulling Applications](../../04-subsystems/hub-native-utilities/signal-pulling-applications.md) | Native Hub applications for pull model |

---

## References

- [Machine Registry](../../04-subsystems/registry-services/machine-registry.md) - Machine configuration
- [Signal Providers](../../04-subsystems/signal-providers/README.md) - Hub ingress endpoints
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md) - Configuration guide
- [ADR-0103](../../decision-logs/0103-machine-signal-emission.md) - Machine Signal Emission decision
