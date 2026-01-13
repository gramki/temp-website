# Documentation Review Prompt

Please perform a comprehensive review of the documentation changes made in this session. Analyze the following aspects:

## 1. Structural Consistency
- [ ] Do all new files follow the established documentation patterns and templates?
- [ ] Are file naming conventions consistent with the codebase?
- [ ] Is the folder structure logical and aligned with existing organization?
- [ ] Are README files present where expected and properly structured?

## 2. Content Quality
- [ ] Is terminology used consistently throughout (persona names, abbreviations, technical terms)?
- [ ] Are concepts defined clearly on first mention?
- [ ] Do cross-references use correct file paths and anchor links?
- [ ] Are status indicators (🟡 Draft, 🔴 Planning, etc.) accurate and consistent?
- [ ] Are code examples, wireframes, and diagrams properly formatted?

## 3. Link Integrity
- [ ] Do all internal markdown links resolve correctly?
- [ ] Are external references to other documentation valid?
- [ ] Are persona references properly linked (full name + abbreviation + role link on first mention)?
- [ ] Do file references match actual file locations?

## 4. Completeness
- [ ] Are all mentioned concepts, subsystems, or features documented?
- [ ] Do all personas have their needs documented (inline or dedicated pages)?
- [ ] Are all referenced journeys, desks, consoles, and channels documented?
- [ ] Are integration points with other systems (Hub, Seer, etc.) properly documented?

## 5. Accuracy and Alignment
- [ ] Do the changes align with existing architectural decisions (ADRs)?
- [ ] Are there conflicts with existing documentation?
- [ ] Do the changes match the stated objectives of the session?
- [ ] Are statistics and metrics (file counts, line counts) accurate?

## 6. Editorial Quality
- [ ] Is the writing clear and professional?
- [ ] Are there spelling or grammatical errors?
- [ ] Is formatting consistent (headers, lists, tables, code blocks)?
- [ ] Are tables properly formatted and readable?

## 7. Cross-System Consistency
- [ ] Do references to Hub concepts match Hub documentation?
- [ ] Do references to Seer concepts match Seer documentation?
- [ ] Are shared concepts (OPDA, autonomy levels, etc.) used consistently?
- [ ] Do integration patterns align with documented system boundaries?

## 8. Session Note Accuracy
- [ ] Does the session note accurately reflect what was accomplished?
- [ ] Are file counts and statistics correct?
- [ ] Are all key decisions and open questions captured?
- [ ] Do commit messages follow the required format: `[ticketID] <type>(<scope>): <subject>`?

## Review Output Format

Please provide:
1. **Summary**: Overall assessment of documentation quality
2. **Issues Found**: List of specific issues with file paths and line numbers where applicable
3. **Recommendations**: Suggested improvements or follow-up actions
4. **Verification Checklist**: Confirmation of what was verified (links tested, terminology checked, etc.)