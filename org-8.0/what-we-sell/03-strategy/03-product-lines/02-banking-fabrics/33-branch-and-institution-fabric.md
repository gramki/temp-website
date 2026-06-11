# Chapter 03.02.33: Branch and Institution Fabric — Product Note

**The system of record for physical branch footprint and external institutional partner networks — owning teller transactions, cash vault management, and the legal/operational interfaces with payment networks, clearing houses, settlement counterparties, and critical third-party service providers.**

---

## What It Governs

Branch and Institution Fabric is the authoritative governance layer for both the bank's physical distribution network and its direct external institutional partner interfaces. It represents the administrative and connection nodes of the bank — organizing branch endpoints and third-party institutional relationships into a cohesive operational substrate.

In scope:
- **Physical Branch Network:** Teller session processing, cash drawer balances, vault inventory, cash shipments, appointment scheduling, queue management, and physical branch profiles.
- **Institutional Partner Network:** Identity profiles, operational agreements, connection sessions, messaging schemas, transaction routing parameters, settlement cut-offs, and service-level logs with external non-customer entities that the bank directly works with — including **Payment Networks** (Visa, Mastercard), **Clearing Houses & Central Depositories** (FedACH, Nacha, FedNow, FedWire), **Settlement Counterparties**, and **Third-Party Service Providers** (credit bureaus, verification APIs, and core platform partners).

Out of scope:
- Account balances and posting rules (governed by Tachyon Kernel/DDA or relevant product ledgers).
- The execution of payment transfers and message assembly (handled by Photon Payments Hub/Transfers Fabric).
- Customer-facing front-office experience channels (handled by Neutrino Consumer Experiences).

---

## Source of Truth

- **Entities owned:** Teller session, cash drawer position, vault inventory, branch configuration, queue ticket, branch/teller calendar; Institutional profile, partner routing tables, network agreement, connection session log, settlement cut-off calendar, partner SLA metrics, service provider profile.
- **Key invariants:**
  - Cash drawer balances reconcile to teller transactions with zero tolerance.
  - Dual control is structurally enforced for all cash vault access, cash orders, and physical cash shipments.
  - Institutional connection parameters and routing directories (such as ACH Routing Transit Numbers or BIN ranges) are validated and kept immutable during active trading sessions.
  - Every external service call or partner network ping has an auditable, tamper-evident log entry mapping to the requesting internal scenario or user context.
- **Configurable vs. compliance floor:** Teller transaction limits, cash holding thresholds, partner SLA alert triggers, and branch hours are configurable. Compliance floor: Bank Secrecy Act (BSA) cash transaction reporting ($10K+), OFAC screening logs for institutional counterparties, dual-control enforcement, and audit logs of network connection state changes retained for regulatory compliance (typically 7+ years).

---

## Scope Highlights

- **Unified Endpoint Directory:** Maintains a single, secure directory of all physical branch locations and external partner connection endpoints.
- **Teller & Cash Operations:** Processes deposits, withdrawals, check-cashing, and cashier's checks while maintaining physical cash drawer and central vault ledger accuracy.
- **Partner Session & SLA Monitoring:** Manages the active communication sessions, message retry rules, and SLA tracking for payment networks and service APIs.
- **Settlement & Cut-Off Schedules:** Manages the operational schedules and cut-off calendars of central clearing houses (ACH, wire networks) to ensure payment pipelines align with settlement windows.
- **Operational Queue & Booking:** Coordinates walk-in tickets, lobby routing, and scheduled customer/partner appointments with physical or specialist resources.

---

## Capability Domains

1. **Physical Branch Operations** — Teller lifecycle, cashiering, workstation mapping, branch calendars, and resource scheduling.
2. **Cash & Vault Ledger** — Cash drawer assignments, vault inventory balances, physical cash ordering, armored car logs, and end-of-day reconciliation.
3. **Institutional Relationship Directory** — Profiles, routing directories, clearing/network identifiers, and metadata for networks, clearing houses, and service providers.
4. **Partner Connection & Schema Registry** — Session management, connection health, retry/circuit-breaking protocols, and transaction/message log structures.
5. **Settlement Cut-Off & Calendar Engine** — Operation calendars for clearing systems, cut-off windows, and settlement lifecycle states.

---

## Boundaries and Adjacencies

| Adjacent Fabric | Relationship |
|---|---|
| **Demand Deposit Fabric** | Deposit Fabric holds ledger balances; Branch and Institution Fabric processes teller transactions that affect those balances. |
| **Transfers Fabric** | Transfers Fabric routes ACH/Wire payments; Branch and Institution Fabric governs the clearing house routing tables, schedules, and endpoint session states. |
| **Card Issuer Txn Processing Fabric** | Processing Fabric executes card authorizations; Branch and Institution Fabric governs the card network connectivity profiles (Visa, Mastercard) and active gateway configurations. |
| **Accounting Fabric** | Accounting Fabric (Tachyon Kernel) records financial ledger entries; Branch and Institution Fabric provides branch cash positions and partner settlement reconciliations. |
| **Customer Record Fabric** | Customer Fabric provides customer identity; Branch and Institution Fabric accesses customer records to authorize physical teller transactions. |
| **Trust Fabric** | Trust Fabric handles identity authentication; Branch and Institution Fabric verifies customer and teller identity at physical locations. |

---

## References

- [Tachyon Product Line](../04-product-lines/01-tachyon.md) — Orchestrates Branch and Institution Fabric as part of the Tachyon Institution product line.
- [Accounting Fabric](01-accounting-fabric.md) — Receives physical cash, teller, and partner network settlement general ledger entries.
- [Transfers Fabric](15-transfers-fabric.md) — Integrates with clearing house schemas and schedules managed in this fabric.
