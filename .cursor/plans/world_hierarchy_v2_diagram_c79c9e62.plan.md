---
name: World Hierarchy V2 Diagram
overview: Build a new interactive SVG diagram (world-hierarchy-v2.html) that uses a tree data model with recursive rendering, bidirectional drill-down/zoom-out navigation via clickable boxes + Prev/Next buttons + breadcrumb, where every entity from World down to Deployment is a typed, colored, labeled box.
todos:
  - id: data-model
    content: Define ENTITY_TYPES color map and the full world tree data structure with all nodes down to Deployment
    status: completed
  - id: layout-engine
    content: Build renderNode() recursive renderer with ancestor-context / focus / children rendering zones and grid layout algorithm
    status: completed
  - id: navigation
    content: Implement focusPath state, breadcrumb bar, clickable child boxes, Prev/Next/Restart buttons, and depth dots
    status: completed
  - id: legend-labels
    content: Auto-generate legend from visible entity types and render step title/description from focused node
    status: completed
  - id: styling
    content: CSS for card layout, breadcrumb pills, hover states on clickable boxes, fade transitions, and responsive sizing
    status: completed
  - id: browser-test-initial
    content: Open world-hierarchy-v2.html in browser, take screenshot of initial render (World level), verify layout and colors are correct
    status: completed
  - id: browser-test-drilldown
    content: Test full drill-down path World > Site > Zone > Enclave > Space > DeploymentCloud > Deployment using click navigation, screenshot at each level, fix any rendering or layout issues found
    status: completed
  - id: browser-test-breadcrumb
    content: Test breadcrumb navigation -- click ancestor segments to jump back multiple levels, verify state and rendering update correctly
    status: completed
  - id: browser-test-buttons
    content: Test Prev/Next/Restart buttons at various depths, verify disabled states at root and leaf levels
    status: completed
  - id: browser-fix-iterate
    content: Fix any visual issues found during testing (overlapping text, clipped boxes, misaligned grids, unreadable labels, broken click targets) and re-test until clean
    status: completed
isProject: false
---

# World Hierarchy V2 -- Composable Tree Diagram

## Target file

`personal-projects/olympus-diagrams/world-hierarchy-v2.html` (new file, preserves the existing v1).

---

## 1. Data Model

A single `world` tree object. Every node has `{ type, name, children? }`.

Full hierarchy (bottom-up composition order):

```
Deployment  <  DeploymentCloud  <  Space  <  Enclave  <  Zone  <  Site  <  World
```

### Instance tree to build

- **World**
  - **Site: US East**
    - **Zone: Zone 1**
      - **Enclave: Prod**
        - **Space: General** -- 2 Deployment Clouds, each with 3 Deployments
        - **Space: PCI** -- 2 Deployment Clouds, each with 3 Deployments
        - **Space: Analytics** -- 2 Deployment Clouds, each with 3 Deployments
      - **Enclave: UAT**
        - Same 3 spaces (General, PCI, Analytics), same depth
      - **Space: Admin** -- 2 Deployment Clouds, each with 3 Deployments (same structure as other spaces, per user confirmation)
      - Zone 2 (collapsed placeholder, "(same structure)")

### Entity type styling

Each type gets a fixed color palette used everywhere:

- **World** -- `fill: #E6F1FB, stroke: #378ADD` (blue)
- **Site** -- `fill: #E1F5EE, stroke: #1D9E75` (teal)
- **Zone** -- `fill: #EEEDFE, stroke: #534AB7` (purple)
- **Enclave** -- `fill: #EAF3DE, stroke: #639922` (green)
- **Space: General** -- `fill: #C0DD97, stroke: #639922`
- **Space: PCI** -- `fill: #97C459, stroke: #3B6D11` (darker green)
- **Space: Analytics** -- `fill: #C0DD97, stroke: #639922`
- **Space: Admin** -- `fill: #FAEEDA, stroke: #BA7517` (amber)
- **DeploymentCloud** -- `fill: #DBEAFE, stroke: #2563EB` (bright blue)
- **Deployment** -- `fill: #F0E6FF, stroke: #7C3AED` (violet)

Every rendered box shows two text lines: the type name (bold, smaller) and the entity name.

---

## 2. Rendering Engine

### 2a. Focus-depth model

State:

```javascript
let focusPath = [0]; // indices into children at each depth
// focusPath = [0]       -> World focused, Sites as children
// focusPath = [0, 0]    -> Site "US East" focused, Zones as children
// focusPath = [0, 0, 0] -> Zone "Zone 1" focused, Enclaves+Admin as children
// ... and so on down to DeploymentCloud showing Deployments
```

The `focusPath` length determines what is expanded.

### 2b. Three rendering zones on the SVG canvas

```
 ┌──────────────────────────────────────────────┐
 │  ANCESTOR CONTEXT (thin nested borders)      │
 │  World > Site: US East > Zone: Zone 1        │
 │  ┌────────────────────────────────────────┐  │
 │  │  FOCUS LEVEL (full render, all children│  │
 │  │  laid out as a grid/flow)              │  │
 │  │                                        │  │
 │  │  ┌─────┐ ┌─────┐ ┌─────┐              │  │
 │  │  │child│ │child│ │child│  ...          │  │
 │  │  └─────┘ └─────┘ └─────┘              │  │
 │  └────────────────────────────────────────┘  │
 └──────────────────────────────────────────────┘
```

- **Above focus depth**: Each ancestor renders as a thin, dashed border with its type+name label. These nest visually to show containment.
- **At focus depth**: The focused node renders fully -- its container plus all direct children as colored boxes in a grid layout.
- **Children at focus depth**: Rendered as compact labeled boxes (type + name, colored by type). Clickable to drill down.
- **Below focus depth** (grandchildren and deeper): Not rendered -- they appear when you drill into a child.

### 2c. `renderNode()` recursive function

```
renderNode(node, depth, x, y, availW, availH) -> SVGElements[]
```

- If `depth < focusPath.length`: render as context border, recurse into `children[focusPath[depth]]` only
- If `depth === focusPath.length`: render fully with all children laid out in a flow grid
- Children laid out using a simple algorithm:
  - Horizontal flow with wrapping
  - Each child box: fixed aspect ratio, sized to fit `availW / cols`
  - Padding and gaps defined per depth level

### 2d. Child layout algorithm

At the focus level, children are laid out in a responsive grid:

- Compute `cols` based on child count (2-4 columns depending on count)
- Each child gets equal width, height computed from content
- Gap: 12px horizontal, 10px vertical
- Padding inside focus container: 16px

---

## 3. Navigation

### 3a. Breadcrumb bar (top of card)

Rendered as clickable text spans:

```
World  >  Site: US East  >  Zone: Zone 1  >  Enclave: Prod
```

- Each segment is clickable -- clicking truncates `focusPath` to that depth (zoom out)
- Current (deepest) segment is bold, not clickable
- Styled as small pill-shaped links

### 3b. Clickable child boxes

- Each child box at the focus level is clickable
- Clicking a child appends its index to `focusPath` (drill down)
- Cursor changes to pointer on hover; subtle hover highlight

### 3c. Prev / Next buttons

- **Next**: If children exist at current focus, drill into the first child (same as clicking it). At leaf level, disabled.
- **Prev**: Zoom out one level (pop last element of `focusPath`). At root, disabled.
- Also keep the "Restart" button to reset `focusPath = [0]`

### 3d. Step indicator dots

Replace the linear dots with depth-based dots -- one dot per hierarchy level (7 total: World through Deployment). The active dot indicates the current focus depth.

---

## 4. Legend

Auto-generated from the entity types visible at the current focus level + its children. Updates on every navigation. Uses the same color swatches as v1.

---

## 5. Transitions

- On drill-down/zoom-out, use a simple CSS `opacity` fade (0.15s) on the SVG container to smooth the transition.
- No complex animations needed -- clarity over flash.

---

## 6. HTML Structure

Same card-based layout as v1, adapted:

```html
<div class="card">
  <div class="breadcrumb" id="breadcrumb"></div>   <!-- new -->
  <div class="step-label">
    <h2 id="stitle"></h2>
    <p id="sdesc"></p>
  </div>
  <div class="depth-dots" id="dots"></div>
  <div id="canvas"></div>
  <div class="legend" id="legend"></div>
  <div class="controls">
    <button id="bp">Prev (zoom out)</button>
    <button id="bn">Next (drill in)</button>
    <button id="br">Restart</button>
  </div>
</div>
```

---

## 7. Browser Testing and Fix Loop

After initial build, open the file in the browser and systematically verify:

### 7a. Initial render check

- Open `world-hierarchy-v2.html` in browser
- Screenshot the World-level view
- Verify: card layout renders, breadcrumb shows "World", depth dots show 7 levels with first active, legend shows World + Site types, child boxes (Sites) are visible and colored correctly, type label + name visible on every box

### 7b. Full drill-down test (click navigation)

- Click each child box to drill down, one level at a time:
  - World -> Site: US East -> Zone: Zone 1 -> Enclave: Prod -> Space: General -> DeploymentCloud: AWS us-east-2 -> (leaf: Deployments visible)
- At each level, screenshot and verify:
  - Ancestor context borders render correctly (nested, dashed, labeled)
  - Focused node shows all children as a grid
  - Breadcrumb updates with correct path
  - Depth dots update
  - Legend updates to show current + child types
  - Box labels (type + name) are readable and not clipped

### 7c. Breadcrumb jump test

- From a deep level (e.g. DeploymentCloud), click "Zone: Zone 1" in breadcrumb
- Verify it jumps back to Zone level correctly (not just one step)
- Click "World" in breadcrumb to verify full reset

### 7d. Button navigation test

- At root: Prev should be disabled, Next should drill into first child
- At leaf (Deployment level): Next should be disabled
- Restart should reset to World level from any depth

### 7e. Fix loop

- For any issues found (overlapping text, clipped boxes, broken click targets, wrong colors, layout overflow, unreadable labels at small sizes):
  - Fix the code
  - Reload in browser
  - Re-verify the specific issue and surrounding functionality
- Repeat until all navigation paths work cleanly

---

## 8. Key differences from v1

- No hardcoded SVG strings -- everything generated from the tree
- Bidirectional navigation (drill down + zoom out + breadcrumb jump)
- Clickable boxes for direct drill-down
- All 7 hierarchy levels rendered, down to individual Deployments
- Admin Space has full children (Deployment Clouds + Deployments)
- Every box labeled with type + name, colored by type
- Single file, zero dependencies, vanilla HTML/CSS/JS

