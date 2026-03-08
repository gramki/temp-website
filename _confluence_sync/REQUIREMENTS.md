# Confluence Sync - Requirements Specification

## Overview

This document specifies the complete requirements for syncing Markdown documentation from a Git repository to Confluence. Requirements are organized by sync stage, with scenarios and expected behaviors for each.

---

## Part 1: Edge Cases and Gaps Identified

### Critical Edge Cases (Not Yet Handled)

| ID | Category | Edge Case | Current Behavior | Risk Level |
|----|----------|-----------|------------------|------------|
| EC-01 | **File Deletion** | File deleted from Git repo | Confluence page remains (orphaned) | Medium |
| EC-02 | **File Rename** | File renamed in Git | Creates new page, old page orphaned | High |
| EC-03 | **Title Change** | H1 title changed in Markdown | Creates new page OR updates with new title, old title page may remain | High |
| EC-04 | **Duplicate Titles** | Two files with same H1 title in different directories | Link resolution picks wrong page; overwrites may occur | Critical |
| EC-05 | **Directory Rename** | Directory renamed in Git | New directory page created, old directory page orphaned with children | High |
| EC-06 | **Circular Links** | Cross-links between files form circular references | Works but infinite recursion possible during validation | Low |
| EC-07 | **Large Files** | Markdown file > 1MB | May hit Confluence API limits, memory issues | Medium |
| EC-08 | **Special Characters in Titles** | Titles with `<`, `>`, `&`, quotes, or Confluence macros | May break XML/storage format | High |
| EC-09 | **Binary in Markdown** | Embedded images with data URLs or binary content | May cause sync failures | Medium |
| EC-10 | **Concurrent Edits** | User edits Confluence page during sync | Last write wins, user changes lost | Medium |
| EC-11 | **Rate Limiting** | Rapid sync with many files hits Confluence rate limits | 429 errors, partial sync | Medium |
| EC-12 | **Network Interruption** | Network fails mid-sync | Partial sync, inconsistent state | High |
| EC-13 | **State Corruption** | JSONL state file corrupted mid-write | Sync state lost or invalid | Medium |
| EC-14 | **Permission Changes** | User loses Confluence permissions mid-sync | Partial sync with permission errors | Medium |
| EC-15 | **Space Deletion** | Target Confluence space deleted | All syncs fail | Low |
| EC-16 | **README Title Mismatch** | README.md H1 differs significantly from directory name | Directory page gets README content with mismatched expectations | Low |
| EC-17 | **Empty Directory** | Directory with only ignored files or no Markdown | No directory page created (expected) OR empty page created | Low |
| EC-18 | **Symlinks** | Symlinked files or directories in source | May duplicate content or fail | Medium |
| EC-19 | **Encoding Issues** | Non-UTF-8 encoded Markdown files | Read failures or garbled content | Medium |
| EC-20 | **Very Deep Nesting** | Directories nested 10+ levels deep | May hit Confluence hierarchy limits | Low |
| EC-21 | **Thread Safety** | Parallel threads updating same parent page cache | Race conditions possible | Medium |
| EC-22 | **Anchor Links** | `[Link](#anchor)` references to headings | Anchor stripped, link may not work in Confluence | Medium |
| EC-23 | **External Links** | Links to external URLs or non-.md files | Preserved but not validated | Low |
| EC-24 | **Front Matter** | YAML front matter in Markdown | Rendered as content, not parsed | Low |
| EC-25 | **Attachments** | Image files, PDFs in directories | Not synced, image links broken | High |
| EC-26 | **Confluence Macros in MD** | Existing Confluence macro syntax in Markdown | May be double-encoded or corrupted | Medium |

### Partially Handled Cases

| ID | Category | Case | Current Status | Improvement Needed |
|----|----------|------|----------------|-------------------|
| PH-01 | Parent Change | File moved to different directory | ✅ Now detected via parent_id tracking | Need to verify with actual test |
| PH-02 | Force Sync | Force sync specific paths | ✅ Config supported | No CLI override yet |
| PH-03 | Broken Links | Detect broken internal links | ✅ Separate script | Not integrated into main sync |
| PH-04 | Progress Reporting | Show sync progress | ✅ Implemented | Could show ETA |
| PH-05 | Parallel Sync | Parallel API calls | ✅ Implemented | Rate limiting not handled |
| PH-06 | Content Hash | Skip unchanged content | ✅ Implemented | Doesn't include title in hash |

---

## Part 2: Requirements by Sync Stage

### Stage 0: Initialization & Configuration

**Purpose**: Load configuration, validate inputs, establish connections.

#### Scenario 0.1: Configuration Loading

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 0.1.1 Valid config file | `confluence-destinations.yaml` exists with valid YAML | Parse and validate all destinations | N/A |
| 0.1.2 Config file missing | File not found | Exit with clear error: "Configuration file not found: {path}" | ✅ Handled |
| 0.1.3 Invalid YAML syntax | Malformed YAML | Exit with parse error and line number | ⚠️ Generic error |
| 0.1.4 Missing required field | `space_key` missing | Exit with: "Missing required field 'space_key' in destination '{id}'" | ✅ Handled |
| 0.1.5 Invalid destination ID | ID contains spaces/special chars | Accept (but recommend slugs) OR reject with validation error | ⚠️ Not validated |
| 0.1.6 Duplicate destination IDs | Two destinations with same `id` | Exit with: "Duplicate destination ID: {id}" | ❌ Not checked |
| 0.1.7 Source folder not found | Path doesn't exist | Exit with: "Folder not found: {path}" | ✅ Handled |
| 0.1.8 Custom data directory | `--data-dir` specified | Use that directory for all state/reports | ✅ Handled |

#### Scenario 0.2: Credential Resolution

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 0.2.1 Token in env var | `CONFLUENCE_TOKEN` set | Use token from environment | N/A |
| 0.2.2 Token in .env file | `data/.env` contains token | Load and use token | ✅ Handled by wrapper |
| 0.2.3 Token missing | Neither env var nor .env | Exit with: "API token not found in environment variable '{var_name}'" | ✅ Handled |
| 0.2.4 Token invalid | Wrong/expired token | API returns 401; report: "Authentication failed. Check your token." | ⚠️ Generic HTTP error |
| 0.2.5 Username missing | `username` not in config | Exit with validation error | ✅ Handled |

#### Scenario 0.3: Connection Validation

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 0.3.1 Valid connection | Correct URL, creds, space | Proceed to sync | N/A |
| 0.3.2 Space not found | Invalid `space_key` | Exit with: "Space '{key}' not found or not accessible" | ⚠️ Generic error |
| 0.3.3 No permission | User can't write to space | Exit with: "Permission denied for space '{key}'" | ⚠️ Generic error |
| 0.3.4 Network unreachable | URL unreachable | Exit with: "Cannot connect to Confluence: {url}" | ⚠️ Generic error |
| 0.3.5 Confluence maintenance | 503 response | Retry with backoff OR exit with clear error | ❌ Not handled |

---

### Stage 1: State Loading & Content Discovery

**Purpose**: Load previous sync state, discover files to sync, build caches.

#### Scenario 1.1: Sync State Loading

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 1.1.1 Fresh sync | No state file | Start with empty state; all files treated as new | ✅ Handled |
| 1.1.2 Valid state file | `sync-state.jsonl` exists | Load into memory as dictionary | ✅ Handled |
| 1.1.3 Corrupted state | Invalid JSON lines | Skip invalid lines, log warning, continue with valid entries | ✅ Handled |
| 1.1.4 Migrating from JSON | Old `sync-state.json` exists | Migrate to JSONL format | ✅ Handled |
| 1.1.5 Very large state | 10,000+ entries | Load efficiently (streaming for JSONL) | ✅ JSONL format |
| 1.1.6 State for deleted files | State contains entries for files no longer in repo | Keep in state (no action) OR mark as stale | ⚠️ Kept indefinitely |

#### Scenario 1.2: File Discovery

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 1.2.1 Normal discovery | Directory with .md files | Find all .md files recursively | ✅ Handled |
| 1.2.2 Hidden files | Files starting with `.` | Skip (e.g., `.draft.md`) | ✅ Handled |
| 1.2.3 Hidden directories | Directories starting with `.` | Skip entire directory (e.g., `.git`, `.vscode`) | ✅ Handled |
| 1.2.4 Ignored by pattern | File matches `.confluence-ignore` pattern | Skip file | ✅ Handled |
| 1.2.5 Negated ignore | File matches `!important.md` after ignore | Include file | ✅ Handled |
| 1.2.6 Wildcard ignore | Directory has `*` in `.confluence-ignore` | Skip entire directory | ✅ Handled |
| 1.2.7 Symlinked file | Symlink to .md file | Follow symlink and sync target | ⚠️ Not explicitly tested |
| 1.2.8 Symlinked directory | Symlink to directory | Follow symlink and sync contents | ⚠️ Not explicitly tested |
| 1.2.9 Empty source folder | No .md files in path | Log warning, no pages synced | ✅ Handled |
| 1.2.10 Non-UTF8 file | Binary or non-UTF8 .md | Skip with warning: "Could not read file: encoding error" | ⚠️ Generic error |

#### Scenario 1.3: Title Cache Building

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 1.3.1 Normal extraction | File with `# Title` | Extract "Title" as page title | ✅ Handled |
| 1.3.2 No H1 heading | File without `#` line | Use cleaned filename as title | ✅ Handled |
| 1.3.3 Multiple H1 | File with multiple `# ` lines | Use first H1 as title | ✅ Handled |
| 1.3.4 H1 with formatting | `# **Bold** Title` | Include formatting in title (may cause issues) | ⚠️ Not cleaned |
| 1.3.5 Empty H1 | `# ` followed by nothing | Use cleaned filename as title | ⚠️ May produce empty title |
| 1.3.6 Duplicate titles | Two files with same H1 | Both cached; link resolution picks first found | ⚠️ Non-deterministic |
| 1.3.7 Title with special chars | `# Page <Title> & More` | Store as-is; must be escaped in Confluence | ⚠️ Not escaped in cache |

---

### Stage 2: Content Preparation (Phase 1 - Local)

**Purpose**: Convert Markdown to Confluence storage format, compute hashes, prepare metadata.

#### Scenario 2.1: Markdown Parsing

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 2.1.1 Standard Markdown | CommonMark syntax | Convert to HTML correctly | ✅ Handled |
| 2.1.2 Fenced code blocks | ` ```python ... ``` ` | Convert to Confluence code macro OR `<pre>` | ✅ HTML <code> |
| 2.1.3 Tables | GFM table syntax | Convert to HTML table | ✅ Handled |
| 2.1.4 Strikethrough | `~~text~~` | Convert to `<del>text</del>` | ⚠️ Depends on extension |
| 2.1.5 Task lists | `- [ ] item` | Convert to checkbox or list item | ⚠️ Depends on extension |
| 2.1.6 Footnotes | `[^1]` references | May not render correctly | ⚠️ Extension dependent |
| 2.1.7 Math/LaTeX | `$formula$` or `$$block$$` | Render as text (no math support) | ⚠️ Not supported |
| 2.1.8 Mermaid diagrams | ` ```mermaid ``` ` | Convert to Confluence mermaid macro (diagram) | ✅ Post-process to macro |
| 2.1.9 HTML in Markdown | `<div>custom</div>` | Pass through to storage format | ⚠️ May break Confluence |
| 2.1.10 Very long document | 50,000+ characters | Convert successfully | ⚠️ Not tested for limits |

#### Scenario 2.2: Link Conversion

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 2.2.1 Relative .md link | `[Link](./other.md)` | Convert to `<ac:link ri:content-title="Other"/>` | ✅ Handled |
| 2.2.2 Absolute .md link | `[Link](/path/to/file.md)` | Resolve from root, convert to Confluence link | ✅ Handled |
| 2.2.3 Parent directory link | `[Link](../sibling/file.md)` | Resolve path, convert to Confluence link | ✅ Handled |
| 2.2.4 Link with anchor | `[Link](file.md#section)` | Strip anchor, link to page (anchor lost) | ⚠️ Anchor stripped |
| 2.2.5 External URL | `[Link](https://example.com)` | Preserve as HTML `<a>` link | ✅ Handled |
| 2.2.6 Link to non-.md file | `[Link](./image.png)` | Preserve as relative link (likely broken) | ⚠️ Not handled |
| 2.2.7 Link to missing file | `[Link](./missing.md)` | Preserve as HTML link (broken in Confluence) | ⚠️ Not validated |
| 2.2.8 Duplicate title link | Link text doesn't match target | May link to wrong page | ⚠️ First match wins |
| 2.2.9 Case sensitivity | `./File.md` vs `./file.md` | Case-sensitive path resolution | ⚠️ OS dependent |
| 2.2.10 URL-encoded path | `./file%20name.md` | Decode and resolve | ⚠️ Not decoded |

#### Scenario 2.3: Directory Page Preparation

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 2.3.1 Directory with README | `README.md` exists in dir | Embed README content in directory page | ✅ Handled |
| 2.3.2 Directory without README | No `README.md` | Generate placeholder: "# {Dir Title}\n*Directory: {name}*" | ✅ Handled |
| 2.3.3 Root folder with README | Source folder root has `README.md` | Embed in source folder's landing page | ✅ Now handled |
| 2.3.4 Custom folder title | `title: "Custom Name"` in config | Use custom title instead of folder name | ✅ Handled |
| 2.3.5 Numbered prefix in name | `01-getting-started/` | Strip number, titlecase: "Getting Started" | ✅ Handled |
| 2.3.6 Underscore/hyphen in name | `my_folder-name/` | Convert to spaces: "My Folder Name" | ✅ Handled |
| 2.3.7 Empty directory | Directory with no .md files | No directory page created | ✅ Handled |
| 2.3.8 Directory with only ignored files | All files match ignore patterns | No directory page created | ✅ Handled |

#### Scenario 2.4: Git Metadata Extraction

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 2.4.1 Normal file | File in Git repo | Get file-specific commit hash and date | ✅ Handled |
| 2.4.2 New file (uncommitted) | File not yet committed | Use repo HEAD commit | ✅ Handled |
| 2.4.3 Not a Git repo | No `.git` directory | Metadata empty/null | ⚠️ May error |
| 2.4.4 Git not installed | `git` command not found | Metadata empty/null, warning logged | ⚠️ May error |
| 2.4.5 GitHub URL detection | Remote named `origin` | Extract GitHub URL from remote | ✅ Handled |
| 2.4.6 Non-GitHub remote | GitLab, Bitbucket, etc. | Extract URL but may format incorrectly | ⚠️ GitHub-specific format |
| 2.4.7 No remote | Local-only repo | No GitHub URL | ✅ Handled (null) |
| 2.4.8 File with spaces | `file name.md` | URL-encode for GitHub link | ⚠️ Not encoded |

#### Scenario 2.5: Content Hash Computation

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 2.5.1 Normal content | Storage format string | Compute SHA-256 hash | ✅ Handled |
| 2.5.2 Whitespace changes | Extra spaces/newlines | Normalize before hashing (currently NOT normalized) | ⚠️ May cause unnecessary updates |
| 2.5.3 Empty content | Empty file | Hash of empty string | ✅ Handled |
| 2.5.4 Large content | 1MB+ content | Hash computed (may be slow) | ⚠️ Not tested |

---

### Stage 3: Directory Hierarchy Creation (Phase 2a)

**Purpose**: Create/update directory pages in Confluence to establish parent-child relationships.

#### Scenario 3.1: Directory Page Creation

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 3.1.1 New directory | Directory not in Confluence | Create page under correct parent | ✅ Handled |
| 3.1.2 Existing directory | Directory page exists | Update if content changed, skip otherwise | ✅ Handled |
| 3.1.3 Nested directories | `a/b/c/` hierarchy | Create in order: a, then b, then c | ✅ Sorted by depth |
| 3.1.4 Directory renamed | Old name → new name | Create new page, old page orphaned | ❌ Not handled |
| 3.1.5 Duplicate title exists | Another page with same title | Update existing page OR fail gracefully | ⚠️ May update wrong page |
| 3.1.6 Parent moved | Parent directory moved | Child pages orphaned or moved | ❌ Not handled |
| 3.1.7 Deep nesting | 10+ levels | May hit Confluence limits | ⚠️ Not tested |

#### Scenario 3.2: Parent ID Resolution

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 3.2.1 Normal parent | Parent page exists | Use parent page ID | ✅ Handled |
| 3.2.2 Parent not yet created | Processing out of order | Sorted by depth ensures parent first | ✅ Handled |
| 3.2.3 Root-level directory | Directly under root page | Use root page ID as parent | ✅ Handled |
| 3.2.4 Parent ID from state | Previous sync stored parent_id | Use stored ID | ✅ Handled |
| 3.2.5 Parent ID changed | File moved to different directory | Detect change, update parent | ✅ Now handled |
| 3.2.6 Parent deleted in Confluence | Parent page manually deleted | Find by title or fail | ⚠️ Generic error |

---

### Stage 4: File Sync (Phase 2b - Parallel)

**Purpose**: Sync prepared content to Confluence using parallel API calls.

#### Scenario 4.1: Page Creation

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 4.1.1 New page | No existing page with title | Create page under correct parent | ✅ Handled |
| 4.1.2 Title already exists (same parent) | Page with title exists under parent | Update existing page | ✅ Handled |
| 4.1.3 Title exists (different parent) | Page exists elsewhere | Create new page OR update wrong page | ⚠️ May update wrong |
| 4.1.4 Title with special chars | `Title & <More>` | Escape for Confluence API | ⚠️ Not escaped |
| 4.1.5 Very long title | 255+ characters | May fail Confluence limits | ⚠️ Not truncated |
| 4.1.6 Empty title | No H1, no filename | Use "Untitled" or fail | ⚠️ May fail |

#### Scenario 4.2: Page Update

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 4.2.1 Content changed | Different content hash | Update page body | ✅ Handled |
| 4.2.2 Parent changed | Different parent_id | Move page to new parent | ✅ Now handled |
| 4.2.3 Both changed | Content and parent different | Update both | ✅ Now handled |
| 4.2.4 Nothing changed | Same hash and parent | Skip update | ✅ Handled |
| 4.2.5 Force sync | `force_sync: true` | Update regardless of hash | ✅ Handled |
| 4.2.6 Version conflict | Page updated in Confluence since last sync | Overwrite with our version | ⚠️ No conflict detection |
| 4.2.7 Page deleted | Page ID exists in state but not Confluence | Create new page | ✅ Handled |
| 4.2.8 Page renamed | Title changed in Markdown | Update title on existing page | ⚠️ May create duplicate |

#### Scenario 4.3: Parallel Processing

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 4.3.1 Normal parallel | 5 threads, 100 files | Sync in parallel batches | ✅ Handled |
| 4.3.2 Single file | 1 file to sync | Use single thread | ✅ Handled |
| 4.3.3 Thread failure | One thread errors | Continue others, report error | ✅ Handled |
| 4.3.4 All threads fail | Network down | Report all errors | ⚠️ Generic handling |
| 4.3.5 Rate limiting | 429 Too Many Requests | Retry with backoff | ❌ Not handled |
| 4.3.6 Cache contention | Multiple threads access page_cache | Thread-safe with lock | ⚠️ Not verified |

#### Scenario 4.4: Error Handling

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 4.4.1 API timeout | Request takes > 30s | Timeout error, file marked as error | ✅ Handled |
| 4.4.2 Server error | 500 response | Retry OR mark as error | ⚠️ No retry |
| 4.4.3 Permission denied | 403 response | Mark as error with clear message | ⚠️ Generic message |
| 4.4.4 Invalid content | Malformed storage format | Mark as error with API message | ✅ Handled |
| 4.4.5 Connection reset | Network interruption | Mark as error | ✅ Handled |

---

### Stage 5: State Update & Reporting

**Purpose**: Persist sync state, generate reports, provide summary.

#### Scenario 5.1: State Persistence

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 5.1.1 Normal update | Successful sync | Append entry to JSONL | ✅ Handled |
| 5.1.2 Error during sync | File failed to sync | Don't update state for that file | ✅ Handled |
| 5.1.3 Partial sync | Some files succeeded | Update state for successful files only | ✅ Handled |
| 5.1.4 Write failure | Disk full or permissions | Log warning, continue | ⚠️ State lost |
| 5.1.5 Concurrent write | Multiple syncs running | Append is atomic per line | ⚠️ May interleave |
| 5.1.6 State compaction | Many updates for same file | Only latest entry matters | ✅ JSONL design |

#### Scenario 5.2: Parent ID Tracking

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 5.2.1 Store parent_id | Page synced | Store parent_id in state entry | ✅ Now handled |
| 5.2.2 Parent changed | Different parent_id | Store new and previous parent | ✅ Now handled |
| 5.2.3 No parent | Root-level page | Store null parent_id | ✅ Handled |

#### Scenario 5.3: Report Generation

| Scenario | Input | Expected Behavior | Error Handling |
|----------|-------|-------------------|----------------|
| 5.3.1 Full report | Sync completed | Generate report with all sections | ✅ Handled |
| 5.3.2 Changes section | Created/updated files | Show in "CHANGES" table | ✅ Handled |
| 5.3.3 Skipped section | Unchanged files | Show in "SKIPPED" section | ✅ Handled |
| 5.3.4 Errors section | Failed files | Show in "Errors" section | ✅ Handled |
| 5.3.5 Empty sync | No files to sync | Report with zero counts | ✅ Handled |
| 5.3.6 Large sync | 1000+ files | Report may be very long | ⚠️ Not paginated |
| 5.3.7 Report persistence | Report generated | Save to `data/{dest}/sync-report-{ts}.txt` | ✅ Handled |

---

## Part 3: Change Detection Logic (Detailed)

### Current Detection Algorithm

```
For each file:
1. Compute content_hash of storage format
2. Get previous entry from sync_state
3. IF content_hash == previous.content_hash AND NOT force_sync:
   a. Get current page from Confluence (with ancestors)
   b. Extract current_parent_id from ancestors
   c. IF current_parent_id == expected_parent_id:
      → SKIP (no change)
   d. ELSE:
      → UPDATE (parent changed)
4. ELSE:
   a. Get current page from Confluence (with body.storage, ancestors)
   b. Compare normalized content
   c. Compare parent IDs
   d. IF content unchanged AND parent unchanged:
      → SKIP
   e. ELSE:
      → UPDATE (content and/or parent changed)
```

### What Triggers an Update

| Change Type | Content Hash | Parent ID | Result |
|-------------|-------------|-----------|--------|
| Content changed | Different | Same | UPDATE |
| Parent changed | Same | Different | UPDATE |
| Both changed | Different | Different | UPDATE |
| Neither changed | Same | Same | SKIP |
| Force sync | Any | Any | UPDATE |

### What Is NOT Detected

| Change Type | Detection Status | Impact |
|-------------|-----------------|--------|
| Title change | ❌ Not detected | May create duplicate page |
| File rename | ❌ Not detected | Creates new page, old orphaned |
| File deletion | ❌ Not detected | Confluence page remains |
| Confluence-side edit | ❌ Not detected | Overwritten on next sync |
| Permission change | ❌ Not detected | May fail on update |

---

## Part 4: Recommendations for Implementation

### High Priority Fixes

1. **Handle file/directory renames**: Track by file hash or content signature, not just path.
2. **Handle deletions**: Compare state to discovered files, optionally delete orphaned pages.
3. **Handle title changes**: Include title in change detection logic.
4. **Add rate limiting**: Implement exponential backoff for 429 responses.
5. **Validate duplicate titles**: Warn or fail when duplicate H1 titles detected.

### Medium Priority Improvements

6. **Escape special characters**: Sanitize titles and content for Confluence XML.
7. **Support attachments**: Upload images and link them in content.
8. **Preserve anchors**: Generate Confluence anchors from Markdown headings.
9. **Add conflict detection**: Check version number before update.
10. **Implement retry logic**: Retry failed requests with backoff.

### Low Priority Enhancements

11. **Support front matter**: Parse YAML front matter for metadata.
12. **Support Mermaid**: Convert to Confluence diagram macro or image.
13. **Add ETA to progress**: Calculate estimated time remaining.
14. **Compact state file**: Periodically compact JSONL to remove duplicates.
15. **Add dry-run for delete**: Show what would be deleted.

---

## Part 5: Test Scenarios

### Unit Test Cases

```
test_content_hash_computation()
test_title_extraction_with_h1()
test_title_extraction_without_h1()
test_link_conversion_relative()
test_link_conversion_absolute()
test_link_conversion_parent_directory()
test_ignore_pattern_matching()
test_directory_title_generation()
test_parent_id_change_detection()
```

### Integration Test Cases

```
test_sync_new_destination()
test_sync_with_existing_pages()
test_sync_content_change()
test_sync_parent_change()
test_sync_no_change()
test_sync_force_refresh()
test_sync_parallel_threads()
test_sync_with_errors()
test_sync_large_directory()
```

### End-to-End Test Cases

```
test_full_sync_fresh_destination()
test_incremental_sync_after_edit()
test_sync_with_moved_file()
test_sync_with_deleted_file() [currently fails]
test_sync_with_renamed_directory() [currently fails]
test_sync_resume_after_failure()
```

---

## Appendix: Glossary

| Term | Definition |
|------|------------|
| **Destination** | A Confluence target (space + root page) configured for syncing |
| **Source Folder** | A Git repository folder containing Markdown files |
| **Storage Format** | Confluence's internal XML-like content format |
| **Content Hash** | SHA-256 hash of storage format for change detection |
| **Parent ID** | Confluence page ID of the parent page in hierarchy |
| **Sync State** | JSONL file tracking previous sync information per file |
| **Force Sync** | Option to update a page regardless of change detection |
| **Orphaned Page** | Confluence page whose source file was deleted/moved |

---

*Document Version: 1.0*
*Last Updated: 2026-01-22*
