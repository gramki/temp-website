# Catalog Services

> **Status:** 🟡 WIP — Design Complete

This document describes the OpenSearch-based catalog for package discovery, search capabilities, and visibility enforcement.

---

## Overview

Catalog Services provides the **discovery layer** for the Marketplace, enabling users to search, browse, and filter packages.

| Attribute | Value |
|-----------|-------|
| **Technology** | OpenSearch |
| **Function** | Index and search package listings |
| **Visibility** | Enforced at query time |
| **Access** | Marketplace Console, CLI |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CATALOG SERVICES                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                      PUBLISHING FLOW                                 │   │
│   │                                                                      │   │
│   │  Package Published → Manifest Extracted → Indexed in OpenSearch     │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                        OPENSEARCH INDEX                              │   │
│   │                                                                      │   │
│   │  ┌─────────────────────────────────────────────────────────────┐    │   │
│   │  │  Package Listings                                            │    │   │
│   │  │  • Package metadata (name, description, version)            │    │   │
│   │  │  • Publisher information                                    │    │   │
│   │  │  • Blueprint contents (types, names)                        │    │   │
│   │  │  • Categories, tags, keywords                               │    │   │
│   │  │  • Visibility controls (for filtering)                      │    │   │
│   │  │  • Timestamps (published, updated)                          │    │   │
│   │  └─────────────────────────────────────────────────────────────┘    │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                       DISCOVERY FLOW                                 │   │
│   │                                                                      │   │
│   │  User Query → Visibility Filter Applied → Search Executed → Results │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Indexing

### What Gets Indexed

When a package is published, the manifest is extracted and indexed:

| Field Category | Indexed Fields |
|----------------|----------------|
| **Identity** | package_id, package_name, version, package_uri |
| **Content** | short_description, long_description, keywords |
| **Blueprints** | blueprint names, types, counts |
| **Publisher** | publisher_id, publisher_name |
| **Categories** | categories, industry_tags, use_cases |
| **Visibility** | visibility_mode, tenant lists, region lists |
| **Timestamps** | published_date, last_updated_date |
| **Status** | status (published, deprecated, withdrawn) |

### Index Structure

```json
{
  "package_id": "dispute-ops-v1.2.0",
  "package_name": "Dispute Operations Suite",
  "version": "1.2.0",
  "short_description": "Complete dispute resolution automation",
  "long_description": "Comprehensive suite including...",
  "keywords": ["disputes", "chargebacks", "resolution"],
  "categories": ["dispute-resolution", "customer-service"],
  "industry_tags": ["financial-services"],
  
  "blueprints": [
    {"name": "dispute-triage", "type": "scenario"},
    {"name": "dispute-resolution", "type": "scenario"}
  ],
  "artifact_types": ["scenario", "tools"],
  
  "publisher_id": "acme-bank-dev",
  "publisher_name": "ACME Bank",
  
  "visibility": {
    "mode": "restricted",
    "tenant_allow_list": ["tenant-partner-bank"],
    "region_allow_list": ["us-east-1", "eu-west-1"]
  },
  
  "published_date": "2026-01-15T10:00:00Z",
  "status": "published"
}
```

---

## Discovery Capabilities

### Search

- **Full-text search** across name, descriptions, keywords
- **Phrase matching** for exact matches
- **Fuzzy matching** for typos

### Filtering

| Filter | Type | Description |
|--------|------|-------------|
| `artifact_types` | Multi-select | Filter by blueprint types (scenario, workbench, etc.) |
| `categories` | Multi-select | Filter by categories |
| `industry_tags` | Multi-select | Filter by industry |
| `publisher` | Single/Multi | Filter by publisher |
| `status` | Single | published, deprecated |

### Sorting

| Sort Option | Description |
|-------------|-------------|
| **Relevancy** | Best match to search query |
| **Recency** | Most recently published first |
| **Name** | Alphabetical by package name |

### Browsing

- Browse by publisher
- Browse by category
- Browse by industry tag

---

## Visibility Enforcement

Visibility controls are enforced at **query time**. Users only see packages they are authorized to access.

### Enforcement Logic

```
1. User requests search/browse
2. Extract user's tenant ID and region
3. Apply visibility filter to query:
   
   SHOW package IF:
     (visibility_mode = "public" 
       AND tenant NOT in tenant_disallow_list
       AND region NOT in region_disallow_list)
     OR
     (visibility_mode = "restricted" 
       AND tenant IN tenant_allow_list
       AND (region_allow_list is empty OR region IN region_allow_list))
     OR
     (visibility_mode = "private"
       AND tenant IN tenant_allow_list)

4. Execute query with visibility filter
5. Return filtered results
```

### Privacy

- Tenant allow/disallow lists are **not visible** to other tenants
- Users cannot determine why a package is not visible
- Region lists use publicly known region identifiers

---

## Package Details

When a user selects a package, Catalog Services provides full details:

### Detail View Contents

| Section | Information |
|---------|-------------|
| **Overview** | Name, version, descriptions, publisher |
| **Blueprints** | List of all blueprints with types |
| **Categories** | Categories, industry tags, keywords |
| **Publisher** | Publisher info, contact, support |
| **Deployment** | Instructions, requirements, prerequisites |
| **Documentation** | Links to docs, screenshots, videos |
| **Version History** | Previous versions, changelogs |

---

## Category/Taxonomy Structure

Marketplace uses a **flat tag-based categorization**:

### Tag Types

| Tag Type | Purpose | Examples |
|----------|---------|----------|
| `categories` | General classification | "customer-service", "fraud-detection" |
| `industry_tags` | Industry-specific | "financial-services", "healthcare" |
| `keywords` | Search discoverability | "disputes", "chargebacks" |
| `use_cases` | Specific applications | "dispute-resolution", "loan-processing" |

### Characteristics

- **Free-form** — Publishers can assign any tags
- **No validation** — No predefined taxonomy (v1)
- **All indexed** — All tags searchable and filterable
- **UI suggestions** — Marketplace Console may suggest common tags

---

## API Operations

### Search

```
GET /marketplace/catalog/search
  ?q={query}
  &artifact_types={types}
  &categories={categories}
  &publisher={publisher_id}
  &sort={relevancy|recency}
  &page={page}
  &limit={limit}
```

### Browse

```
GET /marketplace/catalog/browse/publishers
GET /marketplace/catalog/browse/categories
GET /marketplace/catalog/browse/industries
```

### Package Details

```
GET /marketplace/catalog/packages/{package_id}
GET /marketplace/catalog/packages/{package_id}/versions
```

---

## Related Documentation

- [Blueprints and Packages](./blueprints-and-packages.md) — Package model
- [Publishing Services](./publishing-services.md) — How packages are indexed
- [Marketplace Console](../../06-ux-architecture/tenant-domain/marketplace-console.md) — UI for discovery
- [ADR-0098: Visibility Controls](../../decision-logs/0098-visibility-controls-private-marketplace.md)

