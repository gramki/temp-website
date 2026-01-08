# Agent Lifecycle API

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Agent Lifecycle Service](./agent-lifecycle-service.md)

---

## Overview

The Agent Lifecycle API provides programmatic access to manage Raw Agents, Training Specs, and Employment Specs throughout their lifecycle. This API is used by:

- **CI/CD pipelines** — Publishing Raw Agents, validating Training Specs
- **Hub Operators** — Creating Employment Specs during Scenario Deployment
- **Admin UIs** — Managing agent lifecycle states
- **Kill Switch** — Emergency suspension/revocation

---

## API Endpoints

### Base URL

```
https://seer-api.olympus.io/v1
```

---

## Raw Agent Management

### Register Raw Agent

```http
POST /raw-agents
```

Registers a new Raw Agent container image.

**Request:**
```json
{
  "name": "fraud-analyst-base",
  "version": "2.4.1",
  "image": {
    "registry": "registry.olympus.io",
    "repository": "seer/agents/fraud-analyst",
    "tag": "v2.4.1",
    "digest": "sha256:abc123..."
  },
  "capabilities": {
    "modalities": ["text", "structured-data"],
    "protocols": ["http", "grpc"],
    "frameworks": ["strands"]
  },
  "health": {
    "liveness": "/health/live",
    "readiness": "/health/ready"
  },
  "metadata": {
    "description": "Base fraud analyst agent",
    "owner": "platform-team",
    "repository": "https://github.com/zeta/fraud-analyst-agent"
  }
}
```

**Response:**
```json
{
  "id": "raw-fraud-analyst-base-2.4.1",
  "name": "fraud-analyst-base",
  "version": "2.4.1",
  "state": "registered",
  "createdAt": "2026-01-08T10:00:00Z",
  "imageDigest": "sha256:abc123..."
}
```

### List Raw Agents

```http
GET /raw-agents?name={name}&state={state}
```

### Get Raw Agent

```http
GET /raw-agents/{id}
```

### Update Raw Agent State

```http
PATCH /raw-agents/{id}/state
```

**Request:**
```json
{
  "state": "deployed",
  "reason": "Passed security scan"
}
```

**Valid State Transitions:**
```
registered → deployed → running → retired
```

---

## Training Spec Management

### Create Training Spec

```http
POST /training-specs
```

Creates a new Training Spec (Draft state).

**Request:**
```json
{
  "name": "fraud-analyst-v2",
  "namespace": "acme-disputes",
  "spec": {
    "rawAgent": {
      "name": "fraud-analyst-base",
      "version": "^2.0.0"
    },
    "context": {
      "identity": {
        "displayName": "Fraud Case Analyst",
        "role": "case-analyst",
        "domain": "disputes"
      }
    },
    "behavioral": {
      "systemPrompt": "You are a Fraud Case Analyst..."
    },
    "guardrails": {
      "refs": [
        {"name": "pii-protection", "version": "^1.0.0"}
      ]
    },
    "tools": {
      "protocols": [
        {"protocol": "temenos-t24/get-transactions", "alias": "get_transactions"}
      ]
    },
    "memory": {
      "agentMemory": {
        "stores": [
          {"name": "case-dialog", "type": "conversation"}
        ]
      }
    }
  }
}
```

**Response:**
```json
{
  "id": "ts-fraud-analyst-v2-1.0.0",
  "name": "fraud-analyst-v2",
  "namespace": "acme-disputes",
  "version": "1.0.0",
  "state": "drafted",
  "createdAt": "2026-01-08T10:00:00Z"
}
```

### Validate Training Spec

```http
POST /training-specs/{id}/validate
```

Runs sandbox validation tests.

**Request:**
```json
{
  "scenarios": ["standard-fraud-case", "edge-case-high-value"],
  "timeout": 300
}
```

**Response:**
```json
{
  "validationId": "val-123",
  "state": "validated",
  "results": {
    "passed": 5,
    "failed": 0,
    "scenarios": [
      {
        "name": "standard-fraud-case",
        "result": "passed",
        "duration": 45
      }
    ]
  },
  "completedAt": "2026-01-08T10:05:00Z"
}
```

### Publish Training Spec

```http
POST /training-specs/{id}/publish
```

Publishes a validated Training Spec (makes it available for Employment).

**Request:**
```json
{
  "approver": "disputes-lead",
  "comment": "Approved after review"
}
```

**Response:**
```json
{
  "id": "ts-fraud-analyst-v2-1.0.0",
  "state": "published",
  "publishedAt": "2026-01-08T10:10:00Z",
  "approvedBy": "disputes-lead"
}
```

### List Training Specs

```http
GET /training-specs?namespace={ns}&state={state}&rawAgent={name}
```

### Get Training Spec

```http
GET /training-specs/{id}
```

### Archive Training Spec

```http
POST /training-specs/{id}/archive
```

Archives a Training Spec (no new Employments allowed).

---

## Employment Spec Management

### Create Employment Spec

```http
POST /employment-specs
```

Creates an Employed Agent (typically called by Hub Operator during Scenario Deployment).

**Request:**
```json
{
  "name": "fraud-analyst-emp-001",
  "namespace": "acme-disputes",
  "spec": {
    "training": {
      "ref": {
        "name": "fraud-analyst-v2",
        "namespace": "acme-disputes",
        "version": "1.7.0"
      }
    },
    "workScope": {
      "tenant": "acme",
      "workbench": "acme-disputes",
      "scenario": "dispute-resolution"
    },
    "delegation": {
      "model": "role",
      "role": {"name": "fraud-analyst"},
      "accountable": {
        "type": "user",
        "ref": "disputes-supervisor"
      }
    },
    "operationalEnv": {
      "toolBindings": [
        {
          "protocol": "temenos-t24/get-transactions",
          "alias": "get_transactions",
          "endpoint": "https://core.acme.bank/api/v1/transactions",
          "credentials": {
            "secretRef": {"name": "acme-core-banking-creds"}
          }
        }
      ],
      "memoryBindings": [
        {
          "name": "case-dialog",
          "workbenchStore": "disputes-conversation-store"
        }
      ]
    },
    "capacity": {
      "compute": {"replicas": 2, "cpu": "2", "memory": "4Gi"},
      "tokens": {"daily": 1000000}
    }
  }
}
```

**Response:**
```json
{
  "id": "es-fraud-analyst-emp-001",
  "name": "fraud-analyst-emp-001",
  "namespace": "acme-disputes",
  "state": "requested",
  "createdAt": "2026-01-08T10:00:00Z",
  "versions": {
    "raw": "2.4.1",
    "trained": "1.7.0",
    "employed": "1.0.0"
  }
}
```

### Approve Employment

```http
POST /employment-specs/{id}/approve
```

**Request:**
```json
{
  "approver": "disputes-supervisor",
  "comment": "Approved for production"
}
```

### Activate Employment

```http
POST /employment-specs/{id}/activate
```

Starts the Employed Agent pods in Atlantis.

**Response:**
```json
{
  "id": "es-fraud-analyst-emp-001",
  "state": "active",
  "activatedAt": "2026-01-08T10:02:00Z",
  "runtime": {
    "deploymentName": "fraud-analyst-emp-001-deployment",
    "replicas": 2,
    "endpoint": "https://fraud-analyst-emp-001.seer.olympus.svc"
  }
}
```

### Get Employment Status

```http
GET /employment-specs/{id}
```

**Response:**
```json
{
  "id": "es-fraud-analyst-emp-001",
  "state": "active",
  "runtime": {
    "availableReplicas": 2,
    "readyReplicas": 2,
    "pods": [
      {"name": "fraud-analyst-emp-001-abc123", "phase": "Running", "ready": true},
      {"name": "fraud-analyst-emp-001-def456", "phase": "Running", "ready": true}
    ]
  },
  "metrics": {
    "requestsToday": 150,
    "tokensUsedToday": 450000,
    "averageLatencyMs": 2500,
    "errorRate": 0.02
  }
}
```

### List Employment Specs

```http
GET /employment-specs?namespace={ns}&state={state}&workbench={wb}&scenario={sc}
```

---

## Lifecycle Actions

### Suspend Employment

```http
POST /employment-specs/{id}/suspend
```

Suspends an Employed Agent (retains authority, stops execution).

**Request:**
```json
{
  "reason": "Investigating anomalous behavior",
  "initiator": "security-team",
  "duration": 3600
}
```

### Resume Employment

```http
POST /employment-specs/{id}/resume
```

Resumes a suspended Employed Agent.

### Revoke Employment

```http
POST /employment-specs/{id}/revoke
```

Permanently revokes an Employed Agent (removes authority).

**Request:**
```json
{
  "reason": "Security incident response",
  "initiator": "security-team"
}
```

> **Note**: Revocation is permanent. A new Employment must be created to restore the agent.

---

## Kill Switch

Emergency kill switch for immediate suspension or revocation:

```http
POST /kill-switch
```

**Request:**
```json
{
  "targets": [
    {"type": "employment", "id": "es-fraud-analyst-emp-001"},
    {"type": "employment", "id": "es-fraud-analyst-emp-002"}
  ],
  "action": "suspend",
  "reason": "Security incident",
  "initiator": "security-team",
  "scope": "immediate"
}
```

**Response:**
```json
{
  "killSwitchId": "ks-2026-01-08-001",
  "action": "suspend",
  "targets": [
    {"id": "es-fraud-analyst-emp-001", "result": "suspended", "latencyMs": 150},
    {"id": "es-fraud-analyst-emp-002", "result": "suspended", "latencyMs": 180}
  ],
  "completedAt": "2026-01-08T15:30:00.350Z"
}
```

### Bulk Kill Switch by Filter

```http
POST /kill-switch/bulk
```

**Request:**
```json
{
  "filter": {
    "trainingSpec": "fraud-analyst-v2",
    "tenant": "acme"
  },
  "action": "suspend",
  "reason": "Critical vulnerability in training spec",
  "initiator": "security-team"
}
```

---

## Event Webhooks

Register for lifecycle events:

```http
POST /webhooks
```

**Request:**
```json
{
  "url": "https://hub.acme.io/seer-events",
  "events": [
    "employment.activated",
    "employment.suspended",
    "employment.revoked",
    "training.published",
    "training.archived"
  ],
  "filter": {
    "namespace": "acme-disputes"
  },
  "secret": "webhook-secret-123"
}
```

### Event Payload

```json
{
  "eventId": "evt-123",
  "eventType": "employment.activated",
  "timestamp": "2026-01-08T10:02:00Z",
  "resource": {
    "type": "EmploymentSpec",
    "id": "es-fraud-analyst-emp-001",
    "namespace": "acme-disputes"
  },
  "details": {
    "state": "active",
    "previousState": "approved"
  },
  "actor": {
    "type": "operator",
    "id": "seer-operator"
  }
}
```

---

## Error Responses

### Standard Error Format

```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "Training spec validation failed",
    "details": [
      {
        "field": "spec.guardrails.refs[0]",
        "error": "Referenced guardrail 'pii-protection' not found"
      }
    ],
    "requestId": "req-abc123"
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `NOT_FOUND` | 404 | Resource not found |
| `VALIDATION_FAILED` | 400 | Spec validation failed |
| `STATE_TRANSITION_INVALID` | 400 | Invalid state transition |
| `AUTHORIZATION_FAILED` | 403 | Insufficient permissions |
| `CONFLICT` | 409 | Resource conflict (e.g., version exists) |
| `QUOTA_EXCEEDED` | 429 | Rate/quota limit exceeded |
| `INTERNAL_ERROR` | 500 | Internal server error |

---

## Authentication

All API calls require authentication via:

- **Service Account Token** (for operators, CI/CD)
- **User Token** (for admin UIs)

```http
Authorization: Bearer <token>
```

Tokens are issued by **Cipher IAM** and include:
- Tenant context
- Namespace permissions
- Role claims

---

## SDK

### Python SDK

```python
from seer_sdk import LifecycleClient

client = LifecycleClient.from_environment()

# Create Training Spec
training = client.training_specs.create(
    name="fraud-analyst-v2",
    namespace="acme-disputes",
    spec={...}
)

# Validate
validation = client.training_specs.validate(training.id)

# Publish
client.training_specs.publish(training.id, approver="disputes-lead")

# Create Employment
employment = client.employment_specs.create(
    name="fraud-analyst-emp-001",
    namespace="acme-disputes",
    spec={...}
)

# Activate
client.employment_specs.activate(employment.id)

# Kill switch
client.kill_switch.suspend(
    targets=[employment.id],
    reason="Investigation"
)
```

---

## Related Documentation

- [Agent Lifecycle Service](./agent-lifecycle-service.md) — Conceptual model
- [Training Spec CRD](../hub-integration/training-spec-crd.md) — Full CRD schema
- [Employment Spec CRD](../hub-integration/employment-spec-crd.md) — Full CRD schema
- [Cipher IAM](../../../olympus-hub-docs/04-subsystems/supporting-systems/cipher-iam.md) — Authentication

---

*The Agent Lifecycle API provides full programmatic control over agent creation, deployment, and emergency response.*

