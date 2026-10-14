# Workshop 1 — executive assessment

**Draft, 14 October 2026.** Based on two preserved recordings (A, 33:53; B, 83:29) and local machine transcripts. Timestamps below are elapsed time within each recording. The transcript has not been speaker-verified against the audio. This report records discussion and proposes follow-up; it is not approved minutes, a signed scope change, Sharia approval, or proof that software works.

## What the workshop advanced

The group worked through Murabaha accounting and servicing questions in much greater detail than the high-level requirements. Bede-side participants described gross contractual receivable and deferred profit, daily bank/core reconciliation, profit suspense for non-performing financing, recoverable legal costs, and charity treatment for late charges. FOO-side participants described or showed some existing LMS functions, including partial Ibra, deferment by installments, days-past-due buckets, and full write-off. The exact accounting entries, configurations, interfaces, and acceptance criteria remain to be supplied or agreed. [A 02:32–18:40, 18:51–33:51; B 01:54–07:15, 16:08–29:27]

The main delivery risk is **the boundary between current capability and the Murabaha-specific target**. A screen walkthrough of partial Ibra does not settle the eligible profit base, approval flow, journal impact, or customer document. A verbal statement that disbursement is gated by sale does not demonstrate the end-to-end ownership, possession, acceptance and sale evidence chain in a named build. These are the same unresolved claim conflicts in the [existing capability reconciliation](../../../../planning/sharia-murabaha-2026-10-07/claim-reconciliation.md); its 71 received pricing tests and 14 targeted lifecycle/Ibra checks still had no executed result in the reviewed plan. [A 30:17–33:51; B 45:39–56:55]

## Four decisions that control the design

| Priority | Decision to make | Why it matters | Recording |
| --- | --- | --- | --- |
| 1 | Agree one dated Murabaha sequence: application approval, commodity purchase, ownership/possession proof, customer offer/acceptance, sale execution, bank disbursement, and receivable/schedule activation. Explicitly distinguish an approved application from an active receivable. | Participants used “activation” at different points; the proposed lifecycle/ownership gate cannot be tested against an ambiguous sequence. | B 43:49–56:55 |
| 2 | Decide which system sends the sale-complete signal and which system requests bank disbursement; define retries and reconciliation when the bank succeeds but the LMS does not update. | The current backend-led route and an LMS-led alternative were both discussed; neither was selected. | B 45:39–53:05 |
| 3 | Approve Murabaha profit, rescheduling, deferment, Ibra and non-performing-profit rules with example amounts and journals. | Pricing may start as a percentage/declining schedule, while the sale fixes the contractual amount. A historical deferment scheme adding profit may conflict with that invariant. | A 18:51–33:51; B 29:43–42:02, 68:26–70:43, 76:51–78:03 |
| 4 | Freeze the product and requirements baseline: Tawarruq versus direct Goods Murabaha, which document/version governs, and any exclusions. | Verbal scope comments and the written scope/BRDs are not yet reconciled. | B 42:35–43:49, 57:19–64:58 |

## Capability assessment from this workshop

| Topic | What was reported or shown | Assessment now | Evidence needed |
| --- | --- | --- | --- |
| Partial Ibra | A FOO participant walked through percentage/manual/unearned-profit options and future-installment handling. | **Demo claim; fit unverified.** Bede deferred its response. | Named build, scenario inputs, eligible-profit rule, before/after schedule and GL, approval/audit and settlement output. |
| Lifecycle/sale gate | Sale confirmation before disbursement was discussed. Commodity workflow was described as outside LMS with evidence visible through integration. | **Architecture and sequence open.** | API/owner map; negative test before each evidence gate; complete persisted audit chain. |
| Profit and deferment | Participants described percentage-based pricing and a fixed post-sale contractual amount; days-based deferment and older profit-adding scheme were discussed. | **Policy conflict to resolve.** | Signed Sharia/finance rule with fixed-amount examples and regression tests. |
| Write-off | Full write-off was described as available; partial write-off as needing development. | **Partial write-off is a candidate enhancement, scope open.** | Written in/out-of-scope decision, estimate, journals and tests. |
| Delinquency/notifications | Days-past-due buckets were described as present; value/count thresholds and automated product-driven actions/notifications were described as missing or needing detail. | **Candidate enhancements.** | Risk thresholds, action matrix, channel templates, configuration demonstration and tests. |
| Reconciliation and ECL | Bank/core reconciliation and Bede-owned ECL calculation were discussed. | **Ownership and interface open.** | Input/output contracts, exception process, sample files, posting ownership and reconciled examples. |

**Recommended next gate:** circulate the two question documents actually referenced in the meeting, have Bede product/finance/Sharia mark each rule with an example and approval status, and run a joint integration/lifecycle session before assigning “supported” status. Then execute the [existing targeted tests](../../../../planning/sharia-murabaha-2026-10-07/test-execution-plan.md) on a versioned environment. The closing discussion proposed further sessions; the recording does not prove that documents were sent or the next meeting was booked. [B 79:00–83:26]
