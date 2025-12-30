# ETSL One‑Page Onboarding Primer  
## The Language of Enterprise Truth (Tier‑1)

This one‑page primer introduces the **core ETSL language** every architect, data engineer, and product leader must internalize.  
It is derived from the **Tier‑1 ETSL Canonical Terminology** and is **normative**.

If these terms drift, ETSL collapses.

---

## What ETSL Is (In One Sentence)

**ETSL (Enterprise Truth & Semantics Layer)** is how an enterprise **decides what it accepts as true**, explicitly, over time, across systems.

---

## The Mental Model (Read This First)

- Systems **assert**
- ETSL **accepts or rejects**
- Authority **decides**
- State is **derived**
- Products **interpret**
- Applications **execute**

If you remember nothing else, remember this flow.

---

## The Core Vocabulary (Tier‑1)

### 1. Assertion
A **claim** made by a system or function about an enterprise fact, relationship, or state at a point in time.

> Systems do not publish truth. They publish assertions.

---

### 2. Assertion Source
A system, application, or function that emits assertions.

> An SOR is an assertion source, not enterprise truth.

---

### 3. Authority
An explicitly modeled mandate that determines **which assertions are accepted as valid**, for a defined scope and time.

> Authority is modeled — not assumed, not centralized.

---

### 4. Authority Registry
A formal mapping of **which authority applies to which semantic scope and conditions**.

> This replaces tribal knowledge with explicit rules.

---

### 5. Reconciliation
The **semantic process** of resolving multiple assertions into an accepted enterprise representation using authority, time, and scope.

> Reconciliation is not deduplication or “latest‑wins”.

---

### 6. State
A **derived, point‑in‑time representation** of an entity produced by reconciliation.

> State is never asserted. It is always derived.

---

### 7. ETSL Semantic Artifact
The **formal definition of meaning**: what entities are, how relationships work, and how state is derived.

> Semantics are specified once and executed many times.

---

### 8. ETSL Data Artifact
A **persisted, authority‑qualified, time‑aware representation of enterprise truth**.

> This is the output of ETSL — not a data product.

---

### 9. Derived Assertion
An assertion produced by a system whose behavior was influenced by data products or prior derived state.

> Decisions create new truth and must be traceable.

---

### 10. Data Product
A **consumer‑aligned interpretation** of ETSL Data Artifacts for a specific use case.

> Data Products serve use cases. ETSL serves truth.

---

### 11. Data Application
A software component that consumes **candidate assertions, ETSL Data Artifacts, or Data Products** and applies logic to produce derived data, decisions, or services.

> Pipelines, jobs, services — all are Data Applications.

---

### 12. Data‑Driven Operational Application
An operational system whose runtime behavior is influenced by data products.

> These systems feed decisions back into ETSL as derived assertions.

---

## What ETSL Is NOT

- Not a data lake
- Not a warehouse
- Not a Data Mesh replacement
- Not a reporting layer
- Not centralized data ownership

ETSL is a **truth boundary**, not a platform.

---

## Common Mistakes to Avoid (Read Carefully)

- Calling curated marts “enterprise truth”
- Hiding authority inside code
- Treating reconciliation as a technical problem
- Letting products redefine semantics
- Skipping lineage for derived decisions

These are architectural failures, not implementation bugs.

---

## How This Shows Up in Your Day‑to‑Day Work

If you are:
- **An Architect** → You model authority, scope, and semantics explicitly
- **A Data Engineer** → You implement Data Applications that *execute* semantics
- **A Product Manager** → You consume truth, you do not define it

---

## Final Rule (Memorize This)

> **ETSL decides what is true.  
Everything else decides how to use it.**

---

*This primer is derived from the Tier‑1 ETSL Canonical Terminology.  
If you find yourself redefining these terms, stop and escalate.*  
