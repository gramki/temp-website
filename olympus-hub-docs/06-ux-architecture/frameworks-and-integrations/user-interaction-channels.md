# User Interaction Channels
//TODO: Why is this focused on just 'customers as subjects'?

> **Status:** ⚠️ Notes — Raw notes, needs structuring

## Overview

Hub requires User (Subject) Interaction Channels for successful modeling of Requests and Cases that require collaboration between Agents and the Subject(s).

**Subject** = The customer or account holder who is the focus of a Service Request or Case.

## Use Cases Requiring Subject Interaction

| Use Case | Subject Involvement |
|----------|---------------------|
| Fraud/Dispute Report | Subject provides transaction details, uploads evidence |
| KYC (Know Your Customer) | Subject submits documents, answers verification questions |
| Account Issues | Subject confirms details, authorizes actions |
| Service Requests | Subject tracks status, responds to queries |

## Integration Questions

- How to integrate Neutrino Channels to Olympus Hub?
- How to integrate Angelos Components into Neutrino Channels so that Subjects can handle Case and Request interactions?

## Workbench Environment Configuration

A Workbench has an Environment that defines:
- Allowed Subject Domain
- Sandboxes

## Subject Interaction Points

For each Case or Request, the Subject may receive:

| Interaction Type | Description |
|------------------|-------------|
| **Notification** | Status updates, alerts delivered to Subject |
| **Pending Task** | Action required from Subject to proceed |
| **Optional Actions** | CTAs available at various stages |

## Case/Request Specification

The Case/Request specification can include:
- **Notification Templates** — Pre-defined message templates for Subject communications
- **Hercules Launch URL RSD** — Declarative mechanism to create Launch URLs for Tasks and CTAs

## Hercules Launcher App

Hercules is an Angelos Component that creates launch URLs for deep-linking into Hub applications.

### Invocation Context

| Parameter | Description |
|-----------|-------------|
| **Sandbox** | Target sandbox environment |
| **Angelos Component** | UI component to render |
| **Invocation Parameters** | Data to initialize the component |
| **Authorization Context** (optional) | Subject JID + Invocation-specific-use Token |

### Launch URL Behavior

1. Hercules returns a launch URL for use in CTA buttons or notifications
2. When triggered, Hercules redirects user to appropriate domain if required
3. Renders target component initialized with invocation parameters
4. If Authorization Context provided:
   - URL becomes a **bearer URL** (like Google Docs "anyone with link")
   - Bound to specific Subject
   - Initializes page in pre-authenticated state

### Use Cases

| Context | Subject Type | Example |
|---------|--------------|---------|
| **Consumer** (Neutrino stack) | Customer/Account Holder | Dispute form, KYC upload |
| **Tenant Executive** (Ops Center, Product Center) | Internal User | Admin actions, reports |

The Sandbox and Subject to which the launch URL is bound determine whether it's for Consumer or Tenant Executive use.

### Scoping

- Hercules Launch App requests are scoped to a **Web Stack Subscription** of tenant
- Launch URL always belongs to a specific subscription of a specific tenant
- Associated Sandbox must belong to the same tenant

### Hercules Launch URL RSD

A declarative mechanism to create Launch URL Resources against:
- Tasks in a Request or Case specification
- CTAs (Call-to-Action) in a Request or Case specification

---

*TBD: Expand with detailed integration patterns, API specifications, and examples*

