# Machine Signal Emission Configuration Guide

> **Status:** ✅ Complete  
> **Purpose:** Step-by-step guide for configuring Machine signal emission through Signal Providers

---

## Overview

This guide provides step-by-step instructions for configuring Machines to emit signals through Signal Providers (Hub ingress endpoints). Machines can emit signals using **push** or **pull** models across multiple protocols.

**Signal Flow:**
```
Machine → Signal Provider (Hub Ingress) → Signal Exchange → Trigger → Scenario/Application
```

---

## Prerequisites

Before configuring Machine signal emission:

1. **Machine Definition** must be created with `capabilities.produces_signals: true`
2. **Machine Instance** must be created and associated with a workbench
3. **Hub Ingress Endpoints** must be provisioned (by tenant admin or authorized developers)
4. **Signal Schemas** must be defined in Machine Definition

---

## Configuration Steps

### Step 1: Define Signal Schemas in Machine Definition

Define signal schemas for each signal type the Machine will emit:

```yaml
machine_definition:
  id: "payment-switch"
  capabilities:
    produces_signals: true
  
  signal_emission:
    signals:
      - type: "payment.authorized"
        push:
          protocols: [webhook, atropos_inbox]
          schemas:
            webhook:
              openapi_spec:
                type: object
                required: [payment_id, amount, customer_id]
                properties:
                  payment_id: { type: string }
                  amount: { type: number }
                  customer_id: { type: string }
                  timestamp: { type: string, format: date-time }
            atropos_inbox:
              openapi_schema:
                type: object
                required: [id, source, specversion, type, data]
                properties:
                  id: { type: string }
                  source: { type: string }
                  specversion: { type: string, enum: ["1.0"] }
                  type: { type: string }
                  data: { type: object }
              cloudevents_compliant: true
              cloudevents_spec_version: "1.0"
```

---

## Push Model Configuration

### Protocol 1: Webhook (Heracles)

**Use Case:** Real-time HTTP-based signal emission

**Step 1: Provision Hub Ingress Endpoint**

Tenant admin or authorized developer provisions webhook endpoint:

```yaml
webhook_endpoint:
  id: "payment-ops-signals"
  workbench_id: "payment-operations"
  subscription_id: "prod-subscription"
  tenant_id: "acme-bank"
  
  endpoint: "https://heracles.olympus.tech/api/workbenches/payment-operations/signals"
  
  auth:
    methods: [api_key]
    api_key:
      credentials_ref: "vault://secrets/payment-ops/webhook-key"
```

**Step 2: Configure Machine Instance**

```yaml
machine:
  id: "acme-payment-switch"
  definition_id: "payment-switch"
  workbench_id: "payment-operations"
  
  signal_emission:
    push:
      webhook:
        endpoint: "https://heracles.olympus.tech/api/workbenches/payment-operations/signals"
        method: POST
        auth:
          type: api_key
          credentials_ref: "vault://secrets/acme/payment-switch/webhook-key"
```

**Step 3: Machine Sends Signal**

Machine sends HTTP POST request:

```http
POST /api/workbenches/payment-operations/signals HTTP/1.1
Host: heracles.olympus.tech
Content-Type: application/json
X-API-Key: <api-key-from-vault>

{
  "payment_id": "pay_12345",
  "amount": 100.50,
  "customer_id": "cust_67890",
  "timestamp": "2026-01-15T10:30:00Z"
}
```

### Protocol 2: Atropos Inbox (Event Bus)

**Use Case:** Event-driven signal emission via Event Bus

**Step 1: Configure Machine Instance**

```yaml
machine:
  id: "acme-payment-switch"
  definition_id: "payment-switch"
  workbench_id: "payment-operations"
  
  signal_emission:
    push:
      atropos_inbox:
        broker_endpoint: "kafka://kafka.olympus.tech:9092"
        topic: "payment.events"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/acme/payment-switch/kafka-auth"
```

**Step 2: Machine Publishes Event**

Machine publishes CloudEvents v1.0 compliant event:

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "source": "payment-switch.acme.com",
  "specversion": "1.0",
  "type": "com.acme.payment.authorized",
  "datacontenttype": "application/json",
  "time": "2026-01-15T10:30:00Z",
  "data": {
    "payment_id": "pay_12345",
    "amount": 100.50,
    "customer_id": "cust_67890"
  }
}
```

### Protocol 3: SFTP (Dia)

**Use Case:** File-based batch signal emission

**Step 1: Define File Format Specification**

```yaml
machine_definition:
  id: "settlement-file-system"
  signal_emission:
    signals:
      - type: "settlement.file.ready"
        push:
          protocols: [sftp]
          schemas:
            sftp:
              file_format_spec:
                name: "settlement-file-v1"
                format: "csv"
                structure:
                  header:
                    rows: 1
                    fields:
                      - name: "file_type"
                        position: 0
                        type: "string"
                  body:
                    startRow: 2
                    schema:
                      fields:
                        - name: "transaction_id"
                          position: 0
                          type: "string"
                        - name: "amount"
                          position: 1
                          type: "decimal"
```

**Step 2: Provision Hub Dia SFTP Endpoint**

```yaml
sftp_endpoint:
  id: "settlement-ops-inbound"
  workbench_id: "settlement-operations"
  subscription_id: "prod-subscription"
  tenant_id: "acme-bank"
  
  endpoint: "sftp://dia.olympus.tech:22"
  path: "/inbound/settlements/settlement-operations"
  
  auth:
    type: api_key
    credentials_ref: "vault://secrets/settlement-ops/dia-sftp-key"
```

**Step 3: Configure Machine Instance**

```yaml
machine:
  id: "acme-settlement-files"
  definition_id: "settlement-file-system"
  workbench_id: "settlement-operations"
  
  signal_emission:
    push:
      sftp:
        server_endpoint: "sftp://dia.olympus.tech:22"
        folder_path: "/inbound/settlements/settlement-operations"
        auth:
          type: api_key
          credentials_ref: "vault://secrets/acme/settlement-files/dia-sftp-key"
        file_pattern: "settlement_*.csv"
```

**Step 4: Machine Uploads File**

Machine uploads file via SFTP to Hub Dia SFTP endpoint.

---

## Pull Model Configuration

### Protocol 1: Atropos Subscription

**Use Case:** Hub subscribes to Machine-provided Event Bus topic

**Step 1: Configure Machine Instance**

```yaml
machine:
  id: "external-payment-system"
  definition_id: "external-payment"
  workbench_id: "payment-operations"
  
  signal_emission:
    pull:
      atropos_subscription:
        machine_broker: "kafka://external-payment.acme.com:9092"
        machine_topic: "payment.events"
        hub_topic: "/hub/acme-bank/prod-subscription/payment-ops/atropos/external-payment-events"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/external-payment/kafka-auth"
```

**Step 2: Hub Provisions Signal-Pulling Application**

Hub automatically provisions Atropos Subscriber application:
- Registers as subscriber with Atropos
- Atropos manages subscription aspects
- Messages queued to Hub-hosted topic
- Hub-hosted topic dispatches to Signal Exchange

### Protocol 2: Kafka Connect

**Use Case:** Hub connects to Machine-provided Kafka via Kafka Connect

**Step 1: Configure Machine Instance**

```yaml
machine:
  id: "legacy-kafka-system"
  definition_id: "legacy-kafka"
  workbench_id: "transaction-operations"
  
  signal_emission:
    pull:
      kafka_connect:
        machine_broker: "kafka://legacy-system.acme.com:9092"
        machine_topic: "transactions"
        hub_topic: "/hub/acme-bank/prod-subscription/transaction-ops/atropos/legacy-kafka-transactions"
        connect_config:
          connector_class: "io.confluent.connect.kafka.KafkaSourceConnector"
        auth:
          type: sasl_scram
          credentials_ref: "vault://secrets/legacy-kafka/auth"
```

**Step 2: Hub Provisions Kafka Connect Connector**

Hub automatically provisions Kafka Connect connector:
- Internal Kafka Connect connector
- Provisioned with machine instance
- Tied to machine instance lifecycle

### Protocol 3: SFTP Poll

**Use Case:** Hub polls Machine SFTP for files

**Step 1: Configure Machine Instance**

```yaml
machine:
  id: "batch-file-system"
  definition_id: "batch-file"
  workbench_id: "settlement-operations"
  
  signal_emission:
    pull:
      sftp:
        machine_sftp:
          endpoint: "sftp://batch-files.acme.com:22"
          path: "/outbound/settlements"
          auth:
            type: username_password
            credentials_ref: "vault://secrets/batch-file/sftp-auth"
        hub_sftp:
          endpoint: "sftp://dia.olympus.tech:22"
          path: "/inbound/settlements/settlement-operations"
          auth:
            type: api_key
            credentials_ref: "vault://secrets/hub-dia/sftp-key"
        polling:
          schedule: "0 */5 * * * *"  # Every 5 minutes
          file_filters:
            - pattern: "settlement_*.csv"
              min_size: 1024
```

**Step 2: Hub Provisions SFTP Poller**

Hub automatically provisions SFTP Poller application:
- Polls Machine SFTP on schedule
- Applies file filters
- Reads file fully
- Uploads to Hub Dia SFTP immediately

---

## Common Patterns

### Pattern 1: Multi-Provider Support

Machines can emit signals through multiple providers simultaneously. Hub does not deduplicate signals—each signal is processed independently.

**Example:**
```yaml
machine:
  signal_emission:
    push:
      webhook:
        endpoint: "https://heracles.olympus.tech/api/workbenches/payment-ops/signals"
      atropos_inbox:
        broker_endpoint: "kafka://kafka.olympus.tech:9092"
        topic: "payment.events"
```

### Pattern 2: Provider Selection

Provider selection is the Machine's choice and is outside Hub's scope. Machines are represented in Hub, not defined in Hub (often external systems).

### Pattern 3: Endpoint Provisioning

Hub ingress endpoints are:
- **Subscription-scoped** and **per-workbench**
- **Naming Pattern**: `/hub/{tenant}/{subscription}/{workbench-id}/{signal-provider}/{name-slug}`
- **Provisioned by** tenant admin or authorized developers as resources

---

## Troubleshooting

### Connection Issues

**Problem:** Machine cannot connect to Hub ingress endpoint

**Solutions:**
1. Verify endpoint URL is correct
2. Check authentication credentials in Vault
3. Verify network connectivity
4. Check firewall rules

### Schema Validation Errors

**Problem:** Signals rejected due to schema validation failures

**Solutions:**
1. Verify signal payload matches OpenAPI/CloudEvents schema
2. Check required fields are present
3. Validate data types match schema
4. Review Signal Provider logs for specific validation errors

### Pull-to-Push Conversion Issues

**Problem:** Pulled signals not appearing in Signal Exchange

**Solutions:**
1. Verify Hub-hosted topic is provisioned
2. Check signal-pulling application status
3. Review application logs for errors
4. Verify Hub-hosted topic naming pattern

---

## Related Documentation

- [Machine Registry](../04-subsystems/registry-services/machine-registry.md) - Machine configuration schemas
- [Signal Providers](../04-subsystems/signal-providers/README.md) - Hub ingress endpoints
- [Atropos Event Bus](../04-subsystems/signal-providers/atropos-event-bus.md) - Event Bus configuration
- [Heracles API Gateway](../04-subsystems/signal-providers/heracles-api-gateway.md) - Webhook configuration
- [Dia File Gateway](../04-subsystems/signal-providers/dia-file-gateway.md) - SFTP configuration
- [Signal-Pulling Applications](../04-subsystems/hub-native-utilities/signal-pulling-applications.md) - Pull model applications

---

*Status: ✅ Complete*
