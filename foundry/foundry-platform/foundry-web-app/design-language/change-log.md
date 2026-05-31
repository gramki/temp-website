# Design Language Change Log

Track design-language decisions and exceptions here.

## Versioning policy

- Major: structural changes to design foundations or pattern taxonomy
- Minor: additive rules or components
- Patch: clarifications and non-breaking refinements

## Entries

## v0.1.4 - UI architecture baseline

- Declared Radix + shadcn-style wrapper baseline in `components.md`.
- Added import-boundary guardrail guidance so feature code depends on Foundry UI wrappers.

## v0.1.3 - Badge mapping contract

- Added canonical status and governance badge mapping table in `components.md`.
- Standardized badge background, text, and border token usage across screens.
- Added badge constraints for canonical labels and color-independent meaning.

## v0.1.2 - Color palette decision

- Set default semantic color palette to `Slate + Indigo`.
- Added concrete color token values and governance/status mappings in `tokens.md`.
- Added usage constraints to keep status and governance color semantics stable.

## v0.1.1 - Font pairing decision

- Set default font pairing to `IBM Plex Sans` (UI) and `IBM Plex Mono` (technical text).
- Added font family tokens and usage guidance in `tokens.md`.

## v0.1.0 - Initial scaffold

- Added baseline structure for tokens, components, patterns, states, content, and accessibility.
- Established non-negotiables for prototype and future implementation alignment.
- Declared this folder as source of truth for cross-screen UI consistency.
