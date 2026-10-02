# Bede LMS project summary

Prepared 2026-10-01 and updated 2026-10-02 (Asia/Beirut) from the supplied references. This summarizes FOO's proposal, Bede's later scope request and meeting records; it does not confirm a signed baseline or delivery completion. See the [source comparison](../planning/requirements-reconciliation-2026-10-02.md) for material differences.

## Purpose and solution

FOO proposes to implement Bede's Loan Management System for its Bahrain financing operations. The 1 October draft meeting minutes describe moving from Optasia toward Mifos. The technical proposal identifies the core as Fineract 1.x, with FOO configuration and extensions rather than modifications to the Fineract core source. The goal is to operate financing accounts, repayments, settlement, delinquency, accounting interfaces and reporting within Bede's existing ecosystem.

At go-live, the proposal assumes BHD currency and Murabaha financing. It adds cost, profit and selling-price fields and financing terminology, plus commodity transaction references. These are proposed Islamic-financing capabilities, not evidence of Shariah certification.

## Main workstreams

1. **LMS setup and financial rules:** products, chart of accounts, permissions, maker-checker controls, repayment schedules, grace periods, VAT and fees, insurance within installments, early/partial settlement, restructuring, write-offs, delinquency and customer exposure limits.
2. **Integrations:** CRM customer reads, accounting-entry posting, payment gateway repayments and commodity trading references. FOO's proposal exposes LMS APIs to Bede's backend. Bede's later scope request also expects FOO to integrate the mobile app and backend end to end. The work split requires agreement. API documentation, stable environments and test data are client dependencies.
3. **Reporting:** Metabase reports for receivables and deferred profit, management/finance dashboards, customer statements and reconciliation. Regulatory exports are intended to align with CBB and AAOIFI requirements; up to 20 regulatory reports are included, with templates supplied by Bede. Direct CBB submission and regulatory sign-off are excluded.
4. **Migration:** up to 10,000 active loan agreements and associated history, mapping/transformation, rehearsals, reconciliation and cutover. Source-system cleanup and legacy archival are excluded; the source data must be sufficiently documented and usable.
5. **Delivery and handover:** requirements workshops, signed BRD and SRS, configuration/development, FOO system and end-to-end testing, Bede UAT, security audit support, production cutover, training and post-live support.

FOO's proposal has it build/configure the solution and support integration, testing and cutover. Bede's later request assigns AWS provisioning and UAT/production deployment to Bede, while the kick-off record says FOO hosts development. Bede supplies business rules, chart of accounts, report templates, source data and third-party access, and manages UAT execution and approvals. Many activities in FOO's proposal have capped effort or iteration limits.

## Commercial proposal V1.6.0

| Item | Proposed amount/term |
| --- | --- |
| Professional services after discount | USD 270,000 |
| Subscription license | Listed USD 134,000, fully discounted/waived; five-year term |
| Maintenance and support | USD 60,000 annually; five-year term |
| Post-live transition | 44 man-days included in professional services |
| Payment milestones | 30% mobilization, 40% UAT sign-off, 20% production sign-off, 10% post-live completion |

Amounts exclude taxes, VAT and duties. Annual maintenance starts after production completion and sign-off. Scope changes and extended delivery, third-party or UAT delays can affect cost and schedule under the proposal.

## Schedule and status

The proposals estimate four months, with the detailed plan to follow requirements gathering. The draft meeting minutes mention nine weeks, but do not establish its scope, starting point or approval. A committed delivery date is not established by the supplied material.

The Bede client kick-off PDF records a delivery plan/workshop schedule requested within seven days, a requirement-by-requirement compliance matrix within 7-15 days and an eligibility-engine review within 15 days of its 1 October meeting. Completion has not been verified. The separate recording-based minutes remain a draft from mixed-language, low-volume audio; their relationship to the client record and some owner/schedule attributions need confirmation.

## Principal open points

- **Scope alignment:** meeting discussion covers front-end/wallet reuse and scoring. The technical proposal excludes wallet integration, mobile offer/acceptance mechanisms and the credit-scoring model. Petra's scoring exercise is described in the minutes as a demonstration, not a confirmed production deliverable.
- **Accounting and reporting ownership:** accounting integration is in the proposal, while the minutes still question accounting responsibility. Confirm the ledger boundary, data sources, report list, validation specialist and acceptance criteria.
- **Infrastructure:** technical page 13 describes AWS provisioning; page 30 states Bede's existing infrastructure will be used. Confirm the actual environment responsibilities and deployment plan.
- **Financial reconciliation:** the live estimation Summary read on 2026-10-01 shows USD 269,740 and annual M&S USD 53,948, versus USD 270,000 and USD 60,000 in commercial V1.6.0. It also shows 528.9 commercial man-days. These figures have not been reconciled or treated as interchangeable.
- **Evidence for compliance:** the Annex2 response has 58 requirement rows, with 50 marked fully compliant and 8 compliant with provisions. These are vendor response labels, not independent compliance evidence.
- **Delivery baseline:** confirm BRD/SRS scope, named owners, dependencies, capped budgets, migration acceptance and the timeline before using any estimate as a committed baseline.
- **Bede's later requirements:** the 21-page Bede scope document requests broader app journeys and integrations, full historical migration, IFRS9/AAOIFI outputs, specific hosting/access controls, support/service levels and contract terms. These have not been mapped to FOO's earlier capped proposal or the 58-row Annex2 response. Bracketed numeric targets in Bede's document are indicative and subject to agreement.

## Source references

- `documentation/proposals/FOO - Bede - Loan Management System - Technical Response V1.0.pdf`: PDF pages 9-15, 18-30, 34-35 and 46 for architecture, scope, exclusions, migration, dependencies and schedule.
- `documentation/proposals/FOO - Bede - Loan Management System - Commercial Response V1.6.pdf`: PDF pages 11, 14-17 and 19-20 for schedule and commercial terms.
- `documentation/compliance/Annex2_LMS_Compliance_FOO_Response.xlsx`: `Technical compliance!A11:D68`.
- `documentation/requirements/Bede - Foo LMS - Scope and Requirements.pdf`: Bede's later numbered requirements, 21 PDF pages.
- `meetings/2026-10-01/client-kickoff/Bede LMS Kick-off.pdf` and `Bede LMS Project Kickoff Deck.pptx`: Bede client meeting record and presentation dated 1 October, received 2 October.
- `meetings/2026-10-01/minutes/Bede_Meeting_Minutes_2026-10-01.md`: draft discussion, actions and unresolved points.
- https://docs.google.com/spreadsheets/d/1dprGn0XU50lfuDBHKK7CKuznUqifd-Xldsf7YMlz7dE/edit?gid=158887769#gid=158887769 : `Summary!G1:Q16`, refreshed read on 2026-10-01.
- `documentation/reference/current-documents.md`: complete source register, provenance and retrieval map.
- https://github.com/fadyhanna111/bede-FOO : user-designated project repository; subsequent organization, commit and push were explicitly authorized by the user.
