# Cognitive Operations Steward (COS)

> **Status:** Reference Document  
> **Last Updated:** 2026-01-09  
> **Related:** [Role Definitions](./roles.md) | [ARE Reference](./are.md)

---

## The Problem COS Solves

Agents don't just fail technically — they can degrade *cognitively*.

A healthy agent might slowly become:
- Confused about its purpose
- Inconsistent in its reasoning
- Drifting from intended behavior
- Misaligned with user expectations
- Confident while being wrong

Traditional monitoring catches crashes and latency spikes. It doesn't catch an agent that's "working" but thinking poorly.

**COS exists because someone has to watch whether agents are thinking well, not just running.**

---

## The COS Mandate

> **COS owns day-to-day cognitive health of agents.**

This means:

| COS Owns | COS Does NOT Own |
|----------|------------------|
| Ongoing behavior review | Runtime safety controls (ARE) |
| Drift and confusion detection | Agent design (CSA) |
| Feedback loops to other roles | Agent implementation (AE) |
| Behavioral quality monitoring | Business outcomes (APO) |
| Issue routing and triage | Risk and compliance (ARAO) |

**The distinction matters.** COS doesn't fix problems — COS *finds* them and routes them to the right owner. ARE handles system health. COS handles cognitive health.

---

## Why This Role Is Different

### It's Not Operations (ARE)

ARE monitors whether agents are running safely. COS monitors whether agents are *thinking* soundly.

| ARE Focus | COS Focus |
|-----------|-----------|
| Latency and errors | Reasoning quality |
| Cost and resource usage | Behavioral consistency |
| Kill switches and limits | Drift and confusion |
| Incident response | Issue discovery |
| Availability | Usefulness |

### It's Not Quality Assurance

QA validates before release. COS monitors *continuously* in production.

### It's Not the Agent Product Owner

APO defines what agents should do. COS detects when they're not doing it well.

---

## What COS Cares About

### 1. Is the Agent Behaving as Intended?

Intent comes from APO. COS watches for:

| Signal | Question |
|--------|----------|
| Goal alignment | Is the agent pursuing the right objectives? |
| Scope creep | Is the agent doing things it shouldn't? |
| Decision patterns | Are decisions consistent with policy? |
| User feedback | Are users satisfied or frustrated? |

**If intent is drifting, APO needs to know.**

---

### 2. Is the Reasoning Consistent?

Agents should reason consistently over time. COS watches for:

| Signal | Question |
|--------|----------|
| Similar inputs, different outputs | Is the agent inconsistent? |
| Confidence without basis | Is the agent confabulating? |
| Degrading quality | Are decisions getting worse? |
| Pattern breaks | Did something change unexpectedly? |

**If reasoning is inconsistent, CSA needs to know.**

---

### 3. Is the Agent Confused?

"Confusion" means the agent doesn't understand its situation:

| Confusion Sign | Example |
|----------------|---------|
| Wrong tool selection | Using calculator for text tasks |
| Misunderstood context | Treating a question as a command |
| Circular reasoning | Going in loops without progress |
| Inappropriate confidence | Strong answers to unclear questions |

**If the agent is confused, AE or CSA needs to know.**

---

### 4. Is Drift Occurring?

Drift is gradual change in behavior:

| Drift Type | Cause |
|------------|-------|
| Prompt drift | Prompt changes accumulate |
| Knowledge drift | Underlying data changed |
| Model drift | Model version changed |
| Context drift | Agent's world model became stale |

COS detects drift before it becomes a problem.

**If drift is undetected, agents slowly become wrong.**

---

### 5. Are Users Satisfied?

Ultimately, agents serve users. COS tracks:

| Signal | Meaning |
|--------|---------|
| Override frequency | Users don't trust the agent |
| Escalation patterns | Agent can't handle the work |
| Rework requests | Agent output needs correction |
| Abandonment | Users give up on the agent |
| Feedback sentiment | Explicit user reactions |

**If users are frustrated, someone needs to investigate.**

---

## What COS Owns

### Behavioral Signals

| Signal Category | Examples |
|-----------------|----------|
| Decision quality | Accuracy, consistency, appropriateness |
| Reasoning health | Coherence, grounding, confidence calibration |
| User experience | Satisfaction, trust, utility |
| Alignment | Intent match, scope adherence |

---

### Detection Capabilities

| Detection Type | Method |
|----------------|--------|
| Anomaly detection | Statistical deviation from baseline |
| Pattern matching | Known problematic behaviors |
| Sampling review | Human-in-the-loop spot checks |
| User feedback | Explicit signals from users |
| Cross-agent comparison | Agents handling similar work |

---

### Feedback Routing

COS doesn't fix issues — COS routes them:

| Issue Type | Route To | Action Expected |
|------------|----------|-----------------|
| Intent misalignment | APO | Clarify or redefine intent |
| Design flaw | CSA | Revise cognitive design |
| Implementation bug | AE | Fix code or prompts |
| System reliability | ARE | Investigate operational issue |
| Compliance concern | ARAO | Assess risk and policy |
| Knowledge issue | KMO | Correct or update knowledge |

---

### Cognitive Health Metrics

| Metric | What It Measures |
|--------|------------------|
| Consistency score | Same inputs → similar outputs |
| Confidence calibration | Confidence matches accuracy |
| Drift index | Deviation from baseline behavior |
| User trust score | Override and escalation rates |
| Reasoning coherence | Logical flow in explanations |

---

## How COS Works With Others

| Role | COS's Relationship |
|------|-------------------|
| **APO** | COS reports intent misalignment; APO decides if intent should change. |
| **CSA** | COS reports design-related issues; CSA investigates and revises. |
| **AE** | COS reports bugs and prompt issues; AE investigates and fixes. |
| **ARE** | COS shares observability data; ARE handles system health. |
| **KMO** | COS reports knowledge-related issues; KMO investigates sources. |
| **ARAO** | COS flags compliance concerns; ARAO assesses and decides. |

---

## COS vs. ARE: The Observability Split

| Concern | Owner |
|---------|-------|
| **System health** (uptime, latency, errors, cost) | ARE |
| **Cognitive health** (drift, confusion, quality, consistency) | COS |

They share observability infrastructure but focus on different signals.

---

## Enterprise Learning: Pattern Detection

COS plays a critical role in Enterprise Learning by detecting patterns worth promoting to higher memory levels.

### What COS Detects

| Pattern Type | Detection Signal | Promotion Candidate |
|--------------|------------------|---------------------|
| **Recurring decisions** | Same conclusion across agents | Semantic memory |
| **Stable corrections** | Consistent user overrides | Knowledge update |
| **Emergent best practices** | High-quality patterns | SOP candidate |
| **Cross-agent learning** | One agent's success helps others | Shared memory |
| **Knowledge gaps** | Repeated failures in same area | Knowledge request |

---

### COS Role in Promotion Workflow

```
COS detects pattern
      ↓
COS validates pattern is stable (not noise)
      ↓
COS flags to KMO with evidence
      ↓
KMO evaluates for promotion
      ↓
(After promotion)
COS verifies promotion had intended effect
```

---

### Detection Triggers

| Trigger | COS Action |
|---------|------------|
| Same decision made by 3+ agents | Flag for semantic memory consideration |
| User override pattern > 10 occurrences | Flag for knowledge review |
| Agent success rate improves after learning | Flag as best practice candidate |
| New failure mode emerges | Flag as knowledge gap |
| Conflicting agent behaviors | Flag for resolution |

---

### What COS Does NOT Do in Enterprise Learning

| Activity | Who Does It |
|----------|-------------|
| Approve promotions | KMO (routine), KMO + ARAO (sensitive) |
| Update knowledge | KMO |
| Modify agent behavior | AE |
| Set retention policies | KMO |

COS detects and flags. KMO decides and acts.

---

## What COS Does NOT Do

| Responsibility | Who Owns It |
|----------------|-------------|
| Define agent intent | APO |
| Design reasoning | CSA |
| Implement fixes | AE |
| Operate runtime safety | ARE |
| Approve compliance | ARAO |
| Curate knowledge | KMO |

COS watches and routes. Others own and fix.

---

## The COS Skill Profile

### Analytical Mindset

- Pattern recognition in agent behavior
- Statistical understanding for anomaly detection
- Root cause analysis (to route correctly)
- Ability to distinguish noise from signal

### Agent Literacy

- Understanding of how agents reason
- Familiarity with common failure modes
- Ability to read reasoning traces
- Knowledge of agent architecture patterns

### Communication

- Clear issue documentation
- Effective handoff to other roles
- Escalation judgment (when to escalate, when to wait)
- Cross-functional collaboration

### User Empathy

- Understanding of user expectations
- Ability to interpret user feedback
- Appreciation for user experience impact
- Connecting behavior issues to user outcomes

---

## Anti-Patterns

| Pattern | Why It's Dangerous |
|---------|-------------------|
| "The agent is running, so it's fine" | Running ≠ thinking well |
| "Metrics look good" | Operational metrics don't catch cognitive issues |
| "That's an edge case" | Edge cases reveal deeper problems |
| "Users will adapt" | Users shouldn't work around agent flaws |
| "We'll catch it in the next release" | Drift compounds if unaddressed |
| "It's not my job to fix it" | Correct — but it's your job to find it and route it |

---

## Success Criteria

COS is successful when:

- Cognitive issues are detected early
- Issues are routed to the right owner
- Drift is caught before users notice
- User feedback is incorporated into improvements
- Other roles trust COS's observations
- Agent quality improves over time (not just at release)

---

## Final Word

When someone asks:

> "Is this agent actually helping?"

COS's job is to answer:

> "Here's what the behavioral data shows — and here's where we need to investigate further."

If an agent slowly degrades and no one notices, there's no steward watching.

**Agents can fail while running perfectly. COS catches the failures that metrics miss.**

---

*End of document*

