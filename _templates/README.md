# Documentation Templates

This folder contains templates for common documentation types in the design-docs repository.

## Usage

1. Copy the appropriate template to your target location
2. Rename it appropriately
3. Fill in all sections (mark as "TBD" if incomplete)
4. Remove template instructions (text in `<!-- comments -->`)

## Available Templates

| Template | Purpose | When to Use |
|----------|---------|-------------|
| [subsystem-readme.md](subsystem-readme.md) | Subsystem overview | Creating a new subsystem folder |
| [component-detail.md](component-detail.md) | Detailed component docs | Documenting a specific component within a subsystem |
| [guide.md](guide.md) | How-to guides | Step-by-step instructions for tasks |
| [adr.md](adr.md) | Architecture Decision Record | Capturing significant design decisions |
| [composite-pattern.md](composite-pattern.md) | Composite pattern documentation | Documenting patterns that compose Hub components |
| [open-points.md](open-points.md) | Open questions tracker | Tracking unresolved questions per subsystem |
| [operator.md](operator.md) | Operator documentation | Documenting Hub operators and CRDs |

## Template Maintenance

Templates should be updated when:
- Common patterns emerge that aren't captured
- Sections are consistently skipped (reconsider if needed)
- New document types are introduced

## Contributing

When improving templates:
1. Review existing documents that use the template
2. Identify missing or redundant sections
3. Update template with clear instructions
4. Update this README if adding new templates

