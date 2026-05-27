# Debugging image and Mermaid attachment failures (Confluence sync)

Symptoms: Confluence pages show broken images, empty diagram areas, or `ri:attachment` references that do not resolve — for example [Purpose, Audience, and Scope](https://zeta-tm.atlassian.net/wiki/spaces/CTO/pages/4891410687/01+-+Purpose+Audience+and+Scope) after sync.

## State diagrams: garbled top row / literal `\n` in labels

In **`stateDiagram-v2`**, a one-line note such as `note right of S : a;b;c` is parsed as **multiple statements** because **`;` ends a statement**. You get a row of junk “nodes” at the top and a broken layout. **Fix:** use `note right of S` … `end note` (see USER-GUIDE). Transition labels should use **`<br/>`** for line breaks, not `\n` in the Markdown file.

## Blank Mermaid PNGs (pip `mmdc` / PhantomJS)

The PyPI package **`mmdc`** (PhantomJS) often produces **empty or all-white PNGs** for valid modern Mermaid (nested `subgraph`, `style`, HTML in labels). Confluence then shows a white box. **Fix:** use Node **`@mermaid-js/mermaid-cli`** — install globally (`npm i -g @mermaid-js/mermaid-cli`) or ensure **`npx`** is available; the sync tries `mmdc` on PATH first, then `npx -y @mermaid-js/mermaid-cli`. After fixing tooling, delete `_confluence_sync/data/mermaid-cache/` once so bad cached blanks are not reused (newer sync also drops cache entries that fail a visible-ink check).

## Local Mermaid PNG cache

Rendered diagrams are stored on disk under **`_confluence_sync/data/mermaid-cache/`** as **`<sha256>.png`** (hash of the exact Mermaid source). The sync run prints `Mermaid PNG cache: …` in the banner. This speeds repeat syncs and lets you open PNGs locally. Remove a file or the whole directory to invalidate. The directory is gitignored by default (`_confluence_sync/data/mermaid-cache/` in repo `.gitignore`).

## How images get onto pages

1. **Markdown → storage**: Local images and rendered Mermaid diagrams become Confluence storage that references attachments by filename (e.g. `<ri:attachment ri:filename="mermaid-0.png"/>` inside an `ac:image` macro).
2. **Phase 2b**: Page body is created/updated in Confluence.
3. **Phase 2c**: The sync uploads files to that page via REST:  
   `PUT/POST {base}/rest/api/content/{pageId}/child/attachment`  
   (see [Confluence REST: Content — attachments](https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content---attachments/)).

If step 3 fails, the page **already points at** attachments that were never stored (or were not updated), so images break.

## Frequent cause: `400 Bad Request` on second and later syncs

**Confluence behavior**

- **POST** `.../child/attachment` — **create only**. If an attachment with the same name already exists on the page, the API can respond with **400 Bad Request**.
- **PUT** `.../child/attachment` — **create or update** (new version if the name already exists).

The sync tool uses **PUT** for uploads so re-syncs refresh `mermaid-*.png` and other files instead of failing on duplicates.

If you still see POST-style errors in old logs, upgrade to the version of `attachment_handler.py` that uses PUT.

## What to check in sync output

1. **`[Phase 2c] Uploading attachments...`**
   - `✓ Uploaded: mermaid-0.png` — upload succeeded for that page.
   - `⚠ Warning: Could not upload attachment ... 400` — read the **next line** if present: the handler logs a snippet of the API response body (Atlassian often returns JSON with a message).
2. **Page skipped as unchanged** (`no-change-skipped`): the body is not re-sent, but Phase 2c may still run uploads. With PUT, duplicates should update; if uploads fail, diagrams can still be missing from an **earlier** failed run — use `--force-update` once after fixing upload issues so bodies and attachments align.

## Other causes

| Symptom / clue | Things to verify |
|----------------|------------------|
| All Mermaid images missing | `mmdc` or Python `mmdc` package available so PNGs are generated; otherwise placeholders are synced with no binary. |
| `401` / `403` | `CONFLUENCE_TOKEN` and user can **write** attachments in the target space. |
| Very large PNG | Space/site attachment size limits; try simplifying diagrams. |
| Wrong `pageId` | Rare; would usually break the whole page update, not only attachments. |
| Fabric / editor | If Atlassian changes attachment rules for certain page types, API error body in logs is the source of truth. |

## Manual verification in Confluence

1. Open the page → **•••** → **Attachments** (or page tools): confirm `mermaid-0.png` (and friends) exist.
2. If missing, run sync again from `_confluence_sync`:  
   `python3 run-sync-with-env.py --destination <id> --force-update`  
   (optional: scope with `--folder` if you only need one subtree).
3. Compare **page last updated** vs **attachment** timestamps.

## Quick local checks

```bash
# From repo root — ensure Mermaid can render (if you use Mermaid blocks)
cd _confluence_sync/scripts && ./venv/bin/python -c "from mmdc import MermaidConverter; print('mmdc ok')"

# Dry run (no uploads) still prepares content; use full sync to test attachments
cd _confluence_sync && python3 run-sync-with-env.py --destination corporate-payments-book-cto --dry-run
```

## References

- [Confluence Cloud REST v1 — Content attachments](https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-content---attachments/) (POST vs PUT).
- Main user guide: [USER-GUIDE.md](./USER-GUIDE.md) (Troubleshooting section).
