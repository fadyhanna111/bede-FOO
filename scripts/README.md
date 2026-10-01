# Production helpers

Run from a checkout with Python and the stated libraries installed. Dependencies are not vendored in this repository.

| Script | Purpose and prerequisites |
| --- | --- |
| `index_project_sources.py` | Index preserved PDFs/XLSX and verify source hashes. Needs `pypdf` and `openpyxl`. Optional `--source-dir /path/to/originals` preserves supplied originals, refusing a different same-named project file. |
| `build_minutes.py` | Rebuild the 1 October draft DOCX and Markdown from the retained JSON. Needs `python-docx`. Overwrites the draft outputs when deliberately run; does not render PDFs. |
| `transcribe.py` | Historical CLI fallback. Needs `mlx_whisper` and a valid Whisper model at local `working/whisper-model/`. The retained partial model is unusable and this script did not produce the meeting transcript. Outputs, if run with a valid model, go under the meeting's `transcripts/`. |
| `organize_project.py` | One-time migration from the previous local layout. Preserves files and verifies hashes; refuses missing sources or existing destinations. It should not be rerun in the organized checkout. |
| `verify_archive.py` | Read-only verification of original source hashes, moved binary files, the original recording/minutes, local Markdown links and Python syntax. Uses the Python standard library. |

The document registry records extraction limitations. Do not confuse successful file generation or PDF rendering with approved meeting content or verified production behavior.
