---
name: Career Guides Engagement
overview: "Add org-8.0/engagement/career-guides/ with Function Coaching docs (structured by seniority level: craft/skills/competencies, roles and challenges, how to learn) and Role Coaching docs (interactions/tensions, escalation, further learning), plus a README and optional template."
todos: []
isProject: false
---

# Career Guides (Engagement) — Structure and Function Coaching

## Scope and location

- **Location:** [org-8.0/engagement/career-guides/](org-8.0/engagement/career-guides/) — engagement-only.
- **Contents:** Function Coaching docs (one per function, by seniority level) and Role Coaching docs (one per Engagement role). Both are coaching-style; they link to [career-paths.md](org-8.0/engagement/career-paths.md) and [roles.md](org-8.0/engagement/roles.md) and do not duplicate them.

---

## 1. Folder structure

```
org-8.0/engagement/career-guides/
  README.md                    # Index, audience, link to career-paths & roles
  FUNCTIONS.md                 # Optional: template/checklist for Function Coaching
  ROLES.md                     # Optional: template/checklist for Role Coaching
  functions/
    engineering.md
    architecture.md
    product-management.md
    program-delivery.md
    sre-operations.md
    account-management.md
  roles/
    client-partner.md
    cpa.md
    engagement-owner.md
    epm.md
    ea.md
    ava.md
    epo.md
    sre-lead.md
    engineering-lead.md
    squad-pm.md
    scrum-master.md
```

---

## 2. Function Coaching — content per seniority level

Each function guide is organized **by level of seniority** (from [career-paths.md](org-8.0/engagement/career-paths.md) Section 3). For **each level**, the doc covers three blocks:

### A. Required craft, skills, competencies

- What someone at this designation must be able to do (craft).
- Skills (observable, trainable) and competencies (behaviours, judgment) expected.
- Optional: how this level differs from the previous one (growth from prior level).

### B. Roles you are expected to play; challenges to be ready for

- Which **Engagement roles** (from the function-role table in career-paths) are typically staffed from this level (e.g. Senior Engineer → often EL; Architect → EA/AVA).
- What **challenges** are typical when playing those roles (delivery vs quality, cross-squad coordination, client pressure, etc.) so the person is mentally prepared and can “be ready to solve” them.

### C. How to learn

- Practical ways to build the above: on the job (assignments, rotations, stretch roles), feedback (execution-axis input, functional-axis reviews), and optional pointers to **Further learning** (books/articles with real links) relevant to this level. Can be brief per level and/or one “Further learning” section at the end of the function doc.

---

## 3. Seniority levels per function (from career-paths)

Use these levels so Function Coaching aligns with the existing ladders:


| Function               | IC / individual track                                                                     | Management / leadership track                                        |
| ---------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Engineering**        | Junior Engineer → Engineer → Senior Engineer → Staff Engineer (PE-1) → Principal Engineer | Senior Engineer → EL → Engineering Manager → Sr. Engineering Manager |
| **Architecture**       | Architect → Senior Architect → Principal Architect                                        | Architect → Architecture Manager → Sr. Architecture Manager          |
| **Product Management** | Associate PM → Product Manager → Senior PM                                                | Director of Product → Sr. Director → VP of Product                   |
| **Program / Delivery** | Program Coordinator → Program Manager → Senior Program Manager                            | Director of Delivery → Sr. Director → VP of Delivery                 |
| **SRE / Operations**   | SRE → Senior SRE → SRE Lead (designation) → SRE Manager                                   | Director of SRE → Sr. Director → VP of SRE                           |
| **Account Management** | (To be aligned with org — e.g. levels leading to Client Partner, CPA)                     |                                                                      |


Each function doc will have one section per level (or grouped where levels share expectations). Within each section: **Required craft, skills, competencies** → **Roles to play and challenges** → **How to learn**.

---

## 4. Role Coaching — content (unchanged from prior agreement)

Each role doc includes:

- **Success in the role:** first 90 days, what “good” looks like, key relationships, performance input into the functional axis.
- **Expected interactions, tensions, and how to navigate:** key interactions; normal tensions; guidance to navigate (without duplicating [roles.md](org-8.0/engagement/roles.md) “Typical challenges” verbatim).
- **Escalation: dos and don’ts:** when and to whom to escalate (per [governance.md](org-8.0/engagement/governance.md)); what to do before escalating; what not to do.
- **Further learning:** internal links (roles, career-paths, governance) plus external books/articles with **real, working links** and a one-line “why relevant”.

**EA and AVA role docs only:** Add a short **Architecture vs technical architecture** subsection and in Further learning include the agreed resources (DZone article, *Software Architecture in Practice*, *Just Enough Software Architecture*, *Solution Architecture Foundations*, TOGAF, etc.).

---

## 5. README and optional templates

- **README.md:** Purpose of the folder (coaching for success in functions and roles); audience; that career-paths and roles remain the reference for structure and responsibilities; list of function and role docs with one-line descriptions; link back to main [Engagement Guide](README.md).
- **FUNCTIONS.md (optional):** Checklist or template for Function Coaching: “For each seniority level: (1) Required craft, skills, competencies (2) Roles to play and challenges to be ready for (3) How to learn.”
- **ROLES.md (optional):** Checklist for Role Coaching: interactions/tensions, escalation dos and don’ts, further learning; for EA/AVA add architecture vs technical architecture and resources.

---

## 6. Integration with main guide

- In [org-8.0/engagement/README.md](org-8.0/engagement/README.md) (Guide Contents or Companion Documents): add a row or short section pointing to **Career Guides** ([career-guides/README.md](org-8.0/engagement/career-guides/README.md)) as coaching material for functions and roles.
- [career-paths.md](org-8.0/engagement/career-paths.md): add a sentence or “See also” at the end pointing to the career-guides for coaching by function and role.

---

## 7. Implementation order

1. Create `career-guides/` and `career-guides/README.md`.
2. Add optional `FUNCTIONS.md` and `ROLES.md` templates/checklists.
3. Create function docs under `career-guides/functions/` with the per-level structure (craft/skills/competencies, roles and challenges, how to learn); start with one function (e.g. Engineering) as the pattern.
4. Create role docs under `career-guides/roles/` with interactions/tensions, escalation, further learning; implement EA and AVA with the architecture vs technical architecture content and links.
5. Update main Engagement README and career-paths.md to link to career-guides.

This keeps career-guides engagement-scoped, places Function Coaching under each function with clear seniority-level structure, and preserves the agreed Role Coaching and architecture-distinction content.