# Testing Guide for REST API v2 and Native Folders

This document describes the test suite for the Confluence REST API v2 migration and native folder support.

## Test Files

### 1. `test_v2_api_and_folders.py`
Comprehensive unit and integration tests for:
- REST API v2 migration (space ID resolution, API endpoints)
- Folder operations (create, get, delete, update, list children)
- Page operations with v2 (create, update, delete)
- Title conflict handling (no suffixing)
- Hierarchy validation
- Sync state folder tracking
- Orphan handler with v2 and folders
- Pagination helper

### 2. `test_integration_v2_sync.py`
Full integration tests for:
- Complete sync flow with folders and pages
- README handling (as separate pages, not folder content)
- End-to-end sync scenarios

## Running Tests

### Prerequisites

1. Set environment variables:
   ```bash
   export CONFLUENCE_TOKEN="your-api-token"
   export CONFLUENCE_USERNAME="your-email@example.com"  # Optional, can be in .env
   ```

2. Ensure test destination exists in `confluence-destinations.yaml`:
   - Default test destination: `hub-proposal`
   - Or modify test files to use your test destination

### Run All Tests

```bash
# Run comprehensive v2 API and folder tests
cd _confluence_sync/scripts
python3 test_v2_api_and_folders.py

# Run integration tests
python3 test_integration_v2_sync.py
```

### Run Specific Tests

The test files support running individual test functions. You can modify the `main()` function to run only specific tests.

### Dry Run Mode

Some tests can run in dry-run mode (no actual API calls):
```bash
export DRY_RUN=true
python3 test_v2_api_and_folders.py
```

## Test Coverage

### Completed Tests

✅ **REST API v2 Migration**
- Space ID resolution from space key
- API URL uses `/wiki/api/v2`
- All folder operations use v2
- All page operations use v2

✅ **Folder Operations**
- Create folder (with and without parent)
- Get folder by ID
- Delete folder
- Update folder (title, parent)
- List folder children (folders and pages)
- Find folder by title

✅ **Page Operations v2**
- Create page using `create_page_v2`
- Get page using v2 API
- Update page using v2 API
- Delete page using `delete_page_v2`

✅ **Title Conflict Handling**
- No automatic suffixing
- Clear error messages with `TitleConflictError`
- Search for existing pages on conflict

✅ **README Handling**
- README.md files are separate pages
- README pages are under folders (not folder content)
- Multiple README files in nested directories

✅ **Orphan Detection**
- Detects orphaned pages
- Detects orphaned folders
- Deletes orphans using v2 API
- Handles folder hierarchy (children before parents)

✅ **Hierarchy Validation**
- Validates folder hierarchy
- Validates page hierarchy
- Reports hierarchy issues

✅ **Sync State**
- Tracks folders separately from pages
- Folder history methods (append, get, update)
- Load sync state with folders

✅ **Pagination**
- Cursor-based pagination helper
- Handles large result sets

## Test Results

Tests will output:
- ✓ for passed tests
- ✗ for failed tests
- ⚠ for skipped tests (usually due to missing credentials)

A summary is printed at the end showing total passed/failed tests.

## Notes

- Tests create actual Confluence content - use a test space
- Tests clean up created content when possible
- Some tests may leave content if they fail - manual cleanup may be needed
- Tests require valid Confluence credentials and space access

## Troubleshooting

### "CONFLUENCE_TOKEN not set"
Set the environment variable or add it to `.env` file in the `data` directory.

### "Space not found"
Verify the space key in your destination config exists and is accessible.

### "Permission denied"
Ensure your API token has permissions to create/update/delete pages and folders in the test space.

### Tests fail with 404 errors
The test space or root page may not exist. Create them manually or update the test destination config.
