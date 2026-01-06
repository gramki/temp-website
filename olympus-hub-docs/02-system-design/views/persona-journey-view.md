# Persona Journey View

> **How users experience the system**

---

## Audience

- Product Managers
- UX Designers
- Solution Architects

---

## Overview

This view shows how different personas interact with Olympus Hub throughout their work. It maps the key touchpoints, channels, and workflows for each persona type.

---

## Persona Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         HUB PERSONAS                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   CONFIGURATION PERSONAS              OPERATIONAL PERSONAS                   │
│   ─────────────────────               ────────────────────                   │
│                                                                              │
│   Process Architect                   Supervisor                             │
│   "I design how work should be done"  "I oversee team execution"             │
│                                                                              │
│   Developer                           Agent (Operator)                       │
│   "I build the automations"           "I do the work"                        │
│                                                                              │
│   Administrator                       Business Customer                      │
│   "I configure the platform"          "I request services"                   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Process Architect Journey

**Goal:** Design operational scenarios that define how work should be done.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROCESS ARCHITECT JOURNEY                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. ANALYZE                 2. DESIGN                  3. SPECIFY           │
│   ────────                   ────────                   ───────              │
│   Understand the             Create Scenario            Document in          │
│   business problem           structure                  Normative Spec       │
│                                                                              │
│   ┌─────────────┐           ┌─────────────┐           ┌─────────────┐       │
│   │ Stakeholder │           │ Workbench   │           │ Workbench   │       │
│   │ Interviews  │──────────▶│ Studio      │──────────▶│ Studio      │       │
│   │             │           │ (Design)    │           │ (Normative) │       │
│   └─────────────┘           └─────────────┘           └─────────────┘       │
│                                                                              │
│   Outputs:                  Outputs:                  Outputs:               │
│   • Requirements            • Scenario structure      • Normative Spec CRD   │
│   • Process maps            • Roles and goals         • SOPs referenced      │
│                             • SOP outlines            • Decision criteria    │
│                                                                              │
│   4. VALIDATE               5. HANDOFF                                       │
│   ────────                  ───────                                          │
│   Review with               Pass to Developer                                │
│   stakeholders              for automation                                   │
│                                                                              │
│   ┌─────────────┐           ┌─────────────┐                                 │
│   │ Review      │           │ Workbench   │                                 │
│   │ Session     │──────────▶│ Studio      │                                 │
│   │             │           │ (Handoff)   │                                 │
│   └─────────────┘           └─────────────┘                                 │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Primary Channel:** Workbench Studio (Web)

---

## Developer Journey

**Goal:** Implement automations that execute scenarios.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEVELOPER JOURNEY                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. UNDERSTAND              2. BUILD                   3. TEST              │
│   ──────────                 ─────                      ────                 │
│   Review Normative           Create Hub                 Validate in          │
│   Spec                       Application                DEV workbench        │
│                                                                              │
│   ┌─────────────┐           ┌─────────────┐           ┌─────────────┐       │
│   │ Workbench   │           │ IDE +       │           │ Hub Test    │       │
│   │ Studio      │──────────▶│ Workbench   │──────────▶│ Runner      │       │
│   │ (View Spec) │           │ Studio      │           │             │       │
│   └─────────────┘           └─────────────┘           └─────────────┘       │
│                                                                              │
│   4. INTEGRATE               5. PROMOTE                                      │
│   ─────────                  ───────                                         │
│   Wire triggers,             Move to STAGING,                                │
│   tools, notifications       then PROD                                       │
│                                                                              │
│   ┌─────────────┐           ┌─────────────┐                                 │
│   │ Workbench   │           │ Promotion   │                                 │
│   │ Studio      │──────────▶│ Workflow    │                                 │
│   │ (Automate)  │           │             │                                 │
│   └─────────────┘           └─────────────┘                                 │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Primary Channels:** Workbench Studio (Web), IDE, REST API

---

## Supervisor Journey

**Goal:** Ensure team execution meets SLAs and quality standards.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SUPERVISOR JOURNEY                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DAILY ACTIVITIES                                                           │
│   ────────────────                                                           │
│                                                                              │
│   ┌───────────────────────────────────────────────────────────────────────┐ │
│   │                                                                        │ │
│   │   Morning Check          Throughout Day           End of Day           │ │
│   │   ─────────────          ──────────────           ──────────           │ │
│   │                                                                        │ │
│   │   Review queue           Handle                   Review               │ │
│   │   status                 escalations              performance          │ │
│   │                                                                        │ │
│   │   ┌─────────────┐       ┌─────────────┐         ┌─────────────┐       │ │
│   │   │ Supervisor  │       │ MS Teams    │         │ Supervisor  │       │ │
│   │   │ Desk        │       │ Me_Bot      │         │ Desk        │       │ │
│   │   │ (Queues)    │       │ (Alerts)    │         │ (Analytics) │       │ │
│   │   └─────────────┘       └─────────────┘         └─────────────┘       │ │
│   │                                                                        │ │
│   │   Actions:               Actions:                Actions:              │ │
│   │   • Reassign tasks       • Approve decisions     • Review SLA          │ │
│   │   • Adjust priorities    • Intervene on stuck    • Coach agents        │ │
│   │   • Spot issues          • Resolve escalations                         │ │
│   │                                                                        │ │
│   └───────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Primary Channels:** Supervisor Desk (Web), MS Teams (Me_Bot)

---

## Agent (Operator) Journey

**Goal:** Complete assigned tasks efficiently and correctly.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT JOURNEY                                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. RECEIVE                 2. INVESTIGATE            3. ACT                │
│   ───────                    ───────────               ───                   │
│   Get notified of            Review context,           Execute actions,      │
│   assigned task              gather info               use tools             │
│                                                                              │
│   ┌─────────────┐           ┌─────────────┐           ┌─────────────┐       │
│   │ MS Teams    │           │ Agent Desk  │           │ Agent Desk  │       │
│   │ Me_Bot      │──────────▶│ (Context)   │──────────▶│ (Tools)     │       │
│   │ (Alert)     │           │             │           │             │       │
│   └─────────────┘           └─────────────┘           └─────────────┘       │
│                                                                              │
│   4. DOCUMENT                5. COMPLETE                                     │
│   ────────                   ────────                                        │
│   Add memos,                 Mark complete,                                  │
│   record findings            record outcome                                  │
│                                                                              │
│   ┌─────────────┐           ┌─────────────┐                                 │
│   │ Agent Desk  │           │ Agent Desk  │                                 │
│   │ (Memos)     │──────────▶│ (Complete)  │                                 │
│   │             │           │             │                                 │
│   └─────────────┘           └─────────────┘                                 │
│                                                                              │
│   Or: ESCALATE                                                               │
│   ──────────                                                                 │
│   Escalate to higher tier if needed                                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Primary Channels:** Agent Desk (Web), MS Teams (Me_Bot), MCP (AI Assistant)

---

## Business Customer Journey

**Goal:** Request services and track status.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  BUSINESS CUSTOMER JOURNEY                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. INITIATE                2. PROVIDE INFO           3. TRACK              │
│   ────────                   ───────────               ─────                 │
│   File request               Submit details,           Check status,         │
│   via portal                 documents                 receive updates       │
│                                                                              │
│   ┌─────────────┐           ┌─────────────┐           ┌─────────────┐       │
│   │ Customer    │           │ Customer    │           │ Customer    │       │
│   │ Portal      │──────────▶│ Portal      │──────────▶│ Portal      │       │
│   │ (Start)     │           │ (Forms)     │           │ (Status)    │       │
│   └─────────────┘           └─────────────┘           └─────────────┘       │
│                                                                              │
│   Channels:                  Channels:                 Channels:             │
│   • Web Portal               • Web Portal              • Web Portal          │
│   • Mobile App               • Document upload         • Email notifications │
│   • MS Teams Ask_Bot         • MS Teams Ask_Bot        • SMS updates         │
│   • Call Center                                        • MS Teams Ask_Bot    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Primary Channels:** Customer Portal (Web/Mobile), MS Teams (Ask_Bot)

---

## Channel Matrix

| Persona | Web Console | MS Teams | MCP | REST API |
|---------|-------------|----------|-----|----------|
| **Process Architect** | Workbench Studio | - | ✓ | ✓ |
| **Developer** | Workbench Studio | - | ✓ | ✓ |
| **Administrator** | Hub Control Center | - | ✓ | ✓ |
| **Supervisor** | Supervisor Desk | Me_Bot | ✓ | ✓ |
| **Agent** | Agent Desk | Me_Bot | ✓ | ✓ |
| **Business Customer** | Customer Portal | Ask_Bot | - | - |

---

## Related Documentation

- [Persona](../implementation-concepts/persona.md)
- [Channel](../implementation-concepts/channel.md)
- [Agent Model](../agent-model.md)

