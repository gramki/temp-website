# Chapter 03.02: Banking Fabrics

Domain-specific fabrics for banking systems, organized by functional category.

---

## Overview

Banking Fabrics are the domain-specific building blocks that compose into banking products. Each fabric addresses a distinct banking function with well-defined boundaries, data ownership, and operational responsibilities.

For an introduction to the fabric concept and architectural principles, see [What is a Fabric?](00-what-is-a-fabric.md).

---

## Fabric Catalog

### Foundation (01–04)

Core infrastructure that other banking fabrics depend on.

| # | Fabric | Purpose |
|---|--------|---------|
| 01 | [Accounting Fabric](01-accounting-fabric.md) | General ledger, subledgers, and financial record-keeping |
| 02 | [Customer Record Fabric](02-customer-record-fabric.md) | Customer master data, KYC records, and party management |
| 03 | [Product Fabric](03-product-fabric.md) | Product catalog, pricing, and configuration |
| 04 | [Line and Limits Fabric](04-line-and-limits-fabric.md) | Credit lines, exposure limits, and authorization rules |

### Deposit (05–06)

Liability-side account products.

| # | Fabric | Purpose |
|---|--------|---------|
| 05 | [Demand Deposit Fabric](05-demand-deposit-fabric.md) | Current accounts, savings accounts, and transaction accounts |
| 06 | [Term Deposit Fabric](06-term-deposit-fabric.md) | Fixed deposits, certificates of deposit, and time deposits |

### Credit (07–11)

Asset-side lending and credit products.

| # | Fabric | Purpose |
|---|--------|---------|
| 07 | [Revolving Credit Fabric](07-revolving-credit-fabric.md) | Credit cards, overdrafts, and revolving lines |
| 08 | [Term Loans Fabric](08-term-loans-fabric.md) | Personal loans, auto loans, and amortizing credit |
| 09 | [Mortgage Fabric](09-mortgage-fabric.md) | Home loans, property-backed lending |
| 10 | [Underwriting Fabric](10-underwriting-fabric.md) | Credit decisioning, risk assessment, and approval workflows |
| 11 | [Collections Fabric](11-collections-fabric.md) | Delinquency management, recovery, and workout |

### Card (12–14)

Card issuance and tokenization for issuer-side operations.

| # | Fabric | Purpose |
|---|--------|---------|
| 12 | [Card Issuance Fabric](12-card-issuance-fabric.md) | Consumer and retail card issuance |
| 13 | [Commercial Card Issuance Fabric](13-commercial-card-issuance-fabric.md) | Corporate, purchasing, and fleet card issuance |
| 14 | [Issuer Tokenization Fabric](14-issuer-tokenization-fabric.md) | Network tokenization and secure credential management |

### Payments (15–21)

Money movement and transaction processing from the issuer perspective.

| # | Fabric | Purpose |
|---|--------|---------|
| 15 | [Transfers Fabric](15-transfers-fabric.md) | Account-to-account transfers, wire, ACH, and real-time payments |
| 16 | [Bill Payments Fabric](16-bill-payments-fabric.md) | Biller integration, scheduled payments, and presentment |
| 17 | [Card Issuer Txn Processing Fabric](17-card-issuer-txn-processing-fabric.md) | Authorization, clearing, and settlement for card issuers |
| 18 | [UPI Issuer Txn Processing Fabric](18-upi-issuer-txn-processing-fabric.md) | UPI transaction processing for issuing banks |
| 19 | [Card Authentication Fabric](19-card-authentication-fabric.md) | 3DS, SCA, and cardholder verification |
| 20 | [Issuer Disputes Fabric](20-issuer-disputes-fabric.md) | Chargeback management and dispute resolution (issuer side) |
| 21 | [Issuer Fraud and Risk Fabric](21-issuer-fraud-and-risk-fabric.md) | Transaction monitoring and fraud prevention (issuer side) |

### Acquiring & PSP (22–27)

Payment acceptance and merchant-side transaction processing.

| # | Fabric | Purpose |
|---|--------|---------|
| 22 | [Payment Acquiring Fabric](22-payment-acquiring-fabric.md) | Merchant acquiring and payment acceptance |
| 23 | [Card PSP Fabric](23-card-psp-fabric.md) | Card payment service provider operations |
| 24 | [UPI PSP Fabric](24-upi-psp-fabric.md) | UPI payment service provider operations |
| 25 | [Acquirer Tokenization Fabric](25-acquirer-tokenization-fabric.md) | Merchant-side tokenization and credential management |
| 26 | [Acquirer Disputes Fabric](26-acquirer-disputes-fabric.md) | Chargeback management (acquirer side) |
| 27 | [Acquirer Fraud and Risk Fabric](27-acquirer-fraud-and-risk-fabric.md) | Transaction monitoring and fraud prevention (acquirer side) |

### Regulation & Compliance (28–32)

Regulatory reporting and compliance operations.

| # | Fabric | Purpose |
|---|--------|---------|
| 28 | [Credit Bureau Fabric](28-credit-bureau-fabric.md) | Credit bureau reporting and inquiry |
| 29 | [Statement Fabric](29-statement-fabric.md) | Statement generation and delivery |
| 30 | [Taxation Fabric](30-taxation-fabric.md) | Tax calculation, withholding, and reporting |
| 31 | [Regulatory Compliance Fabric](31-regulatory-compliance-fabric.md) | AML, KYC refresh, and regulatory reporting |
| 32 | [Internal Audit Fabric](32-internal-audit-fabric.md) | Audit trails, controls testing, and examination readiness |

### Distribution (33–35)

Channel and distribution capabilities.

| # | Fabric | Purpose |
|---|--------|---------|
| 33 | [Branch and Institution Fabric](33-branch-and-institution-fabric.md) | Branch operations, teller cash management, and institutional partner networks |
| 34 | [BaaS Fabric](34-baas-fabric.md) | Banking-as-a-Service platform and embedded finance |
| 35 | [Sourcing Fabric](35-sourcing-fabric.md) | Lead management, origination channels, and partner integration |

### Loyalty & Incentives (36)

Loyalty platforms, incentivization engines, reward ledgers, and voucher lifecycles.

| # | Fabric | Purpose |
|---|--------|---------|
| 36 | [Influence Fabric](36-influence-fabric.md) | Loyalty, vouchers, reward ledgers, and incentivization System of Record (SOR) |

### Relationship & Household (37–41)

Customer-centric relationship contexts, household financial operating systems, and concierge servicing.

| # | Fabric | Purpose |
|---|--------|---------|
| 37 | [Deposit Relationship Fabric](37-deposit-relationship-fabric.md) | Deposit relationship context, interest-bearing relationship tiers, and deposit-specific servicing rules |
| 38 | [Credit Relationship Fabric](38-credit-relationship-fabric.md) | Credit relationship context, consolidated credit exposure views, and repayment relationship parameters |
| 39 | [Card Relationship Fabric](39-card-relationship-fabric.md) | Card relationship context, cardholder preferences, and consolidated multi-card relationship views |
| 40 | [Concierge Fabric](40-concierge-fabric.md) | Relationship manager (RM) CRM, task ledger, and operational interaction logs |
| 41 | [Family Fabric](41-family-fabric.md) | Family Financial Operating System (FFOS), family graph, shared wallets, and delegated permissions |

---

## Related

- [Infra Fabrics](../01-infra-fabrics/README.md) — domain-neutral enterprise fabrics
- [The Hubs of Enterprise Banking](../03-hubs/) — bounded operational domains
- [Zeta Product Families](../04-product-lines/) — assembled product lines built on fabrics
