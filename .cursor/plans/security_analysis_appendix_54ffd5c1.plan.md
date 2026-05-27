---
name: Security Analysis Appendix
overview: Write a rigorous security analysis appendix as 8 parallel section drafts, then assemble into one document. Covers device trust anchors, SIM trust chain, colocation verification, clock tamper resistance, compromise vectors, and design rationale — all with verified citations from standards bodies and security literature.
todos:
  - id: batch-1-sec1
    content: "BATCH 1 — Write section fragment: sec1-threat-model.md (Scope, attacker tiers, analytical framing)"
    status: completed
  - id: batch-1-sec2
    content: "BATCH 1 — Write section fragment: sec2-colocation.md (IPC security properties, three-layer synthesis, cross-refs)"
    status: completed
  - id: batch-1-sec3
    content: "BATCH 1 — Write section fragment: sec3-sim-trust-chain.md (UICC hardware, JavaCard isolation, OTA provisioning, applet lifecycle)"
    status: completed
  - id: batch-1-sec4
    content: "BATCH 1 — Write section fragment: sec4-clock-tamper.md (Android + iOS call paths, hookability, timing threshold justification)"
    status: completed
  - id: batch-2-sec5
    content: "BATCH 2 — Write section fragment: sec5-compromise-vectors.md (11 vectors with SMS OTP column, severity methodology, SIM-specific vectors)"
    status: completed
  - id: batch-2-sec6
    content: "BATCH 2 — Write section fragment: sec6-dual-trust-anchor.md (enclave + SIM argument, SMS OTP trust model comparison)"
    status: completed
  - id: batch-2-sec7
    content: "BATCH 2 — Write section fragment: sec7-design-rationale.md (session_id, JWE, leaf cert, P-256 — resolved positions)"
    status: completed
  - id: batch-2-sec8
    content: "BATCH 2 — Write section fragment: sec8-open-areas.md (curated unresolved items)"
    status: completed
  - id: assemble
    content: Assemble all 8 fragments into appendix-security-analysis.md, add header/footer, verify cross-section references, verify all citations
    status: completed
  - id: update-crossrefs
    content: Update cross-references in 03-telco-attestation-protocol.md, README.md, Android supplement, iOS supplement; retire draft-analysis-inputs.md and section fragments
    status: completed
isProject: false
---

# Security Analysis Appendix — Restructure Plan

## Document Identity

- **New file**: `appendix-security-analysis.md` (in `misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/`)
- **Replaces**: `draft-analysis-inputs.md` (retire to avoid parallel maintenance)
- **Role in the doc suite**: Referenced by the protocol doc (`03-telco-attestation-protocol.md`) header and source notes, README working drafts section, and both platform supplements
- **Section fragments**: Written as individual files in `_scratch/` during parallel execution, assembled into the final document as the last step, then deleted

## Central Analytical Argument

> "The protocol's security architecture holds under realistic attack conditions because two independent hardware trust anchors — the device secure enclave and the SIM secure element — provide complementary guarantees that no single compromise can defeat, while layered colocation verification makes remote proxy, replay, and impersonation attacks infeasible."

Every section must either **state a claim**, **substantiate it with evidence**, or **address a counterargument**. No exploratory "here's how this works" — only "here's why this holds."

---

## Execution Strategy — Parallel Batches

Sections are written as independent markdown fragments, then assembled. This enables parallel execution.

```
BATCH 1 (4 parallel agents — no cross-dependencies):
  sec1-threat-model.md
  sec2-colocation.md
  sec3-sim-trust-chain.md
  sec4-clock-tamper.md

BATCH 2 (4 parallel agents — depend on Batch 1 for threat model and trust chain framing):
  sec5-compromise-vectors.md    (needs Sec 1 attacker tiers, Sec 3 SIM vectors)
  sec6-dual-trust-anchor.md     (needs Sec 3 SIM analysis, Sec 4 clock analysis)
  sec7-design-rationale.md      (independent)
  sec8-open-areas.md            (independent)

ASSEMBLE:
  Combine fragments into appendix-security-analysis.md
  Update cross-references in suite, retire fragments and draft
```

Each fragment is self-contained with its own citations section. During assembly, citations are consolidated into a single references section at the end.

---

## Citation Requirements

Every substantive claim must be backed by a verified citation from a credible source. The following citation classes are required:

### Standards bodies and specifications

- NIST SP 800-63B Rev 4 — SMS OTP as restricted authenticator, authenticator assurance levels
- NIST SP 800-157 Rev 1 — derived PIV credentials (hardware-bound key lifecycle)
- GlobalPlatform Card Specification (v2.3.1) — Secure Channel Protocol (SCP03), Issuer Security Domain, applet lifecycle management
- GlobalPlatform TEE System Architecture (v1.2) — trusted execution environment model
- ETSI TS 102 225 / TS 102 226 — OTA SIM provisioning via SCP80/SCP81, RAM/RFM
- ETSI TS 102 241 — UICC API for JavaCard (USAT framework)
- ISO/IEC 15408 (Common Criteria) — EAL4+/EAL5+ evaluation for UICC/SIM hardware
- ARM Architecture Reference Manual (ARMv8-A) — CNTVCT_EL0, CNTKCTL_EL1, Generic Timer
- FIDO Alliance — UAF/FIDO2 authenticator attestation model (comparison point)

### Platform documentation (authoritative primary sources)

- Android Compatibility Definition Document (CDD) — StrongBox requirements (Section 9.11), Biometric requirements (Section 7.3.10)
- Android Keystore system documentation — PURPOSE_AGREE_KEY, setIsStrongBoxBacked(), Hardware Auth Token (HAT)
- Apple Platform Security Guide — Secure Enclave architecture, App Attest, Data Protection
- Apple Developer Documentation — mach_continuous_time(), DeviceCheck framework

### Security research and journals

- Frida documentation and published hooking capabilities (for the hookability analysis)
- Published SIM/UICC security research — e.g., Karsten Nohl's SIM attacks (BlackHat 2013), Borgaonkar et al. on OTA vulnerabilities
- SS7 vulnerability research — Engel (2008, 2014), Positive Technologies SS7 security reports
- IEEE 802.11 latency characterization papers (for timing threshold justification)
- TEE/TrustZone security research — Cerdeira et al. "SoK: Understanding the Prevailing Security Vulnerabilities in TrustZone-assisted TEE Systems" (IEEE S&P 2020)

### Regulatory and industry

- RBI Authentication Mechanisms for Digital Payment Transactions Directions, 2025
- NPCI UPI Information Security Compliance Framework, 2025
- Digital Personal Data Protection Act (DPDPA), 2023
- GSMA FS.28 — SIM Security Guidelines

### Citation format

Inline bracketed references — e.g., [NIST-63B, S5.1.3.3], [Android-CDD, S9.11.1], [GP-Card, S11.1] — with a full references section at the end of the document.

---

## Section Plan

### Section 1: Scope and Threat Model (sec1-threat-model.md)

**Purpose**: Define what the analysis covers and what the attacker model is.

- **In scope**: On-device protocol security (IPC, crypto, SIM, enclave). Attacker capabilities from no-root malware through full root + bootloader unlock. Physical device theft. SIM provisioning chain. Institutional compromise.
- **Out of scope**: Server-side infrastructure security (mTLS between RPA Server and Telco Server), telco KYC accuracy, regulatory enforcement.
- **Attacker tiers**: Formalize the implicit attacker model:
  - Tier 1: No-root malware on device
  - Tier 2: Rooted device / Play Integrity bypass
  - Tier 3: Physical device access + SIM extraction
  - Tier 4: Institutional compromise (CA, code signing key, SIM vendor key custody)
- **Trust anchors enumerated**: Name the two hardware trust anchors (device secure enclave, SIM secure element) and the one organizational anchor (Telco CA) that the protocol depends on. The rest of the paper substantiates why these deserve trust.
- **Citations needed**: [NIST-63B] for authenticator assurance levels, [GP-TEE] for TEE threat model.
- **Length**: ~1.5 pages. Clean definitions, no hedging.

### Section 2: Colocation Verification Analysis (sec2-colocation.md)

**Purpose**: Argue that the three-layer defense (IPC + timing + device attestation) is sufficient to prove same-device, same-time colocation.

**Source material**: Current Sections 1, 2, 3 of `draft-analysis-inputs.md`.

**What to keep (and sharpen)**:

- The **security property comparison** across IPC mechanisms (Binder, Unix domain sockets, loopback, link-local) — framed as analytical evidence ("which mechanisms provide kernel-enforced same-device guarantee?"), not a survey
- The **timing challenge protocol** — folded in as Layer 2 analysis
- The **synthesis table** — what each layer proves, what it catches

**What to remove**:

- Binder mechanics (how getCallingUid() works) — in Android supplement Section 2.1
- iOS localhost mTLS architecture — in iOS supplement Section 2

**What to add**:

- Cross-references to platform supplements for implementation
- Claim-evidence structure with citations: Linux kernel Binder documentation for same-device guarantee; RFC 6761 / IETF loopback semantics for localhost isolation properties

**Citations needed**: Android Binder kernel docs, RFC 6761, IEEE 802.11 latency measurements.

### Section 3: SIM Trust Chain Analysis (sec3-sim-trust-chain.md) — NEW

**Purpose**: Substantiate whether the SIM secure element deserves its role as the protocol's second hardware trust anchor. This section did not exist in `draft-analysis-inputs.md` and is entirely new.

**3.1 UICC Hardware Security Properties**:

- Physical tamper resistance (Common Criteria EAL4+/EAL5+ certification for commercial SIM cards)
- Side-channel resistance (DPA, SPA, fault injection countermeasures)
- Comparison with device secure enclave (StrongBox/Secure Enclave): what the SIM offers that the device enclave does not (operator-controlled, SIM-swap-resistant, independent trust domain) and vice versa
- **Citations**: [ISO-15408] Common Criteria evaluation methodology, [GSMA-FS28] SIM security guidelines, JavaCard/GlobalPlatform security target documents from major SIM vendors (Gemalto/Thales, IDEMIA, G+D)

**3.2 JavaCard Execution Environment and Applet Isolation**:

- Applet firewall: how JavaCard prevents one applet from accessing another's objects and keys (JCRE specification)
- Key isolation: the attestation applet's ECDSA private key cannot be read by the OS, the baseband, or other applets — only signing operations are exposed via APDU
- APDU channel security: the channel between OMAPI and the SIM applet traverses the baseband processor. On an uncompromised device this is transparent, but on a rooted device the APDU stream is observable. Assess whether this matters (the challenge-response is signed, so observation without the SIM key is useless; modification is detectable via signature verification)
- **Citations**: [JCRE] JavaCard Runtime Environment specification (Oracle), [GP-Card, S10] applet firewall and isolation, [ETSI-102241] UICC API

**3.3 OTA Provisioning Security**:

- How the applet arrives on the SIM: GlobalPlatform Secure Channel Protocol (SCP03 for card-level, SCP80/SCP81 for remote OTA)
- Key custody: who holds the Issuer Security Domain (ISD) keys? Telco vs. SIM vendor. If the SIM vendor retains key custody (common in practice), the telco cannot independently guarantee applet integrity — this is a trust delegation that must be contractually and auditably enforced
- eSIM (eUICC) provisioning: SM-DP+ and SM-DS architecture. Profile download is authenticated via the eUICC's certificate (manufactured into hardware). Different trust model from physical SIM OTA — potentially stronger (GSMA SGP.22) but introduces the eSIM platform vendor as an additional trusted party
- Attack surface: rogue OTA push (requires compromised ISD keys or SCP session hijack), downgrade of applet code, unauthorized applet deletion. Assess likelihood and impact.
- **Citations**: [GP-Card, S11] Secure Channel Protocol, [ETSI-225/226] OTA platform, [GSMA-SGP22] RSP architecture for eSIM, published OTA vulnerability research (Nohl, BlackHat 2013; Borgaonkar et al.)

**3.4 Applet Lifecycle and SIM Events**:

- What happens to the attestation key pair during: SIM swap (key destroyed — new SIM requires re-provisioning), eSIM profile switch (profile-bound keys are deactivated), MVNO migration (depends on whether MVNO shares the MNO's SIM estate), SIM toolkit update (applet code updated but key material should persist if ISD manages it correctly)
- Re-provisioning as a security feature: unlike SMS OTP (where a SIM swap transparently redirects OTPs), a SIM swap in the telco attestation model *breaks* authentication and forces re-enrollment — this is the intended behavior
- Residual risks: silent applet replacement via compromised OTA, key extraction from a physically stolen SIM (requires lab-grade equipment and defeats EAL4+ tamper resistance)
- **Citations**: [GP-Card, S9] card lifecycle management, [GSMA-FS28] SIM lifecycle security

### Section 4: Clock Tamper Resistance — Deep Analysis (sec4-clock-tamper.md)

**Purpose**: Substantiate the claim that direct CNTVCT_EL0 reads (Android) and mach_continuous_time() (iOS) are resistant to software tampering.

**Source material**: Current Sections 2 and 7 of `draft-analysis-inputs.md`.

**What to keep**:

- The full call-path diagram (Java -> JNI -> C -> vDSO -> hardware counter)
- The hookability table (each layer, Frida/LD_PRELOAD interception capability, defense)
- The timing threshold analysis (500us / 1ms) and why remote proxy fails

**What to sharpen**:

- Add the iOS call path alongside Android (mach_continuous_time() -> Mach trap -> hardware counter)
- Quantify timing thresholds with cited evidence: WiFi RTT (cite IEEE 802.11 measurements — typically 1-5ms), USB-tethered proxy overhead (cite USB protocol latency), Binder IPC benchmarks
- Address CPU load false-rejection rates with more specificity
- Analyze mach_continuous_time() hookability: it is a Mach system call, not inline assembly — what does this mean for iOS timing guarantee vs. Android?

**Citations needed**: [ARM-ARM] Generic Timer architecture, Android vDSO (AOSP source), Apple mach_continuous_time() kernel docs, IEEE 802.11 latency studies, Frida documentation on hooking capabilities.

### Section 5: Compromise Vector Analysis (sec5-compromise-vectors.md) — the centerpiece

**Purpose**: Demonstrate that the protocol holds against each realistic attack vector.

**Source material**: Current Section 6 of `draft-analysis-inputs.md`, plus new SIM-specific vectors.

**Vectors (expanded from 8 to 11)**:

- Vectors 1-8: Existing (Play Integrity bypass, impersonate RPA, impersonate Telco App, on-device relay, stolen device, biometric spoofing, Telco CA compromise, SMS OTP downgrade)
- Vector 9 (new): Rogue OTA applet replacement — attacker compromises OTA channel to push a modified attestation applet. Defense: SCP03/SCP80 mutual authentication; ISD key compromise required. Informed by Section 3.3.
- Vector 10 (new): APDU channel interception on rooted device — attacker observes/modifies APDU traffic between OMAPI and SIM. Defense: challenge-response is signed by SIM key; observation is useless without key; modification detected by signature verification. Informed by Section 3.2.
- Vector 11 (new): SIM vendor key custody compromise — SIM vendor (not telco) holds ISD keys; rogue insider at vendor could push unauthorized applets. Defense: contractual controls, audit logging, dual-authorization. Informed by Section 3.3.

**Structural changes**:

- Add SMS OTP comparison column to the threat matrix
- Add severity scoring methodology: define likelihood (attacker capability + cost + access required) and impact (what the attacker gains) criteria before the vector table
- Remove discovery narrative ("This was initially assessed as...") — state conclusions directly
- Ensure every "Can the attacker do it?" claim has a citation

**Citations needed**: [Frida-docs] for hooking capabilities, [Android-CDD, S9.11] for StrongBox, [Android-BiometricPrompt] for HAT documentation, [GP-Card] for SCP03 mutual auth, SS7 vulnerability research for SMS OTP comparison column.

### Section 6: Dual Trust Anchor Argument (sec6-dual-trust-anchor.md)

**Purpose**: Consolidate the paper's central claim — the protocol derives its strength from two independent hardware trust anchors (device enclave + SIM secure element), neither of which is sufficient alone, and both of which are dramatically stronger than SMS OTP's trust model.

**Source material**: Current Section 4 "Why this is strong" + Section 6 "Key conclusion" + new Section 3 SIM analysis.

**Structure**:

- 6.1 Device secure enclave: What it guarantees (key non-exportability, user-auth gating, hardware isolation). Conditions under which it holds without Play Integrity. Cite [Android-CDD], [Apple-PSG].
- 6.2 SIM secure element: What it guarantees (operator-controlled, SIM-swap-resistant, independent trust domain). Cross-reference Section 3.
- 6.3 Why both are needed: Device enclave alone does not prove SIM presence (SIM-swap attack). SIM alone does not prove device integrity or user presence (stolen SIM in a different device). Together: device identity (enclave) + subscriber identity (SIM) + user presence (biometric) = three-factor.
- 6.4 Comparison with SMS OTP trust model: SMS OTP trusts SS7 network (shared infrastructure, no per-user hardware binding, no device binding, no user-presence verification). Telco attestation trusts per-device hardware. The asymmetry is the argument. Cite [SS7-Engel], [NIST-63B].

**What to remove**: Crypto specification (ECDHE mechanics, trust chain diagram) — now in protocol doc Section 3.

### Section 7: Design Decision Rationale (sec7-design-rationale.md)

**Purpose**: Document the analytical reasoning behind key protocol design choices. Resolved positions, not open questions.

**Source material**: Current Section 9 of `draft-analysis-inputs.md`.

**Decisions** (each as: Decision / Alternatives considered / Why this choice / Citation):

- session_id over SHA-256(shared_secret) — information leak, verifiability, stateless replay. Cite cryptographic best practice on minimizing session secret exposure.
- JWE-based attestation token — privacy (DPDPA compliance), subscriber PII never client-side. Cite [DPDPA-2023], [RFC-7516] JWE specification.
- Leaf-only certificate in JWE — why not full chain; server-side second opinion. Cite [RFC-5280] certificate path building.
- P-256 over X25519 — pragmatic hardware support across Indian device landscape vs. modern cryptographic preference. Cite [NIST-FIPS-186-5], StrongBox supported algorithms.

### Section 8: Open Areas and Future Work (sec8-open-areas.md)

**Purpose**: Short, bounded section acknowledging the paper's limits.

**Items** (curated — genuinely unresolved only):

- Hardware ECDH (PURPOSE_AGREE_KEY) penetration on API 33+ devices in India
- CNTVCT_EL0 user-space access across Indian device landscape
- Cross-telco interoperability model (standardization body)
- Certificate lifecycle parameters (validity, revocation mechanism)
- Dual-SIM handling and CA architecture
- SIM vendor ISD key custody — contractual vs. technical enforcement gap
- eSIM profile-level attestation as potential SIM verification path for iOS

---

## Assembly Step

After all 8 fragments are written:

1. Combine in section order into `appendix-security-analysis.md`
2. Add document header (title, scope statement, reference to protocol doc)
3. Consolidate per-section citation lists into a single **References** section at the end
4. Verify all inter-section cross-references (e.g., "as established in Section 3.2")
5. Verify every citation is real and correctly attributed (web search to confirm)
6. Final tone pass: remove any residual exploratory language

## Cross-Reference Updates

After the appendix is assembled:

1. `03-telco-attestation-protocol.md`: Update header (line 3) and source notes (line 560) to reference `appendix-security-analysis.md` instead of `draft-analysis-inputs.md`
2. `draft-sim-verification-android.md`: Update any references to `draft-analysis-inputs.md`
3. `draft-ios-architecture.md`: Update any references to `draft-analysis-inputs.md`
4. `README.md`: Move from "Working Drafts" to the main document table or a new "Analysis" subsection; update filename and description
5. Retire `draft-analysis-inputs.md`: Delete after all references are updated
6. Delete `_scratch/sec*.md` fragments: Clean up working files

---

## Tone and Style Guidelines

- **No exploratory narration**: Replace "This was initially assessed as..." with direct claims
- **No shorthand**: Replace "Gives: same-device guarantee" with full sentences
- **Claim-evidence-citation structure**: Every substantive paragraph must be traceable to a verifiable source. The pattern is: claim (prose) -> evidence (technical reasoning or data) -> citation (bracketed reference)
- **Tables for comparison, prose for argument**: Use tables to compare (SMS OTP vs. telco attestation, IPC mechanisms, hookability layers) but use prose to make the analytical argument
- **Citation density target**: No section should go more than 2-3 paragraphs without at least one citation. The compromise vector analysis and SIM trust chain sections should be the most densely cited.

