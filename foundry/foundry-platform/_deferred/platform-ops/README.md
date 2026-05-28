# Platform Ops (Deferred)

**Module scope:** Plumbing — observability dashboards, standard tooling, infrastructure.

## What this module does

Platform Ops provides the operational infrastructure for Foundry Platform. It provides:

- **Observability dashboards** — platform health, Work Order throughput, agent performance, system metrics
- **Standard tooling** — integration with standard observability tools (logging, metrics, tracing)
- **Infrastructure** — platform infrastructure provisioning, scaling, reliability
- **Monitoring & alerting** — platform-level monitoring and alerting

## What Platform Ops is NOT

- **Not Foundry CI.** CI lives in [Release Tools](../release-tools/README.md).
- **Not agent observability.** Agent-level observability (per-agent traces, logs) is part of [Work Order Runtime](../work-order-runtime/README.md).
- **Not Workspace observability.** Workspace-level metrics are part of [Foundry IDE](../ide/README.md).

Platform Ops is the **platform** observability layer — how do we observe and operate Foundry itself?

## Key design decisions

- **Foundry relies on standard observability tools.** We don't build custom observability infrastructure; we integrate with standard tools and build dashboards on top.
- **Platform Ops owns the plumbing.** Infrastructure, scaling, reliability — the operational concerns of running the platform.

## Open questions

- Which observability stack? (Datadog, Grafana, Prometheus, etc.)
- Platform SLOs and SLIs
- Infrastructure topology — cloud provider, regions, scaling model
- Incident response for platform issues

## Read next

- [../../tldr-faq.md](../../tldr-faq.md) — platform ops design decisions
