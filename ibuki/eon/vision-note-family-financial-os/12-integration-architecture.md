# 12. Integration Architecture
FFOS relies on stable, versioned integration contracts with bank cores, payment rails, CRM, and external data sources. Integration patterns prioritize loose coupling, observability, consent tagging, and fault isolation so agentic workflows remain resilient even when downstream systems degrade.

## 12.1 Integration with Core Banking & Surround Systems

### 12.1.1 Accounts, Deposits, Loans, Cards
Use API gateways or service buses to connect FFOS to product processors. Data ingestion leverages read replicas or event feeds enriched with household identifiers; execution uses secure API calls with transaction correlation IDs, retry policies, and compensation hooks.

### 12.1.2 Payments and Collections Rails
Do agents interface with payment hubs, ACH/RTGS gateways, card networks, and collection systems via orchestrator-managed workflows. Guardrail services validate limits, sanctions, and consent scopes before hitting rails, and responses are logged with settlement metadata for reconciliation.

### 12.1.3 CRM, RM Workbench, and Contact Centre Systems
Bidirectional integrations share household context, tasks, approvals, and telemetry with CRM and RM platforms. Actions initiated from RM tools or contact center screens are routed back into FFOS workflows for guardrail enforcement, ensuring no shadow processes bypass audit.

## 12.2 Product Gateway & Abstraction Layer

### 12.2.1 Product Drivers and APIs
Abstraction layer maps financial products to standardized capability contracts (fund transfer, credit line draw, policy issuance, policy servicing). Enables agents to invoke operations without custom coding per product, while monitoring adapters for SLA adherence.

### 12.2.2 Configuration of Product Behaviours for Agents
Product behaviours (fees, eligibility, thresholds, documentation needs) are expressed declaratively, allowing governance agents to evaluate actions consistently across markets and enabling quick updates when regulators or product teams adjust rules.

## 12.3 External Data & Ecosystem Integrations

### 12.3.1 External Billers and Mandates
Secure adapters connect to biller networks, mandate repositories, telco/utilities, and government interfaces for obligation detection and payment coordination. Adapters enforce throttling, consent tagging, and reconciliation logs to ensure third-party interactions remain auditable.

### 12.3.2 Insurance and Investment Platforms
Federated APIs retrieve policy positions, coverage gaps, and investment holdings, enabling foundation agents to compute comprehensive household state while respecting consent and data residency constraints. When data cannot leave partner platforms, FFOS agents run federated queries and store only derived insights permitted by policy.
