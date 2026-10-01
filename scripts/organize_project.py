from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent.parent
meeting = 'meetings/2026-10-01'
moves = {
    'minutes': f'{meeting}/minutes',
    'source/Bede.m4a': f'{meeting}/recordings/Bede.m4a',
    'source/attendees.md': f'{meeting}/attendees/attendees.md',
    'source/attendees.png': f'{meeting}/attendees/attendees.png',
    'source/documents/current-documents.md': 'documentation/reference/current-documents.md',
    'source/documents/Annex2_LMS_Compliance_FOO_Response.xlsx': 'documentation/compliance/Annex2_LMS_Compliance_FOO_Response.xlsx',
    'source/documents/FOO - Bede - Loan Management System - Technical Response V1.0.pdf': 'documentation/proposals/FOO - Bede - Loan Management System - Technical Response V1.0.pdf',
    'source/documents/FOO - Bede - Loan Management System - Commercial Response V1.6.pdf': 'documentation/proposals/FOO - Bede - Loan Management System - Commercial Response V1.6.pdf',
    'project-summary.md': 'documentation/project-summary.md',
    'working/document-index/google-sheet-intake-snapshot-2026-10-01.json': 'documentation/estimates/google-sheet-intake-snapshot-2026-10-01.json',
    'working/Bede_multilingual.m4a': f'{meeting}/recordings/Bede_multilingual.m4a',
    'working/Bede_normalized.wav': f'{meeting}/recordings/Bede_normalized.wav',
    'working/Bede_voice_boost.wav': f'{meeting}/recordings/Bede_voice_boost.wav',
    'working/build_minutes.py': 'scripts/build_minutes.py',
    'working/index_project_sources.py': 'scripts/index_project_sources.py',
    'working/transcribe.py': 'scripts/transcribe.py',
    'working/source-notes.md': f'{meeting}/supporting/source-notes.md',
    'working/minutes-content.json': f'{meeting}/supporting/minutes-content.json',
    'working/original-attachment-path.txt': f'{meeting}/supporting/original-attachment-path.txt',
    'working/render': f'{meeting}/supporting/render',
    'working/render-final': f'{meeting}/supporting/render-final',
    'working/render-release': f'{meeting}/supporting/render-release',
    'working/render-verified': f'{meeting}/supporting/render-verified',
    'working/document-index': 'documentation/search-index',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

records = []
for old, new in moves.items():
    source, target = root / old, root / new
    if not source.exists():
        raise RuntimeError(f'Missing source: {old}')
    if target.exists():
        raise RuntimeError(f'Refusing existing destination: {new}')
    files = [source] if source.is_file() else sorted(p for p in source.rglob('*') if p.is_file())
    hashes = [(p.relative_to(source) if source.is_dir() else None, sha(p)) for p in files]
    target.parent.mkdir(parents=True, exist_ok=True)
    source.rename(target)
    for relative, digest in hashes:
        dest = target / relative if relative is not None else target
        assert sha(dest) == digest, str(dest)
        records.append({'previous_path': old + ('/' + str(relative) if relative is not None else ''), 'path': dest.relative_to(root).as_posix(), 'sha256_at_move': digest})

# Rewrite navigation and scripts, leaving original documents and extracted source text intact.
replacements = dict(moves)
replacements['minutes/'] = replacements.pop('minutes') + '/'
pattern = re.compile('|'.join(re.escape(p) for p in sorted(replacements, key=len, reverse=True)))
for file in set([root / 'agent.md', *root.rglob('*.md'), *list((root / 'scripts').glob('*.py')), root / 'documentation/search-index/source-manifest.json']):
    if 'working' in file.relative_to(root).parts:
        continue
    content = file.read_text()
    content = pattern.sub(lambda match: replacements[match.group(0)], content)
    file.write_text(content)

manifest = root / 'documentation/reference/organization-manifest.json'
manifest.write_text(json.dumps({'organized_date': '2026-10-01', 'timezone': 'Asia/Beirut', 'note': 'Hashes were verified immediately after every move. Navigation and script paths were then updated; original binary source artifacts were not rewritten.', 'files': records}, indent=2))
print(f'Preserved and verified {len(records)} files.')
