# Foundry Web App Prototype

This folder contains the no-backend, clickable prototype for Foundry Web App IA
and journey validation.

## Purpose

- Demonstrate Discovery and Build journey flows with realistic screen transitions.
- Validate information architecture and navigation before API integration.
- Provide stakeholder demos without runtime dependency on backend services.

## Scope constraints

- No API calls; all data is fixture-driven.
- Priority is interaction clarity and flow completeness over implementation depth.
- Prototype UI must follow `../design-language/`.

## Structure

- `storylines/` - walkthrough scripts and target outcomes
- `mock-data/` - static fixtures and scenario presets
- `src/app/` - app shell composition and route-level orchestration
- `src/features/` - journey screens (Discovery, Build, later Governance/Traceability)
- `src/foundry-ui/` - Foundry-owned UI wrappers over Radix/shadcn patterns
- `src/lib/` - shared utilities

## UI architecture guardrails

- Radix primitives are allowed only inside `src/foundry-ui/`.
- Feature screens in `src/features/` import from `src/foundry-ui/components/`.
- Shared tokens, statuses, and typography must match `../design-language/tokens.md`.
- Badge semantics must follow `../design-language/components.md`.

These guardrails are enforced with lint restrictions in `eslint.config.js`.

## Initial journey set

- Discovery track: create case -> progress -> decision gate
- Build track: Product Intent pipeline -> Work Orders -> quality/gate visibility

## Exit criteria for each prototype iteration

- No dead-end navigation in hero journeys
- Required screen states represented (loading, empty, error, blocked, ready)
- Terminology consistent with Foundry domain docs

## Getting started

```bash
npm install
npm run dev
```

## Current stack

- React + TypeScript + Vite
- Radix UI primitives
- Foundry-owned wrappers following shadcn-style composition patterns
