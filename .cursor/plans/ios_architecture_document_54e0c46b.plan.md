---
name: iOS architecture document
overview: Write a detailed iOS architecture document parallel to the Android SIM verification doc, covering the localhost mTLS + Universal Links IPC design, SIM access options, security analysis, and iOS-specific constraints.
todos:
  - id: sec1-ios-context
    content: "Write Section 1: Problem Statement and iOS Context (what carries over, what changes)"
    status: pending
  - id: sec2-ipc
    content: "Write Section 2: IPC on iOS — Localhost mTLS (evaluation of options, recommended approach, security analysis vs Binder, Universal Links both legs)"
    status: pending
  - id: sec3-flow
    content: "Write Section 3: Per-Transaction Flow — iOS 16-step flow adapted for localhost mTLS + Universal Links + App Attest"
    status: pending
  - id: sec4-sim
    content: "Write Section 4: SIM Verification on iOS (carrier entitlements, eSIM attestation, SNA, Apple API, comparison matrix, recommendation)"
    status: pending
  - id: sec5-security
    content: "Write Section 5: Security Analysis (localhost mTLS security, App Attest vs Play Integrity, platform advantages, SIM gap assessment)"
    status: pending
  - id: sec6-ux
    content: "Write Section 6: UX Analysis (app switch flow, failure modes, comparison with Android)"
    status: pending
  - id: sec7-requirements
    content: "Write Section 7: iOS-Specific Requirements (Telco, RPA, Apple, registration additions)"
    status: pending
  - id: sec8-constraints
    content: "Write Section 8: Constraints and Risks (Apple policy, carrier entitlement uncertainty, eSIM trend, iOS version reqs)"
    status: pending
  - id: sec9-conclusion
    content: "Write Section 9: Conclusion"
    status: pending
  - id: update-existing-docs
    content: Update protocol doc Section 9, Participants section, README, and analysis inputs to reference iOS doc
    status: pending
isProject: false
---

# iOS Architecture Document — Detailed Writing Plan

## Target file

`misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/draft-ios-architecture.md`

A new document parallel in structure to [draft-sim-verification-android.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/draft-sim-verification-android.md), covering the full iOS-specific protocol design.

## Design decisions already made (from discussion)

- **IPC**: Localhost TCP + mTLS (RPA as server, Telco App as client)
- **App launch**: Universal Links in both directions (RPA -> Telco App, Telco App -> RPA callback)
- **Callback**: RPA passes its Universal Link callback URL in the initial launch; Telco App fires it when exchange is complete; attestation data delivered over localhost TCP, callback is just a "come back" signal
- **Same-device guarantee**: Localhost (127.0.0.1) is kernel-routed; mTLS provides mutual authentication; timing challenge via `mach_absolute_time()`
- **Device attestation**: Apple App Attest (DeviceCheck framework) replaces Play Integrity

## Document structure — section by section

### Section 1: Problem Statement and iOS Context

- Why a separate iOS architecture is needed
- What carries over from Android unchanged (PKI hierarchy, SIM applet, JWE structure, server-side flow Steps 14-16, session_id structure, proof-of-possession)
- What fundamentally changes (IPC mechanism, SIM access APIs, device attestation API, app lifecycle)
- Reference to the Android doc and protocol spec

### Section 2: IPC on iOS — Localhost mTLS

- Why Binder doesn't exist on iOS
- Evaluation of iOS IPC options (URL Schemes, Universal Links, App Groups/Shared Keychain, Multipeer Connectivity, localhost TCP) with merits/demerits
- **Recommended approach**: Localhost TCP + mTLS
  - RPA opens listening socket (server role) — RPA is in foreground, no background execution issue
  - RPA launches Telco App via Universal Link with port, session_id, rpa_id, rpa_instance_id, callback Universal Link
  - Telco App connects to 127.0.0.1:port as TLS client
  - mTLS handshake — both sides present Telco CA-rooted certificates
  - Same-device guarantee: localhost is kernel-routed, cannot leave device on non-jailbroken iOS
- **Security analysis of localhost mTLS vs. Binder**: what's equivalent (mutual auth, same-device), what's weaker (no OS-level caller identity — compensated by mTLS), what's different (port binding vs. service binding)
- **Universal Links for both legs**: domain ownership verification via `apple-app-site-association`, interception immunity, callback domain as a registered identifier during onboarding

### Section 3: Per-Transaction Flow — iOS (16 steps)

The full 16-step flow adapted for iOS:

- Steps 1-7: ECDHE over localhost mTLS instead of Binder — specify what changes and what stays the same
  - Step 1: RPA opens localhost listening socket instead of binding to Binder service
  - Step 3: `mach_absolute_time()` instead of `CNTVCT_EL0` inline assembly
  - Step 4: Universal Link launch instead of Binder IPC call; include port number
  - Step 5: Telco App connects to localhost and verifies via mTLS (no `getCallingUid()`)
  - Step 5d: App Attest instead of Play Integrity
- Step 8: SIM attestation — see Section 4 for iOS-specific options
- Step 9: JWE construction — unchanged
- Steps 10-12: Timing closure + Telco App returns JWE over TCP + RPA receives and verifies. Telco App fires callback Universal Link to return foreground.
- Steps 13-16: Unchanged (proof-of-possession, server-side token exchange). Device attestation in Step 13 uses App Attest assertion instead of Play Integrity token.

### Section 4: SIM Verification on iOS

- **The core constraint**: iOS does not expose OMAPI or any equivalent third-party API for SIM applet communication
- **Available options**:
  - **Option A: Carrier entitlements from Apple** — Apple grants special entitlements to carrier apps; evaluate whether APDU-level SIM access is available through this path. Requires Apple engagement. Not publicly documented.
  - **Option B: eSIM profile-level attestation** — For eSIM iPhones, attestation at the SM-DP+ level via Telco's server infrastructure. Server-side SIM identity verification rather than on-device applet challenge-response.
  - **Option C: SNA as supplementary signal** — SNA is more reliable on iPhones (overwhelmingly single-SIM or dual-eSIM with Apple-managed routing). Still cannot detect SIM swaps. Useful as a supplementary signal, not primary.
  - **Option D: Apple platform API** — Regulatory mandate (RBI/TRAI) to push Apple to provide a first-party SIM attestation API. Strongest long-term path but longest timeline.
  - **Option E: Core Telephony + Carrier Privileges** — What iOS's `CTCarrier` / `CTTelephonyNetworkInfo` can provide (carrier name, MCC/MNC, allows VoIP). No cryptographic attestation. Weak.
- **Comparison matrix**: Same format as Android doc Section 2.7
- **Recommendation**: Carrier entitlements as primary investigation path; eSIM profile attestation as the fallback; SNA as supplementary signal; regulatory ask for Apple API as long-term

### Section 5: Security Analysis

- **Localhost mTLS security**: Same structure as Android doc Section 4.1
  - URL scheme interception — neutralised by Universal Links
  - Port hijacking — neutralised by mTLS
  - VPN/Network Extension interception — mTLS prevents MITM, only metadata observable
  - Jailbroken device port forwarding — App Attest catches jailbreak; timing challenge catches relay latency
  - No OS-level caller identity — mTLS compensates; Secure Enclave keys are non-exportable
- **App Attest vs. Play Integrity**: Comparison of device attestation guarantees
  - App Attest provides per-instance attested key (stronger than Play Integrity's device-level verdict)
  - Assertion signing — each request can be individually attested
- **iOS platform security advantages**: No sideloading, locked bootloader, jailbreak is rare — these compensate for the slightly weaker IPC model
- **SIM verification gap**: Honest assessment of what's lost if carrier entitlements don't provide APDU access — the protocol has one hardware trust anchor (Secure Enclave) instead of two (StrongBox + SIM SE) on Android. Compensations: App Attest is hardware-rooted, iOS platform security is inherently stronger.
- **What the attacker would need**: On iOS vs. Android — compare attack difficulty

### Section 6: UX Analysis

- **App switch flow**: RPA -> Telco App -> RPA. ~1-2 seconds visual transition. Comparable to 3D Secure redirects.
- **Universal Link UX**: Smooth transition (no Safari intermediate), direct app-to-app.
- **Biometric prompt**: Secure Enclave key use requires LAContext authentication — one biometric prompt during the flow (when?)
- **Failure modes**: Telco App not installed, Universal Link falls through to Safari (graceful degradation message), localhost connection timeout, mTLS handshake failure
- **Comparison with Android UX**: Android is invisible (Binder is seamless); iOS has a visible app switch. Acceptable for high-security authentication.

### Section 7: iOS-Specific Requirements

- **For Telcos**: Universal Link domain hosting (`apple-app-site-association`), App Attest verification server-side, carrier entitlement investigation with Apple
- **For RPAs**: Universal Link callback domain hosting, localhost TCP server implementation, App Attest integration
- **For Apple**: Carrier entitlement scope clarification, potential SIM attestation API
- **Registration additions**: Callback Universal Link domain registered during RPA onboarding; Telco validates callback domains against registered list

### Section 8: Constraints and Risks

- **Apple policy risk**: Apple could restrict localhost inter-app communication. Mitigation: regulatory mandate.
- **Carrier entitlement uncertainty**: APDU access via carrier entitlements is not publicly documented. Mitigation: Apple engagement via TRAI/RBI.
- **eSIM-only trend**: Newer iPhones are eSIM-only (iPhone 14+ in US; India still has physical SIM). eSIM profile attestation path must be viable.
- **iOS version requirements**: App Attest requires iOS 14+. Secure Enclave requires iPhone 5s+. Universal Links require iOS 9+. Minimum viable: iOS 14.
- **Background execution**: Not a concern with RPA-as-server design. Document why.
- **Dual eSIM handling**: iPhone 13+ supports dual eSIM. How does the user select which SIM for attestation?

### Section 9: Conclusion

- iOS path is viable with localhost mTLS + Universal Links
- The IPC gap is bridgeable; the SIM access gap is the real open question
- iOS platform security (no sideloading, locked bootloader, rare jailbreak) compensates for the slightly weaker IPC model
- What remains open: carrier entitlement investigation, Apple engagement

## Updates to existing documents

After the iOS doc is written:

1. **[03-telco-attestation-protocol.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/03-telco-attestation-protocol.md) Section 9 (Open Design Questions)**: Replace the iOS constraints bullet list with a summary and link to the new iOS doc
2. **[03-telco-attestation-protocol.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/03-telco-attestation-protocol.md) Section 2 (Participants)**: Note that on iOS, the IPC mechanism is localhost mTLS + Universal Links instead of Binder
3. **[README.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/README.md)**: Add the iOS architecture doc to the documents table
4. **[draft-analysis-inputs.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/draft-analysis-inputs.md)**: Capture the localhost mTLS + Universal Links design decisions in the iOS section (currently at lines 37-46)

