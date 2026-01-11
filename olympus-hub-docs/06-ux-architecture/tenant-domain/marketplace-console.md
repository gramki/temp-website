# Marketplace Console

> **Status:** 🟡 WIP — Design Complete

The Marketplace Console is a **unified UI** for all Marketplace operations, accessible from multiple desks within Hub Studio.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Unified interface for Marketplace operations |
| **Access** | Agent Developer Desk, Scenario Design Desk, Automation Product Desk, Admin Desk |
| **Personas** | Developer, Process Architect, Product Manager, Tenant Admin |
| **Functions** | Discovery, Subscription, Publishing, Notifications, Administration |

---

## Access Points

The Marketplace Console is accessible from multiple desks:

| Desk | Access Method | Primary Use Case |
|------|---------------|------------------|
| **Agent Developer Desk** | Main navigation | Package publishing, BlueprintSpec usage |
| **Scenario Design Desk** | Main navigation | Scenario BlueprintSpec discovery |
| **Automation Product Desk** | Main navigation | Package discovery, subscription initiation |
| **Hub Control Center** | Admin navigation | Publisher management, subscription authorization |

---

## Console Sections

### 1. Discovery

Browse and search available packages.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MARKETPLACE CONSOLE - DISCOVERY                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  🔍 Search packages...                                                  │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  Browse: [All] [By Publisher] [By Category] [By Industry]                   │
│                                                                              │
│  Filters:                          Results:                                  │
│  ┌───────────────────┐             ┌────────────────────────────────────┐   │
│  │ Artifact Types    │             │ ┌──────────────────────────────┐ │   │
│  │ ☐ Scenarios       │             │ │ Dispute Operations Suite     │ │   │
│  │ ☐ Workbenches     │             │ │ v1.2.0 • ACME Bank          │ │   │
│  │ ☐ Tools           │             │ │ ★★★★☆ • 2 Scenarios         │ │   │
│  │ ☐ Machines        │             │ └──────────────────────────────┘ │   │
│  ├───────────────────┤             │ ┌──────────────────────────────┐ │   │
│  │ Categories        │             │ │ Payment Processing Kit       │ │   │
│  │ ☐ Dispute Res.    │             │ │ v2.0.0 • Partner Corp        │ │   │
│  │ ☐ Payments        │             │ │ ★★★★★ • 4 Scenarios         │ │   │
│  │ ☐ Customer Svc    │             │ └──────────────────────────────┘ │   │
│  ├───────────────────┤             │                                    │   │
│  │ Publisher         │             │ Sort: [Relevancy ▼] [Recency]      │   │
│  │ ☐ ACME Bank       │             │                                    │   │
│  │ ☐ Partner Corp    │             │ Showing 1-10 of 45 packages        │   │
│  └───────────────────┘             └────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Capabilities:**
- Full-text search across package names, descriptions, keywords
- Multi-select filters for artifact types, categories, industries
- Browse by publisher, category, or industry
- Sort by relevancy or recency
- Click-through to package detail pages

---

### 2. Package Details

View complete information about a package.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MARKETPLACE CONSOLE - PACKAGE DETAILS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ← Back to Search                                                            │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                                                                          ││
│  │  📦 Dispute Operations Suite                             [Subscribe]    ││
│  │  by ACME Bank • v1.2.0 • Published 2026-01-15                           ││
│  │                                                                          ││
│  │  Complete dispute resolution automation including triage and            ││
│  │  resolution scenarios with trained agents.                              ││
│  │                                                                          ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  [Overview] [Blueprints] [Version History] [Documentation]                   │
│                                                                              │
│  BLUEPRINTS INCLUDED:                                                        │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  📄 dispute-triage (ScenarioBlueprintSpec)                              ││
│  │  📄 dispute-resolution (ScenarioBlueprintSpec)                          ││
│  │  🔧 card-network-lookup (ToolBlueprintSpec)                             ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  PUBLISHER INFO:                    CATEGORIES:                              │
│  ACME Bank                          • dispute-resolution                     │
│  contact@acme.com                   • customer-service                       │
│  www.acme.com/hub-packages          Industry: financial-services             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 3. Subscription

Manage package subscriptions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MARKETPLACE CONSOLE - SUBSCRIPTIONS                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  MY SUBSCRIPTIONS                                                            │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                                                                          ││
│  │  📦 Dispute Operations Suite                                            ││
│  │  v1.2.0 → v1.3.0 available • Workbench: dispute-ops-dev                 ││
│  │  Status: Active • Subscribed: 2026-01-10                                ││
│  │                                                                          ││
│  │  [View Blueprints] [Update] [Unsubscribe]                               ││
│  │                                                                          ││
│  ├─────────────────────────────────────────────────────────────────────────┤│
│  │                                                                          ││
│  │  📦 Payment Processing Kit                                              ││
│  │  v2.0.0 • Workbench: payments-dev                                       ││
│  │  Status: Active • Subscribed: 2025-12-15                                ││
│  │                                                                          ││
│  │  [View Blueprints] [Unsubscribe]                                        ││
│  │                                                                          ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  PENDING REQUESTS                                                            │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  📦 Fraud Detection Suite • Awaiting admin approval                     ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Capabilities:**
- View all active subscriptions
- See update availability
- Initiate updates
- Request unsubscription
- Track pending requests

---

### 4. Authorization (Admin View)

Approve subscription requests and manage policies.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MARKETPLACE CONSOLE - AUTHORIZATION (Admin)                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PENDING APPROVALS                                                           │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                                                                          ││
│  │  📦 Fraud Detection Suite                                               ││
│  │  Requested by: john.doe@tenant.com                                      ││
│  │  Target: fraud-ops-dev workbench                                        ││
│  │  Requested: 2026-01-11 09:30                                            ││
│  │                                                                          ││
│  │  [View Package] [Approve] [Reject]                                      ││
│  │                                                                          ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  PUBLISHER POLICIES                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  Mode: [Allow list ▼]                                                   ││
│  │                                                                          ││
│  │  Allowed Publishers:                                                    ││
│  │  ✓ ACME Bank                                                            ││
│  │  ✓ Partner Corp                                                         ││
│  │  ✓ Trusted Vendor                                                       ││
│  │  [+ Add Publisher]                                                      ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 5. Package Creation

Create Package Manifest CRDs for publishing.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MARKETPLACE CONSOLE - PACKAGE CREATION                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CREATE NEW PACKAGE MANIFEST                                                 │
│                                                                              │
│  Package Name: ___________________________                                   │
│  Version: ____________                                                       │
│  Short Description: ________________________________________________         │
│                                                                              │
│  INCLUDED BLUEPRINTS:                                                        │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  ☑ dispute-triage (ScenarioNormativeSpec)                               ││
│  │  ☑ dispute-resolution (ScenarioNormativeSpec)                           ││
│  │  ☐ payment-processing (ScenarioNormativeSpec)                           ││
│  │  ☑ card-network-lookup (ToolDefinitionSpec)                             ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  VISIBILITY:                                                                 │
│  ○ Public  ○ Restricted  ○ Private                                          │
│                                                                              │
│  CATEGORIES: [dispute-resolution] [customer-service] [+]                     │
│                                                                              │
│  [Save Draft] [Create Package Manifest]                                      │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 6. Publishing

Publish packages and track status.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MARKETPLACE CONSOLE - PUBLISHING                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  MY PACKAGES                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  📦 Dispute Operations Suite v1.2.0           Published                 ││
│  │      Subscribers: 12 • Last updated: 2026-01-15                         ││
│  │      [View] [New Version] [Deprecate]                                   ││
│  ├─────────────────────────────────────────────────────────────────────────┤│
│  │  📦 Dispute Operations Suite v1.3.0           Pending Approval          ││
│  │      Submitted: 2026-01-11 • Awaiting admin approval                    ││
│  │      [View] [Cancel]                                                    ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  READY TO PUBLISH                                                            │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  📦 Payment Toolkit v1.0.0                    Draft                     ││
│  │      Last modified: 2026-01-10                                          ││
│  │      [Edit] [Publish]                                                   ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 7. Notifications

View Marketplace-related notifications.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MARKETPLACE CONSOLE - NOTIFICATIONS                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  🔵 NEW VERSION AVAILABLE                               Today 10:30    ││
│  │  Dispute Operations Suite v1.3.0 is now available                       ││
│  │  [View] [Update Now]                                                    ││
│  ├─────────────────────────────────────────────────────────────────────────┤│
│  │  🟢 SUBSCRIPTION APPROVED                               Yesterday      ││
│  │  Fraud Detection Suite subscription approved                            ││
│  │  [View Package]                                                         ││
│  ├─────────────────────────────────────────────────────────────────────────┤│
│  │  🟡 OUT-OF-SYNC RESOURCES                               2 days ago     ││
│  │  3 resources need Blueprint updates                                     ││
│  │  [View Resources]                                                       ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 8. Publisher Management (Admin View)

Manage publisher registration and policies.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MARKETPLACE CONSOLE - PUBLISHER MANAGEMENT (Admin)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PUBLISHER STATUS                                                            │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  Status: ✓ Registered Publisher                                        ││
│  │  Registered: 2025-06-15 • Approved by: Hub Win Team                     ││
│  │  Certificate: Valid until 2027-06-15                                    ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  PUBLISHED PACKAGES                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  • Dispute Operations Suite (3 versions) - 12 subscribers               ││
│  │  • Payment Toolkit (1 version) - 5 subscribers                          ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  PUBLISHER ALLOW/DISALLOW LIST                                               │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  Policy Mode: [Allow first, then deny ▼]                                ││
│  │                                                                          ││
│  │  Allow: [All]                                                           ││
│  │  Deny:  publisher-untrusted                                             ││
│  │                                                                          ││
│  │  [Edit Policy]                                                          ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [Marketplace Subsystem](../../04-subsystems/marketplace/README.md)
- [Agent Developer Desk](./automation-development-desk.md)
- [Scenario Design Desk](./scenario-design-desk.md)
- [Automation Product Desk](./automation-product-desk.md)
- [Hub Control Center](./hub-control-center.md)

