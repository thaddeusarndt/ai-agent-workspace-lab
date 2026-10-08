import importlib.util
from pathlib import Path
import sys


def load(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parents[1] / "examples" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_replayed_complete_run_does_not_repeat_delivery():
    ledger = load("cron_replay").RunLedger()
    assert ledger.run("a", True, ["review"])['delivery']
    assert ledger.run("a", True, ["review"])['delivery'] is None


def test_failed_collection_is_retryable_and_is_not_consumed():
    ledger = load("cron_replay").RunLedger()
    assert ledger.run("b", False, [])['status'] == 'coverage_incomplete'
    assert ledger.run("b", True, ["recovered"])['delivery']


def test_complete_empty_collection_is_distinct_from_failure():
    ledger = load("cron_replay").RunLedger()
    assert ledger.run("c", True, [])['status'] == 'complete_no_hit'


def test_report_does_not_treat_referrals_as_bookings():
    report = load("aio_report").render({"as_of": "2026-10-07", "analytics_window": "published aggregate", "confirmed_chatgpt_discovery_bookings": 6, "chatgpt_sessions": 40, "chatgpt_engaged_sessions": 23})
    assert 'Conversion rate: not computed' in report
    assert 'Confirmed ChatGPT-discovery bookings: 6' in report


def test_impossible_engagement_is_rejected():
    import pytest
    with pytest.raises(ValueError):
        load("aio_report").render({"confirmed_chatgpt_discovery_bookings": 6, "chatgpt_sessions": 4, "chatgpt_engaged_sessions": 5})
