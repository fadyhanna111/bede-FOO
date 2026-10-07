# Murabaha capability and test review

Prepared 7 October 2026 from the eight hash-verified [source files](../../documentation/sharia-murabaha/other.md). The source-copy manifest is [here](../../documentation/sharia-murabaha/source-manifest.json). `scripts/build_sharia_review.py` rebuilds the tables and checks 47 mapped questions, 71 original Section 6 cases and 14 proposed targeted cases. It reads the preserved files and does not change any source workbook or Word document.

| File | Purpose |
| --- | --- |
| [Capability matrix TSV](capability-matrix.tsv) and [JSON](capability-matrix.json) | One row per Q01–Q47: assessment result, FOO's complete response text, related specification, interpretation, exact source cells and evidence request. TSV has one physical line per question for spreadsheet import. All implementation dispositions remain open. |
| [Claims reconciliation](claim-reconciliation.md) | Focused review of direct present-tense contradictions, design-scope differences and illustrative scenario claims. |
| [Test execution plan](test-execution-plan.md) | Dependencies, proposed waves, evidence standard, roles and proposed exit gates. |
| [Section 6 execution tracker](section6-execution-tracker.tsv) | The 71 received cases, including their source FRD design-time label and separate execution result. No result was promoted to Pass. |
| [Lifecycle and Ibra targeted tests](lifecycle-ibra-targeted-tests.tsv) | Fourteen proposed cases filling gaps outside the pricing FRD's Section 6 test set. They are new planning rows and all `Not Run`. |
| [Review metrics](review-metrics.json) | Machine-readable counts and scope caveat. |

The assessment marks Q06/Q07 (ownership lifecycle) and Q18/Q19 (Ibra) as major gaps, while FOO's answers describe support. The BRDs specify enhancements and therefore do not themselves prove deployment. The response workbook also contains illustrative screenshots, but they lack a verified build/configuration identity and complete repeatable test record in this source set. Resolve those four questions first, then use the full matrix to validate the remaining claims.
