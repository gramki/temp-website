# PSD Templates by Module Archetype

Each template provides the full PSD structure with **section depth guidance** calibrated to the module's interaction boundary. Sections marked **Deep** are the primary specification surfaces for that archetype and must be thorough. Sections marked **Light** may be brief or state "No impact." Sections marked **Required** apply equally to all archetypes.

| Template | Module Archetype | Primary Specification Surfaces |
|---|---|---|
| `psd-human-interactive.md` | Human-Interactive (Synchronous UI) | UX (Dim 4), Structural (Dim 8) |
| `psd-programmatic-interactive.md` | Programmatic-Interactive (Synchronous M2M) | Extensibility (Dim 6), Technical (Dim 5) |
| `psd-reactive-background.md` | Reactive / Background (Asynchronous) | Technical (Dim 5), Operational (Dim 7), Data (Dim 9) |

## Usage

1. Identify the target module's archetype (from `draft-archetypes.md`).
2. Copy the matching template.
3. Fill in all **Required** and **Deep** sections thoroughly.
4. Fill in **Medium** sections with relevant details.
5. For **Light** sections, provide a brief assessment or state "No impact" with justification.
6. Adjust business sections (Dims 2–3) depth based on the **product archetype** (see guidance in each template).

## Section Depth Matrix

| PSD Section | Human-Interactive | Programmatic-Interactive | Reactive/Background |
|---|---|---|---|
| 0. Header & Traceability | Required | Required | Required |
| 1. Structural Impact (Dim 8) | Required | Required | Required |
| 2. Vendor Value (Dim 2) | Per product archetype | Per product archetype | Per product archetype |
| 3. Customer Value (Dim 3) | Per product archetype | Per product archetype | Per product archetype |
| 4. UX (Dim 4) | **Deep** | Light | N/A |
| 5. Technical (Dim 5) | Medium | **Deep** | **Deep** |
| 6. Extensibility (Dim 6) | Light | **Deep** | Medium |
| 7. Operational (Dim 7) | Light | Medium | **Deep** |
| 8. Data (Dim 9) | Medium | Medium | **Deep** |
| 9. Acceptance Criteria | Required | Required | Required |
| 10. Epic Decomposition | Required | Required | Required |
