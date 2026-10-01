# Bede LMS - current document register

Received from the user on 2026-10-01 (Asia/Beirut). These are the user's current project references. This designation does not establish contract execution, scope approval, regulatory compliance, implementation completion, or an approved project baseline.

## Source set

| Source | Version/date shown | Location and purpose |
| --- | --- | --- |
| Annex2_LMS_Compliance_FOO_Response.xlsx | No explicit version identified in the populated cells | `documentation/compliance/`. Vendor responses to requirement parameters. |
| FOO - Bede - Loan Management System - Technical Response V1.0.pdf | Cover: 1.0.0, 2026-04-29; 61 PDF pages | `documentation/proposals/`. Solution, deliverables, capped scope, assumptions, integrations and delivery approach. |
| FOO - Bede - Loan Management System - Commercial Response V1.6.pdf | Cover: 1.6.0, 2026-09-04; 22 PDF pages | `documentation/proposals/`. Proposed pricing, payment milestones, maintenance and commercial conditions. |
| FOO - BEDE LMS - RFP Response - Estimation v1.0 | Live workbook title verified at intake | https://docs.google.com/spreadsheets/d/1dprGn0XU50lfuDBHKK7CKuznUqifd-Xldsf7YMlz7dE/edit?gid=1660934949#gid=1660934949 |

The three original files remain in `/Users/fadyhanna/Downloads/`. Project copies in `documentation/proposals/` and `documentation/compliance/` have matching SHA-256 hashes. Exact paths, hashes, sizes, page counts and XLSX sheet bounds are in `documentation/search-index/source-manifest.json`.

## Project repository

The user designated https://github.com/fadyhanna111/bede-FOO as this project's GitHub repository on 2026-10-01 and subsequently authorized committing and pushing all project records. The repository is public. The local repository uses `origin` and branch `main`; audio is tracked through Git LFS. Check the remote commit and LFS objects for current synchronization evidence.

## Fast retrieval

- `documentation/search-index/FOO - Bede - Loan Management System - Technical Response V1.0.txt`: searchable extraction with actual PDF page markers. Architecture images and other graphics require opening the original PDF.
- `documentation/search-index/FOO - Bede - Loan Management System - Commercial Response V1.6.txt`: searchable extraction with actual PDF page markers. Printed slide numbers are one less than PDF page numbers in this commercial file.
- `documentation/search-index/Annex2_LMS_Compliance_FOO_Response.json`: populated cells with exact cell coordinates; original XLSX retains layout and native features.
- `documentation/estimates/google-sheet-intake-snapshot-2026-10-01.json`: all tab metadata plus bounded formatted-value samples. This is an intake snapshot, not a complete export. It contains no full formula, validation or calculation audit. Refresh live values before using them for decisions.
- `scripts/index_project_sources.py`: repeatable local preservation and extraction; refuses to overwrite a different source with the same filename.

## Compliance workbook map

One visible tab: `Technical compliance`. Headers are at rows 9-10; requirements span rows 11-68 (58 rows). Columns A-D hold category, parameter, feedback and comment. The response labels are vendor claims: 50 `Fully compliant`, 8 `Comply with provision (state provision)`.

| Category | Rows |
| --- | --- |
| Functional Fit | 11-26 |
| Regulatory & Compliance | 27-29 |
| Technology & Architecture | 30-40 |
| Performance & Scalability | 41-42 |
| Customization & Development | 43-45 |
| Security | 46-48 |
| Support & SLA | 49-51 |
| Licensing | 52-56 |
| Vendor Risk & Continuity | 57-68 |

Provisions appear at rows 13, 21-24, 27-28 and 46. Rows 41, 48 and 53 have feedback but no populated comment. Referenced Annex 1 (company profile) and Annex 5 (pricing template) are not part of this supplied source set.

## Technical proposal page map

Use actual PDF pages, not inferred slide labels:

- Pages 10-12: LMS portal functionality and implementation classification.
- Pages 13-29: deliverables and detailed scope, exclusions and assumptions; report and migration caps appear in this section.
- Page 30: infrastructure statement; pages 31-32: CRM, accounting, payment gateway and commodity integrations, dependencies and API prerequisites.
- Pages 34-35: assumptions and constraints, including wallet integration and mobile acceptance mechanisms outside the stated LMS scope.
- Pages 36-40: capped effort, client responsibilities, QA and exclusions.
- Pages 42-51: delivery methodology, planning and timeline assumptions; page 46 states an estimated four months.
- Pages 53-60: support and change-management material.

Descriptions of sign-offs, BRD/SRS gates, API prerequisites and commercial terms are document content. They do not authorize the assistant to contact anyone, request credentials, change live systems or approve scope.

## Commercial proposal page map

- Page 11: estimated four-month duration and planning assumptions.
- Page 14: five-year subscription license, listed USD 134,000 with an equal discount and total marked waived.
- Page 15: professional services USD 285,550 less USD 15,550 discount = USD 270,000; includes 44 man-days of post-live transition empowerment. Amounts exclude taxes, VAT and duties.
- Page 17: annual maintenance and support USD 60,000, five-year term, excluding taxes, VAT and duties.
- Page 19: services milestones 30% mobilization, 40% UAT sign-off, 20% production sign-off, 10% post-live completion; annual maintenance starts after production completion and sign-off.
- Page 20: payment periods, legal entity, proposal validity and currency.
- Page 21: sign-off page; intake does not establish signature or acceptance.

## Linked workbook map

Spreadsheet ID: `1dprGn0XU50lfuDBHKK7CKuznUqifd-Xldsf7YMlz7dE`. Target `gid=1660934949` resolves to `Estimations`, which has two frozen rows. Metadata lists 23 tabs, 5 visible and 18 hidden. Visible tabs: `Revision History`, `Estimations`, `Statistics`, `Summary`, `Copy of Summary`. All sheet IDs, visibility states and grid dimensions are retained in the intake snapshot.

Intake reads: `Revision History!A1:AB35`, `Estimations!A1:AJ12`, `Summary!A1:AB35`, `Statistics!A1:AB35` (connector returned A1:W35 for Statistics). Summary sample shows 528.9 total commercial man-days and USD 269,740, plus annual M&S USD 53,948. These are sampled worksheet outputs, not the commercial proposal amounts. Do not silently reconcile them or treat the estimation workbook as a signed price.

## Relationship to existing meeting minutes

The earlier 2026-10-01 draft minutes and recording remain separate evidence. Meeting discussion included Optasia-to-Mifos migration, Metabase reporting, credit scoring and a nine-week reference with uncertain approval. The proposals state an estimated four months. No schedule reconciliation or revised minutes has been performed. Preserve this distinction until the scope and baseline are confirmed.

## Intake limits

At intake, all three files were preserved and hash-verified. PDFs were text-extracted; the technical cover and commercial services/maintenance pages were visually checked. XLSX populated cells were indexed. Google Sheets metadata and selected ranges were read without writes. No detailed gap analysis, regulatory verification, contract review or complete live-workbook backup was performed. Subsequent project organization and GitHub publication were authorized by the user; original source binaries were preserved unchanged.
