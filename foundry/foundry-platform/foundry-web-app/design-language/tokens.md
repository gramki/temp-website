# Design Tokens (v0.1)

Design tokens are the only allowed primitive values for visual styling.

## Naming convention

Use semantic names that survive theme changes and visual refinements:

- `color.surface.default`, `color.text.muted`, `color.status.success`
- `space.2`, `space.4`, `space.8`
- `radius.sm`, `radius.md`, `radius.lg`
- `elevation.1`, `elevation.2`

## Foundations

## Color roles

- Surface: base canvas, elevated surfaces, overlays
- Text: primary, secondary, muted, inverse
- Border: subtle, default, strong
- Action: primary, secondary, critical
- Status: success, warning, error, info, blocked

## Color palette (default) - Slate + Indigo

This is the default palette for v0.1 prototype screens.

## Core semantic color tokens

- `color.surface.canvas`: `#F8FAFC`
- `color.surface.default`: `#FFFFFF`
- `color.surface.elevated`: `#F1F5F9`
- `color.surface.inverse`: `#0F172A`

- `color.text.primary`: `#0F172A`
- `color.text.secondary`: `#475569`
- `color.text.muted`: `#64748B`
- `color.text.inverse`: `#F8FAFC`

- `color.border.subtle`: `#E2E8F0`
- `color.border.default`: `#CBD5E1`
- `color.border.strong`: `#94A3B8`

- `color.action.primary`: `#4F46E5`
- `color.action.primaryHover`: `#4338CA`
- `color.action.secondary`: `#334155`
- `color.action.critical`: `#B91C1C`

## Status and governance tokens

- `color.status.info`: `#0284C7`
- `color.status.success`: `#16A34A`
- `color.status.warning`: `#D97706`
- `color.status.error`: `#DC2626`
- `color.status.blocked`: `#7C3AED`

- `color.governance.pass`: `#16A34A`
- `color.governance.review`: `#D97706`
- `color.governance.fail`: `#DC2626`
- `color.governance.hardBlock`: `#7C2D12`
- `color.governance.softBlock`: `#7C3AED`

## Usage constraints

- Governance and status semantics MUST remain consistent across all consoles.
- Do not remap success/warning/error colors per screen or persona.
- Use `color.status.blocked` for workflow block badges; reserve
  `color.governance.hardBlock` for explicit hard-stop actions/states.

## Typography

- Type scale: `xs`, `sm`, `md`, `lg`, `xl`, `2xl`
- Weights: regular, medium, semibold, bold
- Line heights: compact, default, relaxed
- Font pairing (default): `IBM Plex Sans` + `IBM Plex Mono`

## Font family tokens

- `font.family.ui`: `"IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`
- `font.family.mono`: `"IBM Plex Mono", "SFMono-Regular", Menlo, Consolas, monospace`

## Font usage

- UI, navigation, forms, tables, and body copy use `font.family.ui`.
- Work Order IDs, branch names, code snippets, and machine-readable values use `font.family.mono`.
- Use `font.family.mono` sparingly in high-density tables to preserve scanability.

## Spacing

- Base scale in 4px increments.
- Layout spacing uses `space.4+`; inline/control spacing can use `space.2`.

## Radius and elevation

- Radius tokens only: `none`, `sm`, `md`, `lg`
- Elevation tokens only: `0`, `1`, `2`, `3`

## Motion

- Fast: 120ms
- Normal: 180ms
- Slow: 240ms
- Use ease-out for entry and ease-in for exit.

## Do not

- Do not hardcode hex, px, or ad-hoc shadows directly in screen-level components.
- Do not introduce new token names without updating this document and `change-log.md`.
