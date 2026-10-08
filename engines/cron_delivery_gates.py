"""Selected pure gates used by operating scheduled jobs.

These functions decide whether collected output merits a human review.
They do not schedule jobs or send notifications.
"""
import re
from typing import Any, Mapping

def seo_should_wake(stdout: str, returncode: int) -> bool:
    """Wake on errors, fresh content gaps, changed geographic signals, or unknown output."""
    if returncode != 0:
        return True
    fresh_match = re.search(r"\bfresh_gaps=(\d+)\b", stdout, re.I)
    geographic_match = re.search(r"\bgeographic_signals=(\d+)\b", stdout, re.I)
    if fresh_match or geographic_match:
        fresh_count = int(fresh_match.group(1)) if fresh_match else 0
        geographic_count = int(geographic_match.group(1)) if geographic_match else 0
        return fresh_count != 0 or geographic_count != 0
    legacy_match = re.search(r"\bnew/updated this run:\s*(\d+)\b", stdout, re.I)
    if legacy_match:
        return int(legacy_match.group(1)) != 0
    return True

def health_should_wake(result: Mapping[str, Any], returncode: int = 0) -> bool:
    if returncode != 0:
        return True
    # Explicit coverage semantics take precedence over zero issue counters.
    # Keep bounded compatibility with older successful scanner artifacts.
    if ('outcome' in result and result['outcome'] not in {'complete_no_hit', 'candidate', 'coverage_recovered'}
            or ('required_coverage_complete' in result and result['required_coverage_complete'] is not True)):
        return True
    try:
        return int(result.get('critical_live_failures', 1)) != 0 or int(result.get('sub80_important_pages', 1)) != 0
    except (TypeError, ValueError):
        return True

def contact_should_wake(result: Mapping[str, Any]) -> bool:
    if result.get("status") != "ok" or result.get("warnings"):
        return True
    return any(int(result.get(key, 0) or 0) != 0 for key in
               ("new_rows", "pruned_rows", "enriched_rows"))
