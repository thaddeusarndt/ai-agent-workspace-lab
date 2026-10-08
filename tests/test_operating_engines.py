import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

audit = load('aio_audit', 'examples/aio_audit.py')
gates = load('cron_delivery_gates', 'engines/cron_delivery_gates.py')


class AuditTests(unittest.TestCase):
    def test_clean_fixture_and_repeat(self):
        current = audit.audit(ROOT / 'examples/site_snapshot', 'example.com')
        self.assertEqual(current['outcome'], 'complete_no_hit')
        self.assertTrue(audit.should_wake(current))
        self.assertFalse(audit.should_wake(current, current))

    def test_unreadable_input_is_failure_not_no_hit(self):
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, 'bad.html').write_bytes(b'\xff')
            result = audit.audit(folder, 'example.com')
        self.assertEqual(result['outcome'], 'operational_failure')
        self.assertTrue(audit.should_wake(result, result))

    def test_noindex_and_wrong_canonical(self):
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, 'index.html').write_text('<title>Demo</title><h1>Demo</h1><meta content="noindex" name="robots"><link href="https://wrong.example/" rel="canonical">')
            result = audit.audit(folder, 'example.com')
        self.assertTrue(result['coverage_complete'])
        self.assertEqual({x['issue'] for x in result['issues']}, {'noindex_present', 'canonical_host_mismatch'})

    def test_empty_snapshot_and_recovered_coverage(self):
        with tempfile.TemporaryDirectory() as folder:
            previous = audit.audit(folder, 'example.com')
        current = audit.audit(ROOT / 'examples/site_snapshot', 'example.com')
        self.assertFalse(previous['coverage_complete'])
        self.assertTrue(audit.should_wake(current, previous))


class GateTests(unittest.TestCase):
    def test_success_without_new_gaps_is_quiet(self):
        self.assertFalse(gates.seo_should_wake('fresh_gaps=0 geographic_signals=0', 0))

    def test_error_unknown_and_changed_output_wake(self):
        for stdout, code in [('fresh_gaps=0', 2), ('unrecognized output', 0), ('fresh_gaps=2', 0)]:
            self.assertTrue(gates.seo_should_wake(stdout, code))

    def test_incomplete_health_cannot_hide_behind_zero_counters(self):
        result = {'critical_live_failures': 0, 'sub80_important_pages': 0,
                  'outcome': 'operational_failure', 'required_coverage_complete': False}
        self.assertTrue(gates.health_should_wake(result))

    def test_successful_complete_health_can_be_quiet(self):
        result = {'critical_live_failures': 0, 'sub80_important_pages': 0,
                  'outcome': 'complete_no_hit', 'required_coverage_complete': True}
        self.assertFalse(gates.health_should_wake(result))

    def test_contact_errors_and_new_rows_wake(self):
        self.assertFalse(gates.contact_should_wake({'status': 'ok', 'warnings': [], 'new_rows': 0}))
        self.assertTrue(gates.contact_should_wake({'status': 'error'}))
        self.assertTrue(gates.contact_should_wake({'status': 'ok', 'new_rows': 1}))


if __name__ == '__main__':
    unittest.main()
