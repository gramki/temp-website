# Notification Services - Open Points

> **Status:** 🟡 Open Questions — Requiring Clarification

This document captures open points and questions that need clarification for the Notification Services subsystem.

---

## Observer Subscription Scope

**Issue:** Observer registration subscribes at tenant level, but callback URLs are registered per workbench.

**Question:**
- Should Notification Service subscribe per workbench instead of at tenant level?
- Or does it subscribe at tenant level and route callbacks based on `workbench_id` in the correlation data?
- How does it determine which workbench callback URL to use when receiving callbacks from CNS?

**Current State:**
- Observer registration: Tenant-level subscription
- Callback URLs: Per workbench registration

---

## Correlation Tracker in CTA URL

**Issue:** CTA URL includes `{{correlation_tracker}}` placeholder, but it's unclear who replaces it and when.

**Question:**
- Is `{{correlation_tracker}}` a Mustache template variable that Notification Service replaces before sending to CNS?
- Or is it a placeholder that CNS replaces when generating the final CTA URL?
- When is the correlation tracker generated (by NS or CNS)?

**Current State:**
- CTA URL example shows: `"url": "https://hub/requests/req-12345/approve?cta=approve&corr={{correlation_tracker}}"`
- Documentation says "CNS generates appropriate correlation tracker in CTA URL string"

---

## CTA URL Generation Process

**Issue:** The process of generating final CTA URLs with correlation trackers is not fully specified.

**Question:**
- Does Notification Service send CTA URLs as templates to CNS, and CNS replaces placeholders?
- Or does Notification Service generate final URLs after receiving correlation tracker from CNS?
- What is the exact flow for CTA URL generation and correlation tracker injection?

---

## Preconfigured Trigger for Delivery Failures

**Issue:** Documentation mentions "preconfigured built-in trigger" that translates delivery failure signals to MEMO, but this trigger is not documented elsewhere.

**Question:**
- Where is this trigger defined?
- Is it a system-level trigger in Signal Exchange?
- Should this be documented in Signal Exchange trigger documentation?
- What is the trigger ID/name for reference?

**Current State:**
- Mentioned in delivery failure handling flow
- Not documented in Signal Exchange trigger documentation

---

## Signal Provider Registration Lifecycle

**Issue:** Notification Service needs to register as Signal Provider for CTA signal creation, but registration lifecycle is not specified.

**Question:**
- When does Notification Service register as Signal Provider?
  - At service startup (once globally)?
  - Per tenant subscription?
  - Per workbench?
- What is the registration payload structure?
- Is it a one-time registration or per-tenant/workbench?

**Current State:**
- Documentation says "Notification Service acts as a Signal Provider (registered with Signal Exchange)"
- No registration lifecycle details provided

---

## Persona Handler Selection Logic

**Issue:** When a user has multiple personas (e.g., agent and supervisor), the handler selection logic is not specified.

**Question:**
- How is the appropriate handler selected?
  - Priority-based (e.g., Supervisor > Agent)?
  - Context-based (e.g., based on notification event type)?
  - All applicable handlers (e.g., send to both Agent and Supervisor handlers)?
- What is the selection algorithm?

**Current State:**
- Documentation says "determines appropriate handler based on context of notification and user's roles"
- No specific logic documented

---

## Scenario Specification Caching

**Issue:** Notification Service queries Workbench Management for Scenario specifications, but caching strategy is not mentioned.

**Question:**
- Are Scenario specifications cached by Notification Service?
- What is the cache invalidation strategy?
- How are Scenario version changes handled?
- What is the performance impact of per-request lookups vs caching?

**Current State:**
- Documentation says "Queries Workbench Management for Scenario specification"
- No caching strategy mentioned

---

## Read Receipt Mechanism Support

**Issue:** Read receipts are mentioned but mechanism-specific support is not fully documented.

**Question:**
- Which mechanisms support read receipts?
  - Email: Yes (typically)
  - Push: Yes (typically)
  - SMS: No (typically)
  - Webhook: Depends on implementation?
- Should this be documented per mechanism?
- How are read receipts handled for mechanisms that don't support them?

**Current State:**
- Read receipts mentioned as callback type
- Mechanism-specific support not fully documented

---

## Multiple Recipients with Same Preferences

**Issue:** When multiple recipients have identical preferences, optimization opportunities are not addressed.

**Question:**
- Should notifications be batched when recipients share preferences?
- Or is individual sending always required?
- Are there performance optimizations for bulk notifications?

**Current State:**
- Documentation says "each recipient receives notifications individually"
- No optimization strategies mentioned

---

## Time Window Enforcement

**Issue:** Time windows are mentioned in preferences but enforcement logic is not specified.

**Question:**
- How are time windows enforced?
  - Queue notifications outside window for later delivery?
  - Skip notifications outside window?
  - Send immediately regardless of time window?
- What timezone is used for time window evaluation?
- How are time windows handled across different timezones for global users?

**Current State:**
- Time windows mentioned in preference structure
- Enforcement logic marked as "need not specify at this stage"

---

## Template Variable Availability

**Issue:** Template variables are listed but complete data model is not specified.

**Question:**
- What is the complete structure of available template variables?
- Are nested objects accessible (e.g., `{{request.subject.name}}`)?
- What happens if a template variable is missing (error or empty string)?
- Are there helper functions available in templates?

**Current State:**
- Basic template variables listed
- Complete data model and error handling not specified

---

## Related Documentation

- [Notification Services README](./README.md) — Main documentation
- [Signal Exchange](../signal-exchange/README.md) — Observer notifications
- [Signal Provider Interactions](../signal-exchange/signal-provider-interactions.md) — Signal Provider registration

---

*These open points should be resolved during detailed design phase.*

