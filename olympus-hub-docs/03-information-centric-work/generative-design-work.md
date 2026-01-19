# Generative/Design Work

Generative work is creative, exploratory work that generates multiple possibilities and converges on a selected direction through evaluation and elimination. The path forward emerges through creation and selection.

---

## What Is Generative/Design Work?

In generative work, you don't know the answer when you start. You explore options, create variants, evaluate alternatives, and converge on a chosen direction. The emphasis is on **divergence** (create many options) followed by **convergence** (select the best).

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Approach** | Divergent → Convergent |
| **Artifacts** | Multiple variants created |
| **Selection** | Choose/discard rather than iterate-in-place |
| **Agents** | Creators, evaluators, decision-makers |
| **Goal** | Arrive at a viable direction/solution |

### Examples

- Software architecture design (evaluate approaches)
- Product design (create prototypes, test, select)
- Strategy development (analyze options, choose direction)
- Solution design (explore alternatives)
- Creative work (multiple concepts, selection)
- Research and exploration (hypotheses, experiments)
- Business case development (options analysis)

---

## Contrast with Artifact-Centric Work

| Artifact-Centric | Generative/Design |
|------------------|-------------------|
| One artifact iterated | Multiple variants created |
| Feedback → revision | Evaluation → selection |
| Linear progression | Exploration → convergence |
| Goal: approved artifact | Goal: chosen direction |
| Know what to build | Discover what to build |

**Relationship:** Generative work often *precedes* artifact-centric work. Once a direction is chosen, developing that direction becomes artifact-centric.

```
Generative Phase          Artifact-Centric Phase
─────────────────         ────────────────────────
Explore options    →      Develop chosen direction
Create variants    →      Iterate single artifact
Select direction   →      Refine to completion
```

---

## Anatomy of Generative/Design Work

### Lifecycle

```
1. Problem Framing
   Define what needs to be solved
        ↓
2. Exploration
   Generate multiple approaches/variants
        ↓
3. Prototyping
   Develop variants enough to evaluate
        ↓
4. Evaluation
   Assess variants against criteria
        ↓
5. Selection
   Choose direction, discard alternatives
        ↓
6. Refinement
   Develop selected approach (→ artifact-centric)
```

### Participant Roles

| Role | Responsibility |
|------|----------------|
| **Creators** | Generate variants, explore possibilities |
| **Evaluators** | Assess variants against criteria |
| **Decision-makers** | Select direction, authorize resources |
| **Stakeholders** | Provide constraints, requirements, feedback |

### Variant Management

| Aspect | Description |
|--------|-------------|
| **Parallel tracks** | Multiple variants developed simultaneously |
| **Early elimination** | Discard non-viable options quickly |
| **Merging** | Combine elements from multiple variants |
| **Pivoting** | Shift direction based on learnings |
| **Final selection** | Choose one (or synthesized) direction |

---

## Divergence and Convergence

### Divergence Phase

| Activity | Purpose |
|----------|---------|
| Brainstorming | Generate many ideas |
| Research | Explore existing solutions |
| Prototyping | Make ideas concrete enough to evaluate |
| Experimentation | Test hypotheses |

### Convergence Phase

| Activity | Purpose |
|----------|---------|
| Evaluation | Assess against criteria |
| Comparison | Rank alternatives |
| Debate | Discuss tradeoffs |
| Decision | Select direction |

### The Diamond Model

```
        Divergence              Convergence
        ──────────              ───────────
            ╱╲                      ╲╱
           ╱  ╲                      ╲
          ╱    ╲                      ╲
         ╱      ╲                      ╲
        ╱        ╲                      ╲
       ╱ many     ╲       →       select ╲
        options                  direction
```

Many generative efforts involve multiple "diamonds" — cycles of divergence and convergence at different levels.

---

## Design Decisions

A key output of generative work is **design decisions** — choices among alternatives with documented rationale.

| Element | Purpose |
|---------|---------|
| **Options considered** | What alternatives were explored |
| **Criteria** | How options were evaluated |
| **Tradeoffs** | What was gained/lost with each option |
| **Decision** | What was chosen |
| **Rationale** | Why this choice was made |

This documentation is valuable for:
- Understanding why current approach was chosen
- Revisiting if circumstances change
- Onboarding new team members
- Auditing decision quality

---

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Design challenge | Signal → Scenario |
| Design effort | Request (parent) |
| Variants | Sub-requests or parallel Tasks |
| Evaluation criteria | Goals in Normative Layer |
| Evaluation activity | Review Tasks |
| Selection decision | Activity with decision outcome |
| Chosen direction | Request outcome |
| Design decision record | Knowledge artifact |

### How Hub Models Generative/Design Work

```
Signal (design challenge identified)
    ↓
Trigger (matches design scenario type)
    ↓
Scenario (defines design process)
    ↓
Request (design effort instance)
    ↓
Tasks: Create variants (assigned to Creators)
    ↓
Agents develop multiple variants
    ↓
Tasks: Evaluate variants (assigned to Evaluators)
    ↓
Evaluation against criteria
    ↓
Selection Decision (Activity outcome)
    ↓
Request completes with chosen direction
```

### Why Generative Work Suits Hub

| Hub Concept | Why It Fits |
|-------------|-------------|
| **Request for exploration** | Track the entire design effort |
| **Parallel Tasks** | Multiple variants developed simultaneously |
| **Goals as criteria** | Evaluation criteria modeled as goals |
| **Decision as outcome** | Selection formally recorded |
| **Memory** | Alternatives and rationale preserved |

---

## AI in Generative Work

AI agents can contribute to generative work:

| Phase | AI Contribution |
|-------|-----------------|
| **Exploration** | Generate variant ideas, research existing solutions |
| **Prototyping** | Create draft versions of variants |
| **Evaluation** | Assess variants against criteria |
| **Documentation** | Capture rationale, create decision records |

Human judgment typically drives final selection, but AI can accelerate exploration and provide analysis.

---

## Related

- [Ontology: Decision](../01-concepts/ontology-2-normative-layer.md#decision)
- [Ontology: Goal](../01-concepts/ontology-2-normative-layer.md#goal)
- [Review-Based Work](./review-based-work.md) — Evaluation phase of generative work
- [Artifact-Centric Work](./artifact-centric-work.md) — Refinement after direction is chosen
