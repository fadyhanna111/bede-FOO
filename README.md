# Bede - FOO Loan Management System

Project documentation, meeting records, proposed scope and commercial references for Bede's LMS implementation and migration. These records distinguish proposal terms, draft meeting discussion and verified delivery evidence.

## Start here

- [Project summary](documentation/project-summary.md) - purpose, workstreams, commercial terms and open questions.
- [Current document register](documentation/reference/current-documents.md) - authoritative source locations, versions and retrieval map.
- [Agent reference](agent.md) - concise context and navigation for future work.
- [1 October 2026 meeting minutes](meetings/2026-10-01/minutes/Bede_Meeting_Minutes_2026-10-01.md) - draft for review.
- [Editable meeting minutes](meetings/2026-10-01/minutes/Bede_Meeting_Minutes_2026-10-01.docx) and [final PDF preview](meetings/2026-10-01/supporting/render-release/Bede_Meeting_Minutes_2026-10-01.pdf).
- [Live estimation workbook](https://docs.google.com/spreadsheets/d/1dprGn0XU50lfuDBHKK7CKuznUqifd-Xldsf7YMlz7dE/edit?gid=1660934949#gid=1660934949) - refresh live values before using them.

## Folder guide

| Folder | Contents |
| --- | --- |
| `meetings/YYYY-MM-DD/` | One folder per meeting: minutes, attendee evidence, recordings and supporting material. |
| `documentation/proposals/` | Original technical and commercial response PDFs, retaining their supplied filenames and versions. |
| `documentation/compliance/` | Original Annex2 compliance workbook. |
| `documentation/estimates/` | Dated estimation snapshots and references to the live workbook. |
| `documentation/reference/` | Document register and file organization/provenance manifest. |
| `documentation/search-index/` | Searchable PDF text, compliance cells, source hashes and selected page previews. |
| `planning/` | Future delivery plans, scope decisions, actions, risks and workshop records. |
| `scripts/` | Reproducible document indexing and meeting-production helpers. |

## Record conventions

- Use ISO dates (`YYYY-MM-DD`) for meetings and snapshots. Keep supplied filenames and version labels for source documents.
- Preserve original evidence. Clearly label drafts, approved records, superseded versions and assumptions; do not silently overwrite approved records.
- Start new meeting records with `meetings/YYYY-MM-DD/minutes/`, `attendees/`, `recordings/` and `supporting/` as needed.
- Link new records from this README and update `agent.md` and the relevant register so future searches remain short.
- The current minutes are drafts. The proposals are source references, not proof of an executed contract, an approved delivery baseline or production completion.

## Recordings and reproducibility

Audio files are tracked with Git LFS. To retrieve full recordings after cloning, install Git LFS and run `git lfs pull`. An LFS pointer alone is not an audio file.

The original recording and processing variants are in [the meeting recording folder](meetings/2026-10-01/recordings/README.md). [Supporting evidence](meetings/2026-10-01/supporting/README.md) explains final and superseded renders.

Installed Python libraries, the incomplete transcription environment, and the abandoned partial Whisper download remain local under ignored `working/` paths. They are machine dependencies rather than project records; no local files were deleted. Script prerequisites and limitations are listed in [scripts/README.md](scripts/README.md).

The Google Sheets snapshot is partial, not a full workbook backup. The complete external workbook remains available at its linked URL.
