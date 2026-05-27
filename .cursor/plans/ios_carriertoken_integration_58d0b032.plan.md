---
name: iOS carrierToken Integration
overview: Integrate CTSubscriber.carrierToken as the iOS SIM attestation mechanism. Rather than patching individual sections, rewrite each affected section in its entirety so the carrierToken mechanism reads as native to the document's structure — not retrofitted. Every reference to the iOS SIM gap across four documents must be updated consistently.
todos:
  - id: ios-supplement
    content: "Rewrite iOS supplement: Section 1 table, Step 8, Section 4, Section 6, Impact block, Section 8 tables, Section 9 conclusion"
    status: completed
  - id: protocol-doc
    content: Update protocol doc Section 11 and bottom table entry
    status: completed
  - id: security-appendix
    content: Rewrite security analysis Section 8.7 and update scope line 101
    status: completed
  - id: camara-appendix
    content: Rewrite CAMARA comparison Section 5.3 and conclusion
    status: completed
isProject: false
---

# iOS carrierToken Integration Plan

## Guiding Principle: No Patchwork

Each affected section will be rewritten in full, preserving the surrounding document's voice, depth, and analytical style. The carrierToken mechanism should read as if the document was written with this knowledge from the start — no "update:" markers, no "we have since discovered" language, no retrofitted tone.

## Complete Inventory of Changes

Every reference to the iOS SIM gap across four documents has been identified. Changes are grouped by document.

---

### Document 1: iOS Supplement

**File**: `[draft-ios-architecture.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/draft-ios-architecture.md)`

This document has the most changes. The carrierToken mechanism is defined here in detail; all other documents reference this one.

**a) Section 1 summary table (line 28)**
Current: `| SIM applet access | OMAPI (direct APDU to SIM) | No equivalent API | Critical gap |`
Rewrite: Describe `CTSubscriber.carrierToken` as the iOS mechanism, noting it uses EAP-AKA via the carrier's Entitlement Server rather than direct APDU. Impact column: "Different mechanism, equivalent security properties."

**b) Section 3, Step 8 (line 181-182)**
Current: `(See Section 4 — SIM access is the critical iOS gap)`
Rewrite as a concrete step: Telco App retrieves `carrierToken` via `CTSubscriber.carrierToken` (refreshing if expired via `refreshCarrierToken()`), constructs the attestation payload incorporating the token alongside session fields, and signs the composite with the Telco App's Secure Enclave key.

**c) Section 4 "SIM Verification on iOS" (lines 206-297) — Full rewrite**
Current: Opens with "The critical gap," presents four speculative Options A-D, concludes with a comparison matrix and recommendation.
Rewrite as a section that:

- Opens by describing how iOS approaches SIM identity differently from Android (system-mediated vs. app-direct)
- Presents `CTSubscriber.carrierToken` as the iOS SIM presence mechanism, explaining the full EAP-AKA flow through CommCenter and the Carrier Entitlement Server
- Details the composite attestation construction (carrierToken + Secure Enclave signature over session-specific fields)
- Maps the four Android security properties (SIM presence, session binding, freshness, non-forgeability) against the iOS construction
- Notes prerequisites: TS.43-compliant Entitlement Server, `com.apple.CommCenter.fine-grained` entitlement, Telco Attestation Server integration
- Covers eSIM parity (eUICC uses same EAP-AKA mechanism)
- Discusses residual differences from Android (token validity window vs. per-transaction nonce, network dependency for token refresh, Entitlement Server availability)

**d) Section 6 "Reduced SIM assurance" (lines 375-386) — Full rewrite**
Current: Presents a table showing iOS as weaker on "SIM swap on same device."
Rewrite: The section should now be titled something like "SIM Assurance Comparison" and show that with carrierToken, iOS achieves equivalent assurance across all three scenarios (SIM swap on different device, SIM swap on same device, stolen device with original SIM). A swapped SIM produces a different carrierToken because the EAP-AKA challenge is resolved by the new SIM's Ki.

**e) "Impact on protocol security" (lines 288-297)**
Current: States iOS has one trust anchor instead of two, with reduced SIM assurance.
Rewrite: State that iOS achieves dual-anchor parity — the carrierToken provides the SIM trust anchor via EAP-AKA, the Secure Enclave provides the device trust anchor. The trust decomposition differs from Android (Android: SIM applet signs challenge directly; iOS: SIM authenticates via EAP-AKA, device enclave signs the composite) but the security properties converge.

**f) Section 8 requirements table (line 445)**
Current: `| SIM verification | Carrier entitlement (Option A) or SNA fallback (Option C) |`
Rewrite: `| SIM verification | CTSubscriber.carrierToken (carrier entitlement required) |`

**g) Section 8 constraints table (line 468)**
Current: `| No SIM APDU access | Protocol operates at reduced SIM assurance |`
Remove this row or reframe: iOS does not use APDU but achieves equivalent SIM attestation via carrierToken. The constraint is the carrier entitlement prerequisite, not a security gap.

**h) Section 9 conclusion bullet (line 494)**
Current: `Cryptographic SIM attestation: The critical gap.`
Rewrite: Describe carrierToken as providing cryptographic SIM attestation via EAP-AKA. Note that the remaining dependency is the carrier entitlement and TS.43 Entitlement Server deployment.

---

### Document 2: Protocol Doc

**File**: `[03-telco-attestation-protocol.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/03-telco-attestation-protocol.md)`

**a) Step 8 platform note (lines 265-275)**
The current text says iOS SIM applet access is via a "platform-specific mechanism — see platform supplements." This framing is fine and can stay generic. No change needed to the step itself — it already defers to the platform supplements.

**b) Section 11 "SIM Verification" (lines 498-508)**
Current line 506: `iOS: SIM applet access is architecturally constrained. See iOS supplement.`
Rewrite: `iOS: CTSubscriber.carrierToken provides SIM presence proof via EAP-AKA challenge-response, mediated by the OS CommCenter and the carrier's TS.43 Entitlement Server. The Telco App embeds the carrierToken in a Secure Enclave-signed attestation payload, achieving dual-anchor attestation. See iOS supplement.`

Current line 508: The "two independent hardware trust anchors" paragraph currently implies this is Android-only. Rewrite to state this holds on both platforms — Android via OMAPI applet, iOS via carrierToken + Secure Enclave.

**c) Line 558 (README-style table at bottom)**
Current: `SIM access constraints`
Rewrite: `SIM attestation via carrierToken, iOS-specific security/UX analysis`

---

### Document 3: Security Analysis Appendix

**File**: `[appendix-security-analysis.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/appendix-security-analysis.md)`

**a) Section 8.7 (lines 1237-1241) — Full rewrite**
Current title: "iOS SIM Access — eSIM Profile-Level Attestation"
Current content: Frames iOS as a "fundamental gap," proposes eSIM profile-level attestation as the most promising path, notes dependency on Apple.

New title: "iOS SIM Attestation — carrierToken via EAP-AKA"
Rewrite to:

- Describe how iOS achieves SIM presence proof through `CTSubscriber.carrierToken`, which triggers an EAP-AKA challenge-response with the SIM's Ki via the OS CommCenter and the carrier's TS.43 Entitlement Server
- Explain the composite construction (carrierToken + Secure Enclave signature) that achieves session-bound dual-anchor attestation
- Note the prerequisites (carrier entitlement, TS.43 server deployment) and that Indian telcos likely already operate TS.43 servers for VoLTE/eSIM
- Retain eSIM profile-level applet access as a forward-looking enhancement for deeper SIM-level operations beyond attestation
- Frame the remaining open question as one of deployment prerequisites, not architectural feasibility

**b) Scope paragraph (line 101)**
Current: `platform gaps (iOS SIM access)`
Rewrite: `platform prerequisites (iOS carrier entitlement deployment)`

---

### Document 4: CAMARA Comparison Appendix

**File**: `[appendix-camara-comparison.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/appendix-camara-comparison.md)`

**a) Section 5.3 "iOS Gap Mitigation" (lines 251-253) — Full rewrite**
Current: Positions CAMARA as compensating for the missing iOS SIM attestation.
Rewrite title to something like "iOS Complementary Signals" and reposition:

- Note that iOS achieves on-device SIM attestation via carrierToken (EAP-AKA-based)
- CAMARA's SIM Swap and Number Verification serve the same complementary role on iOS as on Android — pre-transaction risk signals and defense-in-depth, not gap compensation
- Remove the "single-anchor" language

**b) Conclusion (line 300)**
Current: mentions CAMARA signals "partially compensate for the iOS SIM-access gap"
Rewrite: remove the iOS gap compensation language; CAMARA's role is uniform across both platforms.

---

## Execution Order

1. **iOS supplement** — all changes (a through h). This is the authoritative source; all other docs reference it.
2. **Protocol doc** — Section 11 and table entry.
3. **Security analysis appendix** — Section 8.7 and scope line.
4. **CAMARA comparison** — Section 5.3 and conclusion.

