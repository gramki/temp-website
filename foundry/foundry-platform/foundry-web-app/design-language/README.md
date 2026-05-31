# Foundry Web App Design Language

This folder defines the shared design language for all Foundry Web App screens.

The goal is to keep UI decisions durable across iterations, regardless of whether
screens are prototyped with mock data or implemented against production APIs.

## Scope

This design language applies to:

- all pages and consoles in `foundry-web-app`;
- all future prototypes under `../prototype/`;
- all persona-facing surfaces unless explicitly marked as exception.

## Rules of use

1. New screens MUST use documented tokens and component patterns.
2. Any exception MUST be documented in `change-log.md` with rationale.
3. Screens are not "done" unless they include standard states from `states.md`.
4. IA and navigation boundaries MUST align with `platform-developer-guide/pages/`.

## Documents

| Document | Purpose |
|----------|---------|
| [tokens.md](tokens.md) | Visual foundations: spacing, typography, color roles, radius, elevation |
| [components.md](components.md) | Canonical components, variants, and do/don't constraints |
| [patterns.md](patterns.md) | Console and page interaction patterns |
| [states.md](states.md) | Empty, loading, error, blocked, and success states |
| [content-style.md](content-style.md) | Naming, labels, status copy, and CTA voice |
| [accessibility.md](accessibility.md) | Accessibility baseline requirements |
| [change-log.md](change-log.md) | Versioned decisions and exceptions |

## Initial non-negotiables (v0.1)

- No one-off visual values in screen code; use defined token names.
- Every page includes breadcrumb, title, and primary-question context.
- Every data surface has loading, empty, and failure states.
- Governance status uses consistent badge semantics across all consoles.
- Links between Discovery, Build, and Governance entities remain visible in flow.

## Current defaults

- Font pairing: `IBM Plex Sans` (UI) and `IBM Plex Mono` (technical text)
- Color palette: `Slate + Indigo` semantic token set in `tokens.md`

## Related docs

- [../README.md](../README.md)
- [../platform-developer-guide/pages/README.md](../platform-developer-guide/pages/README.md)
- [../platform-developer-guide/pages/consoles/CONSOLE-GUIDE.md](../platform-developer-guide/pages/consoles/CONSOLE-GUIDE.md)
