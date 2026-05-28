# Foundry Platform Admin Web App

**Application scope:** Super-admin interface for managing the entire Foundry Platform — Foundry creation, infrastructure monitoring, and platform-level settings.

## Purpose

The Platform Admin Web App is a dedicated interface for **foundry-platform-admin** users who manage the Foundry Platform itself. Unlike the Foundry Web App (used by Foundry members and Foundry Admins), this application provides platform-wide visibility and control.

This separation ensures that platform-level operations — which affect all Foundries — are performed through a distinct interface with appropriate access controls.

## Relationship to Foundry Web App

| Aspect | Platform Admin Web App | Foundry Web App |
|--------|------------------------|-----------------|
| **Audience** | Platform administrators | Foundry members, admins |
| **URL** | `admin.foundry.example.com` | `{foundry-slug}.foundry.example.com` |
| **Scope** | All Foundries | Single Foundry |
| **Authentication** | Platform admin via Olympus Cipher | Foundry-federated via Olympus Cipher |
| **Access** | Highly restricted | Foundry-scoped |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Foundry Platform                                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Platform Admin Web App (admin.foundry.example.com)                  │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │  • Dashboard (platform health)                               │    │    │
│  │  │  • Foundries (list, create, manage)                          │    │    │
│  │  │  • Infrastructure (DB instances, storage)                    │    │    │
│  │  │  • Platform Settings                                         │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │  Used by: foundry-platform-admin                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐  │
│  │ Foundry Web App A   │  │ Foundry Web App B   │  │ Foundry Web App C   │  │
│  │ acme.foundry...     │  │ corp.foundry...     │  │ dev.foundry...      │  │
│  │ (Foundry members)   │  │ (Foundry members)   │  │ (Foundry members)   │  │
│  └─────────────────────┘  └─────────────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Capabilities

### Foundry Lifecycle Management

- Create new Foundries
- View all Foundries across the platform
- Monitor Foundry health and onboarding status
- Archive or delete Foundries
- Resend admin invitations

### Infrastructure Monitoring

- View PostgreSQL instance health
- Monitor storage usage per Foundry
- Track resource allocation and quotas
- View system-wide metrics

### Platform Configuration

- Manage global platform settings
- Configure default quotas for new Foundries
- Manage platform-level integrations (e.g., GitHub App)

## Application Pages

| Page | Purpose |
|------|---------|
| [Dashboard](pages/dashboard.md) | Platform health overview, alerts |
| [Foundries](pages/foundries.md) | List and create Foundries |
| [Foundry Detail](pages/foundry-detail.md) | Single Foundry management |
| [Infrastructure](pages/infrastructure.md) | Database and storage monitoring |
| [Platform Settings](pages/platform-settings.md) | Global configuration |

## Personas

| Persona | Description |
|---------|-------------|
| [Platform Admin](personas/platform-admin/README.md) | foundry-platform-admin user managing the platform |

## Technology Stack

The Platform Admin Web App follows the same technology choices as Foundry Web App for consistency:

| Layer | Technology |
|-------|------------|
| Framework | React with TypeScript |
| Routing | React Router |
| State | React Query for server state |
| Styling | Tailwind CSS |
| Components | Shared component library with Foundry Web App |
| Auth | Olympus Cipher OAuth 2.0 |

## Authentication

Platform admins authenticate via Olympus Cipher:

1. Admin navigates to `admin.foundry.example.com`
2. Redirect to Olympus Cipher for authentication
3. Cipher validates admin is in `foundry-platform-admin` group
4. Return to Platform Admin app with access token
5. App validates token on each request

If user is not in the `foundry-platform-admin` group, access is denied.

## Authorization

All actions require the `foundry-platform-admin` role. The app does not have fine-grained permissions — if you can access the app, you have full platform admin capabilities.

| Action | Required |
|--------|----------|
| View dashboard | `foundry-platform-admin` |
| Create Foundry | `foundry-platform-admin` |
| Archive Foundry | `foundry-platform-admin` |
| Delete Foundry | `foundry-platform-admin` |
| View infrastructure | `foundry-platform-admin` |
| Modify platform settings | `foundry-platform-admin` |

## Security Considerations

- **Separate deployment** — Platform Admin app is deployed separately from Foundry Web Apps
- **Network isolation** — Consider placing behind VPN or IP allowlist
- **Audit logging** — All actions are logged to platform audit trail
- **No direct database access** — All operations go through Platform APIs
- **Session timeout** — Shorter session duration than Foundry Web App

## API Endpoints

The Platform Admin Web App consumes Platform Management APIs:

| API | Purpose |
|-----|---------|
| `GET /api/v1/admin/foundries` | List all Foundries |
| `POST /api/v1/admin/foundries` | Create Foundry |
| `GET /api/v1/admin/foundries/{id}` | Get Foundry details |
| `PATCH /api/v1/admin/foundries/{id}` | Update Foundry |
| `DELETE /api/v1/admin/foundries/{id}` | Delete Foundry |
| `GET /api/v1/admin/infrastructure` | Get infrastructure status |
| `GET /api/v1/admin/settings` | Get platform settings |
| `PATCH /api/v1/admin/settings` | Update platform settings |

## Read Next

- [pages/dashboard.md](pages/dashboard.md) — Dashboard page specification
- [pages/foundries.md](pages/foundries.md) — Foundries page specification
- [personas/platform-admin/README.md](personas/platform-admin/README.md) — Platform Admin persona
- [../management/foundry-management/README.md](../management/foundry-management/README.md) — Foundry Management subsystem
- [../foundry-web-app/README.md](../foundry-web-app/README.md) — Foundry Web App (for comparison)
