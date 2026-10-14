# Workshop 1 — scope and test impact

**Working crosswalk, 14 October 2026.** The workshop recording supplies questions and verbal capability claims. The [requirements extract](../../../../documentation/search-index/Bede%20-%20Foo%20LMS%20-%20Scope%20and%20Requirements.txt) and [existing claim reconciliation](../../../../planning/sharia-murabaha-2026-10-07/claim-reconciliation.md) are the written baselines used here. Requirement IDs are references for review, not a claim that a change is approved. No new execution result is recorded by this report.

| Workshop issue | Written anchor | Current-versus-target reading | Next proof/decision |
| --- | --- | --- | --- |
| Murabaha purchase → ownership/possession → offer/acceptance → sale → disbursement | INT-03, FR-16; prior reconciliation C01–C03 | External commodity/mobile flow was described; LMS evidence/state and activation sequence remain unclear. | Agree sequence and owner/API diagram, then run lifecycle negative and full-chain tests L01–L06 with persisted evidence. |
| Partial Ibra and early settlement | FR-10, FR-18; C04–C06 | Partial-Ibra controls were shown, but eligible profit, approval, output and GL behavior were not accepted. | Agree sample calculations including overdue/unpaid profit and tenor-vs-payment treatment; run I01–I07 and output checks. |
| Fixed contractual profit, deferment and varied schedules | FR-09, FR-22; C07 | Existing percentage-based pricing can derive the sale amount; post-sale total should be invariant under schedule changes, subject to approved policy. Historical profit-adding deferment may conflict. | Finance/Sharia examples for days vs installments, grace, fixed totals, fee separation and customer consent; execute affected Section 6 cases. |
| Subledger, close, legal cost, charity and suspense | FR-09, FR-11, FR-12 | Ledger structure and accounting examples were discussed, not signed off. | Journal matrix by event and GL, including reversal, recovery, period-close and exception; finance approval and ledger tests. |
| Daily reconciliation and disbursement/payment status | FR-13, FR-16, INT-04, INT-05 | Bank/core feed and backend-versus-LMS orchestration are open; mismatched external/LMS statuses were reported. | Interface contract, status/idempotency model, independent bank file/API and failed/retried transaction scenarios. |
| ECL/staging/delinquency/notifications/collections | FR-12, FR-26–FR-30 | DPD buckets were reported; amount/count triggers and stage actions need detail; Bede ECL model described as calculation owner. | Risk/action matrix, ECL data contract, templates/channels, queue behavior and end-to-end tests. |
| Top-up and write-off | FR-20, FR-24 | New-contract Murabaha top-up differs from generic top-up; full write-off reported, partial write-off needs estimate. | Decide scope, process owner, account/commodity links, journal examples, controls and test cases. |
| Product baseline and exclusions | Scope document plus Murabaha BRDs | Verbal “Tawarruq now” and exclusions do not reconcile all written material. | Versioned, signed scope matrix naming first product, future variants, exclusions and change-control treatment. |

## Proposed test order

1. Freeze the exact build, environment, product configuration, document version, and approved Sharia/finance examples. Keep a separate row for each verbal claim, design specification, and observed result.
2. Execute a **negative lifecycle gate**: attempt sale and disbursement before purchase, ownership, possession, acceptance and sale evidence; capture API/UI responses, state, receivable and audit trail. Then complete one positive journey through bank disbursement and status reconciliation.
3. Reproduce partial/full Ibra with not-yet-due and overdue unpaid profit, approval/rejection, fee/cap and customer statement. Compare balances, schedule, GL and audit before/after.
4. Run schedule-change cases that preserve selling price and contractual profit; separately test any approved exception. Cover days-based deferment, top-up as new contract, and missed bank/LMS callbacks.
5. Expand to accounting, delinquency, ECL and notification cases once the rule matrices and integrations are available.

The prior [test execution plan](../../../../planning/sharia-murabaha-2026-10-07/test-execution-plan.md) remains the working evidence procedure. Its original 71 Section 6 cases and 14 targeted checks were **Not Run** when reviewed; workshop discussion is not a substitute for executed tests. Proposed statuses and suggested leads are in [the register](03-actions-and-decisions.tsv).
