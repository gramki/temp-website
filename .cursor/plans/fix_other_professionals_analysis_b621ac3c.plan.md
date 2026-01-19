---
name: Fix Other Professionals Analysis
overview: Expand Legal, Accounting, and Consulting/Creative scenario documents to match the comprehensive Healthcare standard (29 scenarios, 14 journey types, full alternatives/insights, priority matrix).
todos:
  - id: legal-expand
    content: "Expand r2.3-legal-practice.md: Add ~15-17 vertical-specific scenarios (Journey Types 1-10) with alternatives and insights"
    status: completed
  - id: legal-banking
    content: Add 12 banking scenarios (Journey Types 11-14) to r2.3-legal-practice.md with alternatives and insights
    status: completed
  - id: legal-summary
    content: Add summary sections to r2.3-legal-practice.md (tables, statistics, priority matrix)
    status: completed
  - id: accounting-expand
    content: "Expand r2.4-accounting-practice.md: Add ~15-17 vertical-specific scenarios (Journey Types 1-10) with alternatives and insights"
    status: completed
  - id: accounting-banking
    content: Add 12 banking scenarios (Journey Types 11-14) to r2.4-accounting-practice.md with alternatives and insights
    status: completed
  - id: accounting-summary
    content: Add summary sections to r2.4-accounting-practice.md (tables, statistics, priority matrix)
    status: completed
  - id: consulting-expand
    content: "Expand r2.5-consulting-creative.md: Add ~15-17 vertical-specific scenarios (Journey Types 1-10) with alternatives and insights"
    status: completed
  - id: consulting-banking
    content: Add 12 banking scenarios (Journey Types 11-14) to r2.5-consulting-creative.md with alternatives and insights
    status: completed
  - id: consulting-summary
    content: Add summary sections to r2.5-consulting-creative.md (tables, statistics, priority matrix)
    status: completed
---

# Fix Other Professionals Analysis

## Current State vs. Target

| File | Current | Target |
|------|---------|--------|
| [r2.2-healthcare-practice.md](_research/r2-scenarios-professionals/r2.2-healthcare-practice.md) | 2,933 lines, 29 scenarios | Complete (reference) |
| [r2.3-legal-practice.md](_research/r2-scenarios-professionals/r2.3-legal-practice.md) | 167 lines, ~6 scenarios | ~2,500 lines, 25-30 scenarios |
| [r2.4-accounting-practice.md](_research/r2-scenarios-professionals/r2.4-accounting-practice.md) | 142 lines, ~5 scenarios | ~2,500 lines, 25-30 scenarios |
| [r2.5-consulting-creative.md](_research/r2-scenarios-professionals/r2.5-consulting-creative.md) | 189 lines, ~5 scenarios | ~2,500 lines, 25-30 scenarios |

## What Each Document Needs

For each vertical, add:

**1. Vertical-Specific Scenarios (Journey Types 1-10)**: ~15-17 scenarios
- Cover all 10 journey types with vertical-specific scenarios
- Add user story, key needs, emotional drivers, frequency, impact, bank coverage

**2. Banking Operations Scenarios (Journey Types 11-14)**: 12 scenarios
- These are largely common across verticals but should be contextualized:
  - 11.1-11.5: Banking Operations
  - 12.1-12.2: Treasury & Cash Management
  - 13.1-13.3: Credit & Financing Management
  - 14.1-14.2: Compliance & Documentation

**3. For EACH Scenario**:
- Current Alternatives & Solutions (3-5 alternatives with pros, cons, cost, effectiveness)
- Business Owner Insights (expectation, benefit, switching factors, trust, convenience)

**4. Summary Sections**:
- Journey Type Overview table
- Scenario Summary Table (all scenarios with alternatives, expectation, adoption, value)
- Summary Statistics (expectation levels, adoption, value)
- Priority Matrix (Tier 1: Must Excel, Tier 2: Should Excel, Tier 3: Differentiation)
- Documentation Status

## Vertical-Specific Focus Areas

### Legal Practice (r2.3)
Key unique scenarios to develop:
- IOLTA/Trust Account Management (critical compliance)
- Contingency Fee Case Management
- Retainer Management & Drawdowns
- Case Expense Financing
- Partner Distribution Management
- Matter-Based Billing & Collections
- Client Conflict Checking (financial implications)
- Settlement/Judgment Collection

### Accounting Practice (r2.4)
Key unique scenarios to develop:
- Tax Season Cash Flow Management (highly seasonal)
- Year-Round Revenue Smoothing
- Client Receivables During Tax Season
- Staff Capacity Planning for Tax Season
- Seasonal Owner Draw Planning
- Practice Valuation (client portfolio value)
- Managing Multiple Client Tax Deadlines
- Professional Liability Considerations

### Consulting/Creative (r2.5)
Key unique scenarios to develop:
- Multi-Project Cash Flow Coordination
- Variable Income Smoothing
- Retainer vs. Project Billing Decisions
- Project Milestone Payment Management
- Travel Expense Management & Reimbursement
- Subcontractor Payment Management
- Equipment/Software Subscription Management
- Scope Creep Financial Impact

## Execution Approach

Process each vertical sequentially:

1. **Expand vertical-specific scenarios** (Journey Types 1-10)
   - Add missing scenarios based on vertical characteristics from [r1.3-professionals-verticals.md](_research/r1-market/r1.3-professionals-verticals.md)
   - Add full "Current Alternatives & Solutions" for each
   - Add full "Business Owner Insights" for each

2. **Add banking scenarios** (Journey Types 11-14)
   - Adapt from healthcare template with vertical-specific context
   - Add alternatives and insights for each

3. **Add summary sections**
   - Journey Type Overview
   - Scenario Summary Table
   - Summary Statistics
   - Priority Matrix
   - Documentation Status

4. **Unify narrative** - ensure no "original vs. new" language