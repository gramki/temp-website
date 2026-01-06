# ADR-0001: Normalize Signal Format Between Signal Providers and Signal Exchange

## Status

Accepted

## Date

2026-01-05

## Context

Signal Exchange (SX) receives signals from multiple Signal Providers (SPs) including I/O Gateways like Atropos (events), Heracles (HTTP), Dia (files), and Kale (scheduler). Each SP originally had its own signal format based on its transport protocol.

This created several challenges:
- SX had to understand and parse multiple signal formats
- Trigger definitions needed to account for format variations
- Adding new SPs required changes to SX parsing logic
- Schema validation was complex with per-provider schemas

The question arose: Should signals be normalized at the SP/I/O Gateway level before reaching SX?

## Decision

**Normalize all signals at the I/O Gateway level before sending to Signal Exchange.**

All Signal Providers must:
1. Transform protocol-specific signals to Signal Exchange's **Normalized Signal DTO** format
2. Ensure all required fields are present: `tenant_id`, `subscription_id`, `signal_id`, `signal_type`, `timestamp`
3. Preserve provider-specific data in `additional_fields` if needed for response transformation

Signal Exchange:
1. Receives signals in a single, normalized format regardless of origin
2. Validates against one schema (Normalized Signal DTO)
3. Does not need to know the originating protocol

## Consequences

### Positive
- **Simplified SX**: Signal Exchange only handles one signal format
- **Easier trigger authoring**: All triggers work with same field structure
- **Extensible**: New I/O Gateways can be added without SX changes
- **Clear responsibility**: I/O Gateways own transport, SX owns routing

### Negative
- **I/O Gateway complexity**: Each gateway must implement normalization
- **Potential data loss**: If normalization is not careful, protocol-specific nuances may be lost

### Neutral
- `additional_fields` section allows SPs to preserve extra data when needed

## Related

- [Signal Provider Interactions](../04-subsystems/signal-exchange/signal-provider-interactions.md)
- [I/O Gateways](../04-subsystems/signal-providers/README.md)
- [Signal Exchange Overview](../04-subsystems/signal-exchange/README.md)

