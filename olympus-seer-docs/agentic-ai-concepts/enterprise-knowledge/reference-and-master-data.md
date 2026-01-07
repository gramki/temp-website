# Reference and Master Data

## What this is

This knowledge type captures **canonical identifiers and code tables** the enterprise treats as stable, shared meaning:

- product catalogs
- country/currency codes
- reason codes and taxonomy IDs
- customer/account identifiers (master records)

It answers:

> *“What are the canonical values and identifiers we use across the organization?”*

## Typical systems

- MDM systems
- reference data services
- product information management
- governed tables in warehouses/marts (when semantics and ownership are explicit)

## Management characteristics

- **Explicit semantics**: every code/value must have an owned meaning.
- **Change control**: updates are slow, reviewed, and effective-dated.
- **Downstream impact awareness**: reference/master changes ripple into models, rules, reporting.

## Navigation

- Back: [`README.md`](./README.md)

