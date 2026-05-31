# Screen States (v0.1)

All prototype and production-targeted screens must handle these states.

## Required states

- `loading` - data or view is being prepared
- `empty` - no items exist yet
- `error` - operation or fetch failed
- `blocked` - progression stopped by governance or dependency
- `ready` - normal interactive state

## State requirements

## Loading

- Show skeleton or progress indicator.
- Keep layout stable to prevent content jump.

## Empty

- Explain what is missing and why.
- Provide primary CTA where possible.

## Error

- Use actionable message with retry option.
- Show diagnostic context where safe.

## Blocked

- Explain blocker source (for example: governance gate).
- Link to resolution workflow or owning surface.

## Ready

- Show current status metadata near primary action.

## Definition-of-done gate

A screen is not considered complete unless all required states are represented
in spec and at least one demonstration path exists in the prototype.
