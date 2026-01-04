# Branding and Themes

> **Status:** 🔴 Stub — Placeholder for expansion

Manages tenant-specific customization, branding, and visual themes for the Hub user experience.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Enable tenant customization and white-labeling |
| **Scope** | Logos, colors, fonts, themes, labels |
| **Application** | Ops Center, Workbench Studio, Neutrino channels |

---

## Customization Areas

| Area | Elements |
|------|----------|
| **Branding** | Logo, favicon, app name, tagline |
| **Colors** | Primary, secondary, accent, background, text |
| **Typography** | Font families, sizes, weights |
| **Themes** | Light mode, dark mode, custom themes |
| **Labels** | Terminology customization |
| **Email Templates** | Notification email styling |

---

## Branding Configuration

```yaml
branding:
  tenant_id: "acme-bank"
  
  identity:
    app_name: "ACME Operations Hub"
    tagline: "Excellence in Banking Operations"
    logo:
      light: "https://cdn.acme-bank.com/logo-light.svg"
      dark: "https://cdn.acme-bank.com/logo-dark.svg"
    favicon: "https://cdn.acme-bank.com/favicon.ico"
  
  colors:
    primary: "#1E3A8A"       # ACME Blue
    secondary: "#3B82F6"
    accent: "#F59E0B"        # ACME Gold
    background: "#F8FAFC"
    text: "#1E293B"
    error: "#EF4444"
    success: "#22C55E"
    warning: "#F59E0B"
  
  typography:
    heading_font: "Inter"
    body_font: "Open Sans"
    mono_font: "JetBrains Mono"
  
  theme:
    default: "light"
    allow_user_preference: true
    custom_themes:
      - id: "acme-dark"
        name: "ACME Dark"
        colors: { ... }
```

---

## Label Customization

Tenants can customize terminology to match their domain:

```yaml
labels:
  tenant_id: "acme-bank"
  
  overrides:
    "Request": "Case"
    "Workbench": "Operations Center"
    "Signal": "Event"
    "Scenario": "Use Case"
    "Agent": "Analyst"
```

---

## White-Labeling

| Feature | Description |
|---------|-------------|
| **Full White-Label** | Complete removal of Hub branding |
| **Co-Branding** | Tenant branding with "Powered by Hub" |
| **Custom Domain** | Tenant's own domain (ops.acme-bank.com) |
| **Custom Emails** | Emails from tenant's domain |

---

## Theme Distribution

| Channel | Theme Application |
|---------|-------------------|
| **Ops Center** | Full theme support |
| **Workbench Studio** | Full theme support |
| **Agent Studio** | Full theme support |
| **Neutrino Channels** | Partial (customer-facing) |
| **Email Notifications** | Email template styling |
| **API Responses** | N/A |

---

## Related Documentation

- [Subscription Management Overview](./README.md)
- [UX Architecture](../../06-ux-architecture/README.md)

---

*TODO: Detailed design — theme builder UI, CSS variable system, preview*

