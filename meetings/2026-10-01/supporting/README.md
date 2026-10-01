# Meeting production and evidence

- `source-notes.md`: original recording provenance, evidence timestamps and interpretation limits.
- `minutes-content.json`: structured content used to produce the current minutes.
- `original-attachment-path.txt`: original local attachment location for provenance.
- `render-release/`: final verified two-page PDF preview and images for the current draft minutes.
- `render/`, `render-final/`, `render-verified/`: earlier production/verification artifacts, retained for provenance. They are superseded by `render-release/`.

Rebuilding the minutes uses [scripts/build_minutes.py](../../../scripts/build_minutes.py). The original draft DOCX and its final render have been preserved without regeneration during organization.
