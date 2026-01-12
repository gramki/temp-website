# SFTP Poller

> **Category:** Hub Native Utilities - Signal-Pulling Applications  
> **Status:** ✅ Complete

---

## Overview

**SFTP Poller** is a native Hub application that polls Machine-provided SFTP servers for files and uploads them to Hub Dia SFTP endpoints for processing.

**Purpose:** Enable Machines to emit signals via SFTP when Machines write files to their SFTP servers and Hub needs to pull them.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOMAIN MACHINE                                │
│              (writes files to SFTP server)                       │
│                                                                  │
│  SFTP Server: sftp://batch-files.acme.com:22                    │
│  Path: /outbound/settlements                                    │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Poll (on schedule)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              SFTP POLLER                                          │
│              (Signal-Pulling Application)                        │
│                                                                  │
│  1. Polls Machine SFTP on schedule                              │
│  2. Applies file filters                                        │
│  3. Reads file fully                                            │
│  4. Uploads to Hub Dia SFTP immediately                         │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Upload to Hub Dia SFTP
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              HUB DIA SFTP ENDPOINT                               │
│         (subscription-scoped, per-workbench)                    │
│                                                                  │
│  sftp://dia.olympus.tech:22/inbound/settlements/                │
│  payment-operations                                              │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Push semantics (file arrival)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              DIA (Signal Provider)                               │
│              (validates, parses, emits signals)                 │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
                   SIGNAL EXCHANGE
```

---

## Configuration

### Machine Instance Configuration

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

### Application Configuration

```yaml
sftp_poller:
  machine_instance_id: "batch-file-system"
  
  # Source: Machine-provided SFTP
  source:
    endpoint: "sftp://batch-files.acme.com:22"
    path: "/outbound/settlements"
    auth:
      type: username_password
      credentials_ref: "vault://secrets/batch-file/sftp-auth"
  
  # Target: Hub Dia SFTP
  target:
    endpoint: "sftp://dia.olympus.tech:22"
    path: "/inbound/settlements/payment-operations"
    auth:
      type: api_key
      credentials_ref: "vault://secrets/hub-dia/sftp-key"
  
  # Polling configuration
  polling:
    schedule: "0 */5 * * * *"  # Every 5 minutes
    file_filters:
      - pattern: "settlement_*.csv"
        min_size: 1024
        max_size: 10485760  # 10MB
        exclude_patterns:
          - "*.tmp"
          - "*.lock"
```

---

## Behavior

### Polling Mechanism

**Key Points:**
- **Polling Schedule**: Specified in pull configuration (cron expression or interval)
- **File Filters**: Applied during poll (pattern matching, size checks)
- **Full Read**: Files are read fully before upload
- **Immediate Upload**: Files are uploaded to Hub Dia SFTP immediately after full read
- **No Validation**: Pull mechanism does not validate files (validation happens at push endpoint)

### File Processing Flow

1. **Poll**: Application polls Machine SFTP according to configured schedule
2. **Filter**: Application applies file filters (pattern, size, exclude patterns)
3. **Read**: Application reads file fully from Machine SFTP
4. **Upload**: Application uploads file to Hub Dia SFTP immediately after full read
5. **Process**: Hub Dia SFTP processes file arrival (push semantics, validates file format)
6. **Emit**: Hub Dia emits signals to Signal Exchange according to file format specification

### File Validation

**Important Notes:**
- **Pull mechanism does not validate files** - it only reads files fully and pushes them
- **File validation happens at the Hub Dia SFTP push endpoint** according to the file format specification
- **Processing of pushed files follows push endpoint configuration** (validation, parsing, signal emission)

### Hub Dia SFTP Endpoint

**Characteristics:**
- **Subscription-Scoped**: Endpoints are subscription-scoped
- **Per-Workbench**: Endpoints are per-workbench
- **Naming Pattern**: `/inbound/{category}/{workbench_id}`
- **Provisioning**: Provisioned by tenant admin or authorized developers

**Example:**
```
sftp://dia.olympus.tech:22/inbound/settlements/payment-operations
```

---

## Error Handling

### Connection Failures

- **Automatic Retry**: Exponential backoff with configurable max retries
- **Reconnection**: Automatic reconnection
- **Alerting**: Automatic alerting for persistent failures

### File Read Failures

- **Retry Logic**: Configurable retry for transient failures
- **Skip on Error**: Option to skip files that fail to read
- **Quarantine**: Failed files can be quarantined for manual inspection

### Upload Failures

- **Retry Logic**: Configurable retry for transient failures
- **Dead-Letter**: Files that fail to upload are sent to dead-letter location
- **Monitoring**: Metrics and logs for upload failures

---

## Observability

| Metric | Description |
|--------|-------------|
| `sftp_poller.files.polled` | Files polled from Machine SFTP |
| `sftp_poller.files.filtered` | Files filtered out by filters |
| `sftp_poller.files.uploaded` | Files uploaded to Hub Dia SFTP |
| `sftp_poller.files.failed` | Files that failed to upload |
| `sftp_poller.poll.duration` | Time taken for each poll operation |

---

## Example Use Cases

1. **Settlement Files**: Poll partner's SFTP for daily settlement files
2. **Batch Processing**: Poll external system's SFTP for batch data files
3. **Reconciliation**: Poll bank's SFTP for reconciliation files

---

## Related Documentation

- [Signal-Pulling Applications](./signal-pulling-applications.md) - Overview
- [Dia File Gateway](../signal-providers/dia-file-gateway.md) - Signal Provider documentation
- [File Format Specification](../signal-providers/dia/file-format-specification.md) - File format schema
- [Machine Registry](../registry-services/machine-registry.md) - Machine configuration
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md) - Complete guide

---

*Status: ✅ Complete*
