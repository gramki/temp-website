---
name: Seer Sidecar Detailed Design
overview: Create C2-level (Container) design documentation for all 7 sub-components of Seer Sidecar, focusing on functional scope, integration points, and hand-offs. Design at conceptual level (C2) for most components, with C3-level detail for critical enforcement mechanisms. Migrate relevant content from guardrails.md and authority-enforcement.md into the new design documents.
todos:
  - id: guardrail-service
    content: Create C2-level design for Guardrail Service covering functional scope (inbound guardrails on dispatch, outbound guardrails on Hub API calls with per-API and wildcard pattern support, Allow/Alert/Deny response model, per-processor configuration schema, failure defaults to Deny) and integration points
    status: completed
  - id: authority-enforcement-service
    content: Create C2-level design for Authority Enforcement Service covering functional scope (ceiling enforcement, delegation chain enforcement) and integration hand-offs
    status: completed
  - id: policy-enforcement-service
    content: Create C3-level design for Policy Enforcement Service covering functional scope (OPA policy evaluation, violation handling) with detailed API specifications
    status: completed
  - id: resource-quota-service
    content: Create C2-level design for Resource Quota Service covering functional scope (compute, token, API, storage quota tracking) and integration points
    status: completed
  - id: fair-usage-budget-service
    content: Create C2-level design for Fair Usage Budget Service covering functional scope (per-subject, per-signal, per-time-period, per-action-type budget tracking) and integration points
    status: completed
  - id: metrics-service
    content: Create C2-level design for Metrics Service covering functional scope (metrics collection, instrumentation) and integration hand-offs
    status: completed
  - id: hot-reload-service
    content: Create C2-level design for Hot-reload Service covering functional scope (configuration updates, configuration management) and integration points
    status: completed
    dependencies:
      - guardrail-service
  - id: migrate-guardrails
    content: Migrate runtime enforcement content from subsystems/guardrails.md to guardrail-service.md
    status: completed
    dependencies:
      - guardrail-service
  - id: migrate-authority-enforcement
    content: Migrate runtime enforcement content from subsystems/authority-enforcement.md to authority-enforcement-service.md and policy-enforcement-service.md
    status: completed
    dependencies:
      - authority-enforcement-service
      - policy-enforcement-service
  - id: update-adr-0072
    content: Update ADR-0072 (Seer Guardrails Two-Layer Model) to reflect new guardrail execution model (inbound on dispatch, outbound on Hub API calls with per-API and wildcard patterns, Allow/Alert/Deny responses)
    status: completed
    dependencies:
      - guardrail-service
  - id: update-adr-0104
    content: Update ADR-0104 (Seer Agent Runtime Detailed Design) to clarify agent response handling - agents update requests directly via Hub APIs, not via sx-observer forwarding
    status: completed
  - id: update-adr-0074
    content: Update ADR-0074 (Seer Runtime on Atlantis) to reflect new guardrail model (inbound/outbound instead of before/after)
    status: completed
    dependencies:
      - guardrail-service
  - id: update-guardrail-docs
    content: Update all documents referencing before/after guardrails to reflect new inbound/outbound model with per-API configuration
    status: completed
    dependencies:
      - guardrail-service
      - update-adr-0072
  - id: update-agent-response-docs
    content: Update all documents referencing agent response handling to clarify agents update requests directly via Hub APIs (Option A)
    status: completed
    dependencies:
      - update-adr-0104
  - id: create-scope-doc
    content: Create SCOPE.md document with coverage summary, design status, intended depth callout, "Implementation Details Deferred" section, and related documentation references
    status: completed
    dependencies:
      - guardrail-service
      - authority-enforcement-service
      - policy-enforcement-service
      - resource-quota-service
      - fair-usage-budget-service
      - metrics-service
      - hot-reload-service
  - id: update-readme
    content: Update seer-sidecar/README.md with links to all detailed design documents, remove old content references, update status to reflect design completion, add design documents table, and include "Key Design Decisions" section
    status: completed
    dependencies:
      - guardrail-service
      - authority-enforcement-service
      - policy-enforcement-service
      - resource-quota-service
      - fair-usage-budget-service
      - metrics-service
      - hot-reload-service
      - create-scope-doc
  - id: update-concept-docs
    content: Update implementation-concepts/guardrails.md and implementation-concepts/authority-enforcement.md to reference new seer-sidecar design documents and remove migrated content
    status: completed
    dependencies:
      - migrate-guardrails
      - migrate-authority-enforcement
---

