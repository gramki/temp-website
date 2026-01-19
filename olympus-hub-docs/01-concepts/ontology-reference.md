# Ontology of Human–AI Team Operations

This reference explains every concept in the ontology and how they relate.  
Core runtime lifecycle (strict, no shortcuts): **Signal → Trigger → Scenario → Automation → Operation → Activity → Action**.

---

## Quick Navigation

| I want to... | Go to... |
|--------------|----------|
| Understand concepts quickly (glossary) | [Business Guide](./ontology-guide-business.md) |
| Configure workbenches and operations | [Operations Guide](./ontology-guide-operations.md) |
| Implement systems | [Technical Guide](./ontology-guide-technical.md) |
| See visual diagrams | [Ontology Diagrams](./ontology-diagrams.md) |

---

## Table of Contents

- [Reading Guides by Role](#reading-guides-by-role)
- [Introduction](#introduction)
- [Layer Documents](#layer-documents)
- [Layer Summaries](#layer-summaries)
  - [Perception Layer](#perception-layer--whats-happening)
  - [Normative Layer](#normative-layer--what-ought-to-be-done)
  - [Execution Layer](#execution-layer--how-is-it-done)
  - [Automation Layer](#automation-layer--how-is-it-codified-and-scaled)

---

## Reading Guides by Role

Different stakeholders need different levels of detail. Choose your guide:

| Guide | Audience | What You'll Find |
|-------|----------|------------------|
| [**Business Guide**](./ontology-guide-business.md) | Executives, Product Managers, Compliance, Audit | Glossary, key concepts, compliance-relevant sections |
| [**Operations Guide**](./ontology-guide-operations.md) | Ops Engineers, Workbench Designers, Team Leads | Workbench design, task management, configuration |
| [**Technical Guide**](./ontology-guide-technical.md) | Architects, Developers, Platform Engineers | Implementation guidance, data models, integration |

---

## Introduction

The ontology of Human–AI Team Operations is organized into **four layers**.  
Each layer represents a distinct way of knowing and acting in the system, from raw perception of the world to codified automations that can be executed at scale.  
This layered approach makes it easier to understand *what is happening*, *what ought to be done*, *how it is actually done*, and *how it is codified in systems*.

```
┌─────────────────────────────────────────────────────────┐
│  4. AUTOMATION LAYER — "How is it codified and scaled?" │
│     Automation, Automation Runtime, Tools, Registries    │
├─────────────────────────────────────────────────────────┤
│  3. EXECUTION LAYER — "How is it done?"                 │
│     Operation, Activity, Task, Agent, Escalation        │
├─────────────────────────────────────────────────────────┤
│  2. NORMATIVE LAYER — "What ought to be done?"          │
│     Role, Goal, SOP, Capability, Knowledge Base         │
├─────────────────────────────────────────────────────────┤
│  1. PERCEPTION LAYER — "What's happening?"              │
│     Domain, Workbench, Signal, Trigger, Scenario        │
└─────────────────────────────────────────────────────────┘
```

---

## Layer Documents

Each layer has its own detailed reference document:

| Layer | Question | Document | Key Concepts |
|-------|----------|----------|--------------|
| **1. Perception** | What's happening? | [ontology-1-perception-layer.md](./ontology-1-perception-layer.md) | Domain, Workbench, Environment, Machine, Sensors, Signal, Request, Trigger, Scenario, OPD |
| **2. Normative** | What ought to be done? | [ontology-2-normative-layer.md](./ontology-2-normative-layer.md) | Role, Goal, SOP, Responsibility, Capability, Capacity, Decision, Knowledge Base, Runbook, Checklist |
| **3. Execution** | How is it done? | [ontology-3-execution-layer.md](./ontology-3-execution-layer.md) | Operation, Procedure, Workflow, Case, Activity, Task, Escalation, Task Queue, Action, Agent, Human, AI Agent |
| **4. Automation** | How is it codified? | [ontology-4-automation-layer.md](./ontology-4-automation-layer.md) | Automation, Automation Runtime, Tool, Prediction/Decision Applications, Command, Tool Registry, Machine Registry |

**Visual Reference:** [Ontology Diagrams](./ontology-diagrams.md) — Class diagram and relationship graph

---

## Layer Summaries

### Perception Layer — *"What's happening?"*

The Perception Layer is concerned with **observing and interpreting reality**. It captures how the **environment** and its components—machines, sensors, data feeds—generate **signals**. These signals are then interpreted by **triggers** into meaningful **scenarios** that Human–AI teams must respond to.

It is descriptive, not prescriptive: this layer does not say what should be done, only what *is happening*. It is the sensory nervous system of the ontology.

**Example (Banking):**
- Login logs show 5 failed attempts in 2 minutes.
- A trigger interprets this signal and activates the scenario "Suspicious Login Attempt."

→ [Full Perception Layer Reference](./ontology-1-perception-layer.md)

---

### Normative Layer — *"What ought to be done?"*

The Normative Layer defines the **standards, rules, and goals** that shape expected behavior in a given scenario. It is *normative* because it encodes what ought to be done, not just what can be done.

Here we find **roles** (who is responsible), **goals** (what outcomes they must achieve), **responsibilities** (duties), **capabilities and capacities** (what they can do and how much), and **SOPs** (codified best practices). This layer also covers **decisions**, where agents—human or AI—choose a course of action.

**Example (Banking):**
- Role: Security Analyst.
- Goal: Prevent account takeover.
- SOP: Lock account after 3 failed attempts, notify the user.
- Decision: Escalate incident to fraud response team.

→ [Full Normative Layer Reference](./ontology-2-normative-layer.md)

---

### Execution Layer — *"How is it done?"*

The Execution Layer is where **work actually happens**. Here, normative rules and goals are operationalized into **operations**:
- **Procedures** (deterministic steps for a role),
- **Workflows** (deterministic binding of procedures across multiple roles), and
- **Cases** (non-deterministic, evolving collaborations across roles).

These operations prescribe **activities**, which in turn consist of atomic **actions** performed by **agents**—humans or AI—when agent involvement is required, often collaborating as a **Human–AI Team**. Some operations may be fully automated with no agent involvement.

**Example (Banking):**
- Procedure: Security analyst checks logs, verifies user, resets password.
- Workflow: Analyst investigates → IT resets account → Customer notified.
- Case: Fraud investigation evolves as new suspicious transactions are reported.

→ [Full Execution Layer Reference](./ontology-3-execution-layer.md)

---

### Automation Layer — *"How is it codified and scaled?"*

The Automation Layer represents the **codified definitions** of operations, and the systems that run them. Here, **automations** are the software representations of procedures, workflows, or cases. These definitions live inside an **automation system**, which is a software orchestration platform responsible for instantiating and supervising live operations.

This layer ensures consistency, scalability, and enforceability. It allows complex human–AI operations to be reliably repeated, monitored, and adapted by software systems.

**Example (Banking):**
- A BPMN workflow automation codifies suspicious login handling: lock account, notify user, reset password.
- The automation system (e.g., Olympus Hub) automatically instantiates and supervises this workflow when the suspicious login scenario is triggered.

→ [Full Automation Layer Reference](./ontology-4-automation-layer.md)

---

## Layering Summary

The four layers connect in sequence:

1. **Perception**: Detect what is happening.
2. **Normative**: Define what ought to be done.
3. **Execution**: Carry out what must be done.
4. **Automation**: Codify and scale how it is done.

Together they form a complete loop: from sensing reality, through norms and duties, into action, and finally into codified systems that sustain operations at scale.

---

## Document Index

| Document | Purpose |
|----------|---------|
| [ontology-reference.md](./ontology-reference.md) | This file — navigation hub |
| [ontology-guide-business.md](./ontology-guide-business.md) | Guide for executives, PMs, compliance |
| [ontology-guide-operations.md](./ontology-guide-operations.md) | Guide for ops engineers, designers |
| [ontology-guide-technical.md](./ontology-guide-technical.md) | Guide for architects, developers |
| [ontology-1-perception-layer.md](./ontology-1-perception-layer.md) | Perception Layer concepts |
| [ontology-2-normative-layer.md](./ontology-2-normative-layer.md) | Normative Layer concepts |
| [ontology-3-execution-layer.md](./ontology-3-execution-layer.md) | Execution Layer concepts |
| [ontology-4-automation-layer.md](./ontology-4-automation-layer.md) | Automation Layer concepts |
| [ontology-diagrams.md](./ontology-diagrams.md) | Visual diagrams |
| [collaborators.md](./collaborators.md) | Platform concept: Hub Personas working in workbench context |