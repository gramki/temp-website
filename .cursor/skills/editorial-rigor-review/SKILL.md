---
name: editorial-rigor-review
description: Line-by-line editorial review of thought-leadership documents for tonal rigor, commercial voice leaks, meta-narration, vocabulary discipline, shelf life, and audience neutrality. Use when the user asks to review, critique, or tighten a document intended for an executive or thought-leadership audience.
---

# Editorial Rigor Review

Review thought-leadership documents one at a time, applying a tight editorial lens. Present findings with specific lines, the problem, and a proposed fix. **Wait for user validation before applying any change.**

## The Lens

For each document, read every sentence through these eight tests:

### 1. Does every sentence earn its place?
If the sentence can be deleted and the argument loses nothing, flag it. Dead weight dilutes authority.

### 2. Tonal consistency
Does the register hold paragraph to paragraph? Flag any drops from thesis-grade prose to filing-cabinet language ("This section describes...", "The documents in this folder..."). Taglines and headings set the bar — body text must meet it.

### 3. Commercial voice
Flag any:
- First-person plural ("we", "our", "us") that positions the author as a vendor
- Market opportunity language ("the market opportunity remains open")
- Buyer-readiness framing ("when the door opens", "buying moments")
- Competitive positioning or differentiation claims

A thesis is a structural argument. It should read as thought leadership, not a pitch. The reader should never feel sold to.

### 4. Meta-narration
Flag sentences that tell the reader what the document is about to do instead of doing it. Examples:
- "This section will explore..."
- "We now turn to..."
- "The following analysis demonstrates..."

If the argument is well-structured, the reader doesn't need a narrator.

### 5. Vocabulary discipline
Does the document use its own established terms consistently? Flag drift:
- "felt problems" vs "relatable problems" — use the thesis's own vocabulary
- "work model" vs "domain model" vs "operational model" — pick one and hold it
- Introducing synonyms that create ambiguity

### 6. Shelf life
Flag time-specific claims that won't age well:
- "three years into the AI adoption cycle"
- "in the current regulatory environment"
- Specific year references unless historically anchored

Replace with structurally equivalent phrasing: "after successive rounds of AI investment" instead of "three years into..."

### 7. Specificity vs. thesis level
A thesis makes structural arguments. Flag:
- Performance claims ("weeks instead of quarters") — these belong in case studies or framework docs
- Implementation details that belong downstream
- Quantified promises without evidence

The test: would this sentence survive if the technology changed but the structural argument held? If not, it's too specific for a thesis.

### 8. Audience neutrality
The thesis should be consumable by bank CIOs, bank CEOs, the company's own board, and senior leadership. It is not a sales document. Flag anything that assumes a specific buyer relationship.

**Important distinction**: internal navigation docs (READMEs that organize a repo) can reference the company name — that's context, not a commercial voice leak. The thesis *documents themselves* must be neutral.

## Workflow

1. **Read the full document** — understand its arc before flagging anything.
2. **Apply all eight tests** — note each finding with the specific line number, the problem, and a proposed fix.
3. **Categorize findings**:
   - **Fix now**: Clear violations with obvious corrections (commercial voice leaks, timestamps, meta-narration)
   - **Discuss**: Judgment calls where the fix changes meaning or the author may have a reason (reframing a principle, restructuring a section)
4. **Present findings to user** — grouped by category, with proposed fixes. Do not apply changes.
5. **Wait for validation** — the user approves, modifies, or rejects each fix.
6. **Apply approved fixes** — one batch per document.
7. **Move to next document** — follow the reading order if the document suite has one.

## Discipline

- **Don't over-correct.** If a sentence works, leave it. The goal is rigor, not rewriting.
- **Don't confuse audiences.** A README organizing a repo for internal navigation has different rules than a thesis document intended for external executives.
- **Don't propose overwrought replacements.** If the original is five words, the fix should be five words — not a new paragraph.
- **A thesis is not a pitch.** Don't suggest adding competitive framing, case studies, pricing, or ROI quantification to a thesis. Those belong in separate documents.
- **Trust the author's structure.** Flag problems with execution, not with the author's choice of what to argue.
