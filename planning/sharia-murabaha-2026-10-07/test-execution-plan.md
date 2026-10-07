# Murabaha evidence and test execution plan

Prepared 7 October 2026. Proposed plan for the 71 received Section 6 cases plus 14 new lifecycle/Ibra checks. No test was executed in this review. In the source test workbook, `Current Status (FRD)` is a design-time label and `Result` is the execution field; **all 71 Result cells are `Not Run`**. The source priorities are 44 High, 25 Medium and two Low. Its design-time column says four `PASS`, two `Tested`, six `GAP` and 59 `To be tested`; none of those labels is an execution result. The four implied-rate calculation examples have expected values and stored checks, but are not a live LMS execution record.

## Entry gate: agree the test target

1. FOO identifies the product build/commit, environment, tenant, enabled modules, pricing and accounting configuration, API version and any feature flags. Bede confirms which Murabaha variant and rules are in the proposed acceptance scope. Capture the source-document version and relevant Sharia/accounting policy decisions.
2. Freeze the data fixtures: conventional control account; direct Goods Murabaha account before/after sale; fixed-amount declining and flat products; rate-based product; payable/overdue and write-off examples. Reconcile source workbook baselines B1–B5 before test execution.
3. Assign a proposed FOO QA executor and Bede product/finance witness. The accountable owners, dates and approval authority must be confirmed by the project leads. Record defects in the agreed project system, linking back to test ID and build.

## Proposed waves

| Wave | Scope | Evidence emphasis | Gate to move on |
| --- | --- | --- | --- |
| 0 · Baseline | Reproduce four implied-rate examples; establish B1–B5 accounts, ledger mapping and immutable contractual totals. | Input/output calculations, exact currency precision, product settings, schedule and GL opening balances. | Finance/product reviewer accepts fixtures and tolerances. |
| 1 · Core profit | Section 6 tests for §§6.3–6.5 and 6.18: servicing invariants, accrual and partial payment. | Profit paid + remaining = contractual profit; no silent change to Cost, Profit or Selling Price. | High-priority failures triaged before wider rescheduling. |
| 2 · Schedule changes | Section 6 tests for §§6.6–6.13: date shifts, grace, tenor, rate attempts and combined rescheduling. | Before/after schedule, outstanding balance, journal and rejection evidence. | Material invariants and required negative controls pass or have approved disposition. |
| 3 · Controls/regression | Remaining Section 6 tests for §§6.14–6.21: protected fields, waiver, write-off, top-up and conventional regression. | UI and API parity, audit, financial impact, backward compatibility. | Full 71-case register has actual results, evidence and defects. |
| 4 · Lifecycle and Ibra | The [14 targeted cases](lifecycle-ibra-targeted-tests.tsv) cover Q06/Q07/Q18/Q19 and related outputs outside the pricing test workbook. | Premature-sale denial, ownership evidence, approvals, distinct Ibra, calculation methods, letters/API and conventional regression. | Bede reviewers can reconcile the four major claim conflicts against the identified build. |

Waves 1–4 can overlap where fixtures and reviewers are ready; the order is for dependency control, not a calendar commitment. Use [the 71-case tracker](section6-execution-tracker.tsv) for source procedures and expected results. Preserve the original XLSX unchanged; record execution in a working copy or agreed QA system with links to the source test IDs.

## Evidence and result rules

- For each case retain build/config ID, executor/date, preconditions, input and UI/API actions, expected versus actual values, schedule and GL before/after where applicable, screenshots/logs/export, and a defect or decision link. Redact customer PII and credentials from shared evidence.
- Mark `Pass` only after the observed output matches the agreed expected result. Use `Fail` for a reproducible mismatch, `Blocked` for missing prerequisites, and `Not Run` until execution. A source FRD label such as `PASS` must not be copied into the execution result.
- Link any specification change to its requirement question, approving owner and version; rerun affected cases and the conventional regression set after a fix. Keep a separate decision for matters requiring Sharia or accounting interpretation.

## Proposed exit package

Produce the completed 71-case register and targeted-case register, defect list with dispositions, build/config manifest, journal/schedule reconciliation evidence, scope exceptions, and product/finance/Sharia reviewer decisions. The release or contractual acceptance threshold must be agreed by Bede and FOO; this plan does not set one unilaterally. The [claims reconciliation](claim-reconciliation.md) stays open until each disputed statement has linked proof or an agreed wording change.
