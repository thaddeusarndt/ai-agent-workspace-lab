"""Audit a local static-site snapshot with selected operating AIO inspection code.

No network, deployment, scheduler changes, model calls, or customer records.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engines.aio_page_inspection import parse_html


def audit(root, domain):
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError('Site snapshot directory does not exist')
    if not domain or '/' in domain or ':' in domain:
        raise ValueError('Domain must be a hostname, without scheme or path')
    paths = sorted(p for p in root.rglob('*.html')
                   if p.is_file() and not p.is_symlink()
                   and not any(part.startswith('.') or part in {'node_modules', 'drafts'}
                               for part in p.relative_to(root).parts))
    pages, failures, issues = [], [], []
    for path in paths:
        try:
            page = parse_html(path, root)
        except (OSError, UnicodeError) as error:
            failures.append({'path': path.relative_to(root).as_posix(), 'error': type(error).__name__})
            continue
        pages.append({k: page[k] for k in ['path', 'title', 'h1', 'canonical', 'robots',
                                         'schema_count', 'h2_count', 'word_count']})
        for key in ['title', 'h1', 'canonical']:
            if not page[key]: issues.append({'path': page['path'], 'issue': 'missing_' + key})
        if page['canonical'] and urlsplit(page['canonical']).hostname != domain:
            issues.append({'path': page['path'], 'issue': 'canonical_host_mismatch'})
        if page['noindex']:
            issues.append({'path': page['path'], 'issue': 'noindex_present'})
    complete = bool(paths) and not failures
    payload = {'pages': pages, 'issues': issues, 'read_failures': failures}
    fingerprint = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    return {'outcome': 'operational_failure' if not complete else 'candidate' if issues else 'complete_no_hit',
            'coverage_complete': complete, 'html_pages_discovered': len(paths),
            **payload, 'fingerprint': fingerprint,
            'scope': 'Local HTML inspection, not search rankings, crawler access, schema validity or attribution.'}


def should_wake(current, previous=None):
    if current.get('coverage_complete') is not True:
        return True
    if not previous or previous.get('coverage_complete') is not True:
        return True
    return current.get('fingerprint') != previous.get('fingerprint')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot', type=Path)
    parser.add_argument('--domain', required=True)
    parser.add_argument('--previous', type=Path, help='Prior JSON report for change suppression')
    args = parser.parse_args()
    result = audit(args.snapshot, args.domain)
    previous = json.loads(args.previous.read_text()) if args.previous else None
    result['wake_for_review'] = should_wake(result, previous)
    print(json.dumps(result, indent=2))
    return 0 if result['coverage_complete'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
