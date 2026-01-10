# 1.6 Portability as Non-Negotiable

Seer treats cloud-provider portability as a non-negotiable requirement. The same agent, with the same Training Specification, must be deployable on AWS, Azure, GCP, or on-premises infrastructure without modification to its semantic definition.

## Why Portability Matters

### Strategic Risk

Lock-in to a single cloud provider creates strategic risk:
- **Pricing power:** Vendor can increase prices without competitive constraint
- **Service changes:** Provider changes can break agent functionality
- **Availability dependency:** Provider outages affect all operations
- **Exit cost:** Switching becomes prohibitively expensive

### Regulatory Requirements

Many regulated industries face requirements that affect cloud choices:
- **Data sovereignty:** Certain data must remain in specific jurisdictions
- **Provider diversity:** Regulators may require multi-provider strategies
- **Government contracts:** Specific clouds may be mandated or prohibited

### Business Agility

Portability enables business flexibility:
- **Best-of-breed selection:** Use the best provider for each workload
- **Cost optimization:** Move workloads to lowest-cost providers
- **Capability adoption:** Access new capabilities from any provider
- **M&A readiness:** Integrate acquired organizations on different clouds

## What Portability Means in Practice

### Semantic Layer Portability

The agent's semantic definition (Training Spec, Employment Spec, identity, authority) is cloud-agnostic:
- Same Training Spec deploys identically on any supported cloud
- Same identity model applies regardless of provider
- Same guardrails enforce regardless of infrastructure

### Infrastructure Layer Adaptation

While the semantic layer is portable, the infrastructure layer adapts to the provider:
- Container orchestration uses provider-specific configuration
- Model endpoints point to provider-specific services
- Secrets management uses provider-appropriate systems

This adaptation is handled by the platform, not by agent developers.

### Consistent Behavior

Regardless of where an agent runs:
- Same knowledge produces same reasoning
- Same tools produce same actions
- Same guardrails produce same constraints
- Same audit requirements produce same records

## How Seer Achieves Portability

### Abstraction Layers

Seer provides abstractions that hide provider differences:

| Concern | Abstraction |
|---------|-------------|
| **Model Access** | Model Gateway provides unified API regardless of provider |
| **Storage** | Memory Services abstract storage implementation |
| **Identity** | Cipher IAM provides cross-cloud identity |
| **Deployment** | Deployment abstraction handles provider-specific configuration |

### Provider-Agnostic Specifications

Agent specifications use provider-neutral constructs:
- Models identified by capability, not provider endpoint
- Tools defined by protocol, not implementation
- Resources specified by requirement, not provider unit

### Infrastructure Portability Patterns

Common patterns enable infrastructure portability:
- Kubernetes as the common orchestration layer
- OCI containers as the common packaging format
- OpenTelemetry as the common observability standard

## What This Does Not Mean

Portability is not free migration. It means:

- **Same agent runs on multiple clouds:** ✓
- **Zero-effort migration:** ✗ (infrastructure configuration still required)
- **Identical performance everywhere:** ✗ (infrastructure capabilities vary)
- **No cloud-specific optimization:** ✗ (optimization is allowed, dependency is not)

Organizations can optimize for a specific cloud while maintaining the ability to move if needed.

## The Lock-In Alternative

Without portability commitment, organizations face:
- Agents that only run on one cloud
- Training that depends on provider-specific features
- Tools that require provider-specific integrations
- Audit that uses provider-specific logging

Switching providers then requires rebuilding agents, not just redeploying them.

---

**References:**
*   `olympus-seer-docs/seer-design/introduction.md`
*   `olympus-seer-docs/WHY-SEER-OUTLINE-DRAFT.md` — Section 6.6
