# Editorial Review: Raw Agent Subsystems Design

> **Date**: 2026-01-12  
> **Reviewer**: AI Assistant  
> **Scope**: Context Compiler, Seer Agent SDK, Raw Agent Lifecycle Manager

---

## Summary

Overall, the design documents are well-structured and consistent. However, there are several issues that need to be addressed:

1. **Outdated cross-references** to old file names
2. **Terminology inconsistencies** (minor)
3. **Missing cross-references** in some documents
4. **Potential ambiguity** in a few areas

---

## Issues Found

### 1. Outdated Cross-References

#### Issue: References to `context-assembly-engine.md`

**Files Affected:**
- `olympus-seer-docs/seer-design/subsystems/guardrails.md` (line 1028)
- `olympus-seer-docs/seer-design/introduction.md` (line 109)
- `olympus-seer-docs/seer-design/hub-integration/README.md` (line 175)
- `olympus-seer-docs/seer-design/README.md` (line 19)
- `olympus-seer-docs/seer-design/hub-integration/context-assembly.md` (line 380)

**Fix Required:**
Update references from `context-assembly-engine.md` to `context-compiler/compilation-service.md`

**Example:**
```markdown
# Before
- [Context Assembly Engine](./context-assembly-engine.md)

# After
- [Context Compilation Service](./context-compiler/compilation-service.md)
```

#### Issue: References to `agent-observability.md` for SDK content

**Status**: ✅ **Already Correct** - References to `agent-observability.md` are appropriate for platform-level observability. SDK-specific content correctly references the new SDK observability APIs.

---

### 2. Terminology Consistency

#### Issue: Autonomy Level Notation

**Current State:**
- List format: "Full, Suggest, Ask, Watch" (used in descriptions)
- Hierarchy format: "Full > Suggest > Ask > Watch" (used in hierarchy sections)

**Assessment**: ✅ **Acceptable** - Both formats are used appropriately:
- List format for general descriptions
- Hierarchy format for showing precedence/ordering

**Recommendation**: Keep both formats as they serve different purposes.

#### Issue: Archetype Role Capitalization

**Current State:**
- YAML examples use lowercase: `"thinker"`, `"doer"`, `"orchestrator"`, `"governor"`
- Definitions use capitalized: "Thinker", "Doer", "Orchestrator", "Governor"

**Assessment**: ✅ **Acceptable** - YAML values should be lowercase (standard practice), while definitions can be capitalized for readability.

**Recommendation**: Keep current approach.

#### Issue: Container Image Terminology

**Current State:**
- Most places use: "container image" (two words)
- YAML field names use: `containerImage` (camelCase)
- Some places use: "container_image" (snake_case)

**Assessment**: ✅ **Acceptable** - Different contexts require different formats:
- Natural language: "container image"
- YAML field names: `containerImage` (camelCase, Kubernetes convention)
- Code examples: `container_image` (snake_case, Python convention)

**Recommendation**: Keep current approach - it's contextually appropriate.

---

### 3. Missing Cross-References

#### Issue: Context Compiler README missing link to concept doc

**File**: `olympus-seer-docs/seer-design/subsystems/context-compiler/README.md`

**Status**: ✅ **Already Present** - The README already includes the reference to Context Assembly Concepts (line 75).

#### Issue: Raw Agent Spec Manager missing link to archetype roles doc

**File**: `olympus-seer-docs/seer-design/subsystems/raw-agent-lifecycle-manager/raw-agent-spec-manager.md`

**Status**: ✅ **Already Present** - The document already includes the reference to Agent Archetypes (line 337).

---

### 4. Potential Ambiguity

#### Issue: "Four-Source" vs "Four Sources"

**Current State:**
- Section headers use: "Four-Source Compilation" (hyphenated)
- Descriptions use: "four sources" (two words)
- Table headers use: "The Four-Source Model" (hyphenated)

**Assessment**: ✅ **Acceptable** - Hyphenation is used for compound adjectives (Four-Source Compilation), while "four sources" is used as a noun phrase. This follows standard English grammar.

**Recommendation**: Keep current approach.

#### Issue: "Request-Update-Based" vs "Request Update Based"

**Current State:**
- Most places use: "Request-Update-Based" (hyphenated)
- Some places use: "request-update-based" (lowercase, hyphenated)

**Assessment**: ✅ **Acceptable** - Hyphenation is consistent. Capitalization varies by context (title case vs. sentence case).

**Recommendation**: Keep current approach.

#### Issue: Training Spec vs TrainingSpec

**Current State:**
- Natural language: "Training Spec" (two words, capitalized)
- YAML/Code: `TrainingSpec` (camelCase, one word)
- CRD references: `TrainingSpec` (Kubernetes CRD name)

**Assessment**: ✅ **Acceptable** - Different contexts require different formats:
- Natural language: "Training Spec"
- Code/CRD: `TrainingSpec`

**Recommendation**: Keep current approach.

---

### 5. Duplication

#### Issue: Similar content in Python and Java SDK docs

**Assessment**: ✅ **Expected** - Python and Java SDK documents intentionally have similar structure and content because they provide the same logical APIs with language-appropriate idioms. This is not duplication but intentional parallelism.

**Recommendation**: Keep current approach - the parallel structure helps developers find equivalent APIs across languages.

#### Issue: Key Design Decisions repeated across documents

**Assessment**: ✅ **Acceptable** - Key design decisions are appropriately repeated in:
1. Main service/component documents (where decisions are made)
2. README files (summary for quick reference)
3. SCOPE documents (coverage summary)

This is appropriate for documentation hierarchy.

**Recommendation**: Keep current approach.

---

### 6. Completeness

#### Issue: Missing migration note in old files

**Files**: 
- `olympus-seer-docs/seer-design/subsystems/context-assembly-engine.md`
- `olympus-seer-docs/seer-design/subsystems/README.md` (mentions migration)

**Assessment**: ⚠️ **Minor Issue** - The old `context-assembly-engine.md` file still exists and may confuse readers.

**Recommendation**: 
1. Add a deprecation notice at the top of `context-assembly-engine.md`:
   ```markdown
   > **⚠️ DEPRECATED**: This document has been superseded by [Context Compilation Service](./context-compiler/compilation-service.md). Please refer to the new document.
   ```

2. Update `subsystems/README.md` to clarify migration status.

---

## Recommendations Summary

### High Priority

1. ✅ **COMPLETED** - Updated cross-references from `context-assembly-engine.md` to `context-compiler/compilation-service.md` in:
   - `guardrails.md` ✅
   - `introduction.md` ✅
   - `hub-integration/README.md` ✅
   - `README.md` ✅
   - `hub-integration/context-assembly.md` ✅

2. ✅ **COMPLETED** - Deleted `context-assembly-engine.md` file (all references updated first)

**Note**: Cross-references within the new documents are already complete and correct.

### Low Priority

1. ✅ **Documentation hierarchy** - Current approach is appropriate
2. ✅ **Terminology** - Current variations are contextually appropriate
3. ✅ **Duplication** - Current parallel structure is intentional and helpful

---

## Positive Findings

1. ✅ **Consistent structure** across all documents
2. ✅ **Clear design decisions** documented in appropriate places
3. ✅ **Good cross-referencing** within new documents
4. ✅ **Appropriate terminology** for different contexts (YAML vs. natural language)
5. ✅ **Complete coverage** of all planned functionality
6. ✅ **Consistent formatting** and style

---

## Conclusion

The design documents are well-written and consistent overall. The main issues are:
1. Outdated cross-references to old file names (easy fix)
2. A few missing cross-references (easy fix)
3. A deprecation notice needed for the old file (easy fix)

All terminology variations are contextually appropriate and follow standard conventions for their respective contexts (YAML, code, natural language).

---

*Editorial review complete. Ready for fixes.*
