# Research Task

**Model:** Work Model
**Track:** Track 1: The Discovery Track (Learning)
**Owner:** Product Manager, UX Researcher

## Definition

A targeted investigation action — specific data gathering, user interviews, competitive analysis, market sizing, regulatory review — to produce evidence for or against a hypothesis or to answer a specific question. Research Tasks are focused and convergent: you know what question you're trying to answer.

## Purpose

Research Tasks produce the empirical evidence that informs product decisions. They are primarily used during **Idea Validation** — gathering specific evidence to support or challenge a hypothesis — but can also be spawned during Signal Exploration when specific data is needed to understand a Signal's context.

Research Task is distinct from **Signal Exploration Task**, which is the divergent, open-ended work of understanding a Signal and synthesizing Ideas. Research Tasks are convergent and evidence-oriented; Signal Exploration is divergent and hypothesis-generating. The distinction matters because conflating "understand the terrain" with "test the hypothesis" obscures the critical phase transition from exploration to validation (see FAQ Q20).

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | What specific question this research answers |
| Question | Text | The specific question or hypothesis being investigated |
| Method | Enum | `Interview` / `Data Analysis` / `Competitive Analysis` / `Market Sizing` / `Regulatory Review` / `Other` |
| Findings | Text | What was learned |
| Supports Idea | Reference (Dim 1) | Which Idea this research validates/invalidates (if applicable) |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| To Do | Not yet started |
| In Progress | Investigation underway |
| Done | Findings documented |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May support | Signal Exploration Task (Track 1) | May be spawned to gather specific data during exploration |
| Validates | Idea (Dim 1) | Research Task validates/invalidates an Idea |
| Referenced by | Product Decision Record (Dim 1) | PDR cites this Research Task as evidence |
| Sibling | Experiment (Track 1) | Both produce evidence for Idea Validation |
| Sibling | Prototype / Spike (Track 1) | Both produce evidence for Idea Validation |

## Example

- "Conduct 5 user interviews on FX rate-lock workflow to validate Idea: one-click FX lock"
- "Pull usage data to quantify batch payout demand (for Idea: CSV/SFTP batch ingestion)"
- "Run competitor API analysis: how does Competitor X handle multi-currency settlement?"
