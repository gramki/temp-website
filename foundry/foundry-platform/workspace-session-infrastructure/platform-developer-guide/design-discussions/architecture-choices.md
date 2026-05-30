# Architecture Choices

Design questions and decisions for Workspace Session Infrastructure.

## 1. Coder vs raw K8s pods

**Decision: Coder as thin provisioner.**

Use Coder's workspace provisioner pointing at the K8s cluster. Session Infrastructure owns template definitions (Kubernetes provider, not Terraform). Session Management is the source of truth for session state — Coder is the execution layer. WO Runtime still acks to Session Management.

Escape path: replace Coder provisioner with direct K8s calls; pod spec and volumes remain owned by Session Infrastructure.

## 2. Single container vs sidecar

**Decision: Single container with process supervision.**

WO Runtime and Code Server run as processes within one container, managed by supervisord. Shared filesystem for workspace access; supervisor handles independent restarts (`autorestart=true`).

## 3. Ingress-per-session vs shared ingress

**Decision: Wildcard subdomain via Coder's proxy.**

URL format: `{session-id}.sessions.{ingress-domain}`. Coder proxies to workspaces by name — zero per-session Ingress objects. One wildcard cert, one DNS record.

## 4. Image variant strategy

**Decision: Single base image + workspace-type activation at session start.**

Six workspace types share ~95% content. Type-specific runtimes applied via init container or devcontainer features. Foundry admin Layer 3 overlay handles per-workspace customization.

## Read Next

- [../requirements.md](../requirements.md) — functional requirements
- [../../README.md](../../README.md) — module overview
