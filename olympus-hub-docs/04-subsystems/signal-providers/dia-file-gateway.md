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

## Machine Signal Emission via SFTP

Machines can emit signals through Dia using **SFTP** in two models: **push** (Machine uploads to Hub Dia SFTP) and **pull** (Hub polls Machine SFTP and uploads to Hub Dia SFTP).

### Push Model: Machine Uploads to Hub Dia SFTP

**Flow:** Machine uploads file to Hub Dia SFTP endpoint → Dia detects file arrival → Dia validates file format → Dia emits signals to Signal Exchange

**Configuration:**
- Machine uploads files via SFTP to Hub Dia SFTP server endpoint
- Files must conform to the file format specification defined in Machine Definition
- Dia validates file format upon arrival
- Dia parses file and emits signals (one per row if configured)

**Example Machine Configuration:**
```yaml
machine:
  id: "settlement-file-system"
  signal_emission:
    push:
      sftp:
        # Hub Dia SFTP server endpoint
        server_endpoint: "sftp://dia.olympus.tech:22"
        
        # Target folder path on Hub Dia SFTP server (workbench-scoped)
        folder_path: "/inbound/settlements/{workbench_id}"
        
        # Authentication for Hub Dia SFTP
        auth:
          type: api_key
          credentials_ref: "vault://secrets/settlement-files/dia-sftp-key"
        
        # File naming pattern (optional)
        file_pattern: "settlement_*.csv"
```

**File Format Specification:**
Files must conform to the format specification defined in Machine Definition. See [File Format Specification](./dia/file-format-specification.md) for complete schema definition.

**Example File Format Configuration:**
```yaml
machine_definition:
  id: "settlement-file-system"
  signal_emission:
    signals:
      - type: "settlement.file.ready"
        push:
          protocols: [sftp]
          schemas:
            sftp:
              file_format_spec:
                name: "settlement-file-v1"
                format: "csv"
                encoding: "utf-8"
                dialect:
                  delimiter: ","
                  quote: '"'
                structure:
                  header:
                    rows: 1
                    validation:
                      required: true
                      fields:
                        - name: "file_type"
                          position: 0
                          type: "string"
                          constraints:
                            enum: ["SETTLEMENT"]
                  body:
                    startRow: 2
                    schema:
                      fields:
                        - name: "transaction_id"
                          position: 0
                          type: "string"
                        - name: "amount"
                          position: 1
                          type: "decimal"
                  footer:
                    rows: 1
                    validation:
                      required: true
```

**Flow:**
1. Machine uploads file to Hub Dia SFTP: `sftp://dia.olympus.tech:22`
2. Machine uploads to folder path: `/inbound/settlements/payment-operations`
3. Hub Dia detects file arrival
4. Hub Dia validates file format according to specification
5. Hub Dia parses file and emits signals to Signal Exchange (one signal per row if `perRow: true`)
6. Signal Exchange processes as normal push signals

### Pull Model: Hub Polls Machine SFTP

**Flow:** Hub polls Machine SFTP for files → Hub reads file fully → Hub uploads to Hub Dia SFTP → Dia processes file arrival (push semantics)

**Configuration:**
- Machine provides SFTP server endpoint and source path
- Hub uses signal-pulling application (SFTP Poller) to poll Machine SFTP
- Hub uploads pulled files to Hub Dia SFTP endpoint
- Files are processed according to push endpoint configuration

**Example Machine Configuration:**
```yaml
machine:
  id: "batch-file-system"
  signal_emission:
    pull:
      sftp:
        # Machine-provided SFTP server
        machine_sftp:
          endpoint: "sftp://batch-files.acme.com:22"
          path: "/outbound/settlements"
          auth:
            type: username_password
            credentials_ref: "vault://secrets/batch-file/sftp-auth"
        
        # Hub Dia SFTP endpoint (subscription-scoped, per-workbench)
        hub_sftp:
          endpoint: "sftp://dia.olympus.tech:22"
          path: "/inbound/settlements/{workbench_id}"
          auth:
            type: api_key
            credentials_ref: "vault://secrets/hub-dia/sftp-key"
        
        # Polling configuration
        polling:
          schedule: "0 */5 * * * *"  # Every 5 minutes (cron format)
          file_filters:
            - pattern: "settlement_*.csv"
              min_size: 1024  # Minimum file size in bytes
```

**Flow:**
1. Hub connects to Machine-provided SFTP: `sftp://batch-files.acme.com:22`
2. Hub polls Machine SFTP path: `/outbound/settlements` according to configured schedule
3. Hub applies file filters during poll (pattern matching, size checks)
4. Hub reads file fully from Machine SFTP
5. Hub uploads pulled file to Hub Dia SFTP endpoint: `sftp://dia.olympus.tech:22/inbound/settlements/payment-operations` (immediately after full read)
6. Hub Dia SFTP endpoint processes file arrival (push semantics, validates file format)
7. Signal Exchange processes as normal push signals

**Important Notes:**
- **Pull mechanism does not validate files** - it only reads files fully and pushes them
- **File validation happens at the Hub Dia SFTP push endpoint** according to the file format specification
- **Processing of pushed files follows push endpoint configuration** (validation, parsing, signal emission)

### File Format Specification

The file format specification follows the schema defined in [File Format Specification](./dia/file-format-specification.md), which supports:
- **Format Types**: CSV, TSV, Fixed-Width
- **Structure**: Header, Body, Footer sections
- **Validation**: Pattern matching, field validation, cross-validation
- **Integrity Checks**: File size, hash, row count, column count
- **Output**: JSON per-row format with metadata

For detailed file format specifications, see [File Format Specification](./dia/file-format-specification.md).

For detailed configuration, see [Machine Registry](../registry-services/machine-registry.md) and [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md).

## Related Documentation

- [Olympus Academy - Dia](https://dia.olympus.tech/)
- [File Format Specification](./dia/file-format-specification.md) - Complete schema definition for CSV/TSV/Fixed-Width file formats
- [Hub Architecture - Signals](../../02-system-design/hub-architecture.md#13-signals)
- [Hub Architecture - Triggers](../../02-system-design/hub-architecture.md#14-triggers)
- [Ontology - Signal](../../01-concepts/ontology-reference.md#signal)
- [Machine Registry](../registry-services/machine-registry.md)
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md)

---

*Status: 🟡 WIP - Definition phase*

