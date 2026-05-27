---
name: Editorial fixes telco-attestation
overview: Apply all resolved Priority 1 structural fixes and Priority 4 editorial polish items across the telco-device-attestation repository, then update to-fix.md to reflect completion and deferral status.
todos:
  - id: p1-ios-validation
    content: "P1.1 + P1.2: Simplify carrierToken validation language, add TTL/caching/SIM-change semantics in 03-platform-ios.md"
    status: completed
  - id: p1-ios-failure
    content: "P1.3: Remove degraded-path language from iOS failure modes table in 03-platform-ios.md"
    status: completed
  - id: p1-ios-tokenization
    content: "P1.4: Clarify per-RPA tokenization non-issue in 03-platform-ios.md"
    status: completed
  - id: p1-android-hard-fail
    content: "P1.3: Remove degraded mode from Android weaknesses table; reframe Play Integrity 'No verdict' row in 02-platform-android.md"
    status: completed
  - id: p1-protocol-identity
    content: "P1.4: Reframe Step 15k subscriber identity response in 01-protocol.md"
    status: completed
  - id: p1-security-validation
    content: "P1.1: Simplify carrierToken validation reference in appendix-security-analysis.md Section 8.7"
    status: completed
  - id: p4-ios-editorial
    content: "P4.1 + P4.3 + P4.6: Shelf-life fix, RPA expansion, cross-ref standardization in 03-platform-ios.md"
    status: completed
  - id: p4-android-editorial
    content: "P4.3 + P4.6: RPA expansion, cross-ref standardization in 02-platform-android.md"
    status: completed
  - id: p4-protocol-editorial
    content: "P4.4 + P4.7: Telco Server abbreviation, SIM presence vs identity definition in 01-protocol.md"
    status: completed
  - id: p4-security-editorial
    content: "P4.5 + P4.8: Condense analytical method, add TOC in appendix-security-analysis.md"
    status: completed
  - id: p4-camara-editorial
    content: "P4.2: Remove date prefix in appendix-camara-comparison.md"
    status: completed
  - id: update-tofix
    content: Mark all items in to-fix.md as RESOLVED or DEFERRED
    status: completed
isProject: false
---

# Editorial and Structural Fixes for telco-device-attestation

## Scope

- **Priority 1 (4 items)**: Structural fixes based on author answers — carrierToken validation scoping, TTL/caching semantics, hard failure on SIM attestation unavailability (both platforms), subscriber identity response framing.
- **Priority 4 (8 items)**: Editorial polish — shelf-life dates, vocabulary, nomenclature, meta-narration, cross-references, terminology, TOC.
- **Priority 2 & 3**: Mark as deferred in `to-fix.md`.

---

## P1 Changes by File

### [03-platform-ios.md](personal-projects/telco-device-attestation/03-platform-ios.md)

**1.1 — Simplify carrierToken validation language (telco's internal concern)**

- **Lines 196–199**: Replace "validates the carrier_token against the Entitlement Server backend" with "validates the carrier_token using the carrier's established token verification mechanism"
- **Lines 357–359** (Prerequisite 3): Replace "the Attestation Server needs access to the Entitlement Server's token validation endpoint or shared signing key" with "this is an internal integration within the telco's own infrastructure, using whatever token verification mechanism the carrier has established"

**1.2 — carrierToken TTL, caching, and SIM-change invalidation**

- **Line 365** (residual differences table, "Token freshness model" row): Update iOS column to clarify that the protocol relies on token authenticity, not freshness; the Telco App must ensure the token has at least one minute of remaining validity; the Secure Enclave signature over the per-transaction nonce provides session binding
- **Lines 181–188** (Step 8): After the refresh flow, add a note: the Telco App must invalidate any cached `carrierToken` upon detecting a SIM change (e.g., via `CTSubscriber` identity change notification); a cached token from a previous SIM must never be used

**1.3 — Hard failure when carrierToken unavailable**

- **Lines 496–504** (failure modes table): Remove all "Falls back to degraded authentication" and "falls back" language from the Telco App not installed, outdated, and mTLS failure rows. Replace with: attestation fails; the RPA receives an error and determines its own business-level response (which is outside the protocol's scope)

**1.4 — Per-RPA tokenization not a privacy concern on iOS**

- **Line 289**: After "encrypted subscriber identifier", add a clarifying note that the `carrierToken`'s subscriber identifier is not per-RPA — it is the same for all requesting apps. This is not a privacy exposure because the RPA never sees the raw `carrierToken` (it is encrypted inside the JWE, decrypted only by the Telco Server)

### [02-platform-android.md](personal-projects/telco-device-attestation/02-platform-android.md)

**1.3 — Hard failure when SIM attestation unavailable**

- **Line 91** (Play Integrity "No verdict" row): Change "Degraded — fallback path, minimal transactions" to "Risk-informed — Telco Server and RPA Server may apply risk-based transaction limits; the protocol's core SIM and enclave guarantees are unaffected"
- **Line 429** ("Legacy SIMs without applet" row): Change compensation from "Transaction limits tiered by SIM capability" to "Phased rollout: new SIMs pre-provisioned, existing SIMs receive OTA push, legacy SIMs replaced. Attestation is unavailable until the applet is provisioned — the protocol does not define a degraded mode"
- **Line 432** ("SIM contact issues" row): Change "Graceful degradation to lower transaction limits" to "If retries fail, attestation fails. The RPA determines its own business-level response"

### [01-protocol.md](personal-projects/telco-device-attestation/01-protocol.md)

**1.4 — Subscriber identity response framing**

- **Lines 348–351** (Step 15k response): Reframe `subscriber_phone_number` to clarify: the Telco Server returns verified subscriber identity, which typically includes the MSISDN; the Telco Server is encouraged to provide a per-RPA tokenized subscriber identifier; whether MSISDN is included depends on the contractual arrangement between the Telco and the RPA (analogous to OpenID Connect scope-based claims)

### [appendix-security-analysis.md](personal-projects/telco-device-attestation/appendix-security-analysis.md)

**1.1 — Simplify carrierToken validation reference**

- **Line ~1253** (Prerequisite 3 in Section 8.7): Same simplification as in `03-platform-ios.md` — replace specifics about "token validation endpoint or shared signing key" with "internal integration using the carrier's established verification mechanism"

---

## P4 Changes by File

### [03-platform-ios.md](personal-projects/telco-device-attestation/03-platform-ios.md)

- **4.1**: Line 549 — Replace "iOS 14+ covers ~95% of active iPhones in India (2026 estimate)" with "iOS 14+ covers ~95% of active iPhones in India — a proportion that only grows as older devices age out"
- **4.3**: Header paragraph (line 3) — Add "(Relying Party App — the bank or PSP app)" after first use of "RPA"
- **4.6**: Standardize "the protocol doc" to "the [protocol specification](01-protocol.md)" on first use; use file-based references for subsequent mentions

### [02-platform-android.md](personal-projects/telco-device-attestation/02-platform-android.md)

- **4.3**: Header paragraph (line 3) — Add "(Relying Party App — the bank or PSP app)" after first use of "RPA"
- **4.6**: Standardize "the protocol doc" to "the [protocol specification](01-protocol.md)" on first use; use file-based references for subsequent mentions

### [01-protocol.md](personal-projects/telco-device-attestation/01-protocol.md)

- **4.4**: Line 22 — After "Telco Attestation Server" definition, add "(referred to as **Telco Server** hereafter)"
- **4.7**: Section 11 (line ~500) — Add definition: "SIM presence: the SIM is physically operational in the device. SIM identity: which specific SIM is present. The protocol requires both — the attestation proves a specific SIM (identity) is currently in this device (presence)."

### [appendix-security-analysis.md](personal-projects/telco-device-attestation/appendix-security-analysis.md)

- **4.5**: Lines 93–103 — Condense Section 1.4 to one sentence: "The analysis proceeds from trust anchor substantiation (Sections 2–4) through compromise vector evaluation (Section 5) to residual risk identification (Section 8)."
- **4.8**: After the header block — Add a table of contents with anchor links to all numbered sections

### [appendix-camara-comparison.md](personal-projects/telco-device-attestation/appendix-camara-comparison.md)

- **4.2**: Line 13 — Replace "As of early 2026, 140 API instances have been commercially launched across 85 networks in 50 markets" with "CAMARA has reached 140+ commercial API instances across 85 networks in 50 markets [GSMA-OG-Q1-2026]"

---

## Housekeeping

### [to-fix.md](personal-projects/telco-device-attestation/to-fix.md)

- Mark P1 items as **RESOLVED** with a one-line summary of the applied fix
- Mark P2 and P3 items as **DEFERRED**
- Mark P4 items as **RESOLVED**
