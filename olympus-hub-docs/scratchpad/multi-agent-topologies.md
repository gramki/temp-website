# Multi-Agent Topologies - Q&A Archive

> **Status**: Archived - Questions resolved and guides implemented  
> **Implementation**: [Multi-Agent Topology Guides](../../olympus-seer-docs/seer-design/guides/multi-agent-topologies/README.md)

Questions resolved during planning phase for topology guides.

---

## 1. Market-Based / Auction Topology

**Pattern Description:** Tasks are broadcast; agents bid based on cost/confidence/availability; scheduler assigns to best bid.

**Questions:**

1.1. **Bidding Mechanism**: How do agents express bids in Hub?
- Is a "bid" just a task update with cost/confidence fields?
- Or do agents create competing child requests?
- Or is there a dedicated bidding signal/update type?
> Hub does not exatly recognize the notion of 'bid'. It doens't need to.
> Hub or SX doesn't provide a 'scheduler' or 'judge' assessing a winner of a bid. It could be just another agent or app that is making this assessment in the composite.
> Bids can be modeled as update to tasks.
> The judge can wait until sufficient bids are placed or for a timeout (see hub's scheduling capabilities) and elect the winner.
> All of the bid and win process could be an arrangement between co-operating agents/apps.

1.2. **Scheduler/Assigner**: Who evaluates bids and assigns the task?
- Is this a dedicated Hub Application (Assigner) in a composite?
- Or is it the task queue allocation algorithm?
- Or is it the original task creator?
> answered

1.3. **Bid Evaluation**: What data is available for bid evaluation?
- Agent availability? (Is this exposed via Hub?)
- Agent past performance?
- Agent-declared confidence?

**Your Answer:**
> answered above
> this could vary across ensembles. hub or seer doesn't impose anything

---

## 2. Peer-to-Peer (Swarm) Topology

**Pattern Description:** No single controller; agents communicate laterally; global behavior emerges from local interactions.

**Questions:**

2.1. **Lateral Communication**: In Hub, all communication flows through Request state. Agents don't message each other directly. Is this sufficient for swarm patterns?
- Should we document this as a limitation?
- Or is Request state-based coordination considered "lateral" for our purposes?
> Request state based communication can be considered as an equal enabler for lateral interaction.
> However, hub has specific targeted communication mechanism called Memos. Agent A can add a memo with scope of Agent B as the subject. That memos is then meant to be addressed/tagged to B. 
> Alternatively, there are thoughts that can be written and agent a can tag agent B in the thoughts. 
> Yet another alternative, A and B can communicate completely out-of-bad without going through SX. The Raw agents these employed agents are based on can give such communication channel.

2.2. **Emergence**: How do we explain "emergent behavior" in the context of Hub's structured Request model?
- Is it simply that multiple agents react independently to same updates?
- Is there a mechanism for agents to "discover" each other?
> Agents can discover each other from directories; Directories can be made available as tools
> Agents can introduce other agents to a request by adding them as assignees.
> Request is a collaboration substrate, not exactly a enforcer of any sequence or coordination pattern. 
> Let me know if you still have questions here

2.3. **Suitability**: Is Peer-to-Peer/Swarm even a recommended pattern for Hub, or should we document it as "partially supported" with caveats?

**Your Answer:**
>answered above. It is supported without any prejudice of its suitability to any usecase

---

## 3. Role-Specialized Committees Topology

**Pattern Description:** Multiple agents with fixed roles review same problem; final decision via consensus, voting, or arbiter.

**Questions:**

3.1. **Voting Mechanism**: How do committee members cast votes?
- Each agent updates Request with their vote?
- Each agent creates a "perspective" record in Request state?
- Is there a voting-specific update type?
> An ensemble may model a Task called 'Poll'
> The agents who are aware of 'poll' can participate with their votes
> Hub doesn't natively recognize such an update type. 

3.2. **Consensus Detection**: Who detects that consensus has been reached?
- Is it the arbiter/coordinator app in the composite?
- Is it a sentinel watching for quorum?
- Is it built into Request state machine?
> just as in auction

3.3. **Tie-Breaking**: How is a tie-breaker/arbiter implemented?
- Dedicated Hub Application that aggregates votes?
- OPA filter that only activates arbiter when votes are split?
- Manual escalation to supervisor?

**Your Answer:**
> as in auction topology

---

## 4. Hierarchical (Multi-Level Orchestration) Topology

**Pattern Description:** Manager → sub-managers → workers; multiple layers of orchestration.

**Questions:**

4.1. **Sub-Manager Coordination**: How do sub-managers receive work from the top-level manager?
- Child requests with parent-child hierarchy?
- Tasks assigned to sub-manager agents?
- Both (sub-manager is a Scenario-as-Agent that creates child requests)?
> both

4.2. **Cross-Layer Communication**: How do results propagate back up the hierarchy?
- Child request completion updates parent?
- Task completion triggers parent request update?
- Explicit aggregation by manager app?

**Your Answer:**
> child request completion updates parent
> child agent can explicitly trigger updates to parent request

---

## 5. Cognitive Twin / Shadow Agents Topology

**Pattern Description:** One agent proposes action; shadow/twin simulates or checks; actions gated by shadow evaluation.

**Questions:**

5.1. **Gating Mechanism**: How does the primary agent wait for shadow approval?
- Synchronous call via Scenario-as-Tool?
- Poll Request state for shadow's evaluation update?
- State machine transition blocked until shadow completes?

> Primary waits for an update to the Proposal Task it published and assigned to shadow 
> Shadow updates the task with its assessment
> Primary gets notified and picks follow-on action

5.2. **Shadow Scope**: Does the shadow evaluate in its own child request, or in the same request?
- Same request (both in composite)?
> Possible
- Child request (shadow scenario invoked as tool)?
> Possible
- Separate request via Request Sentinel enrollment?
> Not a good usecase. The Primary should be aware of shadow in this toplogy, i guess

5.3. **Action Blocking**: If shadow rejects, how is the action prevented?
- Primary app checks shadow result before acting?
> yes
- Request state machine enforces?
- OPA filter blocks the action update?
> A guardrail to this effect could be added to this Scenario

**Your Answer:**
>

---

## 6. General Questions

6.1. **Multi-Runtime Examples**: For each topology, should I show:
- Seer-only example (all apps are Seer agents)?
- Multi-runtime example (Seer + Rhea + Atlantis)?
- Both where applicable?

**Your Answer:**
> (Already answered: Both)

6.2. **Diagram Style**: Should architecture diagrams use:
- ASCII art (consistent with existing docs)?
- Mermaid (richer, but different from some existing docs)?
- Both?

**Your Answer:**
> Mermaid

6.3. **Sentinel Examples**: For which topologies should I include sentinel examples?
- Cognitive Twin (Request Sentinel as shadow)
- Swarm (health monitoring)
- Others?

**Your Answer:**
> (Already answered: Where they add value)

---

## Summary

All gaps resolved. Implementation complete in `olympus-seer-docs/seer-design/guides/multi-agent-topologies/`:

| Topology | Guide |
|----------|-------|
| Manager-Worker | `01-manager-worker.md` |
| Hierarchical | `02-hierarchical.md` |
| PEC Loop | `03-planner-executor-critic.md` |
| Blackboard | `04-blackboard.md` |
| Market-Based | `05-market-based-auction.md` |
| Peer-to-Peer | `06-peer-to-peer-swarm.md` |
| Committees | `07-role-specialized-committees.md` |
| Event-Driven | `08-event-driven-reactive.md` |
| Cognitive Twin | `09-cognitive-twin-shadow.md` |

---

*Archived: 2026-01-15*
