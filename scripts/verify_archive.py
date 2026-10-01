"""Check source preservation, document navigation and helper syntax without rewriting artifacts."""
from pathlib import Path
import ast
import hashlib
import json
import re
from urllib.parse import unquote

root = Path(__file__).resolve().parent.parent
hash_file = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads((root / 'documentation/search-index/source-manifest.json').read_text())
for entry in manifest['files']:
    path = root / entry['project_path']
    assert hash_file(path) == entry['sha256'], f'Source hash mismatch: {path}'
    original = Path(entry['original_path'])
    if original.exists():
        assert hash_file(original) == entry['sha256'], f'Original hash mismatch: {original}'
    assert (root / entry.get('searchable_text', entry.get('searchable_cells'))).is_file()
organization = json.loads((root / 'documentation/reference/organization-manifest.json').read_text())
for entry in organization['files']:
    path = root / entry['path']
    assert path.is_file(), f'Missing moved file: {path}'
    if path.suffix in {'.pdf', '.docx', '.xlsx', '.m4a', '.wav', '.png'}:
        assert hash_file(path) == entry['sha256_at_move'], f'Changed source binary: {path}'
recording = root / 'meetings/2026-10-01/recordings/Bede.m4a'
assert hash_file(recording) == 'f08bde0a0b079d7717f4447212daf7f41c1df73f1eac047fd723a451856bcfe2'
meeting_markdown = next(entry for entry in organization['files'] if entry['path'].endswith('/minutes/Bede_Meeting_Minutes_2026-10-01.md'))
assert hash_file(root / meeting_markdown['path']) == meeting_markdown['sha256_at_move'], 'Meeting minutes text changed during organization'
broken = []
for file in root.rglob('*.md'):
    if 'working' in file.relative_to(root).parts or '.git' in file.relative_to(root).parts:
        continue
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', file.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        relative = unquote(target.split('#')[0].strip('<>'))
        if not (file.parent / relative).exists():
            broken.append((file.relative_to(root).as_posix(), target))
assert not broken, f'Broken Markdown links: {broken}'
for script in (root / 'scripts').glob('*.py'):
    ast.parse(script.read_text(), filename=str(script))
print(f'PASS: {len(manifest["files"])} supplied source hashes, {len(organization["files"])} moved files, original recording/minutes, Markdown links and Python syntax.')
