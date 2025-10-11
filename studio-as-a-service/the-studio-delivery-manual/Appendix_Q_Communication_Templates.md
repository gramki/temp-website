# Appendix Q — Communication Templates (Exec‑Friendly Scripts)

Purpose: Provide concise, options‑first scripts for common delivery scenarios. Use VP‑calm tone; state the signal and the ask; present options with impacts. Prefer decisions in forums; use these to pre‑wire or follow‑up. Pair with Appendix M (Decision/Evidence templates).

Conventions
- Frame: signal → implication → options → ask
- Tone: calm, factual, no blame; name owners and dates
- Attach: M.6 Evidence Pack link when asking to decide; add Decision Paper (M.1) for Steering

---

## Q.1 Capacity shortfall (last resort add‑people)
Subject: Capacity guardrail breach — options to protect delivery

Executive summary
- Signal: Capacity Health Score = 58 (< 60 guardrail) for two weeks; Ready backlog runway = 1 sprint
- Implication: Risk to meeting next milestone without quality debt rising
Options
- A) Re‑sequence scope to fit funded capacity (no cost; slip non‑critical items by 2 sprints)
- B) Fund additional capacity for 2 sprints (cost $[REDACTED]; onboarding tax ~1 sprint)
- C) Reduce non‑functional scope temporarily with a lighter control (exception with reversion date)
Ask
- Recommend A + partial B for critical path; decision at Weekly→Steering on <date>. Evidence: [link]

Lighter control note (10.4)
- If C chosen, propose explicit reversion on <date> and Evidence Pack to restore control.

---

## Q.2 Integration dependency slipping
Subject: Critical dependency variance — decision to re‑sequence or fund

Executive summary
- Signal: Provider quota approval missed by 2 weeks; DependencyFunding% = 50%
- Implication: Block on Features FEA‑210/211; idle burn $12.5k/day
Options
- A) Re‑sequence behind dependencies; hold date for unaffected scope
- B) Fund expedite/premium fee (cost $[REDACTED])
- C) De‑scope integration stage 1 and demo partial value
Ask
- Recommend A; if B approved, proceed with expedite. Decision at Monthly on <date>. Evidence: [link]

---

## Q.3 Error budget exhausted (stabilize before speed)
Subject: Quality gate — error budget depleted; stabilization plan

Executive summary
- Signal: Error budget remaining = 12% (< 20% min); P0/P1=0; flake 3.5%
- Implication: New feature intake risks incidents; credibility risk
Options
- A) Two‑sprint stabilization: flake repair, add critical‑path tests; pause net‑new intake
- B) Proceed with limited intake under stricter gates; smaller hardening window
Ask
- Recommend A; Steering acknowledgement to pause net‑new until budget ≥ 20%. Evidence: [link]

---

## Q.4 Scope change mid‑increment (SFM)
Subject: Unfunded exposure — change options

Executive summary
- Signal: Unfunded CR exposure = 18% (> 10%); FVS = 62 (Watch)
- Implication: Date hardening is unsafe without funding or scope change
Options
- A) Fund gap $[REDACTED]
- B) De‑scope $[REDACTED] (lowest value)
- C) Re‑sequence to reduce near‑term exposure
Ask
- Recommend A+B split; decision at Steering on <date>. Decision Paper: [link]

---

## Q.5 RfP shelf‑life expired (re‑affirm)
Subject: RfP shelf‑life breach — re‑affirmation needed

Executive summary
- Signal: 7 Features > 90 days since RfP sign‑off; 5 are integration‑tagged
- Implication: Acceptance risk due to drift; dashboards stale for planning
Options
- A) Re‑affirm as‑is in a fast workshop; extend shelf‑life 30 days
- B) Adjust AC/NFR with current constraints; re‑sign
- C) Park low‑value Features; replace with higher‑ready items
Ask
- Recommend A+B for top 5; workshop on <date>. Evidence: [link]

---

## Q.6 Exception request (lighter control)
Subject: Time‑boxed exception to <control> with reversion date

Executive summary
- Signal: <control> blocks near‑term goal; risk surfaces identified and accepted
- Implication: Without a lighter control, delivery date slips by ~1 sprint
Proposal
- Replace <control> with <lighter‑control> until <reversion‑date>; owner <role>
- Evidence: tests/monitoring planned; rollback defined
Ask
- Approve exception; review at Monthly on <date>; convert to policy or revert. Record in M.2.

---

## Q.7 Dependency financial risk (SFM/TCM)
Subject: Dependency financial risk rising — options to reduce idle burn

Executive summary
- Signal: Dependency Financial Risk = $[REDACTED]/week; variance > 2 cycles
- Implication: Idle burn and rework cost risk
Options
- A) Re‑sequence; reduce idle; move catch‑up work earlier
- B) Fund temporary scope swap (equal cost) to keep teams productive
- C) Escalate to provider to obtain committed date or workaround
Ask
- Recommend A+C; Monthly decision on <date>. Evidence: [link]

---

## Q.8 Governance change event (leadership turnover)
Subject: Governance change — continuity pack and next steps

Executive summary
- Signal: New <CIO/CTO/CRO>; prior decisions at risk of reinterpretation
- Implication: Freeze on new hardening until re‑affirmation
Options
- A) Present continuity pack (Appendix O) and re‑affirm RfP items
- B) Re‑sequence behind committed dependencies; avoid unfunded exposure
- C) Park low‑value items; focus on integration readiness and quality gates
Ask
- Recommend A+B; Steering check‑in on <date>. Evidence: [link]

---

Usage Notes
- For each template: fill <date>, costs, and attach an Evidence Pack (M.6). Use Decision Paper (M.1) when asking Steering to choose among options. For exception requests, file M.2 with reversion date.
- Use labels from Appendix L (e.g., `process-exception`, `integration-risk`, `RfP`).
