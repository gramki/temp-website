# Real Ledger Provider for Shadow Ledger 

## Context
A service (called Originating Service) is using an Integration Gateway service to integrate with a Destination Service to complete a financail transaction. As the transaction represents a substantial financial risk and the destination service is expected to be flaky and usually under stress, the gateway should have controls to ensure the exchange is reliable, reconcilable, and should be robust. The Gateway should handle any failures through compensating transactions to the destination service and where not possible should alert the business operations teams to verify and make necessary adjustments to the destination.

Given the transactions can be high value, the security controls at Gateway should ensure that the transactions are only initiated by the authorized personnel and there is no replay and abuse of any authorization/request.

> **Why not model the arrangement as a Payment Channel?**
>
> For those who are already familiar with a Payment Channel template, this integration represents yet another payment channel, albiet something thats not going through the payment switch. Why not therefore, use the Athena Payment Switch itself? Why not model this as a gyro transaction?
> * FC - Outward Clearing Relationship (For messages initiated from Tachyon)
> * FC - Inward Clearing Relationship (For messages initiated from Flexcube; Currently not in scope, but will be same as messages received from Mastercard or Visa)


## Controls Required for a safe implementation

### Message Exchange Controls
* Idempotency
* Deduplication and Reconciliation window 
* Flow Control and Sequencing of Operations to FC 
* Replay prevention
* Circuit breaker/backpressure
* Suspense records (like DLQs) for any unconfirmed exchange

### Security
* Authorization and Assurance (assurance that only an authorized human originator could have created a transaction)
* Non‑repudiation of Originator Message
* Privacy 

### Business Operations Enablement
* Error and Exception Visibility to User and Operations teams
* Financial reconcilation between systems and adjustment/compensation workflows
* Suspense Records aka Exception Management for Operations and Adjustments to FC
* Ops workflow and SLOs for any adjustments and suspense cases resolution

### Customer Servicing Enablement
* Transaction Status visibility for Customer Servicing teams
* Customer Disputes support

### SRE Operations Enablement
* Reliability and Operability for SREs
* Outbox + DLQ/Suspense Records
* DR/replayability
* Change safety
* Robust observability

### Fraud and Risk Enablement
* Fraud signals
* Ability to integrate with various fraud systems  


> **Why This Matters**
>
> The real-world application of this design primarily supports core banking and credit card systems that require reliable envelope that can enable various integrations and calculations over and above what the legacy systems support can support or handle. 
> For initial implementation, Savings and Current Accounts in Flexcube and Credit Card Accounts in VisionPlus are paired with corresponding accounts in Tachyon Kernel. By leveraging Tachyon Kernel, legacy systems like Flexcube and VisionPlus are shielded from frequent, direct interactions. Instead, last-synced data from these systems enables Tachyon Kernel to facilitate complex and advanced financial (and non-financial) transactions via an expanding ecosystem of applications.
>
> _This architectural choice reduces stress on legacy platforms and opens new possibilities for digital services, without compromising reliability or reconcilability._


## Components of the Solution
* Originator Proof: valdiation at the Integration Egress Gateway and replacement with the FC token
* Mutation Guard Pattern at RLP
* Timeout Handling: Enquiry, Compensating transactions, and Exception in Workbench
* Flow Control at Integration Egress Gateway and Back-pressure handling at SLP (Service unavailable error - from SLP, RLP, Integration Gateway)
* Orphaned Responses from RLP as Exceptions and Adjustments in the Workbench
* FC Integration Workbench - Knobs to flow control, disable integration, reconcile, force-post adjustments to FC, Message-level visibility (desensitized), hourly (or more frequent) message timeouts and orphaned message observations 
* Customer Services and Flows for RLP



## Gateway

Gateway models each Request from Orginator -> Gateway and all the consequent exchanges beween Gateway, Destination, and Originator of the Originator's message as a Gateway Message chain. 

The simplified representation of message exchange at Gateway is:
1. Originator sends a Request to Gateway to be forwarded to Destination
2. Gateway prepares a tracking record for the Originator's Request
3. Gateway forwards a Request to the Destination
4. After receiveing Response from the Destination, Gateway updates tracking record and also records the response
5. Gateway delivers the Response to the Originator
6. Gateway enquires the Originator to verify that it has processed the Response delivered against the Originator's Request appropriately. It records the Originator's response for the Enquiry as a evidence for closure of the processing of Originator's Request. 
7. All messages exchanged between Originator, Gateway, and Destination in context of a given Originator Request are tagged to the Reconciliation Batch at Gateway. 
8. Gateway Reconciles the Reconciliation Batch messages with Originator and Destination independently and provides the adjustments that need to be performed at Destination or Originator.
9. All enquiries and adjustments initiated by Gateway are recorded as messages in the same chain as that of the Originator's message and thus belong to the same reconciliation batch. For all such messages, the Originator is the Gateway.
  

Gateway tracks two related entities in the GatewayService database: the Message Chain (the end‑to‑end flow anchored by a `TraceId`) and individual Messages within that chain. Their record structures are:

Message Chain — Record Structure
| Field Name | Description |
|---|---|
| MessageChainId | Alias of `GatewayServiceMessageTraceId`; the Trace Id correlating all messages in the chain. If the Originator did not send a TraceId, the `OriginatingServiceMessageId` of the first (root) message is used. |
| RootOriginatingServiceMessageId | The `OriginatingServiceMessageId` of the root message in the chain. |
| RootOriginationTimestamp | The `OriginationTimeStamp` of the root message (UTC). |
| ReconciliationBatch | The Gateway reconciliation batch for the chain. Derived from the root origination timestamp. All messages inherit this batch. |
| ChainStateFlags | Composable flags describing current chain conditions (see Message Chain — State Model). Example: `["OPEN","IN_FLIGHT","SUSPENSE"]`. |
| SyncedWithOriginator | Boolean indicating there are no pending Originator‑side adjustments for this chain. |
| SyncedWithOriginatorByRunId | Gateway Reconciliation Run Id that concluded the chain is synced with Originator; null if not yet synced. |
| SyncedWithDestination | Boolean indicating there are no pending Destination‑side adjustments for this chain. |
| SyncedWithDestinationByRunId | Gateway Reconciliation Run Id that concluded the chain is synced with Destination; null if not yet synced. |
| HasSuspenseMessages | Boolean indicating at least one message in this chain is in Suspense. Drives batch summary counts.
| OriginatorCommunicatedOutcome | The final outcome communicated to the Originator for this chain (e.g., SUCCESS, FAILURE, SUSPENSE-DEFAULT-SUCCESS, SUSPENSE-DEFAULT-FAILURE). |
| OriginatorDefaultPolicyApplied | If the outcome was based on a suspense default policy, record the policy key/version (e.g., `default.debit.on-destination-suspense-is-faiolure.policy`). |
| IsInDispute | Boolean indicating whether a Dispute has been opened for this chain after initial communication. |
| DisputeCaseId | Reference to the Case Management system’s dispute case identifier, if `IsInDispute=true`. |
| OriginatorReconciliationBatchId | The external (Originator-side) reconciliation window/batch under which the Originator recognizes the posting for this chain (API or signed file). |
| OriginatorReconciliationRecordId | The Originator’s record identifier for this chain in that reconciliation window (e.g., ledger entry id, statement line id). |
| OriginatorReconciliationSource | Provenance for mapping: `API` or `FILE`. If `FILE`, store pointer to file metadata/digest in the audit log. |
| DestinationReconciliationBatchId | The external (Destination-side) reconciliation window/batch under which the Destination recognizes the posting for this chain. |
| DestinationReconciliationRecordId | The Destination’s record identifier for this chain in that reconciliation window. |
| DestinationReconciliationSource | Provenance for mapping: `API` or `FILE`. If `FILE`, store pointer to file metadata/digest in the audit log. |
| ClosedAt | Timestamp when the chain was sealed/closed; null if still active. |

Message — Record Structure
| Field Name | Description |
|---|---|
| GatewayServiceMessageId | ID generated by the Gateway; correlatable to the originator message id. |
| GatewayServiceMessageType | String indicating the message type as understood by the gateway. |
| GatewayServiceMessageTraceId | Trace Id (`MessageChainId`) this message belongs to. |
| OriginatingServiceMessageId | Id generated by the originating service of this message (idempotency key). |
| OriginationTimeStamp | Time of this message at origination in UTC. |
| ParentMessageId | For a derived/compensating message, the previous message’s id in the chain. Forms a linked list back to the root. |
| ParentOriginationTimestamp | The `OriginationTimeStamp` of the parent message. For a root message, this equals its own timestamp. |
| DestiantionRequestMessageId | ID of the request sent to the Destination for this message (destination idempotency key). |
| DestinationAckId | Id of the Response received from the Destination for this message. For timeouts without safe retry semantics, record "TIMEOUT"; after exhausted retries, record "RETRIES-EXHAUSTED". If no reliable identifier exists, use "D-" prefixed `OriginatingServiceMessageID`. |
| DestinationResponseCode | Response/processing code from the Destination for this message (for comprehension). |
| DestinationChangeLockId | ID of the lock acquired before attempting the Destination request for this message. |
| OriginatingServiceResponseAckLockId | Lock id acquired before dispatching the Destination response to the Originator. |
| OriginatingServiceResponseAckId | Id of the acknowledgement received from the Originator for this message (or enquiry response id when explicit ack is required). |
| OriginatingServiceResponseToResponseCode | Response code received in the enquiry to Originator after delivery of the Destination response; '00' if enquiry not required. |



For any Compensation Message initiated by the Gateway itself, the OriginatingService is the Gateway and TraceId is same as the TraceId of the message received from the Originating Service, the parent message id is the previous message in the trace. Any adjustment

Cross‑Window Realization and External Reconciliation References
 
Message Chain — State Model
* This is a composable flag model; multiple flags can be true at once (e.g., `SUSPENSE` and `SYNCED_WITH_ORIGINATOR`). Use `ChainStateFlags` to store the set.
* Flags
  * OPEN: Chain created; root message received.
  * IN_FLIGHT: At least one leg (Destination or Originator) is actively processing or awaiting retry/backoff.
  * SUSPENSE: One or more messages require further action or are awaiting external clarity (e.g., file/API confirmation). `HasSuspenseMessages=true`.
  * SYNCED_WITH_ORIGINATOR: All Originator‑side effects complete; `SyncedWithOriginator=true`.
  * SYNCED_WITH_DESTINATION: All Destination‑side effects complete; `SyncedWithDestination=true`.
  * DISPUTE_OPENED: A Dispute case is linked; customer outcome change, if any, is managed via the Dispute workflow.
  * CLOSED: No further adjustments remain; Disputes may remain linked; `ClosedAt` set.
* Transition Notes (non‑linear)
  * Set IN_FLIGHT on send to Destination or while awaiting Originator ack/enquiry.
  * Add SUSPENSE when actions remain or certainty is pending; remove when conditions for “not in Suspense” are met.
  * Add SYNCED_WITH_ORIGINATOR or SYNCED_WITH_DESTINATION independently when respective sides are complete; these flags can coexist with SUSPENSE if the other side is pending.
  * Add DISPUTE_OPENED when a Dispute is created; it does not block other flags.
  * Set CLOSED when SUSPENSE is cleared and no further adjustments remain.
* Effects of a message (including Gateway‑originated adjustments) may be recognized by the Originator and/or Destination in a later reconciliation window than the Gateway’s `ReconciliationBatch`. For example, a timeout followed by a safe re‑drive may land in the next hour’s statement at the Destination.
* To maintain provable traceability across windows, chain‑level records maintain authoritative external reconciliation mappings (batch id, record id, source) for both Originator and Destination. Message‑level records inherit these mappings implicitly; message‑specific external ids may be captured where needed for drilldown.
* Operationally, execution of adjustments should occur in the next open Gateway batch, while their external recognition may still appear in a later Originator/Destination batch; suspense aging and reports must reflect this separation.

### Reconciliation Batch

Statuses of a Reconciliation Batch
* Open: The first message from an Originator in a given reconciliation time window creates a new Reconciliation Batch at the Gateway. While Open, the batch accepts new root message chains (non-Gateway originator messages) whose `OriginationTimeStamp` falls within the batch window plus the allowed buffer (see `ReconciliationBatch` definition in the record structure above).
* Closed-for-new-Chains: The batch window has ended (including buffer). No new root chains from external originators are accepted into this batch. Existing chains within the batch can still progress (acks, retries, compensations, enquiries). Any new external root chains are attributed to the next batch.
* Reconciled-with-Originator: True if and only if the Originator is fully in sync with all message chains in the batch (per final Originator status); no Originator-side adjustments remain to be introduced. Disputes raised (if any) are linked but do not block this state.
* Reconciled-with-Destination: True if and only if the Destination is fully in sync with all message chains in the batch; no Destination-side adjustments remain to be introduced. Disputes raised (if any) are linked but do not block this state.
* Closed: The batch is eligible to close when there are no Suspense messages remaining in the batch. Disputed chains do not prevent closure. Upon close, produce a signed, immutable reconciliation report.

Note: `Reconciled-with-Originator` and `Reconciled-with-Destination` are independent states; reconciliation procedures may be executed in any order, and completion of one does not block or depend on the other.

State Transitions and Rules
* Open → Closed-for-new-Chains: Triggered automatically when the batch window (e.g., hourly) ends plus a 5-minute skew buffer. Manual early-close is allowed by Ops if downstream is impaired and backpressure is needed.
* Closed-for-new-Chains → Reconciled-with-Originator: Reached when Originator is fully in sync for all chains in the batch; no Originator adjustments remain pending (Disputes may exist).
* Closed-for-new-Chains → Reconciled-with-Destination: Reached when Destination is fully in sync for all chains in the batch; no Destination adjustments remain pending (Disputes may exist).
* Close condition: Batch may be Closed when there are zero Suspense messages in the batch. Disputed chains do not block closing; they remain linked for audit.

Reconciliation Batch — Summary
| Field | Description |
|---|---|
| BatchId | Identifier for the batch (e.g., `YYYYMMDDHH` + Originator route). |
| NumChains | Total number of message chains in the batch. |
| NumSuspenseChains | Count of chains with at least one message currently in Suspense. |
| HasSuspenseChains | Boolean derived from `NumSuspenseChains>0`. |
| NumDisputedChains | Count of chains marked `IsInDispute=true`. |
| HasDisputedChains | Boolean derived from `NumDisputedChains>0`. |
| ReconciledWithOriginator | Boolean: batch-level flag reflecting the state defined above. |
| ReconciledWithDestination | Boolean: batch-level flag reflecting the state defined above. |
| ClosedAt | Timestamp when the batch moved to Closed. |

Batch Identity and Scope
* Batch Id: Derive as `YYYYMMDDHH` (UTC) plus Originator identifier (or route) if multi-tenant; this is already implied by the `ReconciliationBatch` field.
* Inclusion Rule: All messages (requests, responses, enquiries, compensations) linked by the same `GatewayServiceMessageTraceId` and whose root chain’s `ParentOriginationTimestamp` falls within the batch window belong to this batch.
* Ordering: Within a chain, ordering is preserved by `ParentMessageId`; cross-chain ordering is not required for reconciliation, but adjustments must respect per-entity locks when executed.

Operational Guardrails
* No destructive operations during reconciliation; all proposals are adjustments expressed as new compensating messages.
* Per-entity locking (e.g., account) is enforced for executing adjustments to protect against race conditions with late-arriving acks.
* Every reconciliation run produces an auditable summary: counts, amounts, categories, and correlation IDs for each proposed adjustment.

> VP Insight
> In most core‑banking integrations, closing the batch on time and reconciling each side independently prevents small timing glitches from cascading into multi‑day outages. Independence also localizes blame: you can prove whether the gap is on the Originator, Gateway, or Destination side.

Common Reconciliation Mechanics (applies to both sides)
* Classify each chain by outcome using acks/codes, retries, and timeouts.
* Build an expected effect ledger (net debit/credit by entity) versus observed postings/acks.
* Detect gaps, categorize, and propose adjustments using the gap→action mappings below.
* Prefer signed reconciliation files as authoritative snapshots for end‑of‑batch, with APIs used for live checks and drilldowns.
* Authoritative outcome: Uphold the final Originator status as the canonical customer outcome. Prefer adjusting Destination to match Originator; any change to Originator requires a Dispute case.

Gateway Reconciliation Run
* Definition: A Run is a single execution of the reconciliation procedure that produces decisions (adjustments, suspenses, disputes) and a closure summary. Do not confuse a Run with a Batch: a Batch is a time‑bucketed collection of message chains; a Run may process one or more Batches.
* Scope: A Run may include all Gateway Reconciliation Batches that are Closed‑for‑new‑Chains (closed for new Originator input) but still have Suspense Chains.
* Inputs: Include unprocessed Originator reconciliation inputs and Destination reconciliation inputs (files/APIs) only up to the cutoff corresponding to the Batches included in the Run; exclude later windows.
* Outputs: The run-closure-summary must include counts, amounts, categories, and Suspense aging for all unresolved chains, and must update all Message Chains it processed (e.g., suspense flags, dispute links, and external reconciliation mappings). When a chain is concluded as synced with Originator or Destination, the Run must set `SyncedWithOriginatorByRunId` or `SyncedWithDestinationByRunId` respectively. Runs should also update the per-batch summary counts and flags.
* Operational surfaces: Suspense Chains appear as observations in the Channel Workbench for Ops review. Reconciliation is performed in the Reconciliation Console and must reflect all adjustments and disputes originating from each Run.

**Reconciliation Steps: With Destination**
* Trigger for reconciliation
  * Automatic: Immediately after entering `Closed-for-new-Chains`, or on a fixed schedule (e.g., T+5 minutes of batch close).
  * Manual: Ops can trigger ad‑hoc if error rates spike, or to re‑run after downstream recovery.
  * Inputs: All batch chains; Destination acknowledgements (ids/codes); a Destination status/statement API for message ids or time-ranged extracts where supported; or signed reconciliation files (hourly/daily snapshots) delivered via a secure channel. Recommendation: Prefer file‑based immutable snapshots as the authoritative source for end‑of‑batch reconciliation due to stronger consistency guarantees.
* Gaps to detect
    * Missing at Destination: Gateway intended an effect that, given the `OriginatorCommunicatedOutcome` and the default policy (`OriginatorDefaultPolicyApplied`), must be realized at the Destination; yet no reliable ack exists and status/API or reconciliation file shows no effect. If the communicated default treated the operation as failure (e.g., debit default‑fail), absence at Destination is considered complete and not a gap.
    * Duplicated at Destination: Multiple successful effects for the same idempotency key or dedupe key.
    * Orphaned Destination Response: Destination ack without a matching Gateway intention (e.g., late duplicate reply) — treat as no‑op unless it reflects a real effect.
    * In‑flight/Uncertain: Timeouts where Destination idempotency semantics are unclear — move to suspense with explicit watch/retry policy.
  * Adjustment recommendations by gap type
    * Missing at Destination
      * To Destination: Safe re‑drive with the same idempotency key and original parameters; respect rate limits and locking.
      * To Originator: None. If policy forbids re‑drive or retries are exhausted with persistent uncertainty, propose Originator adjustment only if Destination cannot realize the intended effect and product policy requires reflecting failure; otherwise keep in suspense.
    * Duplicated at Destination
      * To Destination: Compensation Reverse (credit for extra debit, or debit for extra credit) referencing the offending `DestinationAckId` and linking via `ParentMessageId`.
      * To Originator: None if Originator posted only once. If Originator also duplicated, propose Originator Reverse‑Duplicate to restore balances.
    * Orphaned Destination Response
      * To Destination: None if the response is a late/no‑effect ack. If it indicates an unintended applied effect, treat as duplicate/unintended and issue Compensation Reverse.
      * To Originator: None.
    * In‑flight/Uncertain
      * To Destination: Suspend with recheck schedule; no posting until status clarity is established.
      * To Originator: None. Keep chain in suspense; do not reflect balances until confirmed. Note: If product policy defines default customer‑facing outcomes during Destination suspense (e.g., treat debit as failure, credit as success), adjustments to Destination must respect the response already communicated to the Originator. Any change to the Originator outcome post‑communication is not reconciliation; it must be handled under Disputes.
    * Cross‑side mismatch: Destination success / Originator reject
      * To Destination: Compensation Reverse if policy and settlement windows allow reversal; else no Destination change.
      * To Originator: If reversal not permissible at Destination, post Originator adjustment to mirror the irreversible Destination effect with full audit and approvals.
* Notes on adjustments
  * Destination adjustments are executed as Gateway‑originated messages and must respect the Originator‑communicated outcome during suspense; changing that outcome triggers a Dispute.

**Reconciliation Steps: With Originator**
* Trigger for reconciliation
  * Automatic: Immediately after entering `Closed-for-new-Chains`, or when Destination reconciliation signals decisions that require Originator alignment.
  * Manual: Ops can trigger ad‑hoc for service recovery or after backlog drains.
  * Inputs: All batch chains; Originator acknowledgements (`OriginatingServiceResponseAckId`), enquiry responses; Originator ledger extracts or signed reconciliation files (hourly/daily snapshots). Recommendation: Prefer file‑based immutable snapshots as the authoritative source for end‑of‑batch reconciliation.
* Gaps to detect
    * Missing at Originator: Given the `OriginatorCommunicatedOutcome` and the default policy (`OriginatorDefaultPolicyApplied`), the Originator is expected to reflect a posting (e.g., communicated SUCCESS or SUSPENSE-DEFAULT-SUCCESS). However, any adjustment at the Originator is only permissible via an approved Dispute; otherwise the Originator status stands and Destination must be adjusted to match. If the communicated default treated the operation as failure and no Dispute exists, absence at Originator is considered complete and not a gap.
    * Duplicated at Originator: Multiple postings for a single `OriginatingServiceMessageId` or dedupe key.
    * Orphaned Originator Ack: Ack without a corresponding Gateway delivery — investigate; usually no action if no ledger effect.
    * In‑flight/Uncertain: Pending enquiries — keep in Originator suspense until SLA.
  * Adjustment recommendations by gap type
    * Missing at Originator
      * To Originator: Open a Dispute if and only if policy requires changing the previously communicated outcome; Originator postings change only through the Dispute workflow.
      * To Destination: Prefer adjusting Destination to uphold the final Originator status; if Destination reversal is prevented by policy or settlement, raise a Dispute with the Originator for outcome change.
      * To Destination: None.
    * Duplicated at Originator
      * To Originator: Reverse‑Duplicate for extra postings, preserving audit trail.
      * To Destination: None.
    * Orphaned Originator Ack
      * To Originator: None (cleanup acknowledgement state only; no balance change).
      * To Destination: None.
    * In‑flight/Uncertain
      * To Originator: Keep in suspense; re‑drive enquiries within SLA; no balance change.
      * To Destination: None.
    * Cross‑side mismatch: Originator success / Destination reject
      * To Destination: Safe re‑drive if the business still intends the effect and risk policy allows.
      * To Originator: If Destination ultimately rejects and re‑drive is not pursued/successful, post Originator reversal to mirror the final Destination state.
* Notes on adjustments
  * Originator adjustments align postings to finalized Destination outcomes or clean up duplicates/acks; reversals at Destination are proposed only when policy allows, otherwise mirror at Originator with audit/approvals.

Reconciliation Outputs (Both Sides)
* A machine‑readable adjustments file (per‑side) listing: correlation id(s), entity, amount/currency, reason code, action (post/reverse/retry/suspend), and prerequisites (locks/approvals).
* A human‑readable reconciliation report: totals by category, counts, success/failure ratios, suspense aging.
* All proposed adjustments are executed as Gateway‑originated messages within the same `TraceId` chain and recorded into the next open batch (to avoid re‑opening a sealed batch).

> Pro Tip
> Keep dedupe keys stable across retries (compose from actor + intent + beneficiary + amount + time bucket). This makes reconciliation deterministic across day and batch boundaries.

> Caution
> Never execute adjustments directly on ledgers without passing through the same mutation guard and locking controls; otherwise, you risk reintroducing race conditions that reconciliation is trying to eliminate.

### Disputes vs Reconciliation
* Reconciliation aligns systems to the intended business effect using compensations, retries, and postings while preserving the Originator outcome that was already communicated (especially during Destination suspense defaults, e.g., treat debit as failure, credit as success).
* A Dispute is initiated when the Gateway must change a response previously communicated to the Originator (e.g., later evidence shows the earlier default outcome is incorrect or cannot be honored). Disputes are handled via a separate Case Management workflow with maker–checker approvals, customer communications, and explicit audit.
* Policy: The final Originator status is authoritative. Always seek to adjust Destination to match the Originator. Destination adjustments must not contradict the Originator‑facing default outcome unless a Dispute case is opened and approved to change the Originator outcome. Dispute references must be linked to the affected message chain and any subsequent compensating entries.

### Suspense Chain
Any Message Chain that is initiated but the processing is not fully concluded while the reconciliation batch is marked closed for any new non-Gateway Originator messages is called a Suspense Chain. 

When is a message not in Suspense?
* A message is not in Suspense if (a) no further adjustment messages are required to be introduced by the Gateway for that message/chain, or (b) the relevant Disputes have been raised (thus moving any customer‑outcome change to the Dispute workflow).


### Mutation Guard Pattern 

Policy and Semantics
* Every message in a Message Chain MUST be processed under a Mutation Guard lock.
* LockGroup: A policy‑driven logical grouping that encodes where/how the mutation occurs (e.g., `DESTINATION:PAYMENT_POST`, `ORIGINATOR:ACK_DELIVERY`, `DESTINATION:ENQUIRY`).
  * Flow Control: Each LockGroup has an enforced quota in the Lock Service. When quota is exhausted, new lock requests fail fast → the Gateway applies backpressure (retry with jitter) rather than overwhelming downstreams.
  * Attribution: All locks are attributed to a LockGroup to honor quotas and enable per‑group observability.
* Per‑Chain Sequencing: At most one active message is processed per `ChainId` at any time. This guarantees ordered effects within a chain and prevents race conditions.
* TTL Discipline: `LockTTL` MUST exceed the worst‑case operation time for the guarded step (including retries). If the Gateway fails to release a lock before TTL expiry, the Lock Service deems the lock released and raises an Operational Exception referencing the `ChainId` and `GatewayServiceMessageId` for Ops review.

Typical Flow (per message)
1. Try Acquire: `lock = LockService.AcquireLock(ChainId, LockGroup, LockRequestTimeout, LockTTL)`
   * On quota/timeout: Treat as backpressure → reschedule with jittered backoff; record metric `lock.acquire.failed` with reason.
2. Execute under lock: `Lock.performBusinessOperation(ChainId, OperationLambda)`
   * OperationLambda performs exactly one mutation leg (e.g., send Destination request, deliver Originator ack) and records outcomes.
3. Release: `Lock.release()`
   * Always attempt release in a finally block. If release fails or TTL already expired, emit `lock.release.failed` and rely on Lock Service expiry; Ops exception is auto‑raised by Lock Service.

Notes
* Use distinct LockGroups for high‑risk or expensive Destination operations to isolate quotas (bulkheads).
* Lock acquisition failure should be interpreted as either quota exhausted or system unavailability—both are safe signals to pause and avoid amplification.
* Mutation Guard applies to compensations, retries, enquiries, and acknowledgements equally; the invariant is one in‑flight operation per chain.


## Security

Goal
* Guarantee non‑repudiation, prevent replay, and ensure a MITM‑resistant path to Destinations, while keeping configuration productized and operable.

### Identity and Trust: Porus (assumptions/requirements)
* Porus is tenant‑aware and authoritative for message authorization policies and key verification.
* Porus must support ECDSA P‑256 only (current scope) with SHA‑256 hashing and detached JWS signatures.
* Porus maintains/obtains tenant‑scoped public keys for applications, payment instruments, and trusted external auth servers; rotation and revocation are handled by Porus.
* Gateway expects Porus to: resolve the correct key, validate JWS, enforce tenant boundaries, and return verification results with key metadata (kid/issuer/tenant).

### Originator Authentication and Authorization
* Method: ECDSA P‑256 over SHA‑256; detached JWS.
* Policy‑driven scope: For each message type, the Transaction Product’s Authorization Policy defines the exact fields to be signed and the canonicalization method. Minimum enforced elements in the signed attributes for every message type:
  * `productId`, `messageType`, `nonce` (globally unique within the product’s lookback window), `iat` (issued-at), `exp` (expiry within policy), `kid` (key id), and a stable version/schema identifier.
* Gateway enforcement (per message):
  1) Verify detached JWS using Porus for the tenant; ensure algorithm ECDSA P‑256 and digest SHA‑256.
  2) Check that the signed field set matches the message type’s Authorization Policy and that message body matches the signed payload (integrity).
  3) Validate `exp` is within policy; `iat` present (clock‑skew bounded by policy).
  4) Enforce nonce uniqueness within the product’s lookback window (see Anti‑Replay).
  5) Enforce allowed originator application list per product/policy.

### Anti‑Replay and Uniqueness
* Per‑product lookback window defines replay bounds; set minimum expectations per product and ensure they are ≥ 2× the max signature validity time.
* `nonce` is mandatory and must be unique within the lookback window for the tuple (tenant, productId, messageType). Store a dedupe record keyed on this tuple.
* Timestamps are used to enforce validity windows (`iat`/`exp`) and skew limits; replay detection relies on `nonce`, not timestamp rechecks.

### External Authorization Servers (Ops adjustments)
* The Authorization Policy lists trusted external auth servers by their public keys (pinning). Gateway verifies JWS from these servers via Porus using the pinned keys.
* Maker–checker and human workflows are enforced by the external auth server before signature issuance; Gateway does not add maker–checker steps.

### Transaction Product Policy Model
* Source of truth: Payment Network Center (PNC) defines Transaction Products and their Authorization Policies; Ops Center exposes visibility and selected controls (e.g., lock groups/quotas, allowed external auth servers) for day‑to‑day operations.
* Policy contents (illustrative): allowed originator apps; signature method/fields; lookback and validity windows; trusted external auth servers (keys); LockGroups and quotas references; observability labels.

### Egress Proxy Between Gateway and the Destination
* All Gateway→Destination calls traverse the Egress Proxy. Proxy holds Destination credentials; private keys reside in HSM; no human can invoke Proxy directly.
* Gateway→Proxy: mTLS with Gateway service certs; Proxy validates client identity and enforces per‑route policies.
* Proxy→Destination minimum expectations (MITM‑resistant):
  * TLS 1.2+ with server certificate verification and strong ciphers; pin CA roots where feasible.
  * Network allow‑listing and egress controls for Proxy; per‑destination endpoint configuration (hostnames, SNI, timeouts).
  * mTLS is used if Destination supports it; otherwise, enforce strict TLS verification and request signing if a destination‑specific mechanism exists.
  * Credentials are short‑lived or rotated regularly; material is accessible only within HSM/secure enclave.

### Audit and Privacy
* Record for each message: verified JWS (or its digest), verification result (algorithm, key id, issuer, tenant), signed attribute set used, `nonce`, and policy version; correlate to `MessageChainId`.
* Immutable storage for audit artifacts (e.g., WORM/append‑only) with retention per product; include hash chains for tamper evidence.
* Structured logs with redaction of sensitive attributes; store only necessary fields for traceability. Encrypt data at rest and in transit.
* Access control: least privilege; all administrative actions (policy updates, key changes, break‑glass) are fully audited.

### Scenarios to be handled at Gateway
FailedMutationDueToLostLock
TimeoutFromDestination
TimeoutForAckFromOriginator
TimeoutforResponseMessageFromOriginator

### Exceptional scenarios to be handled in Gateway
1. Handle Safe Shutdown 
2. Abandoned Reclaimed Locks in Suspicious State 
3. Abandoned Lock Cleanup (due to improper shutdown or bugs)
4. Failed Lock Cleanup


## Business Ops Observability

Ops Levers and Tools
* Reverse Abandoned Debits and Credit to Flexcube
* Post Originator unacknowledged Credits to Shadow Ledger

Shadow Ledger should treat and respond to its clients (journal or channel):
* Timed out Credit as success
* Timed out Debits as failure 

SRE Observability
Reports





## Lock Service

Purpose
* Enforce exclusive, policy‑controlled execution of mutations per `ChainId` and `LockGroup` to provide ordering, backpressure, and operational visibility.

Identity, Authentication, and Authorization
* All calls are authenticated (e.g., mTLS/JWT) and authorized per client/service identity.
* Only the lock owner may release or extend its lock. Forced releases are restricted to privileged Ops identities and must be audited.

Lock Identity and Ownership
* LockId: In the Lock Service, a chain’s lock identifier is the Gateway `ChainId` (one active lock per chain at a time).
* Namespacing: Effective identity is `(ChainId, LockGroup)` to support separate quotas/policies by group while still guaranteeing one active message per chain at the Gateway.
* Correlation: `AcquireLock` accepts a correlation payload (key/value) for downstream observability; store with the lock record and in audit logs.

API (logical)
* AcquireLock(chainId, lockGroup, requestTimeout, ttl, correlation, callerId) → { lockToken, expiresAt }
  * Fails fast with QUOTA_EXHAUSTED or LOCK_ALREADY_HELD when applicable; may return after `requestTimeout` if configured to wait for availability.
* ReleaseLock(lockToken, chainId, lockGroup, callerId) → { released: true }
  * Enforces ownership: returns LOCK_NOT_OWNED if caller ≠ owner.
* ExtendLock(lockToken, additionalTtl, callerId) → { expiresAt }
  * Optional heartbeat/extend path; same ownership rules.
* InspectGroup(lockGroup) → { rateLimitPerMinute, concurrentLimit, utilization, saturation, recentErrors }
* ListLocks(filter?) → paginated active locks for Ops.

Exclusivity and Reacquire Semantics
* While held, a lock for `(ChainId, LockGroup)` cannot be acquired by another caller.
* After a successful release or TTL expiry, the same lock may be acquired again; this is treated as a new acquisition (new `lockToken`).

Quotas and Flow Control (per LockGroup)
* Two controls per group:
  * Rate limit: maximum successful acquires per minute.
  * Concurrency limit: maximum concurrent held locks.
* Default Group: Undefined `LockGroup` values inherit the Default group’s quotas until explicitly defined.
* Management: LockGroups are defined/updated from the Ops Center Workbench (policy‑as‑data); changes are audited and take effect without downtime.
* Observability: Ops Center shows defined and undefined groups with utilization (current held/limit), saturation (rejected/second), and error trends; supports tuning quotas on the fly.

Cleanup and Exceptions
* TTL Expiry: On TTL expiry, the lock is considered released by the service; it emits an Operational Exception with `ChainId`, `LockGroup`, prior `callerId`, and `GatewayServiceMessageId` (if provided) for triage.
* Abandoned Detection: Background reaper cleans orphaned records; anomalies generate alerts.
* Business Exceptions (non‑exhaustive): UNAUTHENTICATED, UNAUTHORIZED, INVALID_PARAMS, QUOTA_EXHAUSTED, LOCK_ALREADY_HELD, LOCK_NOT_OWNED, GROUP_NOT_FOUND (mapped to Default), EXTEND_DENIED.

SLOs and Safety Expectations
* Acquire p99 latency within budget under non‑saturated conditions; explicit signals when quotas drive rejections.
* Idempotent telemetry: all operations produce structured audit logs (who, what, when, why), with correlation ids preserved.
* Hard ownership enforcement on Release/Extend; no silent unlocks outside TTL expiry.

Operational Notes
* Integrate counters/metrics: `lock.acquire.success/fail`, `lock.held.current`, `lock.timeout.expired`, `lock.release.failed`, per `LockGroup` and caller.
* Emit alerts on sustained saturation or repeated `LOCK_NOT_OWNED` (possible misuse).
* Surface actionable guidance in Ops Center for quota tuning and incident drill‑down.
