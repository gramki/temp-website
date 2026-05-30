# DR-002: Distribute Planning Work Across All Four Tracks

**Status:** Accepted
**Date:** 2026-02-15
**Related FAQ:** Q11

---

## Context

When the need for planning work items was identified, two approaches were considered:

1. **Centralized:** Create a 5th "Plan Track" to house all planning activities across the SDLC.
2. **Distributed:** Each existing track owns its own planning entities alongside its core work entities.

## Decision

Each track owns its own planning work. No separate "Plan Track" is created.

| Track | Planning Entities |
|---|---|
| Discovery (Discovery) | Objective Setting Task, Initiative Scoping Task, Prioritization Task |
| Build (Build) | Release Planning Task, Milestone Planning Task, Iteration Planning Task |
| Run (Run) | Deployment Planning Task, Capacity Planning Task |
| Win (Win) | Go-to-Market Planning Task, Customer Rollout Planning Task |

## Rationale

1. **Planning is not separable from execution.** The people who plan are the people who execute. A Build Track tech lead plans iterations and milestones as part of their daily work — separating this into a different track creates artificial handoffs.
2. **Different tracks plan different things.** Discovery planning (Objectives, Initiatives) is fundamentally different from Run planning (deployments, capacity). A single "Plan Track" would contain heterogeneous work owned by different roles.
3. **Track ownership stays clear.** Each track's primary owner is also responsible for planning within that track. No new ownership ambiguity is introduced.
4. **The model stays at 4 tracks.** Adding a 5th track increases model complexity without corresponding benefit.

## Consequences

- **Positive:** Planning work is explicit and trackable within each track.
- **Positive:** No new ownership boundaries or handoff points.
- **Positive:** The 4-track model remains simple and memorable.
- **Negative:** Each track now has two sub-categories of entities (planning + core work). Documentation must clearly distinguish them.
