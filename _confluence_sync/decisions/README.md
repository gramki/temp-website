# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records (ADRs) for the Confluence Sync tool. ADRs document significant architectural decisions, the context in which they were made, and their consequences.

## Index

1. [ADR-0001: Two-Phase Sync Architecture](./0001-two-phase-sync-architecture.md)
   - Implements prepare-then-sync approach with parallel execution

2. [ADR-0002: Module Separation: Content Preparer and Confluence Sync](./0002-module-separation.md)
   - Separates content preparation from Confluence API interactions

3. [ADR-0003: Data Directory Structure: One Subdirectory Per Destination](./0003-data-directory-structure.md)
   - Organizes all data under `data/` with per-destination subdirectories

4. [ADR-0004: Content Hash-Based Change Detection](./0004-content-hash-change-detection.md)
   - Uses SHA-256 content hashes for efficient change detection

5. [ADR-0005: JSONL Format for Sync State](./0005-jsonl-format-sync-state.md)
   - Uses JSON Lines format for streaming state updates

6. [ADR-0006: Destination-Based Configuration Architecture](./0006-destination-based-architecture.md)
   - YAML-based configuration supporting multiple destinations

## Decision Status

- **Accepted**: Decision has been made and implemented
- **Proposed**: Decision is under consideration
- **Deprecated**: Decision has been superseded or is no longer valid
- **Superseded**: Decision has been replaced by another ADR

## How to Add a New ADR

1. Copy the template from `_templates/adr.md`
2. Number sequentially (e.g., `0007-title.md`)
3. Fill in all sections
4. Update this README with the new ADR
5. Link related ADRs in the "Related Decisions" section

## Related Documentation

- [Main README](../README.md) - Overview of the sync tool
- [User Guide](../USER-GUIDE.md) - Comprehensive user documentation
- [Code Documentation](../sync-to-confluence.py) - Inline code documentation
