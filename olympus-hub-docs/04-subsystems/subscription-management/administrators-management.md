# Administrators Management

> **Status:** 🔴 Stub — Placeholder for expansion

Manages tenant administrator accounts, roles, permissions, and access controls.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Manage tenant administrative access |
| **Scope** | Admin provisioning, roles, permissions, audit |
| **Integration** | Cipher IAM for authentication/authorization |

---

## Administrator Roles

| Role | Description | Scope |
|------|-------------|-------|
| **Subscription Owner** | Full control over subscription | Subscription-wide |
| **Tenant Admin** | Full control over tenant configuration | Tenant-wide |
| **Workbench Admin** | Manage specific workbenches | Workbench |
| **Resource Admin** | Manage resources and integrations | Resources |
| **User Admin** | Manage users and agents | Users |
| **Billing Admin** | Access billing and usage | Billing |
| **Security Admin** | Manage security settings | Security |
| **Audit Admin** | Access audit logs (read-only) | Audit |

---

## Role Permissions Matrix

| Permission | Owner | Tenant | Workbench | Resource | User | Billing | Security | Audit |
|------------|-------|--------|-----------|----------|------|---------|----------|-------|
| Manage subscription | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage admins | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage workbenches | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage resources | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manage users | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| View billing | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Manage security | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| View audit logs | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ |

(⚠️ = scoped to their area)

---

## Administrator Lifecycle

```
[Invited] → [Pending] → [Active] → [Suspended] → [Removed]
```

| State | Description |
|-------|-------------|
| **Invited** | Invitation sent |
| **Pending** | Invitation accepted, verification in progress |
| **Active** | Administrator active |
| **Suspended** | Temporarily suspended |
| **Removed** | Administrator removed |

---

## Administrator Provisioning

```yaml
administrator:
  id: "admin-12345"
  tenant_id: "acme-bank"
  
  identity:
    email: "john.smith@acme-bank.com"
    name: "John Smith"
    mfa_enabled: true
  
  roles:
    - role: "tenant_admin"
      scope: "tenant"
    - role: "workbench_admin"
      scope: "workbench:dispute-ops"
  
  access:
    ip_whitelist: ["10.0.0.0/8"]
    session_timeout: 8h
    require_mfa: true
  
  status: "active"
  created_at: "2026-01-01T00:00:00Z"
  last_login: "2026-01-04T09:30:00Z"
```

---

## Audit Trail

All administrator actions are logged:

| Event | Data Captured |
|-------|---------------|
| Login | Time, IP, device, MFA used |
| Configuration change | What changed, before/after |
| User management | Action, target user |
| Resource access | Resource, action, result |
| Permission change | Role, scope, granted/revoked |

---

## Security Features

| Feature | Description |
|---------|-------------|
| **MFA** | Required for sensitive operations |
| **IP Whitelisting** | Restrict access by IP |
| **Session Timeout** | Configurable session duration |
| **Concurrent Session Limit** | Limit simultaneous sessions |
| **Password Policy** | Configurable password requirements |
| **Login Alerts** | Notifications for suspicious logins |

---

## Related Documentation

- [Subscription Management Overview](./README.md)
- [Cipher IAM](../supporting-systems/cipher-iam.md)
- [Tenant Subscription Lifecycle](./tenant-subscription-lifecycle.md)

---

*TODO: Detailed design — SSO integration, delegation, emergency access*

