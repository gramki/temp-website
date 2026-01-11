# Hub CLI Installation Guide

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

Hub provides two command-line interfaces for developers:

| CLI | Purpose | Runs Where |
|-----|---------|------------|
| **`hubdev`** | Open and manage remote workspaces | Your local machine |
| **`hub`** | Build, deploy, and monitor | Inside remote workspace (auto-installed) |

You only need to install `hubdev` on your local machine. The `hub` CLI is pre-installed in all Hub-managed workspaces.

---

## Installing hubdev (Local Machine)

### macOS

```bash
# Using Homebrew
brew tap olympus/hubdev
brew install hubdev

# Verify installation
hubdev version
```

### Linux

```bash
# Using apt (Debian/Ubuntu)
curl -fsSL https://packages.olympus.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/olympus.gpg
echo "deb [signed-by=/usr/share/keyrings/olympus.gpg] https://packages.olympus.io/apt stable main" | sudo tee /etc/apt/sources.list.d/olympus.list
sudo apt update && sudo apt install hubdev

# Using yum (RHEL/CentOS)
sudo yum install -y hubdev

# Verify installation
hubdev version
```

### Windows

```powershell
# Using winget
winget install Olympus.HubDev

# Using Scoop
scoop bucket add olympus https://github.com/olympus/scoop-bucket
scoop install hubdev

# Verify installation
hubdev version
```

### Binary Download

Download pre-built binaries from the [Releases Page](https://github.com/olympus/hubdev-cli/releases).

---

## Initial Configuration

After installation, authenticate to your tenant:

```bash
# Login (opens browser for OAuth)
hubdev login

# Verify authentication
hubdev whoami
```

### Configuration File

hubdev stores configuration locally:

```yaml
# ~/.hubdev/config.yaml
tenant: acme-bank
api-endpoint: https://hub.olympus.acme.bank/api/v1
auth:
  type: oidc
  issuer: https://auth.acme.bank
  client-id: hubdev-cli
```

---

## Opening Your First Workspace

```bash
# List available workbench instances
hubdev workspace list

# Open a workspace (launches VS Code)
hubdev workspace open acme-disputes-sandbox

# Open at a specific branch
hubdev workspace open acme-disputes-sandbox --branch feature/my-feature
```

Once the workspace opens in VS Code, you can use `hub` commands in the terminal:

```bash
# Inside the workspace terminal
hub context                    # View current context
hub get scenario-normative     # List scenarios
hub validate -f my-spec.yaml  # Validate resources
hub sync scenario my-scenario # Deploy scenario (after committing to Git)
```

---

## Verification

```bash
# On local machine
hubdev whoami
hubdev workspace list

# Inside workspace
hub context
hub get workbench-instance
```

---

## Related Documentation

- [CLI Channels for Developers](../06-ux-architecture/tenant-domain/cli-channels-for-developers.md) — Full command reference
- [Automation Development Desk](../06-ux-architecture/tenant-domain/automation-development-desk.md) — Web UI alternative

---

*TODO: Detailed installation instructions, proxy configuration, troubleshooting, upgrade procedures, VS Code extension setup*
