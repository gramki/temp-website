# Content Change Suggestions: ETSL Documentation Corpus

**Date:** December 30, 2025  
**Purpose:** Identify content duplication and redundancy; propose consolidation strategies  
**Status:** Partially Implemented (High-Priority Items Complete)

---

## Implementation Log

### December 30, 2025 — High-Priority Items Completed

**1. Glossary Consolidation**
- `building-data-products-using-etsl-data-artifacts.md`: Replaced ~130 lines of duplicated definitions with reference to Tier-1/Tier-2 + ~35 lines of document-specific terms
- `building-etsl-data-artifacts-in-a-large-enterprise.md`: Replaced ~150 lines of duplicated definitions with reference to Tier-1/Tier-2 + ~35 lines of document-specific terms

**2. "What ETSL Is/Is Not" Consolidation**
- `etsl-one-page-onboarding-primer.md`: Condensed 5 bullets to 3, added reference to Purpose doc Section 4
- `etsl-and-data-mesh-coexistence-guidance.md`: Clarified as "Data Mesh-Specific Misconceptions," added reference to Purpose doc Section 4
- `etsl-purpose-and-story.md`: Retained as canonical source (no changes needed)

**3. Data Mesh Coexistence Overlap**
- `etsl-purpose-and-story.md` Section 9: Reduced from ~30 lines to ~12 lines, removed pattern definitions, added reference to coexistence doc
- `building-data-products-using-etsl-data-artifacts.md` Section 9: Streamlined from ~140 lines to ~70 lines, kept banking examples, removed pattern definitions

**4. Ontology Documents Merged**
- Added CIO Executive Summary to `artifacts-ontology-vs-semantic-vs-data.md`
- Added detailed misconceptions section from `etsl-vs-ontology.md`
- Deleted `etsl-vs-ontology.md` (superseded)
- Updated all references in README.md, data-modeling-guidance.md, relationships-modeling-guidance.md

---

## Executive Summary

After systematic review of all 22 documents in the `etsl-background` folder, I identified **10 categories of content duplication or redundancy**. This document presents findings and recommendations organized by priority.

### Priority Levels
- 🔴 **High Priority**: Clear duplication causing maintenance burden
- 🟡 **Medium Priority**: Overlapping content that could be consolidated
- 🟢 **Low Priority**: Intentional repetition for accessibility; consider linking instead

---

## 1. 🔴 Glossary Duplication (High Priority)

### Finding

Multiple documents maintain independent glossaries with overlapping definitions:

| Document | Glossary Lines | Terms Defined |
|----------|----------------|---------------|
| `tier-1-etsl-canonical-terminology.md` | ~220 | 13 core terms |
| `tier-2-etsl-canonical-classifications.md` | ~118 | 6 classifications |
| `building-data-products-using-etsl-data-artifacts.md` | ~135 | 25+ terms |
| `building-etsl-data-artifacts-in-a-large-enterprise.md` | ~100 | 20+ terms |

The building guides re-define terms already defined in Tier-1/Tier-2, creating maintenance risk when definitions evolve.

### Examples of Duplicated Definitions

**"Data Product"** appears in:
1. `tier-1-etsl-canonical-terminology.md` (line 154-166)
2. `etsl-one-page-onboarding-primer.md` (line 95-98)
3. `etsl-purpose-and-story.md` (line 308-332)
4. `building-data-products-using-etsl-data-artifacts.md` (line 1920-1921, 164-177)
5. `building-etsl-data-artifacts-in-a-large-enterprise.md` (glossary)

**"ETSL Data Artifact"** appears in:
1. `tier-1-etsl-canonical-terminology.md` (line 32-46)
2. `etsl-one-page-onboarding-primer.md` (line 81-84)
3. `artifacts-ontology-vs-semantic-vs-data.md` (line 74-90)
4. `building-data-products-using-etsl-data-artifacts.md` (line 165, 1945-1946)
5. `building-etsl-data-artifacts-in-a-large-enterprise.md` (multiple sections)

### Recommendation

**Option A (Preferred): Reference-Only Glossaries**
- Keep Tier-1 and Tier-2 as the *only* sources of term definitions
- Replace glossaries in building guides with:
  ```markdown
  ## Glossary
  
  This document uses terminology defined in:
  - *Tier-1 ETSL Canonical Terminology* — Core semantic primitives
  - *Tier-2 ETSL Canonical Classifications* — Behavioral classifications
  
  Terms specific to this document are defined inline where introduced.
  ```

**Option B: Consolidate into Single Glossary**
- Create a single `glossary.md` file
- All other documents reference it

### Estimated Impact
- Reduces total glossary content by ~250 lines
- Eliminates definition drift risk
- Simplifies future terminology updates

---

## 2. 🔴 "What ETSL Is / Is Not" Lists (High Priority)

### Finding

Near-identical lists appear in three documents:

| Document | Section | Content |
|----------|---------|---------|
| `etsl-purpose-and-story.md` | Section 4 | "What ETSL Is" / "What ETSL Is Not" |
| `etsl-one-page-onboarding-primer.md` | Lines 116-125 | "What ETSL Is NOT" |
| `etsl-and-data-mesh-coexistence-guidance.md` | Section 12 | "Common Misconceptions" |

### Overlap Examples

All three contain variations of:
- "Not a data lake or warehouse"
- "Not centralized data ownership"
- "Not a Data Mesh replacement"
- "Not a reporting layer"

### Recommendation

**Canonical Location:** `etsl-purpose-and-story.md` Section 4 (most comprehensive)

**Other Documents:**
- `etsl-one-page-onboarding-primer.md`: Keep 3-bullet summary with link to full list
- `etsl-and-data-mesh-coexistence-guidance.md`: Keep only Data Mesh-specific misconceptions

### Suggested Rewrite for Primer

```markdown
## What ETSL Is NOT (Quick Reference)

- Not a data lake, warehouse, or MDM program
- Not centralized data ownership
- Not a Data Mesh replacement

For the complete list, see *ETSL Purpose and Story*, Section 4.
```

---

## 3. 🟡 Data Mesh Coexistence Patterns (Medium Priority)

### Finding

Data Mesh coexistence is covered substantially in three places:

| Document | Scope | Lines |
|----------|-------|-------|
| `etsl-and-data-mesh-coexistence-guidance.md` | Deep dive (13 sections) | ~250 |
| `etsl-purpose-and-story.md` | Section 9 | ~30 |
| `building-data-products-using-etsl-data-artifacts.md` | Section 9 | ~100 |

### Content Overlap

All three describe the same three patterns:
1. Domain-first (no ETSL)
2. ETSL-first (cross-domain truth)
3. Hybrid

### Recommendation

**Keep:** `etsl-and-data-mesh-coexistence-guidance.md` as the authoritative source

**Reduce:**
- `etsl-purpose-and-story.md` Section 9: Shorten to ~10 lines + reference
- `building-data-products-using-etsl-data-artifacts.md` Section 9: Keep banking examples, remove pattern definitions and reference the coexistence doc

### Suggested Rewrite for Purpose Doc

```markdown
## 9. Co-existing with Data Mesh and Domain Ownership

ETSL complements, not replaces, Data Mesh principles. Domain-owned data products continue to exist; 
ETSL provides a semantic backbone for cross-domain truth.

Three coexistence patterns are common: domain-first, ETSL-first, and hybrid. 
For detailed patterns and guidance, see *ETSL and Data Mesh: Co-existence, Complementarity, and Enterprise Evolution*.
```

---

## 4. 🟡 Ontology vs ETSL Content Overlap (Medium Priority)

### Finding

Two documents cover the ontology/ETSL distinction with significant overlap:

| Document | Focus | Length |
|----------|-------|--------|
| `etsl-vs-ontology.md` | CIO-focused one-pager | ~360 lines |
| `artifacts-ontology-vs-semantic-vs-data.md` | Architect-focused deep dive | ~318 lines |

### Overlapping Content

Both contain:
- Core distinction ("meaning vs truth")
- "Grammar vs sentences" mental model
- Concrete Party/Account ownership example
- Common misconceptions
- Governance implications
- Closing principle ("Ontology gives language, ETSL gives memory")

### Recommendation

**Option A (Preferred): Merge Documents**
- Rename `artifacts-ontology-vs-semantic-vs-data.md` to `ontology-and-etsl-artifacts-distinction.md`
- Add a "CIO Summary" section at the top (from `etsl-vs-ontology.md`)
- Move detailed architect content below
- Delete `etsl-vs-ontology.md`

**Option B: Keep Separate, Remove Overlap**
- `etsl-vs-ontology.md`: Keep as CIO-only (cut to ~150 lines)
- `artifacts-ontology-vs-semantic-vs-data.md`: Remove duplicated mental models, reference the one-pager

### Estimated Impact
- Reduces total content by ~150-200 lines
- Clearer reading paths by audience

---

## 5. 🟡 Anti-Pattern Lists (Medium Priority)

### Finding

Anti-patterns are listed in four documents:

| Document | Focus | Examples |
|----------|-------|----------|
| `building-data-products-using-etsl-data-artifacts.md` | Data Product anti-patterns | 10+ |
| `building-etsl-data-artifacts-in-a-large-enterprise.md` | Data Artifact anti-patterns | 10+ |
| `etsl-one-page-onboarding-primer.md` | Common mistakes | 5 |
| `events-vs-facts.md` | Fact/Event modeling anti-patterns | 5 |

### Overlap Examples

"Hiding authority in code" appears in:
- `building-data-products-using-etsl-data-artifacts.md`
- `building-etsl-data-artifacts-in-a-large-enterprise.md`
- `etsl-one-page-onboarding-primer.md`

"Treating reconciliation as a technical problem" appears in:
- `etsl-one-page-onboarding-primer.md`
- `building-etsl-data-artifacts-in-a-large-enterprise.md`

### Recommendation

**Keep context-specific anti-patterns in their respective guides.** But:

1. **Remove generic anti-patterns from specialized docs** that belong in the primer
2. **Add cross-references**: Each guide should say "For foundational anti-patterns, see the Onboarding Primer"
3. **Consider future consolidation**: If anti-patterns continue growing, create `common-anti-patterns.md`

---

## 6. 🟡 Problem Statement / "Why This Matters" (Medium Priority)

### Finding

The enterprise truth problem is narrated in multiple places:

| Document | Section | Style |
|----------|---------|-------|
| `etsl-purpose-and-story.md` | Sections 1-2 | Warm, leadership-focused |
| `building-etsl-data-artifacts-in-a-large-enterprise.md` | Section 3 | Banking scenario, architect-focused |
| `etsl-and-data-mesh-coexistence-guidance.md` | Sections 1-2 | Data Mesh-contrast focused |

### Recommendation

**Intentional differentiation is acceptable here** because:
- Each audience needs the problem framed for their context
- The stories differ (available credit vs regulatory reporting vs domain ownership)

**Minor suggestion:** Add explicit cross-references so readers know other framings exist:

```markdown
> *For the leadership-focused framing of the enterprise truth problem, see ETSL Purpose and Story, Section 1.*
```

---

## 7. 🟢 Common Misconceptions (Low Priority)

### Finding

Misconception tables appear in:
- `etsl-purpose-and-story.md` Section 4 (general)
- `etsl-vs-ontology.md` Section "Common Misconceptions" (ontology-specific)
- `etsl-and-data-mesh-coexistence-guidance.md` Section 12 (Data Mesh-specific)

### Recommendation

**No change needed.** Each misconception table is contextually appropriate:
- General misconceptions → Purpose doc
- Ontology misconceptions → Ontology doc
- Data Mesh misconceptions → Coexistence doc

**Optional:** Add a brief note in each: "For other common misconceptions, see [other doc]."

---

## 8. 🟢 Governance Mechanisms (Low Priority)

### Finding

Governance by design is covered in:
- `etsl-purpose-and-story.md` Section 10
- `building-etsl-data-artifacts-in-a-large-enterprise.md` Section 13

### Recommendation

**Keep both.** The Purpose doc covers governance principles; the Building guide covers operational rituals. They complement each other.

**Optional enhancement:** Add a cross-reference in each:
- Purpose doc → "For operational governance rituals, see the Building Guide, Section 13"
- Building guide → "For governance principles, see ETSL Purpose and Story, Section 10"

---

## 9. 🟢 Comparison with Other Approaches (Low Priority)

### Finding

`etsl-data-products-vs-other-approaches.md` contains detailed comparisons that are:
- Referenced (correctly) from `building-data-products-using-etsl-data-artifacts.md` Section 14
- Self-contained and well-structured

### Recommendation

**No change needed.** The current reference-only approach is correct.

**Minor suggestion:** The file has informal commentary ("That's a very good instinct...") suggesting it was pasted from a conversation. Consider cleaning up the opening lines:

```markdown
# Current opening (informal):
That's a very good instinct.
Without explicit compare/contrast sections...

# Suggested opening (formal):
# ETSL-Based Data Products vs Common Practices
## Comparative Perspectives for Architects and Engineers

This document compares ETSL-based Data Product engineering with familiar approaches...
```

---

## 10. 🟢 Events vs Facts (Low Priority)

### Finding

`events-vs-facts.md` is well-structured and self-contained. No significant duplication with other documents.

### Recommendation

**No change needed.** This document serves a unique purpose and doesn't overlap substantially with others.

---

## Summary of Recommendations

### High Priority Actions ✅ COMPLETED

| # | Action | Documents Affected | Lines Reduced | Status |
|---|--------|-------------------|---------------|--------|
| 1 | Consolidate glossaries to reference-only | 2 building guides | ~200 lines | ✅ Done |
| 2 | Consolidate "What ETSL Is/Is Not" | 3 documents | ~15 lines | ✅ Done |

### Medium Priority Actions ✅ COMPLETED

| # | Action | Documents Affected | Lines Reduced | Status |
|---|--------|-------------------|---------------|--------|
| 3 | Reduce Data Mesh coexistence overlap | 2 documents | ~60 lines | ✅ Done |
| 4 | Merge ontology docs, delete `etsl-vs-ontology.md` | 2 → 1 document | ~200 lines | ✅ Done |

### Remaining Low Priority

| # | Action | Documents Affected | Estimated Line Reduction |
|---|--------|-------------------|-------------------------|
| 5 | Cross-reference anti-pattern lists | 4 documents | ~20 lines |

### Low Priority / No Action

| # | Finding | Recommendation |
|---|---------|----------------|
| 6 | Problem statements differ by audience | Keep as-is |
| 7 | Misconceptions are context-specific | Keep as-is |
| 8 | Governance coverage is complementary | Add cross-references |
| 9 | Comparisons already use references | Clean up informal opening |
| 10 | Facts vs Events is unique | No change |

---

## Implementation Notes

If you proceed with changes:

1. **Update the README.md** to reflect any document merges or deletions
2. **Search for broken references** after any file changes
3. **Consider a changelog** in each modified document noting the consolidation

---

## Questions for Your Review

1. **Glossary strategy:** Do you prefer Option A (reference-only) or Option B (single glossary file)?
2. **Ontology docs:** Merge into one document, or keep separate with reduced overlap?
3. **Anti-patterns:** Create a separate anti-patterns reference doc, or keep them distributed?
4. **Informal content cleanup:** Should `etsl-data-products-vs-other-approaches.md` be cleaned up?

---

*End of Suggestions Document*

