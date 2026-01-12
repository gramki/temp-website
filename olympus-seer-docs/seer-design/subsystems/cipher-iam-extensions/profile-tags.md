# Profile Tags

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Overview

Profile tags provide metadata and categorization for agent profiles at different lifecycle stages. This document describes the tag structure for Raw, Trained, and Employed Agent profiles.

---

## Tag Categories

### Standard Tag Categories

| Category | Purpose | Example |
|----------|---------|---------|
| **Identity** | Agent identification | `agent-code`, `subscription` |
| **Lifecycle** | Lifecycle stage | `type`, `status` |
| **Delegation** | Authority information | `delegator`, `accountable` |
| **Capability** | Agent capabilities | `models`, `tools` |
| **Operational** | Runtime metadata | `workbench`, `version` |

---

## Raw Agent Profile Tags

Raw Agents are templates and don't have full IAM profiles, but they do have metadata tags in the Foundry:

```yaml
# Raw Agent Metadata (Foundry)
rawAgent:
  id: "fraud-analyst-raw"
  tags:
    # Identity
    - key: "agent-type"
      value: "raw"
    - key: "agent-name"
      value: "Fraud Analyst"
    - key: "agent-version"
      value: "1.0.0"
    
    # Capability
    - key: "capability-category"
      value: "investigation"
    - key: "supported-models"
      value: "gpt-4o,claude-3-5-sonnet"
    - key: "supported-tools"
      value: "transaction-lookup,customer-profile"
    
    # Foundry
    - key: "foundry-source"
      value: "zeta-foundry"
    - key: "foundry-certified"
      value: "true"
```

### Raw Agent Tag Schema

| Tag Key | Required | Description |
|---------|----------|-------------|
| `agent-type` | Yes | Always `raw` |
| `agent-name` | Yes | Display name |
| `agent-version` | Yes | Semantic version |
| `capability-category` | Yes | Primary capability |
| `supported-models` | Yes | CSV of supported models |
| `supported-tools` | Yes | CSV of supported tools |
| `foundry-source` | Yes | Originating foundry |
| `foundry-certified` | No | Certification status |

---

## Trained Agent Profile Tags

Trained Agents have metadata in the Foundry plus training-specific tags:

```yaml
# Trained Agent Metadata (Foundry)
trainedAgent:
  id: "fraud-analyst-trained-v2"
  rawAgentRef: "fraud-analyst-raw"
  tags:
    # Identity
    - key: "agent-type"
      value: "trained"
    - key: "agent-name"
      value: "Fraud Analyst v2"
    - key: "training-version"
      value: "2.0.0"
    
    # Training
    - key: "trained-by"
      value: "acme-training-team"
    - key: "training-date"
      value: "2026-01-10"
    - key: "base-raw-agent"
      value: "fraud-analyst-raw"
    - key: "base-raw-version"
      value: "1.0.0"
    
    # Capability (refined from raw)
    - key: "allowed-models"
      value: "gpt-4o"
    - key: "allowed-tools"
      value: "transaction-lookup,customer-profile,fraud-rules"
    
    # Constraints
    - key: "max-concurrent-requests"
      value: "10"
    - key: "authority-ceiling"
      value: "standard"
```

### Trained Agent Tag Schema

| Tag Key | Required | Description |
|---------|----------|-------------|
| `agent-type` | Yes | Always `trained` |
| `agent-name` | Yes | Display name |
| `training-version` | Yes | Training version |
| `trained-by` | Yes | Training team/user |
| `training-date` | Yes | Date of training |
| `base-raw-agent` | Yes | Source raw agent |
| `base-raw-version` | Yes | Version of raw agent |
| `allowed-models` | Yes | CSV of allowed models |
| `allowed-tools` | Yes | CSV of allowed tools |
| `max-concurrent-requests` | No | Request limit |
| `authority-ceiling` | No | Authority constraints |

---

## Employed Agent Profile Tags

Employed Agents have full IAM profiles with comprehensive tags:

```yaml
# Employed Agent Profile (Cipher IAM)
employedAgent:
  profileId: "fraud-analyst-acme-retail"
  tags:
    # Identity
    - key: "agent-type"
      value: "employed"
    - key: "agent-code"
      value: "fraud-analyst-acme-retail"
    - key: "spiffe-id"
      value: "spiffe://acme.hub.io/seer/agent/acme-seer-subscription/fraud-analyst-acme-retail"
    
    # Lifecycle
    - key: "status"
      value: "active"
    - key: "deployed-at"
      value: "2026-01-12T10:00:00Z"
    - key: "profile-version"
      value: "3"
    
    # Training Reference
    - key: "training-spec"
      value: "fraud-analyst-trained-v2"
    - key: "training-version"
      value: "2.0.0"
    
    # Delegation
    - key: "delegation-type"
      value: "user"
    - key: "delegator"
      value: "user:john.smith@acme.com"
    - key: "accountable"
      value: "user:jane.manager@acme.com"
    
    # Authority
    - key: "inherited-roles"
      value: "fraud-reviewer,dispute-handler"
    - key: "inherited-groups"
      value: "disputes-team,fraud-analysts"
    
    # Operational
    - key: "subscription"
      value: "acme-seer-subscription"
    - key: "workbench"
      value: "acme-disputes"
    - key: "namespace"
      value: "acme-disputes"
    
    # Credentials
    - key: "virtual-key-id"
      value: "vk_acme_fraud_analyst_retail_001"
    - key: "token-secret-ref"
      value: "fraud-analyst-acme-retail-secrets"
```

### Employed Agent Tag Schema

| Tag Key | Required | Description |
|---------|----------|-------------|
| `agent-type` | Yes | Always `employed` |
| `agent-code` | Yes | Unique agent code |
| `spiffe-id` | Yes | SPIFFE identity |
| `status` | Yes | Profile status |
| `deployed-at` | Yes | Deployment timestamp |
| `profile-version` | Yes | Profile version number |
| `training-spec` | Yes | Training spec reference |
| `delegation-type` | Yes | `user`, `role`, or `bot` |
| `delegator` | Conditional | Required if not bot |
| `accountable` | Yes | Accountable human |
| `inherited-roles` | Yes | CSV of inherited roles |
| `inherited-groups` | Yes | CSV of inherited groups |
| `subscription` | Yes | Seer subscription |
| `workbench` | Yes | Workbench ID |
| `virtual-key-id` | Yes | Virtual key identifier |

---

## Tag Lifecycle

### Tag Updates

| Event | Tag Changes |
|-------|-------------|
| **Profile Created** | All tags set |
| **Delegation Updated** | Delegation/authority tags updated |
| **Authority Re-resolved** | `inherited-roles`, `inherited-groups` updated |
| **Profile Revoked** | `status` set to `revoked` |

### Tag Versioning

Profile version is incremented on any tag change:

```yaml
- key: "profile-version"
  value: "3"  # Incremented from 2
- key: "last-updated"
  value: "2026-01-12T14:30:00Z"
```

---

## Tag Queries

### Find Agents by Tag

```http
GET /v1/agents/profiles?tag=workbench:acme-disputes
```

### Common Query Patterns

| Query | Tag Filter |
|-------|------------|
| All agents in workbench | `workbench:acme-disputes` |
| All active agents | `status:active` |
| All agents by delegator | `delegator:user:john.smith@acme.com` |
| All bot mode agents | `delegation-type:bot` |

---

## Related Documentation

- [Architecture](./architecture.md) — Profile types overview
- [Agent Profile API](./agent-profile-api.md) — API for profile management
- [Authority Delegation](./authority-delegation.md) — Delegation tags

---

*Profile Tags provide comprehensive metadata for agent identification, lifecycle tracking, and operational management.*
