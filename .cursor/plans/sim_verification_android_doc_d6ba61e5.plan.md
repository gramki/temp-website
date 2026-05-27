---
name: SIM Verification Android Doc
overview: Write a comprehensive analysis document `draft-sim-verification-android.md` in the `supplement-telco-device-attestation/` folder, covering the OMAPI-based SIM verification approach, comparison with alternatives, telco requirements, constraints, mitigations, and a detailed security/UX analysis of the recommended approach and discarded alternatives. Also update `03-telco-attestation-protocol.md` Section 8 (SIM Verification) to reference the new document.
todos:
  - id: sec1-problem
    content: "Write Section 1: Problem Statement"
    status: completed
  - id: sec2-mechanisms
    content: "Write Section 2: Available Mechanisms — Comparative Analysis (6 mechanisms + comparison matrix)"
    status: completed
  - id: sec3-recommended
    content: "Write Section 3: Recommended Approach — OMAPI with Attestation Applet (design, protocol integration, fallback)"
    status: completed
  - id: sec4-security-ux
    content: "Write Section 4: Security and UX Analysis (recommended approach weaknesses, discarded alternatives, UX comparison)"
    status: completed
  - id: sec5-telco-reqs
    content: "Write Section 5: Telco Requirements (applet dev, OTA, ARA-M, key mgmt, eSIM)"
    status: completed
  - id: sec6-constraints
    content: "Write Section 6: Constraints and Risks"
    status: completed
  - id: sec7-mitigations
    content: "Write Section 7: Mitigation Approaches"
    status: completed
  - id: sec8-conclusion
    content: "Write Section 8: Conclusion"
    status: completed
  - id: update-protocol
    content: Update 03-telco-attestation-protocol.md Section 8 to reference the new analysis
    status: completed
isProject: false
---

# SIM Verification on Android — Detailed Document Plan

## Target file

`misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/draft-sim-verification-android.md`

## Document structure (8 sections, written sequentially)

### Section 1: Problem Statement

- The ECDHE + Binder + timing flow proves mutual authentication between RPA and Telco App on the same device but does NOT prove SIM presence
- Define precisely what "SIM verification" must prove: the specific physical SIM (not just MSISDN or network registration) is present, active, and belongs to the Telco
- Distinguish between: network-level identity (which number is this?), physical presence (is the SIM chip here?), and cryptographic attestation (can this SIM prove it is what it claims?)

### Section 2: Available Mechanisms — Comparative Analysis

Six subsections, one per mechanism. Each covers: how it works (API surface), what it proves, what it does NOT prove, prerequisites, strengths, weaknesses.

- **2.1 SIM Applet via OMAPI** — `SEService` / `Reader` / `Session` / `Channel` / `transmit()`. ARA-M access control. Challenge-response with SIM-resident private key. Available since Android 9 (API 28).
- **2.2 SIM Applet via TelephonyManager APDU** — `iccOpenLogicalChannel()`, `iccTransmitApduLogicalChannel()`. Same applet, different code path through the modem. Relevant as OEM fallback.
- **2.3 Silent Network Authentication (GSMA Number Verify)** — HTTP over mobile data, PGW subscriber identification. WiFi limitation, dual-SIM ambiguity, DSDS switching, CGNAT, SIM swap blind spot, roaming.
- **2.4 USSD** — `sendUssdRequest()`, signaling channel, unencrypted, synchronous, unreliable, user-visible dialogs, no crypto, rate-limited.
- **2.5 TelephonyManager Standard APIs** — `getSimState()`, `getSimOperator()`, IMSI/ICCID (carrier-privileged only). No crypto. Spoofable with root.
- **2.6 Carrier Privileges Check** — `hasCarrierPrivileges()`. ARA-M certificate hash match. Subsumed by OMAPI access control.
- **2.7 Comparison Matrix** — summary table across: crypto strength, SIM presence proof, network dependency, dual-SIM handling, WiFi support, custom SIM requirement, OEM consistency, UX impact.

### Section 3: Recommended Approach — OMAPI with Attestation Applet

- **3.1 Why OMAPI** — synthesis of Section 2 comparison. Cryptographic proof from separate hardware trust anchor; no network dependency; clean dual-SIM; millisecond latency; no UX disruption.
- **3.2 Attestation Applet Design** — high-level spec. AID structure. APDU commands (SELECT, CHALLENGE, GET_PUBLIC_KEY). Key pair generation on-SIM at provisioning. Signing algorithm (ECDSA P-256 preferred; RSA 2048 fallback for JavaCard 2.2.x). Challenge format (nonce + session context binding). Response format (signature + attestation metadata).
- **3.3 Integration with Protocol Flow** — where the SIM applet interaction sits in the 13-step transaction flow from [03-telco-attestation-protocol.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/03-telco-attestation-protocol.md) (after session key derivation, before SIM claim production). The applet's signed attestation is included in the encrypted SIM claim.
- **3.4 Fallback: TelephonyManager APDU** — same applet, different API. When to use (broken OMAPI). Detection and fallback logic.

### Section 4: Security and UX Analysis

This is the detailed analysis section covering BOTH the recommended approach and discarded alternatives.

**4.1 Security analysis of the recommended approach (OMAPI + Attestation Applet)**

- Compromise vectors specific to SIM applet path:
  - Root + OMAPI hooking: can Frida intercept APDU commands/responses? (The APDU goes through the modem/baseband — a separate processor. Hooking the Java-level OMAPI call can observe the challenge/response but cannot forge the SIM's signature.)
  - SIM cloning: physical extraction of SIM private key requires chip decapping — $10K+ per attempt, not scalable.
  - Relay attack on the SIM applet: attacker on a rooted device relays APDU to a remote SIM. Timing constraints and session binding to the ECDHE context prevent this.
  - ARA-M tampering: requires ISD keys — only the Telco holds these.
- Strengths: two independent hardware trust anchors (StrongBox + SIM secure element); SIM applet is isolated from Android OS entirely.
- **Weaknesses that need compensation**:
  - OMAPI OEM inconsistency — compensated by TelephonyManager APDU fallback
  - Legacy SIMs without applet — compensated by phased rollout and transaction limits
  - Logical channel contention — compensated by prompt open-transact-close pattern
  - JavaCard 2.2.x SIMs without ECC — compensated by RSA fallback in applet
  - SIM contact issues on budget devices — compensated by retry logic and user guidance

**4.2 Security analysis of discarded alternatives**

- Silent Network Auth: no physical SIM proof (SIM swap passes), WiFi blind spot, CGNAT ambiguity, dual-SIM data routing issues, dependency on telco PGW infrastructure.
- USSD: unencrypted (IMSI catcher can intercept/modify), no cryptographic attestation, synchronous/blocking, rate-limited — fundamentally not a security mechanism.
- TelephonyManager APIs: spoofable with root (identifiers come through RIL, hookable), no challenge-response, no crypto.
- Carrier Privileges alone: proves SIM-app binding but not SIM liveness or freshness — a static check with no challenge-response.

**4.3 UX analysis — recommended approach vs. alternatives**

- OMAPI: invisible to user (no prompt, no network switch, no dialog), millisecond latency, works on WiFi, works offline. Best UX.
- SNA: may require WiFi→cellular switch (connectivity blip, user confusion), fails if cellular data off, DSDS data SIM switching visible to user.
- USSD: may pop up system dialogs, noticeable delay (1-3 seconds), blocks radio signaling.
- The recommended approach is the only one that adds zero user-perceptible friction.

### Section 5: Telco Requirements

- **5.1 Applet Development and Certification** — JavaCard attestation applet, testing across SIM vendors (Thales, Idemia, G+D, local), GlobalPlatform certification.
- **5.2 OTA Provisioning Infrastructure** — GlobalPlatform RAM, SMS-PP/BIP delivery, capacity planning for millions of SIMs.
- **5.3 ARA-M Management** — new SIMs: provisioned at manufacturing. Existing SIMs: OTA ARA-M update. Prerequisite: ISD key custody.
- **5.4 Key Management** — ISD key custody audit, per-SIM applet key pair provisioning (generated on-SIM, public key registered with Telco Server), deactivation/porting/replacement lifecycle.
- **5.5 eSIM Considerations** — applet inclusion in eSIM profile packages at SM-DP+. OTA push to activated profiles via ISD-P. Same OMAPI interface.

### Section 6: Constraints and Risks

- **6.1 Legacy SIM Cards** — memory, JavaCard version, flash degradation. Estimate of tail.
- **6.2 SIM Vendor Key Custody** — batches where telco doesn't hold ISD keys. Cannot OTA provision or update ARA-M.
- **6.3 OMAPI OEM Inconsistency** — broken SEService on some OEMs (Xiaomi, others). OMAPI disabled at build time.
- **6.4 BSNL Infrastructure Gap** — OTA platform, JavaCard capability, SIM vendor diversity.
- **6.5 Logical Channel Contention** — finite channels (3-4), NFC/banking applets may hold channels.
- **6.6 Baseband/Modem Quirks** — APDU delays during telephony, OEM modem differences, timeout handling.

### Section 7: Mitigation Approaches

- **7.1 Phased Rollout by SIM Capability** — Tier 1 (new SIMs, immediate), Tier 2 (OTA to existing, 3-6 months), Tier 3 (replacement for legacy, 12-18 months). Transaction limits tiered by SIM capability.
- **7.2 OEM Compatibility Program** — OMAPI conformance testing, top 20 devices by India market share, TelephonyManager APDU fallback, OEM escalation path.
- **7.3 Telco Readiness Assessment** — OTA platform audit, ISD key custody, ARA-M management. Gap analysis per telco. Timeline commitments.
- **7.4 SIM Replacement Incentive** — free replacement for legacy SIMs, aligned with 4G-to-5G migration.
- **7.5 Graceful Degradation** — devices/SIMs without applet: carrier privileges check + SNA (where available), lower transaction limits. No SMS OTP fallback for high-value transactions.

### Section 8: Conclusion

- OMAPI + attestation applet is the recommended primary mechanism
- Provides cryptographic SIM presence proof from tamper-resistant hardware, independent of device OS and main processor
- Constraints are operational (telco readiness, legacy SIMs, OEM consistency), not architectural — each has a defined mitigation
- Combined with the ECDHE + Binder + timing flow, the protocol has two independent hardware trust anchors (StrongBox for app keys, SIM secure element for SIM attestation)

## Secondary update

After the document is complete, update [03-telco-attestation-protocol.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/03-telco-attestation-protocol.md) Section 8 (SIM Verification) to:

- Replace the current placeholder text with a summary of the OMAPI approach
- Reference `draft-sim-verification-android.md` for the full analysis

