# Control Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Operations Desk](./README.md)  
> **Primary Persona:** [Agent Reliability Engineer (ARE)](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)

---

## Purpose

The Control Console enables the **Agent Reliability Engineer (ARE)** ([role definition](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)) to intervene in agent operations through kill switches, throttling, circuit breakers, and rollback capabilities.

---

## Sections

### Kill Switch Panel

Immediate agent shutdown controls.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ KILL SWITCH PANEL                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ⚠️  EMERGENCY CONTROLS - Requires confirmation                              │
│                                                                             │
│ FLEET-WIDE                                                                  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ [🛑 KILL ALL AGENTS]  │ Stop all agent execution immediately                │
│ [⏸️ PAUSE ALL]        │ Pause new task acceptance fleet-wide               │
│                                                                             │
│ BY AGENT CLASS                                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Class                │ Active │ Status   │ Actions                         │
│ expense-approver     │ 8      │ 🟢 Running│ [⏸️ Pause] [🛑 Kill]           │
│ invoice-processor    │ 12     │ 🟢 Running│ [⏸️ Pause] [🛑 Kill]           │
│ order-validator      │ 5      │ 🟡 Paused │ [▶️ Resume] [🛑 Kill]          │
│ data-enricher        │ 6      │ 🟢 Running│ [⏸️ Pause] [🛑 Kill]           │
│                                                                             │
│ BY INDIVIDUAL AGENT                                                         │
│ ──────────────────────────────────────────────────────────────────────────  │
│ [Search agent...                                             ]              │
│                                                                             │
│ expense-approver-07  │ 🔴 Killed │ Killed Jan 13, 14:22 │ [▶️ Restart]     │
│ order-validator-03   │ 🟡 Paused │ Paused Jan 12, 09:15 │ [▶️ Resume]      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Throttling Controls

Rate limiting and capacity management.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ THROTTLING CONTROLS                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ FLEET THROTTLE                                            Current: Normal   │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ○ Normal (100%)  ○ Reduced (75%)  ○ Minimal (25%)  ○ Emergency (10%)       │
│                                                                             │
│ BY AGENT CLASS                                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Class                │ Current      │ Max Rate   │ Actions                  │
│ expense-approver     │ 100%         │ 50/min     │ [Set: _____%]           │
│ invoice-processor    │ 100%         │ 100/min    │ [Set: _____%]           │
│ order-validator      │ 50%          │ 25/min     │ [Set: _____%]           │
│ data-enricher        │ 100%         │ 75/min     │ [Set: _____%]           │
│                                                                             │
│ SCHEDULED THROTTLES                                                         │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Maintenance Window: Sat 02:00-06:00 UTC → Minimal (25%)                     │
│ Peak Hours: Mon-Fri 09:00-17:00 UTC → Normal (100%)                         │
│                                                                             │
│ [Apply Changes] [Schedule] [History]                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Circuit Breakers

Automatic fault isolation.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CIRCUIT BREAKERS                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ACTIVE CIRCUITS                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Circuit              │ Status   │ Threshold │ Current │ Auto-Reset         │
│ ───────────────────────────────────────────────────────────────────────────│
│ expense-api          │ 🟢 Closed │ 5 failures│ 0       │ 60s                │
│ invoice-ocr          │ 🟢 Closed │ 3 failures│ 1       │ 30s                │
│ vendor-lookup        │ 🟡 Half   │ 5 failures│ 3       │ 120s               │
│ compliance-check     │ 🔴 Open   │ 3 failures│ 5       │ 180s (2:45 left)   │
│                                                                             │
│ CIRCUIT DETAIL: compliance-check                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Opened: Jan 13, 15:02                                                       │
│ Reason: 5 consecutive timeouts                                              │
│ Impact: 12 agents affected                                                  │
│ Fallback: Using cached compliance rules                                     │
│                                                                             │
│ [Force Close] [Extend Open] [Configure] [History]                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Rollback

Version rollback capabilities.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ROLLBACK                                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Agent: [expense-approver ▼]                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ CURRENT VERSION: v2.3.1                                                     │
│ Deployed: Jan 11, 2026 │ Health: 🟢 0.91                                    │
│                                                                             │
│ AVAILABLE ROLLBACK TARGETS                                                  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Version  │ Deployed     │ Duration     │ Final Health │ Action             │
│ v2.3.0   │ Jan 6, 2026  │ 5 days       │ 0.89         │ [Rollback]         │
│ v2.2.0   │ Dec 21, 2025 │ 16 days      │ 0.87         │ [Rollback]         │
│ v2.1.0   │ Dec 5, 2025  │ 16 days      │ 0.85         │ [Rollback]         │
│                                                                             │
│ ⚠️  Rollback will:                                                         │
│ • Stop all current instances of expense-approver                            │
│ • Deploy selected version to production                                     │
│ • Drain existing tasks (est. 2 min)                                         │
│                                                                             │
│ [Preview Rollback] [Execute Rollback]                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Immediate kill switch for agents**
- **Graduated throttling controls**
- **Circuit breaker monitoring and management**
- **One-click rollback with validation**
- **Audit trail of all control actions**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Control status visibility |
| **Predictable** | Circuit breaker guarantees |
| **Directable** | Kill switch, throttle, rollback |
| **Authority Enforceable** | Intervention authority |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
