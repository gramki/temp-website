# Accessibility Baseline (v0.1)

Accessibility requirements for all Foundry Web App screens.

## Keyboard and focus

- All interactive elements must be keyboard reachable.
- Focus order must follow visual and logical flow.
- Focus indicators must be clearly visible.

## Semantics

- Use semantic headings and landmarks.
- Lists, tables, and form controls must be properly labeled.
- Icon-only actions require accessible names.

## Color and contrast

- Text and status indicators must meet WCAG contrast targets.
- Do not encode status using color alone; pair with text/icon shape.

## State announcements

- Loading and error states should be communicated to assistive technologies.
- Dynamic updates (for example, status changes) should be announced where needed.

## Minimum audit checklist

- Keyboard-only navigation across major workflow paths
- Focus visibility across all controls
- Empty/loading/error states readable by screen reader
- Status and badges understandable without color perception
