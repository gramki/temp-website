# Subscription Notifications

> **Status:** 🟡 WIP — Design Complete

Notifications for tenant subscription lifecycle events including renewals, usage alerts, and platform announcements.

---

## Notification Types

### Subscription Lifecycle

| Event | Recipients | When |
|-------|------------|------|
| **Renewal Reminder (90 days)** | Tenant Admin | 90 days before expiry |
| **Renewal Reminder (30 days)** | Tenant Admin | 30 days before expiry |
| **Renewal Reminder (7 days)** | Tenant Admin | 7 days before expiry |
| **Subscription Renewed** | Tenant Admin | Renewal processed |
| **Subscription Expired** | Tenant Admin | Subscription ends |

### Usage Alerts

| Event | Recipients | When |
|-------|------------|------|
| **Quota Warning (80%)** | Tenant Admin | 80% of quota used |
| **Quota Warning (90%)** | Tenant Admin | 90% of quota used |
| **Quota Exceeded** | Tenant Admin | Quota limit reached |
| **Usage Anomaly** | Tenant Admin | Unusual usage detected |

### Platform Announcements

| Event | Recipients | When |
|-------|------------|------|
| **Scheduled Maintenance** | All affected | Before maintenance window |
| **Maintenance Complete** | All affected | After maintenance |
| **New Feature Available** | All tenants | Feature released |
| **Policy Update** | Tenant Admins | Policy changes |
| **Terms Update** | Tenant Admins | Terms of service changes |

---

## Notification Templates

### Example: Renewal Reminder

```
Subject: Subscription Renewal Reminder - {days} days remaining

Your Hub subscription is due for renewal.

Subscription: {subscription_name}
Expiry Date: {expiry_date}
Days Remaining: {days}

Please contact your Hub representative to discuss renewal.

[Contact Support] [View Subscription]
```

### Example: Quota Warning

```
Subject: Usage Alert - {quota_type} at {percentage}%

Your {quota_type} usage has reached {percentage}% of your limit.

Current Usage: {current_usage}
Limit: {limit}
Remaining: {remaining}

Consider upgrading your plan or optimizing usage.

[View Usage] [Upgrade Plan]
```

---

## Related Documentation

- [Platform Notifications README](./README.md)
- [Subscription Management](../subscription-management/README.md)

