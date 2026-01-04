# Hercules Launcher

> **Status:** 🔴 Stub — Placeholder for expansion

**Hercules Launcher** is a deep-linking service that generates Launch URLs for Hub applications, enabling direct access to specific pages, tasks, and actions.

---

## Overview

Hercules enables:
- **Bearer URLs** — Pre-authenticated access (like "anyone with link")
- **Subject-Bound URLs** — Scoped to specific customer/subject
- **CTA Generation** — Dynamic links in notifications and emails
- **Cross-Channel Access** — Same URL works in web, email, mobile

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         HERCULES LAUNCHER                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INPUT                              │  OUTPUT                                │
│  ├── Sandbox (tenant/workbench)     │  ├── Launch URL                       │
│  ├── Angelos Component/Page         │  │   • Bearer token embedded          │
│  ├── Invocation Parameters          │  │   • Time-limited validity          │
│  └── Authorization Context          │  │   • Subject-bound (optional)       │
│      ├── Subject JID                │  └── Metadata                         │
│      └── Invocation Token           │      • Expiry                         │
│                                     │      • Scope                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Use Cases

### 1. Task Notification Links

When a task is assigned, include a direct link to the task solver:

```
Subject: New Task Assigned - Verify KYC Documents

A new task has been assigned to you.

[Open Task] ← Hercules Launch URL
```

### 2. Customer Self-Serve Links

Send customers links to complete subject tasks:

```
Subject: Action Required - Submit Additional Documents

Please upload the requested documents.

[Upload Documents] ← Hercules Launch URL (subject-bound)
```

### 3. Request Status Links

Share request status with stakeholders:

```
Request REQ-1234 has been updated.

[View Status] ← Hercules Launch URL
```

---

## URL Types

### Bearer URL

Pre-authenticated URL that grants access without separate login.

| Attribute | Description |
|-----------|-------------|
| **Access** | Anyone with the link can access |
| **Token** | Embedded bearer token |
| **Expiry** | Time-limited (configurable) |
| **Scope** | Limited to specific action/view |

### Subject-Bound URL

URL scoped to a specific subject (customer).

| Attribute | Description |
|-----------|-------------|
| **Access** | Only the specified subject |
| **Verification** | Subject must authenticate |
| **Context** | Pre-loaded with subject data |

### Authenticated URL

URL requiring standard authentication.

| Attribute | Description |
|-----------|-------------|
| **Access** | Requires login |
| **Context** | Parameters passed via URL |
| **Scope** | User's normal permissions apply |

---

## Launch URL Specification

### Request Specification Document (RSD)

Declarative mechanism to define Launch URL generation:

```yaml
launch_url_rsd:
  id: task-completion-link
  component: task-solver
  
  parameters:
    task_id: "{{task.id}}"
    request_id: "{{request.id}}"
    mode: "solve"
  
  authorization:
    type: bearer
    expiry: "PT24H"  # 24 hours
    scopes:
      - "task:read"
      - "task:complete"
  
  subject_binding:
    enabled: false
```

### Subject Task Link

```yaml
launch_url_rsd:
  id: customer-document-upload
  component: document-upload
  
  parameters:
    request_id: "{{request.id}}"
    document_type: "{{required_document}}"
  
  authorization:
    type: subject_bound
    subject_id: "{{subject.jid}}"
    expiry: "P7D"  # 7 days
  
  channel_hints:
    email: true
    sms: true
    push: true
```

---

## Integration Points

| Integration | Usage |
|-------------|-------|
| **Notification Service** | Generate links for notification CTAs |
| **Email Templates** | Embed links in emails |
| **Mobile Push** | Deep links in push notifications |
| **Task Management** | Task assignment notifications |
| **Signal Exchange** | Response links for async flows |

---

## Security Model

| Aspect | Mechanism |
|--------|-----------|
| **Token Generation** | Cryptographic signing |
| **Expiry Enforcement** | Server-side validation |
| **Subject Verification** | Identity check for bound URLs |
| **Audit** | All launches logged |
| **Revocation** | Tokens can be invalidated |

---

## Related Documentation

- [Angelos Framework](./angelos-framework.md)
- [Notification Services](../04-subsystems/subscription-management/README.md)
- [Neutrino Integration](./neutrino-integration.md)

---

*TODO: Detailed RSD schema, security implementation, channel-specific considerations*

