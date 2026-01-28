# Identity, Authority, and Delegation: Scope Confusion Analysis

> **Status**: 🔴 Analysis  
> **Last Updated**: 2026-01-22  
> **Purpose**: Identify documentation issues where Identity, Authority, and Delegation appear Seer-specific but should be Hub-wide concepts

---

## Executive Summary

**Core Problem**: The documentation creates an impression that Identity, Authority, and Delegation are Seer-specific concepts, when they should be **foundational Hub concepts** that apply to ALL Hub agents (regardless of runtime: Seer, Rhea, Perseus, or custom).

**The Confusion**: 
- Readers may conclude that only Seer Agents have identity, authority, and delegation
- Non-Seer Hub Agents (Rhea, Perseus) appear to lack these capabilities
- The "Hub Agent vs Seer Agent" framework reinforces this by extensively detailing Seer identity while under-specifying Hub identity

---

## Sources of Confusion

### 1. **"Hub Agent Identity = Agent Persona" Under-Specification**

**Location**: `olympus-hub-docs/11-decision-frameworks/hub-agent-vs-seer-agent/hub-agent-vs-seer-agent-core.md` lines 53-71

**The Problem**:
The document states "Hub Agent identity = Agent Persona. Deployment identity is a runtime concern" but:
- Does not specify how Agent Persona is obtained for non-Seer Hub Agents
- Does not explain if Rhea/Perseus agents get identity the same way
- Creates impression that only Seer defines the identity model

**Quote that confuses**:
> "Hub doesn't require SPIFFE — it's runtime-specific"

This is technically correct but creates confusion: if Hub doesn't require SPIFFE, what DOES Hub require for identity? The document doesn't say.

**What's Missing**: Hub should define Agent Persona registration independently of Seer. Currently, all identity detail is in Seer docs.

---

### 2. **Authority Documentation Lives Primarily in Seer**

**Location**: Multiple Seer files, minimal Hub coverage

**The Problem**:
| Document | Location | Issue |
|----------|----------|-------|
| `authority-ceilings.md` | Seer only | No Hub equivalent |
| `authority-enforcement.md` | Seer only | No Hub equivalent |
| `delegation-chains.md` | Seer only | Hub has thin reference |
| `agent-authority-controls.md` | Hub scratchpad | Draft, incomplete, titled "in Seer" |

Authority concepts are fundamental to ANY Hub agent, but the authoritative documentation is all in Seer. This implies:
- Only Seer Agents have authority ceilings
- Only Seer Agents participate in delegation chains
- Non-Seer Hub Agents operate without governance

---

### 3. **Delegation Documents Point to Seer as "Authoritative Source"**

**Location**: 
- `olympus-hub-docs/02-system-design/implementation-concepts/request-scoped-delegation.md`
- `olympus-hub-docs/02-system-design/implementation-concepts/scenario-scoped-delegation.md`
- `olympus-hub-docs/02-system-design/implementation-concepts/agent-delegation.md`

**The Problem**:
All Hub delegation documents contain:
> **Authoritative Source:** [Delegation Chains (Seer)](...) 

Or:
> **Authoritative Source:** [Request-Scoped Delegation (Seer)](...) 

This creates a clear hierarchy where Seer owns delegation semantics and Hub is derivative. If delegation is a Hub concept that applies to all Hub agents, Hub should be authoritative.

---

### 4. **Cipher IAM Extensions = "Seer Extensions"**

**Location**: 
- `olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/`
- Title: "Cipher IAM Extensions" (for Seer)

**The Problem**:
The entire "Cipher IAM Extensions" subsystem is under Seer docs, implying:
- Agent profiles are Seer-specific
- Authority delegation is Seer-specific
- Two-layer identity model is Seer-specific

But these should be Hub-wide concepts. A Rhea-based Hub Agent should also:
- Have an Agent Profile in Cipher IAM
- Participate in delegation chains
- Have authority ceilings

Currently, the documentation doesn't explain how non-Seer agents get these capabilities.

---

### 5. **ADR-0129 Implies Seer-Specific Identity**

**Location**: `olympus-hub-docs/decision-logs/0129-agent-identity-model.md`

**The Problem**:
While stored in Hub decision-logs, the ADR repeatedly references Seer concepts:
- "Employed Agents" (Seer lifecycle term)
- SPIFFE (Seer runtime)
- Training Spec, Employment Spec (Seer artifacts)

The ADR title is generic ("Agent Identity Model") but content is Seer-focused. What about:
- Rhea agents?
- Perseus agents?
- Custom Hub Applications acting as agents?

---

### 6. **"Seer + Hub Division" Assigns Identity to Seer**

**Location**: `olympus-seer-docs/why-seer/appendices/appendix-b-seer-hub-division.md`

**The Problem**:
The responsibility matrix explicitly states:
> **Identity**: Agent identity, delegation chains (enterprise and request-scoped), two-layer identity model → **Seer Owns**

This clearly says Seer owns agent identity. But the "Hub Agent vs Seer Agent" framework says Hub Agents have Agent Persona identity. These are inconsistent.

If Hub owns work and Seer owns agents, what happens when a Hub Agent is NOT a Seer Agent?

---

### 7. **Employment Spec = Seer Only**

**Location**: Throughout Seer docs

**The Problem**:
Employment Spec is the artifact that configures:
- Delegation (scenario-scoped or request-scoped)
- Authority ceilings
- Work scope

But Employment Spec only exists for Seer Agents. What configures these for Rhea/Perseus agents?

---

### 8. **Title Confusion: "Agent Authority Controls in Seer"**

**Location**: `olympus-hub-docs/scratchpad/agent-authority-controls.md`

**The Problem**:
Even Hub's own scratchpad document is titled "Agent Authority Controls **in Seer**" — reinforcing that authority controls are Seer-specific.

---

## What Should Be True (But Isn't Documented)

### Hub Should Own (for ALL Hub Agents):

| Concept | Should Apply To | Current State |
|---------|-----------------|---------------|
| **Agent Persona** | All Hub Agents | Documented as Seer concept |
| **Agent Registration in Cipher IAM** | All Hub Agents | Only shown for Seer |
| **Delegation Templates** | All Hub Agents | Only in Seer's Cipher IAM Extensions |
| **Authority Ceilings** | All Hub Agents | Only documented for Seer |
| **Accountability** | All Hub Agents | Only documented for Seer |
| **Kill Switches** | All Hub Agents | Only documented for Seer |

### What Seer Adds (Beyond Hub Baseline):

| Concept | Seer-Specific | Notes |
|---------|---------------|-------|
| **SPIFFE ID** | Yes | Deployment identity for Atlantis runtime |
| **Raw → Trained → Employed lifecycle** | Yes | AI agent lifecycle |
| **Training Spec / Employment Spec** | Yes | AI-specific configuration |
| **Model Gateway** | Yes | LLM access |
| **Guardrails** | Yes | AI-specific constraints |

---

## Recommended Resolution Path

### Option A: Make Hub Authoritative for Identity/Authority/Delegation

1. Create Hub-level documentation for:
   - `agent-identity.md` (Hub concept, not Seer-specific)
   - `agent-authority.md` (Hub concept)
   - Move `agent-delegation.md` to be authoritative (not point to Seer)

2. Update "Seer + Hub Division" to:
   - Hub owns: Agent Persona, base delegation model, base authority concepts
   - Seer owns: Seer-specific extensions (SPIFFE, lifecycle, AI capabilities)

3. Create "Cipher IAM for Hub Agents" documentation separate from "Cipher IAM Extensions for Seer"

### Option B: Clarify Runtime-Neutral Hub Identity Model

1. Add explicit section in Hub docs: "Identity Model for Non-Seer Hub Agents"
2. Explain how Rhea/Perseus agents get:
   - Agent Persona registration
   - Delegation capabilities
   - Authority ceilings

3. Update ADR-0129 to be explicitly runtime-neutral or create Hub-specific ADR

### Option C: Accept Seer Dominance, Document the Gap

1. Explicitly state: "Full identity/authority/delegation requires Seer runtime"
2. Document that Rhea/Perseus agents have limited governance capabilities
3. This would be honest but may not match product intent

---

## Files Requiring Review/Update

### High Priority (Creates Confusion):

| File | Issue |
|------|-------|
| `hub-agent-vs-seer-agent-core.md` | Under-specifies Hub identity |
| `agent-delegation.md` | Points to Seer as authoritative |
| `request-scoped-delegation.md` | Points to Seer as authoritative |
| `scenario-scoped-delegation.md` | Points to Seer as authoritative |
| `appendix-b-seer-hub-division.md` | Says Seer owns identity |
| `0129-agent-identity-model.md` | Seer-focused despite being in Hub |

### Medium Priority (Missing Content):

| File | What's Needed |
|------|---------------|
| New: `hub-agent-identity.md` | Runtime-neutral Hub identity model |
| New: `hub-agent-authority.md` | Hub authority concepts |
| `cipher-iam-infrastructure.md` | How non-Seer agents register |
| `agent-model.md` | Clarify identity for all agent types |

### Low Priority (Terminology):

| File | Issue |
|------|-------|
| `agent-authority-controls.md` | Rename to remove "in Seer" |
| Various Seer docs | May need to clarify "Seer extends Hub" vs "Seer owns" |

---

## Key Questions to Resolve

1. **Is Agent Persona a Hub concept or a Seer concept?**
   - Current docs: Mixed/ambiguous
   - Recommended: Hub concept (Seer extends it)

2. **Can Rhea/Perseus agents have delegation chains?**
   - Current docs: Not addressed
   - Expected: Yes, if Hub owns delegation

3. **Who implements Cipher IAM Extensions?**
   - Current: Seer team
   - Should be: Hub team (with Seer using them)

4. **What's the minimum identity for a Hub Agent?**
   - Current: Unclear
   - Should be: Agent Persona in Cipher IAM (no SPIFFE required)

---

## Next Steps

1. [ ] Review with Hub architecture team
2. [ ] Decide on Option A, B, or C
3. [ ] Create migration plan for documentation updates
4. [ ] Update "Seer + Hub Division" based on decision
5. [ ] Create Hub-authoritative identity/authority/delegation docs if needed
