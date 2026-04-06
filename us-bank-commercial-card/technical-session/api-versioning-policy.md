# API Versioning and Lifecycle Policy

## Versioning Scheme

Every API endpoint is versioned independently using the URL path:

```
/v1/resource
/v2/resource
```

Each version of an endpoint operates as a distinct contract. Introducing a new version (`v2`) does not alter or retire the previous version (`v1`). Both coexist and are maintained according to their respective lifecycle stage.

## Compatibility Contract

Within a given version, request and response bodies may be extended with **optional** or **conditional** attributes at any time. These additions are non-breaking and do not trigger a new version.

Clients must implement the **tolerant reader** pattern:

- Ignore unrecognized fields in response bodies.
- Do not fail on the presence of additional data.
- Do not depend on field ordering.

This contract allows the platform to evolve APIs continuously — adding capabilities, enriching responses, and introducing optional parameters — without disrupting existing integrations.

## What Triggers a New Version

A new version is introduced only when a **breaking change** is required:

- Removing or renaming an existing field.
- Changing the data type or semantics of an existing field.
- Restructuring the request or response payload.
- Altering authentication or authorization requirements for the endpoint.
- Changing error response structures in ways that affect client handling.

Non-breaking changes — adding optional fields, introducing new query parameters with defaults, extending enumerations — are absorbed into the current version.

## Version Lifecycle

Every API version moves through a defined lifecycle:

| Stage | Visibility | Behavior | Duration |
|---|---|---|---|
| **Active** | Publicly listed on the developer portal | Fully supported; receives non-breaking enhancements | Indefinite |
| **Deprecated** | Publicly listed with deprecation notice | Fully functional; no new features | Minimum 6 months |
| **Unlisted** | Removed from public documentation | Fully functional for existing consumers by arrangement | By agreement |
| **Retired** | Not available | Endpoint returns errors | Permanent |

### Active

The version is publicly documented, fully supported, and receives non-breaking enhancements. This is the default state for all versions.

### Deprecated

A version enters deprecation when a successor version is available and the older version is scheduled for eventual retirement. During this stage:

- The API continues to function identically. No degradation in behavior or performance.
- The deprecation window is **at minimum 6 months** from the date of the deprecation announcement.
- Clients are notified via **email** and **release notes on the developer portal**.
- A **migration guide** is published, detailing the differences between the deprecated version and its successor, along with recommended steps for transition.

Older versions frequently remain active well beyond the minimum deprecation window. The goal is orderly migration, not forced cutover.

### Unlisted

After the public deprecation window closes, a version may transition to unlisted status rather than immediate retirement. In this state:

- The API is removed from public developer portal documentation.
- It remains fully operational for specific consumers who need additional time to migrate.
- Continued support is managed by arrangement between the platform and the consuming organization.

This stage exists to accommodate real-world migration timelines without holding back portal clarity.

### Retired

A version is retired only after all known consumers have migrated. The endpoint ceases to function and returns appropriate error responses.

## Migration Support

When a new version is introduced, the following are provided:

- **Migration guide** — a document describing what changed, why, and how to update client implementations.
- **Changelog** — a detailed list of additions, modifications, and removals between versions.
- **Deprecation timeline** — the date deprecation begins and the earliest date retirement could occur.

## Quality Assurance

All public API versions are covered by automated regression suites. These suites validate contract compliance, response correctness, and backward compatibility for every supported version across releases.

## Summary

| Principle | Policy |
|---|---|
| Versioning granularity | Per endpoint |
| Version location | URL path (`/v1/...`, `/v2/...`) |
| Non-breaking changes | Absorbed into current version |
| Breaking changes | New version required |
| Client obligation | Tolerant reader pattern |
| Deprecation notice | Email + developer portal release notes |
| Minimum deprecation window | 6 months |
| Extended support | Available by arrangement (unlisted) |
| Migration support | Guide + changelog provided |
| Regression coverage | All public API versions |
