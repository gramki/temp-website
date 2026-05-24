# ACE Executive Illustration — AI Agent Prompt (Self-Sufficient)

Use this document **verbatim** as the single source of truth for generating illustrations. No other files are required.

---

## 1. Purpose and audience

- **Subject:** ACE — **Agent Centric Engineering**: an agent-centric product development system (tagline may appear once: *For the Engineers, By the Engineers*).
- **Audience:** **Executives** — optimize for clarity, narrative, and one idea per frame. Avoid implementation trivia, vendor logos, and repository jargon beyond what is specified below.
- **Outcome:** A **four-frame** visual story (same narrative as a short video scribe). Each frame must remain **simple and legible** when viewed as a presentation slide or printed on letter/A4.

---

## 2. Visual style

- **Style:** **Whiteboard explainer** / **RSA Animate–style scribe**: hand-drawn line art, slightly sketchy ink strokes, light cross-hatching or simple shading for depth where helpful.
- **Palette:** **Monochrome** (black ink on white / off-white) unless the product owner specifies a brand palette. If color is used, keep it minimal (one accent for “Product Intent” token only).
- **Tone:** Professional, approachable, slightly whimsical — **not** corporate clip-art glossy; **not** photorealistic.
- **Typography:** Hand-lettered or rounded sans that matches the sketch; **short labels only** (no paragraphs on the art). If text would be unreadable at slide size, **omit it** and rely on shapes and a separate speaker script.

---

## 3. Deliverable format (choose one and state it in the generation request)

**Option A — Four separate images:** One image file per frame, same aspect ratio (e.g. **16:9**), consistent style and “paper” background.

**Option B — Single composite:** One image with **four equal horizontal panels** or a **2×2 grid**, each panel labeled in the corner: **Frame 1** … **Frame 4**.

The prompt below describes **content per frame**; the generating agent should implement **either** A **or** B as requested.

---

## 4. Global narrative (read once across all frames)

1. **Foundry** is where software products are crafted; it is governed by three models and hosts workshops.  
2. A **Workshop** holds shared **Knowledge, Skills, Artifacts, and History** and hosts **Workbenches**.  
3. A **Workbench** contains **six workspaces**; humans enter each workspace through an **IDE**; work is organized as **Scenarios → Tasks** with **human–agent teams**.  
4. **Product Intent** is the thread that flows through workspaces from shaping to delivery; **governance** applies on transitions (shown lightly, **no** dedicated governance-only frame).

---

## 5. Frame 1 — Foundry

### Intent for the viewer

“ACE is anchored in a **Foundry**: governed, serious, and the container for how we build.”

### Must depict

- **Title block** (small): **ACE** or **Agent Centric Engineering** (pick one primary line).
- **Foundry** as a **large outer frame** (thick border, rounded rectangle, or “factory floor” outline) spanning most of the canvas.
- **Inside or along the top edge of Foundry**, three **equal** governance pillars or badges, clearly labeled:

  1. **Product Model**  
  2. **Work Model**  
  3. **Operating Model**

- A **short line** (hand-caption) such as: *Foundry hosts workshops* or *Workshops live inside the Foundry* — optional if space is tight.

### Optional (one only)

- Sub-line from ACE source material: *Foundry is where software products are crafted* — only if legible.

### Do not include in Frame 1

- Workshops in detail, repositories, workspaces, Product Intent paths, or IDE icons.

---

## 6. Frame 2 — Workshop

### Intent for the viewer

“A **Workshop** is the unit of practice: it **stores and reuses** what the organization knows and produces, and it **hosts Workbenches**.”

### Must depict

- **Workshop** as a **named container** inside Foundry (nested rectangle or building inside the Foundry frame from Frame 1 **stylistically echoed** — thinner border is fine).
- **Four parallel “shelves” or pillars** (same visual weight, same icon family), feeding or supporting the workshop. Labels **exactly**:

  1. **Knowledge** — facts, domain, standards (books, lightbulb, or document stack metaphor).  
  2. **Skills** — how work is done; playbooks, methods (toolbox, recipe cards, or “playbook” stack).  
  3. **Artifacts** — outputs: designs, specs, code, tests (folder + gear, blueprint, or merged doc+code metaphor).  
  4. **History** — decisions, feedback, evolution, audit trail (timeline, scroll, or layered pages).

- **Workbenches** as **one or more smaller boxes** inside the workshop labeled **Workbench** or **Workbenches** (singular/plural acceptable).

### Mapping note (for artist accuracy only — do not put this small print on the slide)

The full ACE model lists many repository types; for **this** illustration only the **four themes** above are shown. Detailed taxonomy is out of scope.

### Do not include in Frame 2

- The six workspaces as full columns (that is Frame 3).  
- Product Intent journey (Frame 4).  
- Full lists of repository proper names.

---

## 7. Frame 3 — Workspaces (Approach B: one zoom + five minis)

### Intent for the viewer

“Work happens in **six workspaces** (one per functional station). Each has a **human–agent team**, **Scenarios → Tasks**, and its **own IDE context**. The pattern is the same everywhere; **one** station is enlarged so you can read the pattern.”

### Layout (strict)

- **One horizontal row of six workspace stations**, left to right, **fixed order**:

  1. **Product specification**  
  2. **UX design**  
  3. **Development**  
  4. **QA** (Quality assurance)  
  5. **Release**  
  6. **Governance**

- **Station 1 — Product specification — is the ZOOM column:**  
  - Approximately **2× the width** and **2× the height** of each mini column (hero column on the **left**).  
  - **Baseline-aligned** with the five minis so the row reads as one band.

- **Stations 2–6 — MINI columns:**  
  - **Equal** narrow width.  
  - **Same vertical template** for each mini: **workspace label** (one line) + **tiny IDE icon** at bottom (or top — pick one and repeat identically).

### Zoom column (Product specification) — must include

1. **Title:** **Product specification workspace** (or shortened **Spec** if space is tight, with full name in caption below the whole row).  
2. **Human–agent team:** simple human figure(s) plus a distinct **agent** node (circle, chip, or small robot silhouette — consistent with Frame style).  
3. **IDE:** **larger** version of the **same IDE glyph** used in minis — positioned as the **human’s interface** (connector or overlap from human → IDE window). IDE = simple **monitor + document window** or **laptop + window**; **no** real product logos.  
4. **Scenarios → Tasks:** a **single horizontal micro-flow** (two words or two micro-boxes + one arrow). **Do not** repeat this full string inside the five minis.

### Five mini columns — each must include

1. **Workspace name** (one line): **UX design**, **Development**, **QA**, **Release**, **Governance**.  
2. **Tiny IDE icon** — **identical silhouette** to the zoom column’s IDE, **scaled down only**.  
3. **No** separate Scenarios→Tasks text in minis (the zoom establishes the pattern).

### Governance (integrated — no extra frame)

- **Governance** is the **sixth mini** like the others (label + mini IDE).  
- Optionally **one subtle visual** on the Governance mini only: thin **double border** or small **shield/check** icon **above** the IDE — **same** IDE glyph underneath. This signals “same interface, governance station” without a second diagram.

### Caption under the entire six-station row (required)

Use **one** of these (artist may hand-letter):

- **Each workspace: human–agent team, scenarios → tasks, own IDE context.**  
- Or shorter: **Same pattern at every station — detail shown for Product specification.**

### Do not include in Frame 3

- The full Product Intent path (Frame 4).  
- The four repository pillars as large primary elements (they belong in Frame 2; optional **faint** connectors from zoom column to “Knowledge / Skills / Artifacts / History” only if it stays subordinate to IDE + Scenarios→Tasks).

---

## 8. Frame 4 — Product Evolution Cycle (Product Intent)

### Intent for the viewer

“**Product Intent** is the token that moves through workspaces from **release-fed intent** to **delivery**; some steps are **parallel** or **iterative**; **governance** runs on handoffs without dominating the diagram.”

### Central visual element

- **Product Intent:** a **single recurring token** (glowing chip, labeled capsule, or bold **PI** monogram in a circle) that **travels** along arrows. **Same** token everywhere on this frame.

### Stages and flow (must match this logic exactly)

Use **workspace nodes** or **labeled swim stops** consistent with Frame 3 names (abbreviations on-art OK: **Spec**, **UX**, **Dev**, **QA**, **Release**, **Gov**).

**Primary path (solid arrows, numbered 1–7 optional):**

1. **Release** produces / emits **Product Intent** (arrow from Release → Intent token, or caption: *Release produces Product Intent*).  
2. Intent **triggers** work in **Product specification** (arrow to Spec).  
3. **Spec ↔ UX** — **bidirectional** loop (two arrows or double-headed arrow) between **Spec** and **UX**.  
4. From **Spec**, Intent moves to **Development** **and** **QA** in **parallel** (two **solid** arrows from Spec splitting to **Dev** and **QA** — both active from Spec).  
5. **Dev → QA** (solid arrow).  
6. **QA → Release** — label this leg **Product delivery** or *Delivery* on or near the arrow.

**Secondary / feedback path (dashed arrows, visually lighter):**

7. **Optional return to Spec:** **dashed** arrows from **Dev** and/or **QA** back to **Spec** (may be one merged dashed arc to Spec).

### Governance on transitions (lightweight — required but minimal)

- **Do not** add a large Governance swimlane parallel to the whole diagram.  
- Show **one** of the following:  
  - **Small checkpoint icon** (shield, stamp, or “G”) on **each main handoff arrow**; **or**  
  - **One caption** near the diagram: *Every Product Intent transition invokes governance scenarios.*  
- **Governance workspace** may appear as a **small satellite node** with short arrows from **handoff points** **or** only via the caption — **prefer caption + small checkpoints** if the canvas is crowded.

### Legibility rules

- **One** primary story: the **Intent token** path.  
- **Parallel** Dev and QA from Spec must be **obvious** (fork, not sequential ambiguity).  
- **Dashed** vs **solid** must be **visually distinct** in monochrome (weight + dash pattern).

### Do not include in Frame 4

- Full Scenarios→Tasks breakdown (that is Frame 3).  
- Six full IDE illustrations (Frame 3 already did IDE story).

---

## 9. Consistency checklist (all frames)

| Element | Rule |
|--------|------|
| Foundry | Appears Frame 1; may appear as **ghost outline** in Frame 2 only if it helps nesting — optional. |
| Workshop | Frame 2 primary; optional faint label in Frame 3. |
| Repository themes | **Knowledge, Skills, Artifacts, History** — Frame 2 only as **primary** art. |
| Workspaces | **Six** types, **same names** as Section 7. |
| IDE | **One** glyph design, **six** placements in Frame 3 (one large, five small). |
| Scenarios → Tasks | **Zoom column only** in Frame 3. |
| Product Intent | **Frame 4** token + path only. |
| Governance | **No** standalone frame; checkpoints and/or **one** caption in Frame 4; Governance as **sixth mini** in Frame 3. |

---

## 10. Negative prompts (tell the image model explicitly)

- No illegible micro-font walls of text.  
- No real IDE or cloud vendor logos (no VS Code, JetBrains, AWS, etc. marks).  
- No photorealistic humans or stock-photo collages.  
- No extra frames beyond the four specified.  
- No merging Frame 3 and Frame 4 into one unreadable mega-diagram.  
- No implying a **single** shared IDE for all teams — **six** IDE placements in Frame 3 are required.

---

## 11. Optional speaker script (not on-image; for presenter or video VO)

- **Frame 1:** “ACE centers on a Foundry — governed by how we define the product, how work runs, and how the org operates.”  
- **Frame 2:** “Inside Foundries we run Workshops — backed by knowledge, skills, the artifacts we produce, and the history of what we decided and learned.”  
- **Frame 3:** “Each Workbench contains workspaces — spec, UX, build, test, release, and governance. People step in through an IDE; agents are part of the team; scenarios break work into tasks. What you see enlarged for specification repeats at every station.”  
- **Frame 4:** “Product Intent is the thread: it circulates between specification and design, fans out to build and test, returns to release as delivery — and governance sits on the handoffs.”

---

## 12. Source alignment (reference)

This prompt is aligned with the ACE structural summary and **Product Evolution Cycle** as defined in internal material: Foundry under three models; workshops with repositories and Workbenches; six workspace types; workspaces use IDE, scenarios, tasks, human–agent teams; Release produces Product Intent; Spec↔UX; Spec to Dev and QA in parallel; Dev to QA; QA to Release as delivery; optional return from Dev/QA to Spec; governance invoked on intent transitions.

---

*End of prompt — sufficient for a capable illustration or image-generation agent to produce the four-frame ACE executive storyboard.*
