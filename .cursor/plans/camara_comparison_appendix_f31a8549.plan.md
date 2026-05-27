---
name: CAMARA Comparison Appendix
overview: Write a separate appendix document (appendix-camara-comparison.md) that rigorously evaluates GSMA CAMARA Open Gateway APIs as an alternative to the Telco-Attested Device Authentication protocol, acknowledging CAMARA's value while demonstrating its structural inability to address on-device malware and social engineering threats.
todos:
  - id: write-appendix
    content: Write appendix-camara-comparison.md with all 7 sections, header, and references
    status: completed
  - id: update-readme
    content: Add new document to README.md under Security Analysis table
    status: completed
  - id: update-crossref
    content: Add cross-reference in appendix-security-analysis.md closing observation
    status: completed
isProject: false
---

# CAMARA Comparison Appendix — Plan

## Document

New file: `[appendix-camara-comparison.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/appendix-camara-comparison.md)`

Separate standalone document alongside the existing `[appendix-security-analysis.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/appendix-security-analysis.md)`. Cross-referenced from the suite's `[README.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/README.md)` under "Security Analysis."

## Analytical Framing

The document should not read as a dismissal of CAMARA. It should read as a rigorous evaluation that:

1. Acknowledges CAMARA's genuine advances over SMS OTP and legacy header enrichment
2. Maps each CAMARA API's security properties against the protocol's threat model (the 4-tier attacker model from appendix Section 1)
3. Identifies the architectural boundary that CAMARA cannot cross (network-layer vs. device-layer)
4. Concludes with a positioning of CAMARA as a complementary signal layer, not a substitute

## Document Structure

### Header

- Title: "Evaluation: GSMA CAMARA Open Gateway APIs as Authentication Alternative"
- Cross-reference to the protocol spec, existing security analysis appendix, and platform supplements
- One-paragraph thesis: CAMARA APIs represent a significant advance in standardized network-side fraud signals, but they operate at the network layer and have no visibility into the device execution environment — making them structurally unable to defend against on-device malware (Tier 1-2) and unable to provide the cryptographic hardware-anchored guarantees that the attestation protocol achieves

### Section 1: CAMARA Open Gateway — What It Is

- Brief, factual overview of the GSMA CAMARA project and Open Gateway initiative
- The relevant APIs, grouped by function:
  - **Authentication**: Number Verification (network-based, SIM-based), OTP SMS
  - **Fraud signals**: SIM Swap, Device Swap, Call Forwarding Signal
  - **Identity**: KYC Match, Device Identifier
- Deployment status in India (Jio, Airtel, Vi — SIM Swap live, Number Verification announced)
- Integration model: server-to-server (backend) vs. frontend-initiated (Number Verification), aggregator model, OIDC/OAuth2 authentication

### Section 2: Number Verification — Deep Analysis

This is the API most likely to be proposed as an alternative, so it deserves detailed treatment.

- **How it works**: Frontend-initiated OIDC Authorization Code flow; telco's auth server correlates the request's source IP (assigned by PGW/UPF) against its session table to resolve IP-to-MSISDN; match/no-match returned
- **What it proves**: The device making this HTTP request is connected to the mobile network via a SIM whose MSISDN matches the claimed number
- **What it does not prove**: (mapped against each of the protocol's four guarantees from Section 6.3.3 of the security analysis)
  - No device identity — cannot distinguish which app is making the request
  - No device integrity — cannot detect root, malware, instrumentation
  - No user presence — no biometric verification, no hardware auth token
  - No colocation — no on-device IPC identity check, no timing challenge
  - No cryptographic binding — returns a boolean, not a hardware-anchored signature
- **Constraints**: Mobile data required (fails on Wi-Fi unless NV 2.0 with TS.43 entitlement server); no CIBA support
- **Comparison with SMS OTP**: Acknowledge that Number Verification is meaningfully stronger than SMS OTP (no shareable credential, no phishing surface, no SS7 exposure, no SIM-swap vulnerability for the verification itself)

### Section 3: SIM Swap and Device Swap — Signal vs. Proof

- **How SIM Swap works**: Backend API call; telco checks its provisioning records for recent swap events; returns boolean or timestamp
- **What it proves**: A SIM swap event did or did not occur within a lookback window
- **Structural limitation**: Retrospective detection, not prevention. The protocol's SIM attestation key is destroyed on swap (prevention); SIM Swap API detects after the fact (detection). Timing windows, propagation delays, and lookback configuration create gaps.
- **Device Swap**: Same pattern — detects IMEI change, does not prevent authentication from the new device
- **Value acknowledged**: These are useful pre-transaction risk signals that complement (but do not replace) on-device attestation

### Section 4: The Architectural Boundary — Network Layer vs. Device Layer

This is the central analytical section.

- CAMARA APIs answer questions about **network state** (which SIM is on which IP, when was the last swap). They have zero visibility into the **device execution environment** (what apps are running, whether the OS is compromised, whether the user is present).
- Map each of the 11 compromise vectors from the security analysis appendix (Section 5.2) against CAMARA's detection capability:
  - Vectors 1-4 (Tier 1-2, on-device): CAMARA cannot detect any of them
  - Vector 5-6 (Tier 3, physical): CAMARA cannot detect (stolen device with correct SIM passes all network checks)
  - Vector 7 (Tier 4, CA compromise): Orthogonal — CAMARA has no CA
  - Vector 8 (downgrade): CAMARA Number Verification is a better fallback than SMS OTP but still not equivalent to the full protocol
  - Vectors 9-11 (Tier 4, OTA/SIM infrastructure): Orthogonal — CAMARA does not interact with the SIM applet layer
- The fundamental gap: **malware on the user's device is invisible to CAMARA**. A banking trojan that overlays the legitimate RPA, captures credentials, and initiates transactions through the real app passes every CAMARA check — correct SIM, correct device, correct network, no recent swap. The request looks identical to a legitimate one from the network's vantage point.
- Social engineering: A user who is socially engineered into performing a transaction on their own device (APP fraud — the primary focus of the RBI discussion paper) is also invisible to CAMARA — the user is on their own device, their own SIM, their own network.

### Section 5: What CAMARA Adds — The Complementary Value

Explicit acknowledgment that CAMARA is valuable, positioned correctly:

- **Transition period strengthening**: During the attestation protocol rollout (Section 8.1 of security analysis), CAMARA SIM Swap + Number Verification provide a stronger fallback than raw SMS OTP for devices without the attestation applet
- **Pre-transaction risk scoring**: Backend SIM Swap, Device Swap, Call Forwarding Signal checks before the attestation flow begins — defense in depth
- **iOS gap mitigation**: On iOS where OMAPI is unavailable and the protocol operates in single-anchor mode (Section 8.7), CAMARA signals provide a network-level SIM identity check that partially compensates
- **Cross-telco integration simplification**: The Open Gateway aggregator model partially addresses the N:M integration problem (Section 8.3), though the commercial bilateral relationships persist
- **Regulatory alignment**: CAMARA is a GSMA-backed, industry-standard framework — recommending it as a complementary layer strengthens the proposal's credibility with regulators who may already be aware of Open Gateway

### Section 6: Comparison Matrix

A concise summary table comparing:

- SMS OTP vs. CAMARA (Number Verification + SIM Swap) vs. Telco-Attested Device Authentication
- Across dimensions: device binding, SIM-swap resistance, user presence, malware resistance, social engineering resistance, cryptographic proof, privacy, scalability of attack, regulatory alignment

### Section 7: Conclusion

- CAMARA is the best available network-side fraud signal framework — a genuine advance over SMS OTP and legacy header enrichment
- CAMARA is not a device-side authentication protocol — it cannot provide hardware-anchored cryptographic proof of device identity, SIM presence, or user presence
- The recommended architecture is **attestation protocol + CAMARA signals**: the protocol provides the hard cryptographic guarantees, CAMARA provides complementary risk signals
- This is not protocol vs. CAMARA — it is protocol + CAMARA vs. either alone

### References

- CAMARA project (camaraproject.org), GSMA Open Gateway, specific API specifications
- Cross-references to the security analysis appendix sections
- Indian deployment references (Jio/Airtel/Vi announcements)

## Cross-Reference Updates

- Add the new document to `[README.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/README.md)` under the "Security Analysis" table
- Add a brief cross-reference in the existing `[appendix-security-analysis.md](misc/rbi-digital-payment-fraud/supplement-telco-device-attestation/appendix-security-analysis.md)` Section 8 (Open Areas) closing observation, noting that a companion analysis evaluates CAMARA as an alternative

## Execution Strategy

The document is approximately 7 sections and will be written as a single document (no fragment-based parallel assembly needed — the sections are tightly cross-dependent and the total length is moderate compared to the security analysis appendix).