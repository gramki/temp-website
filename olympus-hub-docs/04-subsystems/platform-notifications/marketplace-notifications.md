# Marketplace Notifications

> **Status:** 🟡 WIP — Design Complete

Notifications for Marketplace events including publishing, subscriptions, updates, and security issues.

---

## Notification Types

### Publishing Notifications

| Event | Recipients | When |
|-------|------------|------|
| **Publisher Registration Approved** | Tenant Admin | Hub Win approves registration |
| **Publisher Registration Rejected** | Tenant Admin | Hub Win rejects registration |
| **Package Published** | Developer, Admin | Package clears security scan |
| **Package Rejected** | Developer, Admin | Package fails validation/scan |
| **Package Deprecated** | Subscribers | Publisher deprecates package |
| **Package Withdrawn** | Subscribers | Publisher/admin withdraws package |

### Subscription Notifications

| Event | Recipients | When |
|-------|------------|------|
| **Subscription Request** | Tenant Admin | User requests subscription |
| **Subscription Approved** | Requester | Admin approves |
| **Subscription Rejected** | Requester | Admin rejects |
| **BlueprintSpecs Available** | Developer | Subscription activated |
| **Unsubscription Pending** | Developer | Unsubscription initiated |
| **Unsubscription Complete** | Developer | All derived resources removed |

### Update Notifications

| Event | Recipients | When |
|-------|------------|------|
| **New Version Available** | All subscribers | Publisher releases new version |
| **Update Applied** | Developer | Derived resource updated |
| **Out-of-Sync Warning** | Developer | Resources behind latest version |
| **Orphaned Resources** | Developer | Blueprint withdrawn |

### Security Notifications

| Event | Recipients | When |
|-------|------------|------|
| **Vulnerability Detected** | Publisher, Subscribers | Security scan finds issue |
| **Package Blacklisted** | Subscribers | Package blocked |
| **Security Advisory** | Affected parties | Critical issue discovered |

---

## Notification Templates

### Example: New Version Available

```
Subject: New Version Available - {package_name}

A new version of {package_name} is available.

Current Version: {current_version}
New Version: {new_version}

What's New:
{release_notes}

Compatibility: {compatibility_status}

[View Details] [Update Now]
```

### Example: Security Vulnerability

```
Subject: [Security] Vulnerability in {package_name}

A security vulnerability has been detected in a package you use.

Package: {package_name}
Version: {affected_version}
Severity: {severity}

Description:
{vulnerability_description}

Recommended Action:
{recommended_action}

[View Details] [Update Package]
```

---

## Related Documentation

- [Platform Notifications README](./README.md)
- [Marketplace Security](../marketplace/security-and-compliance.md)
- [Version Management](../marketplace/version-management.md)

