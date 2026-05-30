# Adoption Goal (Deprecated)

**Status:** Deprecated — see DR-016

## Deprecation Notice

The Adoption Goal entity has been eliminated. Targets (time-bound, quantitative measures of Win Outcome progress) are now **embedded in Initiatives** as Key Results, following the OKR pattern. See the updated Initiative entity (`entities/definition-model/dim1-initiative.md`) for details.

**Rationale:**
- "Adoption" was stage-specific (only Activation), but targets span all AAARRR stages
- "Goal" conflicted with Objectives (Strategy), creating hierarchy confusion
- Targets are naturally attributes of the coordination construct (Initiative), not independent entities
- Win Reviews assess Initiative target progress directly

See DR-016 for the full decision record.
