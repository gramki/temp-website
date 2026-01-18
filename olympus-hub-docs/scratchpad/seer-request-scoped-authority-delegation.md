# Request Scoped Authority Delegation for Employed Agents

> **Status**: ✅ **DOCUMENTATION COMPLETE** (2026-01-17)  
>
> **Comprehensive Document**: The design has been consolidated into a single implementation concept:  
> [`olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md`](../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)
>
> **Implementation Plan**: See [request-scoped_delegation_docs.plan.md](../../.cursor/plans/request-scoped_delegation_docs_39e9c2a9.plan.md)
>
> This scratchpad contains the original brainstorming, Q&A, and planning materials.
>
> ---
>
> ### Documentation Deliverables (54 documents total)
>
> | Phase | Category | New | Updated | Status |
> |-------|----------|-----|---------|--------|
> | 0 | Context Summary | 1 | 0 | ✅ Complete |
> | 1 | Cipher IAM Extensions | 3 | 5 | ✅ Complete |
> | 2 | Hub Infrastructure (SX, RLM) | 4 | 9 | ✅ Complete |
> | 3 | Agent Integration (Sidecar, SDK, Gateway) | 3 | 9 | ✅ Complete |
> | 4 | Specs and Channels | 0 | 11 | ✅ Complete |
> | 5 | Cross-cutting (ADRs, Security, Runbooks) | 8 | 1 | ✅ Complete |
>
> ### Key New Documents
> - `olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md` (Authoritative)
> - `olympus-hub-docs/02-system-design/implementation-concepts/request-scoped-delegation.md` (Hub perspective)
> - `olympus-hub-docs/scratchpad/request-scoped-delegation-context-summary.md` (Reference)
> - `olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/delegation-templates.md`
> - `olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/delegation-certificates.md`
> - `olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/business-user-profiles.md`
> - `olympus-hub-docs/04-subsystems/signal-exchange/delegation-handling.md`
> - `olympus-hub-docs/04-subsystems/request-management/delegation-context.md`
> - `olympus-seer-docs/seer-design/subsystems/seer-sidecar/delegation-service.md`
> - `olympus-seer-docs/seer-design/subsystems/seer-agent-sdk/python-sdk/delegation-apis.md`
> - `olympus-seer-docs/seer-design/subsystems/seer-agent-sdk/java-sdk/delegation-apis.md`
> - `olympus-hub-docs/decision-logs/0127-request-scoped-authority-delegation.md` (ADR)
> - `olympus-hub-docs/decision-logs/0128-channels-vs-signal-providers-delegation.md` (ADR)
> - `olympus-seer-docs/seer-design/security/request-scoped-delegation-security.md`
> - `olympus-hub-docs/08-operations/runbooks/delegation-incident-response.md`

---

## Objective:
- Employed agents are provisioned without authority
- Authority should be assigned per request. This could make the agent behave like a client of an identity profile and use the delegated authority of that profile to perform actions, queries etc.
- This to support creation of agents that can represent business users
- To support short interaction scenarios and tasks that are delegated by such users.

---

## Why This is Different: Two Identity Domains

### The Gap in Existing Delegation Models

The current Seer delegation model (User, Role, Bot) operates in the **Enterprise/Operator Identity Domain** — it governs how internal enterprise users (bank employees, supervisors, operators) delegate authority to agents:

| Existing Model | Delegator | Identity Domain | Example |
|----------------|-----------|-----------------|---------|
| **User Delegation** | Internal employee | Enterprise Cipher IAM | `john.smith@bank.com` (fraud analyst) delegates to agent |
| **Role Delegation** | Internal IAM role | Enterprise Cipher IAM | `fraud-analyst` role permissions delegated to agent |
| **Bot Mode** | None (explicit roles) | Enterprise Cipher IAM | Agent has `automated-processor` role directly |

These models solve: *"How does an enterprise employee delegate their internal permissions to an agent?"*

### What This Document Addresses

Request-Scoped Delegation operates in the **Business User Identity Domain** — it governs how end-users of the business (customers, external employees) delegate authority to agents:

| New Capability | Delegator | Identity Domain | Example |
|----------------|-----------|-----------------|---------|
| **Request-Scoped Delegation** | Business Customer | Customer Identity | A retail banking customer delegates to their AI assistant to "pay my bills" |
| | Business Employee | External Business Identity | A company employee delegates to an expense approval agent |
| | Business System | External System Identity | An external ERP system delegates to a reconciliation agent |

This solves: *"How does an end-user (customer/business employee) delegate their authority to an agent acting on their behalf?"*

### Key Differences

| Aspect | Enterprise Delegation (Existing) | Business User Delegation (This Doc) |
|--------|----------------------------------|-------------------------------------|
| **Who delegates?** | Internal operators (bank employees) | End-users (bank customers, external employees) |
| **When determined?** | At employment time (static) | At request time (dynamic) |
| **Identity system** | Cipher IAM (enterprise identity) | Business domain identity (customer identity, external IdP) |
| **Duration** | Agent lifetime | Request/session scoped |
| **Use case** | Agent performs internal operations | Agent represents user in their interactions |

### Illustrative Examples

**Example 1: Personal Finance AI Assistant**
- A retail banking customer uses an AI assistant in their mobile app
- Customer says: "Pay my credit card bill from my checking account"
- The agent needs to act **as the customer** to initiate the payment
- This requires the **customer** to delegate authority to the agent — not a bank employee

**Example 2: Expense Approval Bot**
- A company uses an expense approval workflow
- An employee (not a bank employee — a customer's employee) wants to delegate approval authority to an AI agent for small expenses
- The agent needs to act **as that employee** within the company's expense system
- This requires the **business employee** to delegate authority — not the bank's internal staff

**Example 3: Family Banking Agent**
- A parent wants to set up an AI agent to monitor their teenager's spending
- The parent delegates limited authority to the agent to view transactions and send alerts
- The agent acts **on behalf of the parent** (the customer), not on behalf of a bank employee

### Relationship to Existing Models

Request-Scoped Delegation does **not replace** the existing delegation models. An agent may have:

1. **Enterprise delegation** (User/Role/Bot) — governing what the agent can do within Hub's internal systems
2. **Business user delegation** (Request-Scoped) — governing what the agent can do on behalf of the end-user

These are orthogonal concerns. An agent might:
- Have `Bot Mode` enterprise delegation (minimal internal permissions)
- Plus request-scoped delegation from a customer (act on customer's behalf for specific operations)

---

## Brief approach

   - Trained agents assume identity per session
    - Scenario invocation is assocaited with a delegated authority token
    - Deferred Authority employment model
    - Delegatable Authority Template in Cipher; 
    - Idenity Profile Owner (user) gives a Delegation Certificate referring to the delegate,  delegation authority, and time windows.
    - Agent converts Delegation Certificate to a request-scoped authority token with the help of Cipher IAM Extensions. (This token makes delegator as the identity associated with token, with Employed Agent as a client)
    - When does a user delegate authority to an agent?
 

## Concepts:
 Agent Employment without Delegation
 Authority Request
 Delegation Template 
 Delegation Certificate
   Delegation Template Reference
   Delegation Constraints 
      - Delegate: specific-identity, IAM group, IAM role
      - expiry: Time-based, Session-Scoped  
      - chaining-allowed: t/f
      - Time window
 Delegation Access Token (and a derived identity profile)
 Pre-Announced Authority Request
 Authority Request Cascading Rules/Policy
 Authority Request -> Delegation Certificate -> Delegation Access Token conversions at the I/O Gateway
 Raw Agent should be unimpacted and uniformed about delegation models; May be capable of making Authority Request with a delegation template.
 

 Request Assignment can contain a Delegated Access Token; 
 - If present, Notification Service can forward this token to the assignee when sending any notifications.
 - Agents can query request for Access Token
 - SX-observer, I/O Gateway, Sidecar -- who should query to get Assignee access token?
 I/O Gateway 

Before-Guardrail for Delegation Check:
- Check if the Session already has a Delegated Access Token
- Check if the any acestor has a Delegated Access Token or can Delegate access walking through each level
- If none of the ancestors can give access token, post Authority Request in current Session and in the ancestor chain till the point it allows Authority Request Cascading

Every Agent in the ancestor chain, when asked for Delegation Access Token, checks if its 
   * Session has a Delegation Certificate that can allow delegation (chaining or directly) 
   * Session is associated with a Delegation Access Token whose corresponding certificate allows chaning
   * If the caller is an Assignee and if the Assignment object has:
      * A Delegation Certificate that is attributable to the assignee (the caller) [because of id, role, group] or 
      * A Delegation Access Token that is issued to the caller
This perfomed through API exposed by the request-lifecycle-manger; It represent the Request (Session) Context of an Agent.


A Channel can add Delegation Certificate, Delegation Access Tokens to the Request
A Channel (not every signal provider) can recognize if an interaction with a Scenario requires Delegation Access Token with certain Delegation Template, or just an authenticated, access controlled call is sufficient. This check can be made pre-emptively, as  pre-condition to invoke a Scenario or access a request of that Scenario.
Signal Providers can't delegate. Channels can facilitate delegation related interactions.

---

## Brainstorming: Questions and Design Considerations

### Q1: Relationship to Existing Delegation Model (User/Role/Bot)

**Context**: The existing Seer delegation model (User/Role/Bot) operates in the **Enterprise Identity Domain** — governing internal operator permissions. Request-Scoped Delegation operates in the **Business User Identity Domain** — governing end-user (customer/business employee) delegation.

These are **orthogonal concerns**, not competing models.

**Questions**:
1. How do the two delegation types **compose**? 
   - An agent could have Bot Mode (enterprise) + Request-Scoped (business user) simultaneously
   - How are these represented in EmploymentSpec?
This is like an Oauth Client identifier and Access token segregation. The Bot Mode or for that matter any Employed Agent identity would be seen as the identity of the client in OAuth realm. In place of client secret, the Employed Agent credentials will serve as the client secret. The Delegation Access Token will a token issued with the Employed Agent as the client and the delegation template as the scope. 

2. Should EmploymentSpec have a new section for business user delegation capabilities?
   ```yaml
   delegation:
     enterprise:
       type: bot
       accountable: "user:ops-manager@bank.com"
     business_user:
       enabled: true
       templates_accepted: ["dt-personal-finance-ops"]
   ```
> There should be separate section, but that should be called request-scoped-delegation; 
> In the employment spec, the modes of delegation should be distict.
> For employment with request scoped delegation, the config shoudl have delegation_templates_accepted

3. How does this interact with the **ceiling model** (Training Spec → Employment Spec narrowing)? 
   - Do Training Spec ceilings constrain what business user delegation can grant?
   - The agent's enterprise authority is separate from the business user's delegated authority

> Training mode still constrains what is usable by the employed agent. Although the delegation certificate may have included more privileges in delegation, the training spec still limits the privileges to what it can permit. Thus the effective delegation access token granted to the employed agent is always the minimal set of privileges (intersection). The OPA Policies are also inherited from Training Spec and collectively enforced with the Delegation Template policies. Policies is union - all policies should allow.

**Design Direction**: 
- Keep enterprise delegation (User/Role/Bot) as-is
- Add a **parallel** business user delegation capability in EmploymentSpec
- Both apply simultaneously — enterprise delegation governs internal permissions; business user delegation governs what the agent can do on behalf of the end-user

> This is clarified with OAuth client analogy above.

---

### Q2: Delegation Template Lifecycle and Ownership

**Questions**:
1. Who **creates** Delegation Templates? 
   - Is this a Tenant Admin function? 
   - Can Process Architects define them as part of Scenario design?
   - Are they global to a workbench or scenario-specific?
> Delegation templates need to be authorized by Tenant admin (the workflow is left to tenants)
> Developers and Process Architects can define them
> Templates are Workbench-scoped and can be referenced in any Scenario


2. What is the **relationship** between Delegation Template and Scenario? 
   - Should a Scenario declare which Delegation Templates it can accept?
   - This would enable the pre-emptive check mentioned for Channels.

> A Scenario can declare the templates required or acceptable
> However, it is not essential. A Channel should be able to additional delegation requirement during the lifecycle of a request. There may be optional and additional delegation requirements discovered during the life of the request as agents get involved and operations evolve. Furthermore, the previous delegation may have expired or the scope may have been revised due to change in delegator privileges. Considering all of it, Channel should be ready for authority requests during the life of request. 

3. Where are Delegation Templates **stored**? Cipher IAM Extensions registry?
> Cipher IAM
> Cipher IAM is the only IAM recognized for all the interactions.
> Any external IAMs in the service of user's identity would be federated with Cipher IAM
> Cipher IAM is the only service relied for authority delegation and access tokens (as an authorization server)

4. Do Delegation Templates have **versioning**? What happens when a template changes after certificates have been issued?

**Suggested Structure for Delegation Template**:
```yaml
delegation_template:
  id: "dt-personal-finance-ops"
  name: "Personal Finance Operations"
  description: "Allows agent to perform personal finance operations on behalf of user"
  
  # What authority this template can delegate
  delegatable_authority:
    roles: ["account-viewer", "payment-initiator"]
    permissions: ["read:accounts", "initiate:payments"]
    ceilings:
      value:
        maxSingleTransaction: 1000
        maxDailyTotal: 5000
  
  # Constraints on how this template can be used
  constraints:
    max_validity_duration: "PT24H"  # Max 24 hours
    chaining_allowed: false
    requires_mfa_at_delegation: true
    allowed_delegate_types: ["employed-agent", "user"]
  
  # Scope restrictions
  scope:
    workbenches: ["retail-banking"]
    scenarios: ["personal-assistant", "expense-approval"]
```

> Templates are immutable and versioned.
> A change in template will not invalidate existing delegation implicitly. But the scope of delegation will remain as per the template version under which the delegation was made. 
> This model can be revisited if the adoption requires/demands changes.
---

### Q3: Delegation Certificate Issuance Flow

**Questions**:
1. **When** does a user issue a Delegation Certificate?
   - Proactively before scenario invocation (pre-announced)?
   - Reactively when an agent requests authority (Authority Request)?
   - As part of scenario initiation (Channel-mediated)?

> All are possibled. This will be combination of user agent and channel's choices.
> But both UA and Channel must support reactive mode, where Authority Requests are discovered during the life of the request.

2. **How** is user consent captured for delegation?
   - Explicit approval flow (similar to OAuth consent)?
   - Implicit (based on their session with the Channel)?

> Yes. A delegation certificate is a representation of user consent.
> However, A delegation certificate an be issued in favor of multiple known/unknown agents by specifying them using wildcard ex: *@domain, iam-group, iam-role. Any agent with the matching subject identity pattern or part of role or group can then benefit from the Delegation Certificate. The Channel can request for Delegation Access Token for a suitable Employed Agent using such Delegation Certificate. 
> So there are explicit and implicit scenarios. Explicit to arrive at certificate. Implicit to EAs who are eligible as per any existing certificates.
> Certificates are stored with Cipher and can be queried by channels for a given user and by the EA identiy or the delegation-template required.  

3. **Who validates** the Delegation Certificate?
   - The Channel at request creation?
   - Cipher IAM Extensions when token is requested?
   - I/O Gateway when agent makes calls?

**Suggested Flow for User-Initiated Delegation**:
```
User → Channel → [Consent UI] → Cipher IAM Extensions
                                       │
                                       ├─ Validate user has authority to delegate
                                       ├─ Validate template constraints
                                       ├─ Issue Delegation Certificate
                                       │
                                       ▼
                              Request created with
                              Delegation Certificate attached
```
> Cipher must validate the delegation certificate before issuing a Delegation Access Token
> However, given these certificates are signed digital certs, the channel can also 'verify'


---

### Q4: Authority Request Pattern

**Questions**:
1. What happens when an agent needs authority it doesn't have?
   - Does the agent **block** waiting for authority?
   - Does the agent **fail** and record an Authority Request for async resolution?
   - Is there a **timeout** behavior?

> Block waiting for authority
> Timeout is agent's implementation-specific

2. How does Authority Request differ from **Escalation** in the Task model?
   - Is Authority Request a special type of escalation?
   - Or is it a separate concept?

> Unrelated. 
> Escalation in task model is to involve a person/agent in the escalation matrix to look into the task 

3. Who **fulfills** an Authority Request?
   - The human who initiated the request?
   - A supervisor?
   - Any user who has the authority to delegate?

> The 'Agent' who has the capability to fulfill.
> Very often it would be the end-user who initiated the request.
> However, as stated above in the 'implicit' flow, a channel can fulfill the request using an existing certificate
> If there is another agent with a delegation access token with a delegatable access, then that agent can also fulfill the authority request if its behavior allows for it and if it is an authority (including identity) that it can delegate.

4. What is the **UX** for Authority Request fulfillment?
   - Channel notification to the user?
   - Task created for supervisor?

**Suggested Authority Request States**:
```
[PENDING] → [GRANTED] → (agent proceeds)
         → [DENIED] → (agent fails/escalates)
         → [EXPIRED] → (request times out)
```

> More often than not, it is a channel notification to the user.
> Other variations are explained earlier.
> Supervisor is not involved

---

### Q5: Session vs Request Scoping

**Questions**:
1. What is the relationship between **Session** (mentioned in the doc) and **Request**?
   - Is Session the same as Request?
   - Or is Session an agent-level concept that spans multiple Requests?
> Hub Request and Agent Session are one and the same in their scope.
2. For nested/hierarchical Requests (parent-child):
   - Does the child Request inherit the parent's Delegation Access Token?
   - Or does each Request need explicit delegation?
> Child does not inherit the access token.
> Every agent in the tree must have their own delegation access token
> A child may be granted an implicit token by the Channel or Agent if the Delegation Certificate or Delegation Access Tokens so allow for it.

3. How does this interact with **Composite Applications** where multiple agents participate in the same Request?
   - Does each agent need its own delegation?
   - Can one agent's delegation be shared with child agents?
> Answered above

**Clarification Needed**: The document uses "Session" in several places. Need to clarify if this is:
- Agent Session (pod lifecycle)
- Request Session (single request processing)
- Conversation Session (multi-turn interaction)

> It is same as Hub Request. So Request Session.
> There can be multiple 'conversation sessions' across various channels in a single request. 

---

### Q6: Token Lifecycle and Security

**Questions**:
1. What is the **lifetime** of a Delegation Access Token?
   - Is it tied to Request lifecycle (destroyed on completion)?
   - Can it outlive the Request?
> Delegation Certificate can outlive a request
> Delegation Access Token is scoped to a single hub request

2. How are tokens **revoked**?
   - If user revokes consent mid-request, what happens?
   - How does this interact with the kill switch?
> Revocations of the delegator are cascaded
> Killing a trained agent or an employed agent stops use of all delegated access tokens
> if the agent is brought back up and the agent can continue to participate in requests that had tokens delegation tokens

3. What is the **token format**?
   - JWT with embedded claims?
   - Opaque token with server-side lookup?
> JWT; 
> claims are embedded
> scopes are also embedded and they are same as delegation template ids


4. How does token refresh work for long-running requests?

**Security Considerations**:
- Tokens should be **bound to the specific agent identity** (prevent token theft)
- Tokens should include **audience** (which PEPs can accept them)
- Tokens should be **non-transferable** (unless chaining is allowed)

> yes to all
> If a token is timebound and if it expired, then authority requests are made to receive new tokens to proceed

---

### Q7: PEP Integration Points

**Questions**:
1. Which PEPs need to be aware of Delegation Access Tokens?
   - Tool Gateway: Yes (tool invocation authorization)
   - Model Gateway: Probably not (LLM access is agent-level)
   - Signal Exchange: Yes (request updates)
   - Seer Sidecar: Yes (early enforcement)
> Yes to all, but Model Gateway. Model Gateway will rely on the agent identity and policy, but very likely that policy is defined in training spec or in employment spec and is not part of delegation template

2. How do PEPs **validate** the token?
   - Call to Cipher IAM Extensions?
   - Local validation with public key?

> Local validation with public key

3. How do tokens interact with **existing OPA policies**?
   - Is DelegatedAuthority a new context type in OPA input?


**Suggested OPA Context Extension**:
```rego
input.delegation_context = {
  "has_delegation": true,
  "delegator_id": "user:jane.doe@acme.com",
  "template_id": "dt-personal-finance-ops",
  "delegated_roles": ["account-viewer"],
  "delegated_permissions": ["read:accounts"],
  "ceilings": {
    "maxSingleTransaction": 1000
  },
  "issued_at": "2026-01-16T10:00:00Z",
  "expires_at": "2026-01-16T22:00:00Z",
  "chaining_allowed": false
}
```
> The delecation access token - claims and scope is certainly part of the context. 
> We can go with a structure similar to whats suggested. 
> However, I think we may have multiple delegation templates associated with a single delegation token (just as scopes in oauth)

---

### Q8: Raw Agent Transparency

**Statement**: "Raw Agent should be unimpacted and uninformed about delegation models; May be capable of making Authority Request with a delegation template."

**Questions**:
1. How does the agent **make** an Authority Request if it's uninformed?
   - Is this a sidecar-mediated behavior?
   - Is there an SDK call that abstracts this?
> Agent may use a tool to request delegation
> Agent may have invoked a tool that makes an update to request for authority
> Side-car mediation is certainly a method
> However the critical point to note in the comment is the 'delegation model' not the fact that it requires delegated authority expressed through a delegation access token. That is, an agent need not know how a delegator is delegating authority and what are the constraints associated with that. It is sufficient for it to know that the authority request it made is addressed with an access token. 

2. If the agent can specify a delegation template in the Authority Request, doesn't that require **awareness** of the delegation model?

> No. The delegation template details would have been injected in training spec or employment spec. A raw agent wouldn't have know the specific of which templates it is requried to have. It is sufficient for raw agent to know that it needs to make an authority request with the configured params and that it shoudl have delegation access token.

3. Should there be **two modes**:
   - Transparent mode: Agent is unaware; sidecar handles everything
   - SDK mode: Agent can explicitly request authority using SDK

**Suggested Design**: 
- Raw agents remain unaware of delegation mechanics
- Sidecar or SDK intercepts authorization failures and automatically posts Authority Requests
- The Delegation Template is derived from the tool/action being attempted (via Training Spec configuration)

> Above explaintation clarifies all of this. 
> However, if a SDK is doing it, it is being done by the Raw Agent. (Can't use the same phrasing for side car as that's not embedded into raw agent code)

---

### Q9: Chaining and Cascading

**Questions**:
1. What is the difference between **chaining** (delegation certificate allows re-delegation) and **cascading** (authority request walks up the request hierarchy)?
> Chaining is delegation being granted from a delegate to another delegate; chaining of delegations.
> Cascading is the process of forwarding Authority Request from child to parent context.
> Both are unrelated concepts

2. For chaining:
   - Can an agent delegate to a child agent?
   - What prevents infinite delegation chains?
   - Is there a max chain depth?
> There is no notion of a child agent per say
> An agent can delegate its authority to another agent if its own delegation permits that
> Max limit can be included in the certificate. Cipher enforces it when a delegation access token is requested 


3. For cascading:
   - If a child request needs authority, and the parent request has it, is this automatic or does it require explicit policy?
   - What happens in cross-workbench invocations where no parent-child relationship exists?

> Explicit policy is required for any chaining
> The certificate governs the agents that can be in the chain of delegation. (for example: domain, iam-group, etc.,)

---

### Q10: Channel Responsibilities

**Statement**: "Channels can facilitate delegation related interactions. Signal Providers can't delegate."

**Questions**:
1. What specifically can a Channel do?
   - Present consent UI to user?
   - Attach Delegation Certificate to Request?
   - Convert Certificate to Access Token?
> All of the above

2. What is the **handoff** between Channel and Cipher IAM Extensions?
> Channel-specific. Its ultimately the Cipher IAM Extensions that should authenticate and take consent from the delegator to generate a delegation certificate that meets the authority request.

3. For AI assistant Channels (MCP):
   - How does an AI assistant obtain delegation from its human user?
   - Is this different from web/mobile Channels?

> All channels may have their own integration models with Cipher IAM. We are not specifying them in detail here.
> MCP clients may be asked to redirect the user to a brower page hosted by cipher or may be given some out of band method to take consent. 
> The specific interactions vary.

---

### Q11: Scenario Declaration of Delegation Requirements

**Implication**: For Channels to pre-emptively check delegation requirements, Scenarios must declare them.

**Suggested Scenario Automation Spec Extension**:
```yaml
spec:
  # Existing fields...
  
  delegation_requirements:
    mode: required | optional | none
    templates_accepted:
      - "dt-personal-finance-ops"
      - "dt-account-management"
    minimum_permissions:
      - "read:accounts"
    fallback_behavior: fail | escalate | degrade
```
> let us explicitly call out 'request_scoped_delegation_requirements'

---

### Q12: Accountability with Deferred Delegation

**Current Model**: Every Employed Agent has an `accountable` human specified at employment time.

**Questions**:
1. With Deferred Delegation, who is accountable?
   - The human who delegated (the delegator)?
   - The accountable human from EmploymentSpec?
   - Both (for different aspects)?

> Both form different aspects
> However, as the accountability for most audit and regulatory requriements is to exist in the business domain users, it will be accountable human from EmploymentSpec. 

2. How does this affect **audit trails**?
   - Actions should be auditable to both the delegator and the accountable human?
> Yes to both

3. What happens when the delegator and accountable human are different people?
> They are likely to be different always.
> Accountable person should explain agent behavior
> Delegator is merely relying on the agent
---

## Next Steps

1. **Clarify terminology**: Define Session, Request, Delegation Certificate, Delegation Access Token with precise semantics
2. **Define interaction with existing model**: Clarify if this extends or replaces User/Role/Bot delegation
3. **Sequence diagrams**: Create detailed sequence diagrams for:
   - Proactive delegation (user delegates before scenario)
   - Reactive delegation (Authority Request flow)
   - Cascading delegation (parent-child requests)
4. **CRD/API design**: Define the data structures for:
   - Delegation Template
   - Delegation Certificate
   - Delegation Access Token
   - Authority Request
5. **Component responsibilities**: Assign clear ownership to:
   - Cipher IAM Extensions
   - I/O Gateway (Agent Ingress Gateway)
   - Seer Sidecar
   - Request Lifecycle Manager

---

## Additional Design Considerations

### Use Case Mapping

| Use Case | Delegation Mode | Authority Source | Example |
|----------|-----------------|------------------|---------|
| Personal AI Assistant | Deferred + Request-scoped | User delegates per conversation | "Pay my bills" assistant |
| Approval Workflow Agent | Deferred + Task-scoped | Approver delegates per approval task | Expense approval bot |
| Customer Service Agent | User Delegation (existing) | Customer service rep at employment | Support agent handling tickets |
| Fully Automated Bot | Bot Mode (existing) | Static roles at employment | Reconciliation processor |

### Comparison with OAuth 2.0

This model shares similarities with OAuth 2.0 but has key differences:

| Aspect | OAuth 2.0 | Request-Scoped Delegation |
|--------|-----------|---------------------------|
| Actors | User, Client, Resource Server | User (Delegator), Agent (Delegate), PEPs |
| Token Type | Access Token, Refresh Token | Delegation Access Token |
| Consent | Scope-based consent screen | Template-based consent |
| Lifetime | Token TTL | Request-scoped or time-bounded |
| Revocation | Token revocation endpoint | Kill switch + explicit revocation |
| Chaining | Not supported | Explicit chaining policy |

### Component Mapping (Initial)

| Component | Responsibility in Delegation Flow |
|-----------|-----------------------------------|
| **Channel** | Captures user consent, initiates delegation flow, attaches Certificate to Request |
| **Cipher IAM Extensions** | Validates delegation authority, issues Certificates and Tokens, manages Templates |
| **Request Lifecycle Manager** | Stores delegation context per Request, provides API for token lookup |
| **Seer Sidecar** | Pre-guardrail delegation check, Authority Request posting, token injection |
| **I/O Gateway** | Token validation on outbound calls, delegation context forwarding |
| **Tool Gateway** | Token validation, policy enforcement with delegation context |
| **Signal Exchange** | Token validation for Request updates |

### Potential Risks

1. **Complexity**: Adding a second identity domain (business user) alongside enterprise identity increases system complexity
2. **Performance**: Token validation on every call may add latency
3. **UX Friction**: Consent flows may interrupt user experience
4. **Security Surface**: New token type = new attack vectors; bridging two identity domains creates new risks
5. **Operational Overhead**: More concepts to monitor, debug, and audit
6. **Identity Federation**: Business user identities may come from external IdPs — requires federation support

### Mitigation Strategies

1. **Gradual Rollout**: Start with specific scenarios (personal assistants) before generalizing
2. **Caching**: Cache token validation results within request scope
3. **Progressive Consent**: One-time consent with remembered preferences
4. **Security Review**: Dedicated security audit before implementation
5. **Observability**: Enhanced logging and tracing for delegation flows

---

## Confirmed Design Decisions (from Q&A)

Based on the discussion, the following architectural patterns are confirmed:

| Pattern | Confirmation |
|---------|--------------|
| Authority Request as `REQUEST_UPDATE` sub-type | ✅ Yes — follows REMIND pattern |
| Authority Grant delivered as `REQUEST_UPDATE` | ✅ Yes — with token in both payload and environment |
| Channels are observer modules | ✅ Yes — receive all REQUEST_UPDATEs |
| Token placed in `environment.auth.delegations` | ✅ Yes — Signal Exchange refreshes on each update |
| Cascading via Request Hierarchy | ✅ Yes — follows lifecycle cascade pattern |
| Cross-workbench cascading is best-effort async | ✅ Yes — same as lifecycle cascade |
| Channels can implicitly fulfill via existing certificates | ✅ Yes — check certificates first, then prompt user |
| Agent cannot query its own certificates | ✅ Unless that privilege is delegated |

---

## Additional Confirmed Decisions (C2-Level)

### Delegation Requirements Ownership

**Decision**: Delegation template selection is a **developer/process architect responsibility** — not automatic.

- When whitelisting tools, developers/architects must understand required privileges
- They select which Delegation Templates represent the right scope
- Templates are not tailored per-Scenario; they represent cognitive burden trade-offs for delegators
- Right trade-offs are design and context-informed decisions

---

### Policy Composition Model

**Decision**: **All applicable policies must ALLOW** (intersection/AND logic).

When delegated authority is used:
- Training Spec policies must ALLOW
- Employment Spec policies must ALLOW  
- Delegation Template policies must ALLOW
- If any policy DENIES → action is denied

---

### Chaining Authorization Flow

**Decision**: Agent-initiated chaining via SDK; Channel only uses Certificates.

| Actor | Chaining Capability |
|-------|---------------------|
| **Agent with delegatable token** | Can delegate using SDK-provided capability |
| **Tool** | Can create delegated token when initializing scenario for child agent |
| **Channel** | Does NOT participate in Access Token chaining; makes decisions based on Delegation Certificate only |

---

### Business User Identity in Cipher

**Decision**: Cipher maintains business user profiles with imported + added claims.

| Aspect | Decision |
|--------|----------|
| **Identity Source** | Cipher maintains relevant profiles for business users |
| **Claims** | Imports claims from federated IdP; supports addition of claims |
| **Authority Policy** | Defined by Tenant Admin in Cipher IAM |
| **Revocation** | Cipher has mechanisms (out of scope for this discussion) |

---

### Token Scoping per Agent

**Decision**: Each Delegation Access Token is issued to **exactly one agent**.

- Token is bound to specific IAM Profile ID / SPIFFE ID
- Multiple agents on same request each need their own token
- Certificate delegate pattern determines eligibility; token binds to specific agent

---

### Denial and Timeout Behavior

**Decision**: Agent-specific behavior; default is **degraded capability continuation**.

| Outcome | Default Behavior |
|---------|------------------|
| **DENIED by user** | Request continues with degraded capability |
| **TIMEOUT** | Request continues with degraded capability |
| **Certificate revoked** | Request continues with degraded capability |

Agents can override this behavior (fail request, escalate, etc.) based on their implementation.

---

## Subsystems and Content Updates Required

This section catalogs all documentation that needs to be created or updated to introduce Request-Scoped Authority Delegation across Hub and Seer.

### Legend

| Status | Meaning |
|--------|---------|
| 🆕 NEW | New document to be created |
| ✏️ UPDATE | Existing document needs modification |
| 📖 REFERENCE | Document to cross-reference (no changes needed) |

---

### Hub Subsystem Updates

#### 1. Signal Exchange (`04-subsystems/signal-exchange/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `README.md` | ✏️ UPDATE | Add delegation-related REQUEST_UPDATE types to overview |
| `message-envelope.md` | ✏️ UPDATE | Add `environment.auth.delegations` structure; define schema for delegation tokens |
| `observer-notifications.md` | ✏️ UPDATE | Document Channel as observer for AUTHORITY_REQUEST; notification delivery with token refresh |
| `request-factory.md` | ✏️ UPDATE | Handle delegation context initialization when creating requests |
| `delegation-handling.md` | 🆕 NEW | New doc: How Signal Exchange handles delegation token refresh, AUTHORITY_REQUEST/GRANTED routing |

#### 2. Request Management (`04-subsystems/request-management/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `README.md` | ✏️ UPDATE | Add delegation context as part of request state |
| `request-lifecycle.md` | ✏️ UPDATE | Add delegation context to request state model; describe delegation-related transitions |
| `request-storage.md` | ✏️ UPDATE | Define storage for Delegation Certificates and Access Tokens per request |
| `request-hierarchy.md` | ✏️ UPDATE | Document Authority Request cascading rules; certificate inheritance |
| `delegation-context.md` | 🆕 NEW | New doc: API for delegation context lookup, token retrieval by assignees |

#### 3. Channel Documentation (`02-system-design/implementation-concepts/` & `06-ux-architecture/tenant-domain/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `channel.md` | ✏️ UPDATE | Add delegation responsibilities: certificate attachment, implicit fulfillment, AUTHORITY_REQUEST handling |
| `mcp-channels.md` | ✏️ UPDATE | MCP-specific delegation flow for AI-to-AI scenarios |
| `rest-channels.md` | ✏️ UPDATE | REST Channel delegation flow for programmatic access |

#### 4. Hub Implementation Concepts (`02-system-design/implementation-concepts/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `request-update.md` | ✏️ UPDATE | Add AUTHORITY_REQUEST and AUTHORITY_GRANTED as REQUEST_UPDATE sub-types |
| `observer-pattern.md` | ✏️ UPDATE | Reference Channels as delegation-aware observers |
| `request-scoped-delegation.md` | 🆕 NEW | New implementation concept explaining the overall design |

---

### Seer Subsystem Updates

#### 5. Cipher IAM Extensions (`seer-design/subsystems/cipher-iam-extensions/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `README.md` | ✏️ UPDATE | Add Request-Scoped Delegation as a capability area |
| `authority-delegation.md` | ✏️ UPDATE | Add Delegation Template, Certificate, Access Token concepts; distinguish from User/Role/Bot |
| `credential-management.md` | ✏️ UPDATE | Add Delegation Access Token lifecycle, validation, binding to SPIFFE ID |
| `policy-enforcement-points.md` | ✏️ UPDATE | Add delegation token validation as PEP responsibility |
| `integration-patterns.md` | ✏️ UPDATE | Add patterns for request-scoped delegation across subsystems |
| `delegation-templates.md` | 🆕 NEW | New doc: Delegation Template registry, schema, constraints, examples |
| `delegation-certificates.md` | 🆕 NEW | New doc: Certificate lifecycle, issuance, revocation, chaining rules |
| `business-user-profiles.md` | 🆕 NEW | New doc: Business user identity management, claim import, federation |

#### 6. Seer Sidecar (`seer-design/subsystems/seer-sidecar/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `README.md` | ✏️ UPDATE | Add delegation check as sidecar responsibility |
| `authority-enforcement-service.md` | ✏️ UPDATE | Add delegation token validation; Authority Request initiation logic |
| `policy-enforcement-service.md` | ✏️ UPDATE | Add delegation policy composition (AND logic); multi-layer policy evaluation |
| `delegation-service.md` | 🆕 NEW | New doc: Pre-guardrail delegation check, chaining via sidecar, token injection |

#### 7. Agent Ingress Gateway (`seer-design/subsystems/agent-ingress-gateway/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `README.md` | ✏️ UPDATE | Add delegation context forwarding as gateway responsibility |
| `request-routing.md` | ✏️ UPDATE | Include delegation token in request context passed to agents |
| `signal-exchange-integration.md` | ✏️ UPDATE | Delegation token refresh from Signal Exchange on updates |

#### 8. Seer Agent SDK (`seer-design/subsystems/seer-agent-sdk/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `README.md` | ✏️ UPDATE | Add delegation APIs to SDK capability overview |
| `python-sdk/hub-integration-apis.md` | ✏️ UPDATE | Add delegation APIs: request_authority(), get_delegation_token(), delegate_to_child() |
| `java-sdk/hub-integration-apis.md` | ✏️ UPDATE | Add delegation APIs (Java equivalents) |
| `python-sdk/delegation-apis.md` | 🆕 NEW | New doc: Detailed delegation API reference for Python SDK |
| `java-sdk/delegation-apis.md` | 🆕 NEW | New doc: Detailed delegation API reference for Java SDK |

#### 9. Agent Lifecycle Specs (`seer-design/hub-integration/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `employment-spec-crd.md` | ✏️ UPDATE | Add `delegation_mode: deferred` and `request_scoped_delegation` section |
| `training-spec-crd.md` | ✏️ UPDATE | Add `delegation_requirements` section with template references |
| `employed-agent.md` | ✏️ UPDATE | Describe Employed Agent as OAuth-like client; delegation token as access token |
| `request-dispatch.md` | ✏️ UPDATE | Include delegation token handling in request dispatch flow |

#### 10. Seer Implementation Concepts (`seer-design/implementation-concepts/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `agent-identity-credentials.md` | ✏️ UPDATE | Add Delegation Access Token; OAuth 2.0 analogy; deferred delegation model |
| `delegation-chains.md` | ✏️ UPDATE | Add Request-Scoped delegation as distinct from User/Role/Bot; composition rules |
| `authority-enforcement.md` | ✏️ UPDATE | Add delegation token enforcement; policy composition (AND logic) |
| `seer-sidecar.md` | ✏️ UPDATE | Add delegation check as pre-guardrail responsibility |

---

### Cross-Cutting Documentation

#### 11. Decision Logs (`olympus-hub-docs/decision-logs/`)

| File | Status | Description |
|------|--------|-------------|
| `0127-request-scoped-authority-delegation.md` | ✅ CREATED | ADR: Two identity domains; delegation outside enterprise IAM |
| `0128-channels-vs-signal-providers-delegation.md` | ✅ CREATED | ADR: Why Channels can delegate but Signal Providers cannot |
| `00XX-authority-request-as-request-update.md` | 🆕 PLANNED | ADR: Authority Request/Grant as REQUEST_UPDATE sub-types |
| `00XX-delegation-policy-composition.md` | 🆕 PLANNED | ADR: All policies must ALLOW (intersection logic) |
| `00XX-delegation-token-per-agent.md` | 🆕 PLANNED | ADR: Token bound to single agent SPIFFE ID |

#### 12. Guides (`olympus-hub-docs/10-guides/`)

| File | Status | Description |
|------|--------|-------------|
| `configuring-request-scoped-delegation.md` | 🆕 NEW | Developer guide: How to configure delegation in TrainingSpec/EmploymentSpec |
| `delegation-template-design.md` | 🆕 NEW | Process Architect guide: Designing appropriate delegation templates |

#### 13. Journeys (`olympus-hub-docs/08-personas-and-journeys/journeys/`)

| File | Status | Changes Required |
|------|--------|------------------|
| `request-lifecycle.md` | ✏️ UPDATE | Add delegation flow to request lifecycle journey |
| `delegation-workflow.md` | 🆕 NEW | New journey: End-to-end delegation from user to agent action |

---

### Update Summary by Area

| Area | New Docs | Updated Docs | Total |
|------|----------|--------------|-------|
| **Hub: Signal Exchange** | 1 | 4 | 5 |
| **Hub: Request Management** | 1 | 4 | 5 |
| **Hub: Channels** | 0 | 3 | 3 |
| **Hub: Implementation Concepts** | 1 | 2 | 3 |
| **Seer: Cipher IAM Extensions** | 3 | 5 | 8 |
| **Seer: Sidecar** | 1 | 3 | 4 |
| **Seer: Agent Ingress Gateway** | 0 | 3 | 3 |
| **Seer: Agent SDK** | 2 | 4 | 6 |
| **Seer: Hub Integration (Specs)** | 0 | 4 | 4 |
| **Seer: Implementation Concepts** | 0 | 4 | 4 |
| **Decision Logs** | 4 | 0 | 4 |
| **Guides** | 2 | 0 | 2 |
| **Journeys** | 1 | 1 | 2 |
| **TOTAL** | **16** | **37** | **53** |

---

### Recommended Update Sequence

**Phase 1: Foundation (Cipher + Core Concepts)**
1. Cipher IAM Extensions — Delegation Templates, Certificates, Tokens
2. Hub Implementation Concept — Request-Scoped Delegation overview
3. ADR — Two Identity Domains decision

**Phase 2: Request Flow (Signal Exchange + Request Management)**
4. Message Envelope — `environment.auth.delegations` schema
5. Request Update — AUTHORITY_REQUEST/GRANTED sub-types
6. Request Management — Delegation context storage and API
7. Signal Exchange — Delegation handling

**Phase 3: Agent Integration (Sidecar + SDK + Gateway)**
8. Seer Sidecar — Delegation service, pre-guardrail check
9. Agent Ingress Gateway — Token forwarding
10. Agent SDK — Delegation APIs

**Phase 4: Specs and Channels**
11. Employment Spec / Training Spec — Delegation configuration
12. Channel documentation — Delegation responsibilities

**Phase 5: Operational Docs**
13. Decision Logs — Remaining ADRs
14. Guides — Developer and Process Architect guides
15. Journeys — End-to-end delegation workflow

---

## Design Critique and Open Questions

> **Added**: 2026-01-17  
> **Purpose**: Capture critical review of the design for future refinement iterations

### Strengths of the Design

1. **Clear Problem Framing**: The distinction between enterprise delegation (permanent, operational) and request-scoped delegation (temporary, task-specific) is well articulated. The "two identity domains" framing prevents conceptual confusion.

2. **OAuth Analogy is Helpful**: Mapping to familiar OAuth concepts (Client = Agent, Access Token = Delegation Access Token, Scope = Template) aids understanding for developers and architects.

3. **Separation of Concerns**: The Template → Certificate → Token hierarchy provides clean layering:
   - Templates define *what* can be delegated
   - Certificates record *consent*
   - Tokens enable *execution*

4. **Comprehensive Flow Coverage**: Proactive, reactive, implicit, and cascading flows are all addressed, covering the main scenarios.

5. **Policy Composition Model**: The "all must ALLOW" intersection logic is correct and prevents privilege escalation.

---

### Potential Concerns and Gaps

#### 1. Certificate Lifecycle Complexity

**Issue**: The design focuses heavily on request-scoped tokens but is less clear on Certificate lifecycle.

| Question | Impact |
|----------|--------|
| How long do Certificates live? | They can "outlive a request" per Q&A, but no max duration is specified |
| What happens when user logs out of all Channels? | Are certificates still valid? Can agent still use them? |
| How does a user revoke access to *one agent* but not others using the same template? | Certificate delegate pattern may allow broad matching |
| What's the user experience for managing Certificates? | No UX guidance provided |

**Recommendation**: Define Certificate lifecycle policies and provide a user-facing Certificate management interface.

---

#### 2. Channel Availability Assumption

**Issue**: The reactive flow assumes a Channel is always available to prompt the user.

| Scenario | Problem |
|----------|---------|
| User started via MCP, then closed connection | No UI to prompt for consent |
| Request takes hours; user goes offline | Authority Request may timeout repeatedly |
| User is on mobile; app is in background | Push notification? Or timeout? |

**Current Fallback**: Timeout → degraded capability (per design). But degraded may not be viable for some use cases (e.g., can't "degrade" bill payment — either it happens or it doesn't).

**Recommendation**: 
- Define structured fallback patterns beyond "degrade"
- Consider async consent flows (email/SMS approval links)
- Provide guidance on which scenarios should "fail" vs. "degrade" vs. "queue and retry"

---

#### 3. Token Refresh Timing

**Issue**: Token refresh happens on REQUEST_UPDATE delivery, but there are edge cases.

| Edge Case | Problem |
|-----------|---------|
| Long gap between REQUEST_UPDATEs | Agent may hold stale/expired token |
| Token about to expire during Tool Gateway call | May fail mid-call |
| Agent is processing synchronously (no updates) | No refresh opportunity |

**Recommendation**: 
- Consider proactive refresh mechanism (agent/sidecar can request refresh)
- Define token validity duration best practices
- Add guidance on handling token expiry during execution

---

#### 4. Multi-Agent Performance

**Issue**: In composite applications with many agents, each needs its own token (per SPIFFE ID). 

| Concern | Impact |
|---------|--------|
| Many agents = many token issuance calls | Cipher IAM load; latency |
| Agents may need tokens for the same template | Redundant Certificate → Token conversions |
| Coordination between agents | How do they know who has delegation? |

**Recommendation**: 
- Consider batch token issuance for known agent sets
- Cache token issuance results (same certificate + same agent = same token)
- Define multi-agent delegation patterns explicitly

---

#### 5. Chaining Depth and Auditability

**Issue**: Chaining can create deep delegation chains that are hard to audit.

| Question | Current Answer |
|----------|----------------|
| Max chain depth? | "Cipher enforces limit" (not specified) |
| Chain provenance tracking? | Certificate links back, but visualization not defined |
| What if chain crosses workbenches? | Audit trail fragmentation? |

**Recommendation**: 
- Define explicit max chain depth (e.g., 3)
- Require chain provenance in Delegation Access Token claims
- Provide tooling to visualize delegation chains

---

#### 6. Business User Identity Federation

**Issue**: The design mentions Cipher maintains business user profiles with "imported claims" but federation mechanism is vague.

| Question | Impact |
|----------|--------|
| How does Cipher know about a new business user? | First login? Pre-provisioning? |
| What claims are imported vs. added? | Policy authoring depends on known claims |
| How do we handle IdP changes (e.g., user email changes)? | Identity continuity |
| What about anonymous/pseudonymous users? | Consumer apps may not have strong identity |

**Recommendation**: Define business user identity onboarding patterns and claim import policies.

---

#### 7. Consent Fatigue and UX Trade-offs

**Issue**: The design optimizes for security (explicit consent via templates), which may create UX friction.

| Trade-off | Options |
|-----------|---------|
| Frequent consent prompts | Consent fatigue; user may approve without reading |
| Long-lived certificates | Less friction, but higher risk if compromised |
| Implicit fulfillment | Good UX, but user may forget they authorized |

**Recommendation**: 
- Provide template design guidance to minimize cognitive load
- Consider "remember this choice" patterns with periodic re-consent
- Define risk tiers (low-risk templates can have longer certificate validity)

---

#### 8. Degraded Capability Semantics

**Issue**: Default behavior on denial/timeout is "degraded capability continuation," but this is undefined.

| Question | Example |
|----------|---------|
| What does "degraded" mean? | Agent can read but not write? Agent informs user and stops? |
| How does agent know what's degraded? | SDK API for checking granted scopes? |
| What if degraded state is unacceptable? | Agent behavior is implementation-specific (not guided) |

**Recommendation**: 
- Define structured degradation patterns
- Provide SDK APIs for capability discovery (`delegation.get_granted_scopes()`)
- Add guidance for agents to communicate degradation to users

---

#### 9. Regulatory and Compliance Considerations

**Issue**: Audit trails are mentioned but compliance requirements are not addressed.

| Requirement | Question |
|-------------|----------|
| GDPR Right to Access | Can users see all their delegation history? |
| GDPR Right to Erasure | Can users delete their delegation history? What about audit requirements? |
| Data Residency | Where are Certificates stored? Does this differ by jurisdiction? |
| SOC2 / PCI-DSS | What controls are needed for Delegation Access Tokens? |

**Recommendation**: Add compliance section addressing these requirements.

---

#### 10. Token Size and Performance

**Issue**: If `delegations` array contains multiple tokens, envelope size grows.

| Concern | Impact |
|---------|--------|
| Multiple JWTs in envelope | Each JWT can be ~1KB; 10 delegations = 10KB overhead |
| Frequent token refresh | Network and Cipher IAM load |
| Token in every REQUEST_UPDATE | Bandwidth for long-running requests |

**Recommendation**: 
- Consider token reference pattern (ID instead of full JWT in envelope)
- Define max delegations per request
- Evaluate compression for high-delegation scenarios

---

#### 11. Revocation Propagation Latency

**Issue**: Revocation is checked on REQUEST_UPDATE delivery, but between updates, a revoked token could still be used.

| Scenario | Risk |
|----------|------|
| User revokes certificate | Token remains valid until next update |
| Malicious agent races to use token | May succeed before revocation propagates |
| Tool Gateway validates token | May accept revoked token if not checking revocation list |

**Recommendation**: 
- Define revocation propagation SLA
- Consider push-based revocation for high-risk templates
- Tool Gateway should check revocation list, not just token signature

---

#### 12. Testing and Observability

**Issue**: No guidance on testing or debugging delegation flows.

| Need | Gap |
|------|-----|
| Developer testing | How to simulate delegation in dev/test? |
| Debugging "why no authority?" | What logs/traces are available? |
| Monitoring | What metrics/alerts for delegation health? |

**Recommendation**: 
- Define test fixtures for delegation flows
- Add delegation events to Cognitive Audit Fabric with query capabilities
- Define key metrics (authority request latency, grant/deny ratio, revocation rate)

---

#### 13. Migration Path

**Issue**: No guidance on transitioning existing agents to request-scoped delegation.

| Question | Impact |
|----------|--------|
| Can an agent use both User delegation and Request-Scoped? | Composition rules unclear |
| How do we migrate a User-delegation agent? | Need gradual adoption path |
| What about existing Scenarios? | Need to add delegation requirements |

**Recommendation**: Define migration patterns and coexistence rules.

---

#### 14. Template Deprecation and Evolution

**Issue**: Templates are immutable and versioned, but deprecation is not addressed.

| Question | Impact |
|----------|--------|
| How to deprecate a template? | Existing certificates may reference it |
| How to migrate to a new template version? | Re-consent required? |
| What if template permissions change? | Security implications |

**Recommendation**: Define template lifecycle (draft → active → deprecated → retired) with migration guidance.

---

### Summary: Priority Areas for Future Refinement

| Priority | Area | Reason |
|----------|------|--------|
| **High** | Channel availability / async consent | Current design assumes synchronous consent |
| **High** | Degraded capability semantics | "Degrade" is undefined; agents need guidance |
| **High** | Revocation propagation | Security risk from latency |
| **Medium** | Certificate lifecycle management | UX and security implications |
| **Medium** | Business user identity federation | Foundation for delegation |
| **Medium** | Testing and observability | Essential for adoption |
| **Low** | Token size optimization | Performance concern for high-delegation scenarios |
| **Low** | Template evolution | Needed for long-term maintenance |

---

### Positive Note

Despite these open questions, the core design is **sound and well-structured**. The OAuth analogy, the Template → Certificate → Token hierarchy, and the clear component responsibilities provide a solid foundation. These critiques represent refinement opportunities, not fundamental flaws.
