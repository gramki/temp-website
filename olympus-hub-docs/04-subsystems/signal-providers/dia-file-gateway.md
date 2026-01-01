# Dia - File Gateway

Dia is the I/O Gateway for **File signals**—batch inputs, document uploads, and file-based integrations. As Olympus's Object and File Store as a Service, Dia provides pluggable storage backends supporting multiple protocols.

> **Olympus Academy:** [Dia Documentation](https://dia.olympus.tech/)

## Overview

| Attribute | Value |
|-----------|-------|
| **Signal Type** | Files, Batch inputs |
| **Protocol** | HTTP, SFTP, FTP, WebDAV |
| **Direction** | Inbound (file arrival) and Outbound (file generation) |
| **Role** | Senses file arrivals, executes Triggers, creates Requests |

## Key Concepts (from Olympus Academy)

| Concept | Description |
|---------|-------------|
| **DiaStorage** | Resource declaration for storage provisioned through Fang pipeline |
| **Tags** | Key-value labels assigned to files/folders for flexible organization and retrieval |
| **Smart Folder** | Dynamic folders that automatically gather files based on search criteria |
| **File Plugin** | Self-serve framework for viewing file details and processor-specific actions |

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Batch Processing** | Daily/periodic file feeds from partners |
| **Reconciliation** | Statement files, settlement files |
| **Bulk Operations** | Mass updates, bulk imports |
| **Document Intake** | Scanned documents, attachments |
| **Report Distribution** | Generated reports, exports |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FILE SOURCES                          │
│   (SFTP servers, S3 buckets, Partner uploads, Scans)    │
└────────────────────────┬────────────────────────────────┘
                         │ Files
                         ▼
┌─────────────────────────────────────────────────────────┐
│                        DIA                               │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ File        │  │ Trigger     │  │ Request     │      │
│  │ Watcher     │→ │ Executor    │→ │ Publisher   │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                          │
│  File Sources:                                           │
│  • SFTP/FTP drop locations                              │
│  • S3/Azure Blob/GCS object notifications               │
│  • HTTP multipart uploads                               │
│  • Email attachments                                     │
└────────────────────────┬────────────────────────────────┘
                         │ Request (+ file reference)
                         ▼
                   OPERATIONS CENTER
```

## Signal Processing Modes

### Single-File Mode
Each file becomes one Request:

```
File arrival → Trigger → Single Request
```

### Batch-Split Mode
File is parsed, each record becomes a Request:

```
File arrival → Parse → Trigger per record → Multiple Requests
```

### Aggregate Mode
Multiple files aggregated into one Request:

```
Multiple files → Wait for complete set → Trigger → Single Request
```

## Trigger Configuration

```yaml
# Example: Single-file Trigger
trigger:
  name: "daily-settlement-file"
  gateway: dia
  
  # File matching
  filter:
    source: "sftp://partner.example.com/outbound"
    pattern: "settlement_*.csv"
    schedule: "0 6 * * *"  # Expected at 6 AM
  
  # File validation
  validation:
    format: CSV
    required_headers: ["transaction_id", "amount", "status"]
    max_size: "100MB"
  
  # Transformation
  transform:
    request_type: "SettlementFileProcessing"
    mapping:
      file_name: "$.file.name"
      file_size: "$.file.size"
      record_count: "$.file.line_count"
      file_reference: "$.file.storage_url"
  
  # Target
  target:
    workbench: "settlement-operations"
    scenario: "daily-settlement"
```

```yaml
# Example: Batch-split Trigger
trigger:
  name: "bulk-customer-update"
  gateway: dia
  
  # File matching
  filter:
    source: "s3://company-uploads/customer-updates/"
    pattern: "customer_update_*.json"
  
  # Parsing
  parse:
    format: JSONL  # JSON Lines
    record_path: "$"  # Each line is a record
  
  # Per-record transformation
  transform:
    request_type: "CustomerUpdateRequest"
    mapping:
      customer_id: "$.record.customer_id"
      updates: "$.record.changes"
      batch_id: "$.file.batch_id"
      record_index: "$.record.index"
  
  # Target
  target:
    workbench: "customer-operations"
    scenario: "customer-update"
```

## Capabilities

### Protocol Support (Olympus Dia)
| Protocol | Capability |
|----------|------------|
| **HTTP** | RESTful file upload/download |
| **SFTP** | Secure file transfer protocol |
| **FTP** | File transfer protocol |
| **WebDAV** | Web-based file access |

### Storage Backend Support
| Backend | Capability |
|---------|------------|
| **Object Store** | Pluggable backend storage |
| **Smart Folders** | Dynamic file organization by criteria |
| **Tagging** | Key-value metadata for files and folders |

### File Parsing
| Format | Support |
|--------|---------|
| **CSV/TSV** | Header detection, custom delimiters |
| **JSON/JSONL** | JSON objects, JSON Lines |
| **XML** | XPath-based record extraction |
| **Fixed-width** | Position-based parsing |
| **Excel** | .xlsx, .xls parsing |
| **PDF** | Text extraction, OCR integration |

### File Lifecycle
- **Staging**: Temporary storage during processing
- **Archival**: Move to archive after processing
- **Retention**: Configurable retention policies
- **Cleanup**: Automatic cleanup of processed files

### Error Handling
- **Quarantine**: Invalid files moved to quarantine
- **Partial Processing**: Process valid records, report failures
- **Retry**: Configurable retry for transient failures

## Integration with Fang Pipeline

Dia integrates with the Olympus Fang pipeline for storage provisioning:
- Publishers declare DiaStorage resource requirements
- Provisioned automatically through CI/CD pipeline
- Consistent storage configuration across environments

## Authentication

Dia ensures resources are accessible only to authorized users/applications:
- Integration with Cipher IAM
- Per-file/folder access controls
- Protocol-level authentication (SFTP keys, HTTP tokens)

## Observability

| Metric | Description |
|--------|-------------|
| `dia.files.received` | Total files received |
| `dia.files.parsed` | Files successfully parsed |
| `dia.files.quarantined` | Files sent to quarantine |
| `dia.records.processed` | Records processed (batch-split) |
| `dia.requests.created` | Requests created |

## Related Documentation

- [Olympus Academy - Dia](https://dia.olympus.tech/)
- [Hub Architecture - Signals](../../02-system-design/hub-architecture.md#13-signals)
- [Hub Architecture - Triggers](../../02-system-design/hub-architecture.md#14-triggers)
- [Ontology - Signal](../../01-concepts/ontology-reference.md#signal)

---

*Status: 🟡 WIP - Definition phase*

